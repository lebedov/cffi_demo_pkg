#!/usr/bin/env python

from _cffi_demo_pkg import ffi, lib

def rms(x):

    # Parameter sanity check without having to import numpy:
    assert type(x).__name__ == 'ndarray'
    assert x.dtype.char == 'f'

    # Need to cast ctypes interface to array to pass it to cffi interface:
    xp = ffi.cast('float *', x.ctypes.data)
    return lib.rms(xp, x.size)
