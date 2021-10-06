from unittest import TestCase, main
from unittest.mock import patch

from gagaussian.general import Distribution


class TestDistribution(TestCase):
    @patch.multiple(Distribution, __abstractmethods__=set())
    def setUp(self):
        self.distribution = Distribution(25, 2)
        self.distribution.read('numbers_gaussian.txt')

    def test_cannot_instantiate(self):
        """showing we normally can't instantiate an abstract class"""
        with self.assertRaises(TypeError):
            Distribution()

    @patch.multiple(Distribution, __abstractmethods__=set())
    def test_set_mean(self):
        self.distribution.set_mean(31)
        self.assertEqual(self.distribution.mean, 31, 'incorrect mean')

    @patch.multiple(Distribution, __abstractmethods__=set())
    def test_get_mean(self):
        self.assertEqual(self.distribution.mean, self.distribution.get_mean(),
                         'incorrect mean')

    @patch.multiple(Distribution, __abstractmethods__=set())
    def test_set_stdev(self):
        self.distribution.set_stdev(6)
        self.assertEqual(self.distribution.stdev, 6, 'incorrect stdev')

    @patch.multiple(Distribution, __abstractmethods__=set())
    def test_get_stdev(self):
        self.assertEqual(self.distribution.stdev,
                         self.distribution.get_stdev(), 'incorrect stdev')

    @patch.multiple(Distribution, __abstractmethods__=set())
    def test_get_data(self):
        self.assertEqual(self.distribution.data,
                         self.distribution.get_data(), 'incorrect data')

    @patch.multiple(Distribution, __abstractmethods__=set())
    def test_read(self):
        self.distribution.read('numbers_binomial.txt')
        self.assertEqual(self.distribution.data,
                         self.distribution.get_data(), 'incorrect data')


if __name__ == '__main__':
    main()
