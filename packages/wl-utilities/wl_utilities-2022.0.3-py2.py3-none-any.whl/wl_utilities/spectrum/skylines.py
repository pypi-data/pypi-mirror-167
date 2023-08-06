import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import median_filter
from astropy.stats import sigma_clip

"""
A script with the Skyline class that identifies skylines in a given spectra, returns a mask of elements masked out as skylines, and the area masked by the skylines. A minimal working example is provided below.

- 15/9/2022, Rohit Kondapally (rohitk@roe.ac.uk)

Todo:
    1. The standard deviation estimation is not quote correct -- need to fix this too
    2. The class/methods work on one spectra currently. Potentially may want to optimise it to run on multiple spectra at once, efficiently.
"""


class Skyline:
    """
    A class to identify the skyline regions within spectra and return the corresponding mask for selecting these regions. It also gives area masked out by the sky regions.

    Attributes:
    -----------
    wavel : An array of wavelengths (a numpy array like)
    sigma_spec : An array of ivar (*sensfunc) values (a numpy array like)

    Methods:
    --------
    get_mask(mfilt_size=601, sigma_level=5.0, angs_pad=1.0):
        Get a boolean mask which selects skylines in the supplied spectrum

    masked_area(wmin, wmax):
        Get the area and fraction of area covered by skylines over a specified wavelength range

    get_floor():
        Get the floor level of the ivar spectrum

    std_filter(input_arr, size, mode="wrap"):
        Perform a running standard deviation across the spectrum

    pad_skylines(self, skyline_bool, angs_pad):
        Pads a region around either side of each skyline identified to make sure all affected wavelengths (elements) are masked

    Notes
    -----

    1. A basic usage example assuming an array of wavelengths (`wl`) and ivar (`sigma_sky`):

    # Initialise the Skyline class with the wavelength and the ivar array
    skyl = Skyline(wl, sigma_sky)

    # Get a boolean array that indicates which elements are affected by skylines based on a few key user-defined parameters
    sky_mask = skyl.get_mask(mfilt_size=601, sigma_level=5.0, angs_pad=1.0)

    # Get the area covered by the above identified skylines
    area, frac_area = skyl.masked_area(7900., 9600.)
    print("Area masked by skylines: {0} Angstroms, and fraction of area masked: {1}%".format(area, frac_area))
    """

    def __init__(self, wavel, sigma_spec):
        self.wavel = wavel
        self.sigma_spec = sigma_spec

        # Calculate the spectral resolution/binning of the data i.e. number of Angstroms per data unit
        self.spec_res = wavel[1] - wavel[0]

    def get_floor(self):
        """
        Get the floor level of the ivar spectrum
        """
        sigma_floor = median_filter(self.sigma_spec, size=self.mfilt_size)
        return sigma_floor

    def std_filter(self, input_arr, size, mode="wrap"):
        """
        Perform a running standard deviation filtering on input data

        Parameters:
        -----------
        input_arr : Input 1D array to perform filtering on
        size : The size of array to use for the running filter
        mode : Determines how input array is extended beyond. Default value implemented is 'wrap'.

        Returns:
        --------
        filt_arr : The filtered array (with the same shape as input_arr)

        Notes
        -----
        Currently allowed values for the mode parameter are: 'wrap', 'reflect', and 'none'
        """
        if mode.lower() == "wrap":
            input_ext = np.append(input_arr, input_arr[:size])
        elif mode.lower() == "reflect":
            # input_ext = np.append(input_arr[-size:][::-1], input_arr)
            input_ext = np.append(input_arr, input_arr[-size:][::-1])
            # input_ext = input_ext[int(size/2):-int(size/2)-1]
        elif mode.lower() == "none":
            input_ext = np.copy(input_arr)
        else:
            raise (NotImplementedError("Currently only 'wrap' and 'none' modes are supported!"))

        # Get the sliding window - a 2D array of shape = (len(input_ext), size)
        idx = np.arange(size) + np.arange(len(input_ext) - size + 1)[:, None]

        # Perform a sigma clip of the data
        # sig_clip_data = sigma_clip(input_ext[idx], sigma=3., axis=1, masked=False, maxiters=15)

        filt_arr = np.nanstd(input_ext[idx], axis=1)[:-1]

        # Need to "roll" the array by the filter size in order to get the filtered values in the correct place
        filt_arr = np.roll(filt_arr, int(size / 2))

        return filt_arr

    def pad_skylines(self, skyline_bool, angs_pad):
        """
        Pad a region around each skyline by `angs_pad` Angstroms

        Parameters:
        -----------
        skyline_bool : Skyline
        angs_pad : Angstroms to pad around each detected skyline (default = 1 Angstrom)
        """
        # Number of elements to pad with True's (i.e. mark as sky-lines) around each "line"
        nel_pad = int(angs_pad / self.spec_res)

        # Indices of elements where skylines start/end
        flip_indx = np.diff(skyline_bool).nonzero()[0]

        # The array of extra indices to "pad" i.e. set True and mark as skylines
        pad_indx = np.array([]).astype(int)
        for fi in flip_indx:
            tmp = np.arange(fi - nel_pad, fi + nel_pad + 1).astype(int)
            pad_indx = np.append(pad_indx, tmp)

        # This line is so that no elements outside the wavelength range are attempted to be padded (or else it will return an index error)
        pad_indx[pad_indx >= len(skyline_bool)] = len(skyline_bool) - 1

        # Take the unique element list
        pad_indx = np.unique(pad_indx)
        # print("No. of extra elements padded: {0}".format(len(pad_indx)))

        skyline_bool_pad = skyline_bool.copy()
        skyline_bool_pad[pad_indx] = True

        return skyline_bool_pad

    def get_mask(self, mfilt_size=601, sigma_level=5.0, angs_pad=1.0):
        """
        Find the skylines and return a boolean array that indicates the wavelength that are occupied by skylines

        Parameters:
        -----------
        mfilt_size : Size of the window filter to use for median and standard deviation filtering (in units of elements)
        sigma_level : Number of sigma above the median floor level used to define the "skylines"
        pad_angs : The number of Angstroms to pad around each detected skyline to make sure we're masking enough affected area

        Returns:
        --------
        skyline_bool_fin : A boolean array indicating the elements that are marked as "skylines". Has the same shape as self.wavel
        """

        self.mfilt_size = mfilt_size

        # First get the floor level
        sigma_floor = self.get_floor()

        """
        # Now define an appropriate level above the floor to cut to select "skylines"
        """
        # First get only the ivar values below the floor level (i.e. set all above to be NaN's)
        sigma_spec_below = np.copy(self.sigma_spec)
        sigma_spec_below[self.sigma_spec > sigma_floor] = np.nan

        # Now run the standard deviation filter to get the deviation about the median
        sigma_spec_std = self.std_filter(sigma_spec_below, mfilt_size)

        # This gets us an initial estimate of all skylines that are `sigma_level' above the floor (`sigma_floor')
        skyline_bool = self.sigma_spec > (sigma_floor + (sigma_level * sigma_spec_std))

        # Now pad a region around these skylines as required
        self.skyline_bool_fin = self.pad_skylines(skyline_bool, angs_pad)

        return self.skyline_bool_fin

    def masked_area(self, wmin, wmax):
        """
        Get the area (in Angstroms) and fraction of area masked by skylines between a specified region of the spectrograph

        Parameters:
        -----------
        wmin : The minimum wavelength used for the area calculation
        wmax : The maximum wavelength used for the area calculation

        Returns:
        --------
        area : Total area masked by skylines between wmin and wmax (in units of Angstroms)
        frac_area : Fraction of total area masked by skylines between wmin and wmax
        """

        # TODO: Add a consistency check for wavelength ranges being within the bounds of the input data wavelength array?

        # Calculate the maximum (observed) area based on user defined ranges
        max_area = np.sum((self.wavel > wmin) & (self.wavel <= wmax)) * self.spec_res

        # Calculate area taken up by the skylines
        area = np.sum(self.skyline_bool_fin & (self.wavel > wmin) & (self.wavel <= wmax)) * self.spec_res
        frac_area = area / max_area

        return area, frac_area * 100


