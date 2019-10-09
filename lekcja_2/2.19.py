# Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie.
# Chcemy zbudować napis z trzycyfrowych bloków, gdzie liczby j
# edno- i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill().


def main():
    new_list = [1, 2, 14, 12, 123, 421, 12, 123, 421, 12, 1, 2]
    new_string = ""
    for i in new_list:
        new_string += str(i).zfill(3)

    print(new_string)


if __name__ == "__main__":
    main()
