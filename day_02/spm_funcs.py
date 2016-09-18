"""
This will be your new module defining SPM-like functions

Here you want the get_spm_globals function from the earlier exercise, with
anything that function imports and other definitions that the function needs.

When you are done, you should be able to run this spm_funcs.py module as a
script and see the script print a message beginning with "OK".

You run this module as a script like this::

    python3 spm_funcs.py

or, in IPython (recommended)::

    %run spm_funcs.py
"""
# Python 2 compatibility
from __future__ import print_function, division

import numpy as np

import nibabel as nib


def spm_global(vol):
    """ Calculate SPM global metric for array `vol`

    Parameters
    ----------
    vol : array
        Array giving image data, usually 3D.

    Returns
    -------
    g : float
        SPM global metric for `vol`
    """
    # +++your code here+++
    return


def get_spm_globals(fname):
    """ Calculate SPM global metrics for volumes in image filename `fname`

    Parameters
    ----------
    fname : str
        Filename of file containing 4D image

    Returns
    -------
    spm_vals : array
        SPM global metric for each 3D volume in the 4D image.
    """
    # +++your code here+++
    return


def main():
    # This function run when file executed as a script
    glob_vals = get_spm_globals('ds107_sub012_t1r2.nii')
    expected_values = np.loadtxt('global_signals.txt')
    if np.allclose(glob_vals, expected_values, rtol=1e-4):
        print('OK: your values and SPMs are close')
    else:
        print('SPM and your values differ')
        print('Yours:', [float(v) for v in glob_vals])
        print('SPMs:', expected_values)


if __name__ == '__main__':
    # File being executed as a script
    main()
