from unittest import main, TestCase

import cffi_demo_pkg

try:
    import numpy as np
except ImportError:
    print('numpy required to run tests')
else:
    from numpy.testing import assert_equal

class test_cffi_demo_pkg(TestCase):
    def setUp(self):
        np.random.seed(0)

    def test_rms(self):
        n = 5
        x = np.random.rand(n).astype(np.float32)
        r = cffi_demo_pkg.rms(x)
        
        assert_equal(r, np.sqrt(np.mean(x**2)))

if __name__ == '__main__':
    main()
