import sys


def task_3_3():
    sys.stdout.write("3.3: ")
    for i in range(0, 30):
        if i % 3 != 0:
            sys.stdout.write(str(i) + " ")
    sys.stdout.write('\n')


def main():
    task_3_3()


if __name__ == "__main__":
    main()
