import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d

from draw import open_image, get_points


# @dataclass
# class Parameters:
#     a: int = 0
#     b: int = 1
#     h: float = 0.02
#     t_max: float = 0.3
#     init_expr: str = '1-x'
#     left_bound: float = 0
#     right_bound: float = 0
#
#     def __post_init__(self):
#         self.N: int = int((self.b - self.a) / self.h)
#         self.x: Coords = [0.0 for _ in range(self.N + 2)]
#         for i in range(self.N + 2):
#             self.x[i] = round(self.a + (i - 0.5) * self.h, 2)
#         # НУ
#         self.T0: Temperature = [round(eval(self.init_expr), 2) for x in self.x]
#
#         # ГУ
#         # self.T0[0] = self.left_bound
#         # self.T0[-1] = self.right_bound
#
#         self.T0[0] = self.T0[1] - self.h * self.left_bound  # олеся 2 рода
#         self.T0[-1] = self.right_bound  # олеся 1 рода
#
#         self.tau: float = self.h * self.h / (2 * self.D(-1))
#         # self.tau: float = 0.001
#
#     def D(self, i: int) -> int:
#         return 1 if self.x[i] < 0.5 else 2

# def thermal_conductivity_explicit(params: Parameters):
#     T = [params.T0]
#     t = params.tau
#     T0 = params.T0
#     T1 = [0.0 for _ in range(params.N + 2)]
#     while round(t, 4) <= params.t_max:
#         for i in range(1, params.N + 1):
#             k = (params.tau * params.D(i)) / (params.h * params.h)
#             T1[i] = k * T0[i + 1] + (1 - 2 * k) * T0[i] + k * T0[i - 1]
#
#         T1[0] = T1[1] - params.h * params.left_bound  # олеся 2 рода
#         T1[-1] = params.right_bound  # олеся 1 рода
#         # print(t // params.tau + 1, T1[1:-1])
#         T.append(T1.copy())
#         T0 = T1.copy()
#         t += params.tau
#     return T

def compute(layer: int) -> dict[list[list[float]]]:
    X, Y = get_points(open_image(layer, 'images'))
    t_max = 30
    t = 0
    left_bound = []
    right_bound = []
    bottom_bound = min(Y)
    top_bound = max(Y)
    dx = dy = 1
    dt = 0.1

    Tleft = 100
    Tright = 100
    Tbottom = 100
    Ttop = 100

    lam = 0.251
    rho = 1108  # Плотность тканей, кг/м^3
    c = 3150  # Удельная теплоемкость тканей, Дж/(кг*°C)

    # dx = dy = 0.1
    # dt = rho * c * dx * dx / 2 / lam / 1000000

    print(dt)


    for i in range(0, len(X), 2):
    # for i in range(0, len(X)):
    #     if not i % 2:
    #         left_bound.append(X[i])
    #     else:
    #         right_bound.append(X[i])
    #     for _ in range(int(1 / dx)):
            left_bound.extend([X[i]] * int(1 / dx))
            right_bound.extend([X[i + 1]] * int(1 / dx))

    print('Заданы Г. У.')

    x = np.arange(min(left_bound), max(right_bound) + 1, dx)
    y = np.arange(bottom_bound, top_bound + 1, dy)

    print(f'Построена сетка {len(x)}x{len(y)}')

    T0 = [[38 for _ in y] for _ in x]
    T1 = [[0 for _ in y] for _ in x]

    TT = {}

    print('Заданы Н. У.')

    k = lam * dt / rho / c
    kx = dt / (dx * dx)
    ky = dt / (dy * dy)

    n = len(x)
    m = len(y)

    while t <= t_max:
        for i in range(n):
            for j in range(m):
                if x[i] < left_bound[j] or x[i] > right_bound[j]:
                    continue
                elif x[i] == left_bound[j]:
                    T1[i][j] = Tleft
                    # if j == 0:
                    #     T1[i][j] = (T0[i][j] + kx * (Tleft - 2 * T0[i][j] + T0[i + 1][j])
                    #                 + ky * (Tbottom - 2 * T0[i][j] + T0[i][j + 1]))
                    # elif j == m - 1:
                    #     T1[i][j] = (T0[i][j] + kx * (Tleft - 2 * T0[i][j] + T0[i + 1][j])
                    #                 + ky * (T0[i][j - 1] - 2 * T0[i][j] + Ttop))
                    # else:
                    #     T1[i][j] = (T0[i][j] + kx * (Tleft - 2 * T0[i][j] + T0[i + 1][j])
                    #                 + ky * (T0[i][j - 1] - 2 * T0[i][j] + T0[i][j + 1]))
                elif x[i] == right_bound[j]:
                    T1[i][j] = Tright
                    # if j == 0:
                    #     T1[i][j] = (T0[i][j] + kx * (T0[i - 1][j] - 2 * T0[i][j] + Tright)
                    #                 + ky * (Tbottom - 2 * T0[i][j] + T0[i][j + 1]))
                    # elif j == m - 1:
                    #     T1[i][j] = (T0[i][j] + kx * (T0[i - 1][j] - 2 * T0[i][j] + Tright)
                    #                 + ky * (T0[i][j - 1] - 2 * T0[i][j] + Ttop))
                    # else:
                    #     T1[i][j] = (T0[i][j] + kx * (T0[i - 1][j] - 2 * T0[i][j] + Tright)
                    #                 + ky * (T0[i][j - 1] - 2 * T0[i][j] + T0[i][j + 1]))
                else:
                    if j == 0:
                        T1[i][j] = (T0[i][j] + kx * (T0[i - 1][j] - 2 * T0[i][j] + T0[i + 1][j])
                                    + ky * (Tbottom - 2 * T0[i][j] + T0[i][j + 1]))
                    elif j == m - 1:
                        T1[i][j] = (T0[i][j] + kx * (T0[i - 1][j] - 2 * T0[i][j] + T0[i + 1][j])
                                    + ky * (T0[i][j - 1] - 2 * T0[i][j] + Ttop))
                    else:
                        # print(i, j)
                        T1[i][j] = (T0[i][j] + kx * (T0[i - 1][j] - 2 * T0[i][j] + T0[i + 1][j])
                                    + ky * (T0[i][j - 1] - 2 * T0[i][j] + T0[i][j + 1]))

        # TT[t] = T1.copy()
        TT[t] = [[0 for _ in y] for _ in x]
        for i in range(len(T1)):
            for j in range(len(T1[0])):
                TT[t][i][j] = T1[i][j]
        print(f'{t:.2f}')
        t += dt
        T0 = T1.copy()

    # for i in range(n):
    #     for j in range(m):
    #         print(f'{T0[i][j]:.2f}', '\t', sep='', end='')
    #     print('\n')

    TTT = {}
    for t, temp in TT.items():
        TTT[t] = [[0 for _ in x] for _ in y]

    # TTT

    for t, temp in TT.items():
        for i in range(n):
            for j in range(m):
                TTT[t][j][i] = TT[t][i][j]
        # TT[t] = T.copy()


    return TTT

    # temp = plt.imshow(T)
    # plt.colorbar(temp)
    # plt.show()

    c=1


if __name__ == '__main__':
    compute(1)
