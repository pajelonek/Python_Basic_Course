# Posortować wyrazy z napisu line raz alfabetycznie, a raz pod względem długości.
# Wskazówka: funkcja wbudowana sorted().


def main():
    line = "am\t i\n python\tlong_word\ns"
    print(sorted(line.split(), key=len))
    print(sorted(line.split()))


if __name__ == "__main__":
    main()
