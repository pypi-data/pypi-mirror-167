
import numpy as np
from adfp.function import Function


class Square(Function):
    def forward(self, x):
        return x ** 2

    def backward(self, gy):
        x, = self.inputs
        gx = 2 * x * gy
        return gx


def square(x):
    return Square()(x)


class Exp(Function):
    def forward(self, x):
        return np.exp(x)
    def backward(self, gy):
        x, = self.inputs
        gx = exp(x) * gy
        return gx


def exp(x):
    return Exp()(x)


class Sin(Function):
    def forward(self, x):
        return np.sin(x)
    def backward(self, gy):
        x, = self.inputs
        gx = gy * cos(x)
        return gx


def sin(x):
    return Sin()(x)


class Cos(Function):
    def forward(self, x):
        return np.cos(x)
    def backward(self, gy):
        x, = self.inputs
        gx = gy * -sin(x)
        return gx


def cos(x):
    return Cos()(x)


class Tanh(Function):
    def forward(self, x):
        y = np.tanh(x)
        return y

    def backward(self, gy):
        y, = self.outputs
        y = y()
        gx = gy * (1 - y * y)
        return gx


def tanh(x):
    return Tanh()(x)