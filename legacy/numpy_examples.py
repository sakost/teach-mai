import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# NUMerical PYthon

def poly(coeffs, x):
    return np.sum([coeff ** power * x for power, coeff in enumerate(coeffs)], axis=0)


def main():
    np.random.seed(12312)
    sns.set_style('darkgrid')

    x = np.linspace(-15, 15, 200)
    y = poly([2, 3, 1], x)  # x^2 + 3x + 2

    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    main()
