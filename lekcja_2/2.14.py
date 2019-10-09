# Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line.


def main():
    line = "am\t I\n python\tlong_word\ns"
    # Longest word in 'line'
    print(max(line.split(), key=len))
    # Size of longest word in 'line'
    print(len(max(line.split(), key=len)))


if __name__ == "__main__":
    main()
