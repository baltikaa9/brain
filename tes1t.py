def main():
    T1 = [123]

    T2 = T1[::]

    T1.append(5)
    print(T2)


if __name__ == '__main__':
    main()
