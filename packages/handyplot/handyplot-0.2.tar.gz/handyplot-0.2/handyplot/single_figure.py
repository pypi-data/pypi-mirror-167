import matplotlib.pyplot as plt
import numpy as np


class SingleFigure:
    def __init__(self):
        self._base_data = None
        self._fig_list = []
        self._legend_list = []
        self._x_limit = None
        self._y_limit = None
        plt.figure()

    def add_legend(self, loc="best"):
        """
        Add legend for figure.
        :param loc: str | Legend location. (best, upper+l/r/c, lower+l/r/c, right, center+l/r, center)
        :return:
        """
        plt.legend(self._fig_list, self._legend_list, loc=loc)

    def add_line_data(self, data, linewidth=1, color="black", legend=""):
        """
        One line each time.
        :param data:
        :return:
        """
        fig, = plt.plot(self._base_data, data, linewidth=linewidth, c=color)
        self._fig_list.append(fig)
        self._legend_list.append(legend)

    def add_point_data(self, data, marker="o", color="w", edgecolor="red", size=35, legend=""):
        fig = plt.scatter(self._base_data, data, marker=marker, color=color, edgecolor=edgecolor, s=size)
        self._fig_list.append(fig)
        self._legend_list.append(legend)

    def save(self, filename="unknown", dpi=1000):
        plt.savefig(filename, dpi=dpi)

    def set_base_data(self, base_data):
        self._base_data = base_data
        self._x_limit = [base_data.min(), base_data.max()]

    def set_title(self, title):
        plt.title(title)

    def set_x_label(self, text):
        plt.xlabel(text)

    def set_x_limit(self, range):
        self._x_limit = []
        self._x_limit.append(range[0])
        self._x_limit.append(range[1])

    def set_y_label(self, text):
        plt.ylabel(text)

    def set_y_limit(self, range):
        self._y_limit = []
        self._y_limit.append(range[0])
        self._y_limit.append(range[1])

    def show(self):
        if self._x_limit is not None : plt.xlim(self._x_limit)
        if self._y_limit is not None : plt.ylim(self._y_limit)
        plt.show()


if __name__ == "__main__":
    figure_1 = SingleFigure()
    base_data = np.array([0, 1, 2, 3, 4, 5])
    figure_1.set_base_data(base_data)
    figure_1.add_point_data(np.array([1, 2, 3, 4, 5, 6]))
    figure_1.add_line_data(np.array([0, 3, 2, 1, 4, 5]))
    figure_1.set_title("font")
    figure_1.set_x_label("x")
    figure_1.set_y_label("y")
    figure_1.set_y_limit([0, 6])
    figure_1.show()