#
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+


def task_3_5(x, y):
    template = "+"
    for i in range(0, x):
        template += "---+"

    template += "\r\n|"
    for i in range(0, x):
        template += "   |"
    draw = ""
    for i in range(0, y):
        draw += template + "\r\n"
    draw += "+"
    for i in range(0, x):
        draw += "---+"

    print(draw)


def main():
    task_3_5(5, 3)


if __name__ == "__main__":
    main()
