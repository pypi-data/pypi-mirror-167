import numpy as np

from scipy.ndimage import maximum_filter
from astropy.table import Table
from astropy.nddata import block_reduce


def mask_dilation(masked_array, box_size=3):
    """
    Dilate the mask for a set of masked spectra values

    Parameters
    ----------
    masked_array : ~numpy.ma.array
        Input masked array
    box_size : int
        box_size for `maximum_filter` (along spectral direction), default=3 will grow
        mask by one pixel.

    """
    mask_grown = maximum_filter(masked_array.mask, (1, box_size))
    return np.ma.array(data=masked_array.data, mask=mask_grown)


def masked_br(masked_array, block_size, func):
    """
    Block reduce function incorporating mask propagation

    If ``data`` is not perfectly divisible by ``block_size`` along a
    given axis then the data will be trimmed (from the end) along that
    axis.

    Parameters
    ----------
    masked_array : ~numpy.ma.array
        Input masked array
    block_size : int or array-like (int)
        Block size for block_reduce - must conform to
        ~astropy.nddata.block_reduce requirements.
    func : callable, optional
        The method to use to downsample the data.  Must be a callable
        that takes in a `~numpy.ndarray` along with an ``axis`` keyword,
        which defines the axis or axes along which the function is
        applied.  The ``axis`` keyword must accept multiple axes as a
        tuple.

    Returns
    -------
    output : array-like
        The resampled data with corresponding mask
    """

    data = block_reduce(masked_array.data, block_size, func)
    mask = np.ceil(block_reduce(masked_array.mask, block_size, func))
    return np.ma.array(data=data, mask=mask)


def software_bin(spectra_table, bin_factor, dilate_mask=True, dilate_box_size=3):
    """
    Software bin a set of WEAVE spectra.

    Performs standard mean-resampling of 1-D spectra, with corresponding
    error propagation (ivar) and

    Parameters
    ----------
    spectra_table : ~astropy.table.Table
        Table including a sample of sky-subtracted 1D spectra returned by weave-io query.
        Must include: 'wvl', 'flux', 'ivar' & 'sensfunc' columns.
    bin_factor : int
         Number of pixels by which to bin. For WEAVE tests - 2 and 4 are the
         expected options. But high bin factors are permitted.
    dilate_mask : bool, default=True
        Include mask dilation, e.g. to exclude regions around sky lines when
        summing signal.
    dilate_box_size : int, default=2
        Boxcar kernel width for mask dilation

    Returns
    -------
    output_table : ~astropy.table.Table
        Software binned version of the input `spectra_table`

    Notes
    -----
    N.B. Inverse variance weighted mean possible to implement, but not
    necessarily directly comparable to on-chip binning w.r.t output
    fluxes and noise propagation (?).
    """

    def get_col(name):  #
        if dilate_mask:
            return mask_dilation(spectra_table[name].data, dilate_box_size)
        else:
            return spectra_table[name].data

    wvl_binned = masked_br(get_col("wvl"), (1, bin_factor), np.mean)
    flux_binned = masked_br(get_col("flux"), (1, bin_factor), np.mean)
    sensfunc_binned = masked_br(get_col("sensfunc"), (1, bin_factor), np.mean)
    ivar_binned = masked_br(get_col("ivar"), (1, bin_factor), np.sum)

    output_table = Table(
        data={"wvl": wvl_binned, "flux": flux_binned, "sensfunc": sensfunc_binned, "ivar": ivar_binned},
        masked=True,
    )

    return output_table
