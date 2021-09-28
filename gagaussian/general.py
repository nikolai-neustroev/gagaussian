from abc import ABC, abstractmethod
from typing import NoReturn


class DistributionInterface(ABC):
    @abstractmethod
    def __init__(self, mean: float, stdev: float):
        raise NotImplementedError

    @abstractmethod
    def __add__(self, other):
        raise NotImplementedError

    @abstractmethod
    def __repr__(self):
        raise NotImplementedError

    @abstractmethod
    def read(self, file: str) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    def calculate_mean(self):
        raise NotImplementedError

    @abstractmethod
    def calculate_stdev(self):
        raise NotImplementedError

    @abstractmethod
    def pdf(self):
        raise NotImplementedError

    @abstractmethod
    def plot(self):
        raise NotImplementedError

    @abstractmethod
    def plot_pdf(self):
        raise NotImplementedError


class Distribution(DistributionInterface, ABC):
    def __init__(self, mean=0., stdev=1.):
        """General distribution parent class.

        Args:
            mean (float): The mean value of the distribution.
            stdev (float): The standard deviation of the distribution.
        """
        self.mean = mean
        self.stdev = stdev
        self.data = []

    def read(self, file: str) -> NoReturn:
        """Method to read data from a text file.

        Args:
            file (str): Name of a file to read.

        Returns:
            NoReturn
        """
        with open(file) as file:
            data = []
            line = file.readline()
            with line:
                data.append(int(line))
                line = file.readline()
        file.close()

        self.data = data
