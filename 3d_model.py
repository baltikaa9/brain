import numpy as np
from matplotlib import pyplot as plt


def main():
    # Задаем параметры модели
    L = 0.1  # Длина области моделирования, м
    T = 600  # Время моделирования, с
    dx = 0.001  # Шаг по пространству, м
    dt = 0.1  # Шаг по времени, с

    # Создаем сетку
    x = np.arange(0, L + dx, dx)
    t = np.arange(0, T + dt, dt)
    nx = len(x)
    nt = len(t)

    # Задаем начальные и граничные условия
    T0 = 36  # Начальная температура, °C
    Tleft = 38  # Левая граница, °C
    Tright = 40  # Правая граница, °C
    T = np.ones((nt, nx)) * T0
    T[:, 0] = Tleft
    T[:, -1] = Tright

    # Решаем уравнение теплопроводности методом конечных разностей
    k = 0.6  # Коэффициент теплопроводности, Вт/(м*°C)
    rho = 1000  # Плотность тканей, кг/м^3
    c = 3700  # Удельная теплоемкость тканей, Дж/(кг*°C)
    alpha = k / (rho * c)
    for n in range(0, nt - 1):
        for i in range(1, nx - 1):
            T[n + 1, i] = T[n, i] + alpha * dt / dx ** 2 * (T[n, i + 1] - 2 * T[n, i] + T[n, i - 1])

    # Визуализируем результаты

    for i, _T in enumerate(T):
        if not i % 10:
            print(f'{int(i/10)} c: {list(_T)}')


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X, Tt = np.meshgrid(x, t)
    ax.plot_surface(X, Tt, T, cmap='coolwarm')
    ax.set_xlabel('x, м')
    ax.set_ylabel('t, с')
    ax.set_zlabel('T, °C')
    plt.show()


if __name__ == '__main__':
    main()
