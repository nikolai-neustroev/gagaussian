from unittest import TestCase, main

from gagaussian import Binomial


class TestBinomial(TestCase):
    def setUp(self):
        self.binomial = Binomial(0.4, 20)
        self.binomial.read('numbers_binomial.txt')

    def test_initialization(self):
        self.assertEqual(self.binomial.p, 0.4, 'p value incorrect')
        self.assertEqual(self.binomial.n, 20, 'n value incorrect')

    def test_read(self):
        self.assertEqual(self.binomial.data,
                         [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
                         'data not read in correctly')

    def test_calculate_mean(self):
        mean = self.binomial.calculate_mean()
        self.assertEqual(mean, 8)

    def test_calculate_stdev(self):
        stdev = self.binomial.calculate_stdev()
        self.assertEqual(round(stdev, 2), 2.19)

    def test_replace_stats_with_data(self):
        p, n = self.binomial.replace_stats_with_data()
        self.assertEqual(round(p, 3), .615)
        self.assertEqual(n, 13)

    def test_pdf(self):
        self.assertEqual(round(self.binomial.pdf(5), 5), 0.07465)
        self.assertEqual(round(self.binomial.pdf(3), 5), 0.01235)

        self.binomial.replace_stats_with_data()
        self.assertEqual(round(self.binomial.pdf(5), 5), 0.05439)
        self.assertEqual(round(self.binomial.pdf(3), 5), 0.00472)

    def test_add(self):
        binomial_one = Binomial(.4, 20)
        binomial_two = Binomial(.4, 60)
        binomial_sum = binomial_one + binomial_two

        self.assertEqual(binomial_sum.p, .4)
        self.assertEqual(binomial_sum.n, 80)


if __name__ == '__main__':
    main()
