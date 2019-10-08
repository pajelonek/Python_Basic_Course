def main():
    line = "I\t am\n python"
    string_from_first_letters = ''
    string_from_last_letters = ''
    for word in line.split():
        string_from_first_letters += word[0]
        string_from_last_letters += word[len(word) - 1]
    print(string_from_first_letters)
    print(string_from_last_letters)


if __name__ == "__main__":
    main()
