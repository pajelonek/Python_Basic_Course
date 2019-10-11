def task_3_4():
    command = "stop"
    while True:
        text = input()
        if text == command:
            exit()
        try:
            number = float(text)
            third = number * number * number
            print(str(number) + " " + str(third))
        except ValueError:
            print("ValueError: Type number!")


def main():
    task_3_4()


if __name__ == "__main__":
    main()
