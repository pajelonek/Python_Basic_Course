# W tekście znajdującym się w zmiennej line zamienić ciąg znaków "GvR" na "Guido van Rossum"


def main():
    line = "I\t GvR\n python"
    print(line.replace("GvR", "Guido van Rossum"))


if __name__ == "__main__":
    main()
