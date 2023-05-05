if __name__ == '__main__':
    meslina = "Meslina"
    str1 = "Hello " + meslina

    def basamak_sayisi(number):
        return len(str(number))

    n = 1000
    for i in range(0, n):
        b = basamak_sayisi(n) - basamak_sayisi(i + 1)
        bosluk = " " * b
        print(bosluk + str(i + 1) + ": " + str1)