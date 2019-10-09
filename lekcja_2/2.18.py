# Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na napis.


def main():
    big_number = 1234012301230130103120310
    print(len(str(big_number)) - len(str(big_number).replace('0', '')))


if __name__ == "__main__":
    main()
