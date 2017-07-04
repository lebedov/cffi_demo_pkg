#!/usr/bin/env python

import cffi

ffi = cffi.FFI()
ffi.cdef('float rms(float *data, int n);')
ffi.set_source('_cffi_demo_pkg', 
"""
#include <math.h>
float rms(float *data, int n) {
    float result = 0;
    for (int i=0; i<n; i++) {
        result += pow(data[i], 2);
    }
    return sqrt(result/n);
}
""", libraries=['m'])

if __name__ == '__main__':
    ffi.compile(verbose=True)
