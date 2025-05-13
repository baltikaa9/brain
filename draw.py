import cv2
import numpy as np
import math

from matplotlib import cm


def open_image(i: int, folder_path: str) -> np.ndarray:
    img = cv2.imread(f'{folder_path}/image({i}).png', 0)  # чтение изображений
    data = np.stack(img, axis=0)  # преобразование в массив
    return data

def get_points(data: np.ndarray, empty=True) -> tuple[list[float], list[float]]:
    X, Y = [], []

    for y in range(360):  # фильтрация точек
        for x in range(330):
            if data[y][x] < 100:
                data[y][x] = 0

    y, x = data.nonzero()
    # ax1 = fig.add_subplot(222)
    # fig.subplots_adjust(wspace=0.6, hspace=0.6)

    if not empty:
        return x, y

    X.extend([x[0]])
    Y.extend(sorted(list(set(y)) * 2))

    x_count = 1
    for i in range(1, len(x) - 1):
        if x[i] < x[i - 1]:
            X.append(x[i - 1])
            X.append(x[i])
            x_count += 2
    if x[-1] > x[-2]:
        X.append(x[-1])
    else:
        X.append(x[-2])
        Y = Y[:-2]
    x_count += 1
    return X, Y


# fig = plt.figure()
def draw2d(i: int, ax, folder_path):
    # print(i, ax, folder_path)
    data = open_image(i, folder_path)

    X, Y = get_points(data, False)

    ax.scatter(X, Y[::-1], color='black')
    # ax.triplot(x, y[::-1], color='black')


def draw3dдырявое(count: int, ax, folder_path):
    imgs = tuple(cv2.imread(f'{folder_path}/image({i}).png', 0) for i in range(count, 0, -1))

    X, Y, Z = [], [], []
    z = 0

    for img in imgs:
        data = np.stack(img, axis=0)

        for y in range(360):
            for x in range(330):
                if data[y][x] < 50:
                    data[y][x] = 0

        y, x = data.nonzero()

        X.extend([x[0]])
        Y.extend(sorted(list(set(y)) * 2))

        x_count = 1
        for i in range(1, len(x) - 1):
            if x[i] < x[i - 1]:
                X.append(x[i - 1])
                X.append(x[i])
                x_count += 2
        if x[-1] > x[-2]:
            X.append(x[-1])
        else:
            X.append(x[-2])
            Y = Y[:-2]
        x_count += 1

        Z.extend([z] * x_count)
        z += 1
        # np.savetxt("array.csv",[X,Y], delimiter=";",newline=" ")

    for i in range(2, l := len(X) // 2):
        if not l % i:
            rows = l // i
            cols = l // rows

    x = [[0 for _ in range(cols)] for _ in range(rows)]
    y = [[0 for _ in range(cols)] for _ in range(rows)]
    z = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            x[i][j] = X[i * cols + j]
            y[i][j] = Y[i * cols + j]
            z[i][j] = Z[i * cols + j]

    # ax2 = fig.add_subplot(211, projection='3d')
    #
    # ax.scatter(X, Y, Z, color='black')
    ax.plot_trisurf(x, y, z, vmin=z.min() * 2, cmap=cm.Blues)
    # plt.show()
    # ax.plot_wireframe(np.array(x), np.array(y), np.array(z), color='black')


def draw3d(count: int, ax, folder_path):
    count = 10
    imgs = tuple(cv2.imread(f'{folder_path}/image({i}).png', 0) for i in range(count, 0, -1))

    data = np.stack(imgs, axis=0)
    c=0
    for i in range(len(imgs)):
        for y in range(360):
            for x in range(330):
                if data[i][y][x] < 200:
                    data[i][y][x] = 0


    nonzero = data.nonzero()
    z, y, x = nonzero

    # for i in range(2, l := len(nonzero[0] // 2)):
    #     if not l % i:
    #         rows = l // i
    #         cols = l // rows
    #
    # X = [[0 for _ in range(cols)] for _ in range(rows)]
    # Y = [[0 for _ in range(cols)] for _ in range(rows)]
    # Z = [[0 for _ in range(cols)] for _ in range(rows)]
    #
    # for i in range(rows):
    #     for j in range(cols):
    #         X[i][j] = x[i * cols + j]
    #         Y[i][j] = y[i * cols + j]
    #         Z[i][j] = z[i * cols + j]

    # X = []
    # Y = []

    # for i in range(len(imgs)):
    #     for y in range(360):
    #         for x in range(330):
    #             if data[i][y][x]:
    #                 X.append(x)
    #                 Y.append(y)

    # Z = np.array([[0 for _ in range(len(x))] for _ in range(len(y))])

    # for i in range(len(imgs)):
    #     for y in range(360):
    #         for x in range(330):
    #             if data[i][y][x]:
    #                 Z[y][x] = i

    # for k in range(len(imgs)):
    # for i in range(len(x)):
    #     for j in range(len(y)):
    #         Z[i][j] = z[i]

    # ax2 = fig.add_subplot(211, projection='3d')
    # x, y = np.meshgrid(x, y)




    # fig.subplots_adjust(wspace=0.6, hspace=0.6)

    # ax.plot_wireframe(np.array(X), np.array(Y), np.array(Z), color='black')
    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    ax.plot_trisurf(x, y, z, vmin=z.min() * 2, cmap=cm.Blues)
    # ax.scatter(x, y, z, color='black')
    # plt.show()

    return x,y,z