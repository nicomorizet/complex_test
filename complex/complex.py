import numpy as np
from math import sqrt, atan2, cos, sin
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Arc


class Complex:
    def __init__(self, x=0.0, y=0.0):
        self.real = np.round(x, 2)
        self.imag = np.round(y, 2)

    # Addition
    def __add__(self, other):
        add_real = self.real + other.real
        add_imag = self.imag + other.imag
        return Complex(add_real, add_imag)

    # Subtraction
    def __sub__(self, other):
        sub_real = self.real - other.real
        sub_imag = self.imag - other.imag
        return Complex(sub_real, sub_imag)

    # Multiplication
    def __mul__(self, other):
        mul_real = self.real * other.real - self.imag * other.imag
        mul_imag = self.real * other.imag + self.imag * other.real
        return Complex(mul_real, mul_imag)

    # Modulus (or Magnitude)
    def __abs__(self):
        r = sqrt(self.real**2 + self.imag**2)
        return r

    # Phase (or Argument)
    def phase(self):
        phi = atan2(self.imag, self.real)
        # Converting to degrees
        phi = phi * 180 / np.pi
        return phi

    # Division
    def __truediv__(self, other):
        r1 = abs(self)
        r2 = abs(other)
        phi1 = self.phase()
        phi2 = other.phase()
        div_real = (r1 / r2) * cos(phi1 - phi2)
        div_imag = sin(phi1 - phi2)
        return Complex(div_real, div_imag)

    # Conjugate
    def conj(self):
        return Complex(self.real, -self.imag)

    # Pretty Print
    def __str__(self):
        return "({:.3f}, {:.3f} * i)".format(self.real, self.imag)

    # Plot
    def plot(self):
        r = abs(self)
        phi = self.phase()
        lim = 10
        fig, ax = plt.subplots()
        lbl_str = 'z=' + str(self.real) + 'x+' + str(self.imag) + '*i'
        plt.scatter(self.real, self.imag,
                    label=lbl_str,
                    marker="*", color="green", s=50)
        plt.quiver(np.array(0), np.array(0),
                   np.array(self.real), np.array(self.imag),
                   units="xy", color="blue", scale=1)
        plt.xlabel('Real Part')
        plt.ylabel('Imaginary Part')
        plt.title('Complex Plane')
        ax.set_aspect('equal')
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        plt.xlim(-lim, lim)
        plt.ylim(-lim, lim)
        vertical_line = Line2D([self.real, self.real], [0, self.imag],
                               linestyle='dashed', color='black')
        ax.add_line(vertical_line)
        horizontal_line = Line2D([0, self.real], [self.imag, self.imag],
                                 linestyle='dashed', color='black')
        ax.add_line(horizontal_line)

        plt.text(0.5 * lim, 0.75 * lim, r'$r=$' + str(np.round(r, 2)))
        plt.text(0.5 * lim, 0.65 * lim, r'$\phi=$' + str(np.round(phi, 2)) + ' deg.')

        # Arc
        if phi < 0:
            theta1 = phi
            theta2 = 0
        else:
            theta1 = 0
            theta2 = phi
        ax.add_patch(Arc((0.0, 0.0), 2, 2,
                         theta1=theta1, theta2=theta2, edgecolor='purple'))

        plt.legend()
        plt.grid()
        plt.show()


if __name__ == '__main__':
    a = 4*sqrt(2)
    b = 4*sqrt(2)
    z = Complex(a, b)
    z.plot()
