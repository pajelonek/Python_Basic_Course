# Podać sposób wyświetlania napisu word tak,
# aby jego znaki były rozdzielone znakiem podkreślenia.
import sys


def main():
    word = "word"
    for i in range(0, len(word) - 1):
        sys.stdout.write(word[i] + "_")
    sys.stdout.write(word[len(word) - 1])


if __name__ == "__main__":
    main()
