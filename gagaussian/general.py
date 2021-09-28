from abc import ABC, abstractmethod


class DistributionInterface(ABC):
    @abstractmethod
    def __init__(self, mean, stdev):
        raise NotImplementedError

    @abstractmethod
    def __add__(self, other):
        raise NotImplementedError

    @abstractmethod
    def __repr__(self):
        raise NotImplementedError

    @abstractmethod
    def read(self, file):
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
