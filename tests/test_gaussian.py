from unittest import TestCase, main

from gagaussian import Gaussian


class TestGaussian(TestCase):
    def setUp(self):
        self.gaussian = Gaussian(25, 2)
        self.gaussian.read('numbers_gaussian.txt')

    def test_initialization(self):
        self.assertEqual(self.gaussian.mean, 25, 'incorrect mean')
        self.assertEqual(self.gaussian.stdev, 2,
                         'incorrect standard deviation')

    def test_read(self):
        self.assertEqual(self.gaussian.data,
                         [1, 3, 99, 100, 120, 32, 330, 23, 76, 44, 31],
                         'data not read in correctly')

    def test_calculate_mean(self):
        self.assertEqual(self.gaussian.calculate_mean(),
                         sum(self.gaussian.data) / float(
                             len(self.gaussian.data)),
                         'calculated mean not as expected')

    def test_calculate_stdev(self):
        self.assertEqual(round(self.gaussian.calculate_stdev(), 2), 92.87,
                         'sample standard deviation incorrect')

    def test_pdf(self):
        self.assertEqual(round(self.gaussian.pdf(25), 5), 0.19947,
                         'pdf function does not give expected result')
        self.gaussian.calculate_mean()
        self.gaussian.calculate_stdev()
        self.assertEqual(round(self.gaussian.pdf(75), 5), 0.00429,
                         'pdf function after calculating mean and stdev does '
                         'not give expected result')

    def test_add(self):
        gaussian_one = Gaussian(25, 3)
        gaussian_two = Gaussian(30, 4)
        gaussian_sum = gaussian_one + gaussian_two

        self.assertEqual(gaussian_sum.mean, 55)
        self.assertEqual(gaussian_sum.stdev, 5)

    # def test_plot(self):  # TODO: implement with matplotlib
    #     self.fail()
    #
    # def test_plot_pdf(self):
    #     self.fail()


if __name__ == '__main__':
    main()
