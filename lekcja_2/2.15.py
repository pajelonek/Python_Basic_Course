# Na liście L znajdują się liczby całkowite dodatnie.
# Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.


def main():
    new_list = [1, 15, 23, 51, 23]
    new_string = ""
    for i in new_list:
        new_string += str(i)
    print(new_string)


if __name__ == "__main__":
    main()
