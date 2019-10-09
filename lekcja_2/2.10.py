# Mamy dany napis wielowierszowy line.
# Podać sposób obliczenia liczby wyrazów w napisie.
# Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony
# od innych wyrazów białymi znakami (spacja, tabulacja, newline).


def main():
    line = "I\t am\n python"
    print(len(line.split()))


if __name__ == "__main__":
    main()
