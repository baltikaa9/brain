import math

import numpy as np

from draw import get_points
from draw import open_image

# Параметры крови (для уравнения Пеннеса)
rho_blood = 1060  # кг/м³
cp_blood = 3617  # Дж/(кг·К)
Ta = 37.0  # Температура артериальной крови (°C)

# Скорость перфузии (зависит от ткани)
w_b_gray = 0.008  # Серое вещество (1/с)
w_b_white = 0.0008  # Белое вещество (1/с)
w_b_other = 0.0001  # Остальные ткани (1/с)

# Метаболическое тепловыделение (Вт/м³)
Q_met_gray = 8000  # Серое вещество
Q_met_white = 4000  # Белое вещество
Q_met_other = 100  # Остальные ткани

props = {
    "gray": {"rho": 1040, "cp": 3650, "lam": 0.51},
    "white": {"rho": 1040, "cp": 3650, "lam": 0.49},
    "other": {"rho": 1908, "cp": 1300, "lam": 0.32}
}


def thermal_conductivity(layer: int) -> dict[list[list[float]]]:
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
                elif x[i] == right_bound[j]:
                    T1[i][j] = Tright
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

def pennes(
    points: tuple[list[float], list[float]],
    T_outside: float = 0.0,
    T_left: float = 100.0,
    T_right: float = 100.0,
    T_bottom: float = 100,
    T_top: float = 100,
    t_max: float = 10,
    dx: float = 1,
    dt: float = 0.1,
    lam: float = 0.251,
    c: float = 3150,
    rho: float = 1108,
    T_init: float = 38,
) -> dict[float, np.ndarray]:
    X, Y = points
    # t_max = 10
    t = 0
    left_bound = []
    right_bound = []
    bottom_bound = min(Y)
    top_bound = max(Y)
    dy = dx
    # dt = 0.1

    # Параметры уравнения Пеннеса
    # lam = 0.251  # Теплопроводность (Вт/(м·°C))
    # rho = 1108  # Плотность (кг/м³)
    # c = 3150  # Теплоемкость (Дж/(кг·°C))
    rho_blood = 1060  # Плотность крови
    cp_blood = 3617  # Теплоемкость крови
    Ta = 37.0  # Температура артерий
    w_b = 0.008  # Перфузия
    Q_met = 8000  # Метаболизм

    # Генерация границ
    for i in range(0, len(X), 2):
        left_bound.extend([X[i]] * int(1 / dx))
        right_bound.extend([X[i + 1]] * int(1 / dx))


    x = np.round(np.arange(min(left_bound), max(right_bound) + 1, dx), 3)
    y = np.round(np.arange(bottom_bound, top_bound + 1, dy), 3)
    n = len(x)
    m = len(y)

    print('init start', n, m)

    T0 = np.full((n, m), T_outside, dtype=np.float64)

    print('Инициализация температуры')

    for i in range(n):
        for j in range(m):
            # print(f'итерация {i*m+j} / {m*n}')
            if left_bound[j] < x[i] < right_bound[j]:
                if y[j] == bottom_bound:
                    T0[i][j] = T_bottom
                elif y[j] == top_bound:
                    T0[i][j] = T_top
                else:
                    T0[i][j] = T_init  # Начальная температура внутри головы
            elif x[i] == left_bound[j]:
                T0[i][j] = T_left  # Используем параметр T_left
            # Для правой границы
            elif x[i] == right_bound[j]:
                T0[i][j] = T_right  # Используем параметр T_right


    print('init end')
    # print(T0)

    TT = {0: T0}
    k = lam * dt / (rho * c) * 1000000

    while t <= t_max:
        T1 = np.copy(T0)
        for i in range(n):
            for j in range(m):
                if x[i] <= left_bound[j] or x[i] >= right_bound[j]:
                    continue
                    
                if y[j] <= bottom_bound or y[j] >= top_bound:
                    continue

                laplacian = (T0[i - 1, j] - 2 * T0[i, j] + T0[i + 1, j]) / (dx ** 2) \
                            + (T0[i, j - 1] - 2 * T0[i, j] + T0[i, j + 1]) / (dy ** 2)

                # Уравнение Пеннеса
                perfusion = (w_b * rho_blood * cp_blood * (Ta - T0[i][j])) / (rho * c)
                metabolism = Q_met / (rho * c)
                T1[i][j] = T0[i][j] + k * laplacian + dt * (perfusion + metabolism)

        TT[round(t, 2)] = T1.copy()
        T0 = T1.copy()
        if abs(t - round(t)) < 1e-6: print(round(t))
        t += dt

    return TT
