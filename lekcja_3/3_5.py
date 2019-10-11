#
# |....|....|....|....|....|....|....|....|....|....|....|....|
# 0    1    2    3    4    5    6    7    8    9   10   11   12
# MAX : 99999 !!!!!


def task_3_5(length):
    measure = "|"
    for i in range(1, length + 1):
        measure += "....|"

    measure += "\r\n0"

    for i in range(1, length + 1):
        digits = len(str(i))
        measure += ((5 - digits) * ".")
        measure += str(i)

    print(measure)


def main():
    task_3_5(999)


if __name__ == "__main__":
    main()
