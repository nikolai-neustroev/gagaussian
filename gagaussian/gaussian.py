from typing import List, NoReturn

from .general import Distribution


class Gaussian(Distribution):
    def __init__(self):
        """Gaussian distribution class."""
        super().__init__()

    def __add__(self, other) -> 'Gaussian':
        """Method to add together two Gaussian distributions.

        Args:
            other (Gaussian): other Gaussian distribution.

        Returns:
            Gaussian: Gaussian distribution.
        """
        pass

    def __repr__(self) -> str:
        """Method to print the characteristics of the Gaussian distribution.

        Returns:
            str: characteristics of the Gaussian.
        """
        pass

    def calculate_mean(self) -> float:
        """Method to calculate the mean value of the distribution.

        Returns:
            float: The mean value of the distribution.
        """
        pass

    def calculate_stdev(self) -> float:
        """Method to calculate the standard deviation value
        of the distribution.

        Returns:
            float: The standard deviation value of the distribution.
        """
        pass

    def pdf(self, x: float) -> float:
        """Probability density function.

        Args:
            x (float): Point for calculating the probability density function.

        Returns:
            float: Probability density.
        """
        pass

    def plot(self) -> NoReturn:
        """Plotting histogram.

        Returns:
            NoReturn
        """
        pass

    def plot_pdf(self, n_spaces=50) -> (List[float], List[float]):
        """Plotting probability density function.

        Args:
            n_spaces (int): Number of plotted points.

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
        """
        pass
