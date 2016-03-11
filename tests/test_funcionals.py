import unittest
from casacore import functionals


class TestFunctionals(unittest.TestCase):
    def test_something(self):
        #self.functional = functionals.functional(name='test')
        #functionals.chebyshev(self.functional)
        return

    def test_gaussian1d(self):
        gauss1d = functionals.gaussian1d([1, 2, 3])

        assert gauss1d.ndim() == 1
        assert gauss1d.npar() == 3
        assert gauss1d.__len__() == 3

        assert gauss1d.get_parameters() == [1, 2, 3]
        gauss1d.set_parameters([3, 4, 5])
        assert gauss1d.get_parameters() == [3, 4, 5]
        gauss1d.set_parameter(0, 2)
        assert gauss1d.get_parameters()[0] == 2

        assert gauss1d.get_masks() == [True, True, True]
        gauss1d.set_mask(0, False)
        assert gauss1d.get_masks() == [False, True, True]
        # gauss1d.set_masks([True, True, True])
        # assert gauss1d.get_masks() == [True, True, True]

        gauss1d.set_parameters([0, 0, 1])
        assert gauss1d.f(0) == [0]
