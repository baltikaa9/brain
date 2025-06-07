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

def pennes(
    points: tuple[list[float], list[float]],
    T_outside: float = 0.0,
    t_max: float = 10,
    dx: float = 1,
    dt: float = 0.1,
    lam: float = 0.251,
    c: float = 3150,
    rho: float = 1108,
    T_init: float = 38,
) -> dict[float, np.ndarray]:
    X, Y = points
    t = 0
    left_bound = []
    right_bound = []
    bottom_bound = min(Y)
    top_bound = max(Y)
    dy = dx

    # Параметры уравнения Пеннеса
    # lam = 0.251  # Теплопроводность (Вт/(м·°C))
    # rho = 1108  # Плотность (кг/м³)
    # c = 3150  # Теплоемкость (Дж/(кг·°C))
    rho_blood = 1060  # Плотность крови
    cp_blood = 3617  # Теплоемкость крови
    Ta = 37.0  # Температура артерий
    w_b = 0.008  # Перфузия
    Q_met = 8000  # Метаболизм
    cf = 1000000

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
            if left_bound[j] < x[i] < right_bound[j]:
                T0[i][j] = T_init
            else:
                T0[i][j] = T_outside

    print('init end')

    TT = {0: T0}
    k = lam * dt / (rho * c) * cf

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

        for j in range(m):
            # левая граница: i=0
            if left_bound[j] <= x[0] <= right_bound[j]:
                T1[0, j] = T1[1, j]

            # правая граница: i = n-1
            if left_bound[j] <= x[n - 1] <= right_bound[j]:
                T1[n - 1, j] = T1[n - 2, j]

        for i in range(n):
            # нижняя граница: j=0
            if left_bound[0] < x[i] < right_bound[0]:
                T1[i, 0] = T1[i, 1]

            # верхняя граница: j = m-1
            if left_bound[m - 1] < x[i] < right_bound[m - 1]:
                T1[i, m - 1] = T1[i, m - 2]

        TT[round(t, 2)] = T1.copy()
        T0 = T1.copy()
        if abs(t - round(t)) < 1e-6: print(round(t))
        t += dt

    return TT