if __name__ == "__main__":
    """
    A minimal working example of using the above class to get skylines. Note that the class only works with an array of data -- no weaveio interface is needed.
    """

    # Do the weaveio import here
    from weaveio import *

    # First search weaveio and obtain a sky spectra from the red arm for a given night
    data = Data()

    yesterday = 57811  # state yesterday's date in MJD

    runs = data.runs
    is_red = runs.camera == "red"
    is_yesterday = floor(runs.exposure.mjd) == yesterday  # round down to an integer, which is the day

    """
    # Get the low res spectra so that it covers the full wavelength range:
    # obs = obs[any(red_arm.resolution == "low", wrt=obs)]
    """

    is_low_res = any(runs.resolution == "low", wrt=runs)

    runs = runs[is_red & is_yesterday & is_low_res]  # filter the runs to red ones that were taken yesterday

    # Now get the l1single_spectra of the sky fibres
    spectra = runs.l1single_spectra  # get all the spectra per run
    sky_spectra = spectra[spectra.targuse == "S"]  # filter to the spectra which are sky

    # Count the number of sky fibres
    print("No. of sky spectra taken yesterday with the red-arm: ", count(sky_spectra)())

    # Get the required data into an astropy.table format
    table = sky_spectra[
        ["wvl", "flux", "ivar", "camera", "sensfunc"]  # design a table of wavelength and flux
    ](
        limit=1
    )  # select a singular sky spectrum from this table to use as input for the Skyline class

    # This is effectively the sigma of the sky spectrum - take just one for now. These are the inputs to the Class
    sigma_sky = 1 / np.sqrt(table["ivar"]) * table["sensfunc"]
    wl = table["wvl"]

    """
    # Now find the skylines
    """

    # Initialise the Skyline class with the wavelength and the ivar array
    skyl = Skyline(wl, sigma_sky)

    """
    # Now get an array of booleans that define which regions are masked as "skylines".
    # You can specify the filter size used for median filtering,
    # the sigma_level used for defining skylines above the median level 
    # and the angstroms to pad around each detected skyline
    """
    sky_mask = skyl.get_mask(mfilt_size=601, sigma_level=5.0, angs_pad=1.0)

    # This will then print out the area masked out by the skylins over a chosen wavelength range
    min_wave = 7900.0
    max_wave = 9600.0
    area, frac_area = skyl.masked_area(min_wave, max_wave)

    print("Area masked by skylines: {0} Angstroms, and fraction of area masked: {1}%".format(area, frac_area))

    # Make a plot of the spectrum and the skylines
    # Make a plot of the spectra and the skylines masked out
    fig = plt.figure()
    plt.plot(wl, sigma_sky, "r--", lw=0.7, alpha=0.5)
    plt.plot(wl[sky_mask], sigma_sky[sky_mask], "b:", lw=0.8, alpha=0.5, label="Skylines")

    # Plot the floor level
    plt.plot(wl, skyl.get_floor(), "k-", lw=1.0, alpha=0.8, label="Floor")
    # plt.show()
