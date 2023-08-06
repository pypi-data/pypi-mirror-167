from abc import ABC, abstractmethod
import math


class Vector(ABC):
    def __str__(self):
        return self.__class__.__name__ + str(self.__dict__)

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __sub__(self, other):
        pass

    @abstractmethod
    def __mul__(self, scalar):
        pass

    @abstractmethod
    def __pow__(self, scalar, modulo=None):
        pass

    @abstractmethod
    def __truediv__(self, scalar):
        pass

    @abstractmethod
    def __floordiv__(self, scalar):
        pass

    @abstractmethod
    def __mod__(self, scalar):
        pass

    @abstractmethod
    def __bool__(self):
        pass

    @abstractmethod
    def __abs__(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def magnitude(self):
        pass

    @abstractmethod
    def magnitude_squared(self):
        pass

    @abstractmethod
    def normalize(self):
        pass

    @abstractmethod
    def dot(self, other):
        pass

    @abstractmethod
    def cross(self, other):
        pass

    @abstractmethod
    def scale_to_magnitude(self, magnitude):
        pass

    @abstractmethod
    def reflect(self, normal_vector):
        pass

    @abstractmethod
    def distance_to(self, other):
        pass

    @abstractmethod
    def distance_to_squared(self, other):
        pass

    @abstractmethod
    def lerp(self, other, alpha):
        pass

    @abstractmethod
    def apply(self, func):
        pass

    @abstractmethod
    def angle_to(self, other):
        pass


if __name__ == '__main__':
    pass
