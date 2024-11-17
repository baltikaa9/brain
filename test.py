import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def main():
    u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
    x = np.cos(u) * np.sin(v)
    y = np.sin(u) * np.sin(v)
    z = np.cos(v)

    # x = [168, 169, 170]
    # y = [73, 73, 73]
    # z = [0, 0, 0]
    #
    # Z = [[0 for _ in range(3)] for _ in range(3)]

    # x = [1, 2, 3]
    # y = [1, 2, 3, 4, 10]
    # z = [[0 for _ in range(len(x))] for _ in range(len(y))]
    #
    # for i in range(len(x)):
    #     for j in range(len(y)):
    #         z[j][i] = x[i] * y[j]
    #
    # x, y = np.meshgrid(x, y)
    # z = np.array(z)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # X, Y, Z = axes3d.get_test_data(0.05)
    ax.plot_surface(x, y, z)

    # z = np.array(F(x, y))
    # ax.legend()
    plt.show()
    c=1


if __name__ == '__main__':
    main()
