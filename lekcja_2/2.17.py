def main():
    line = "am\t i\n python\tlong_word\ns"
    print(sorted(line.split(), key=len))
    print(sorted(line.split()))


if __name__ == "__main__":
    main()
