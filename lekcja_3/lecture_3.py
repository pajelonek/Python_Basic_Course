import sys


def task_3_3():
    sys.stdout.write("3.3: ")
    for i in range(0, 30):
        if i % 3 != 0:
            sys.stdout.write(str(i) + " ")
    sys.stdout.write('\n')


def task_3_5(length):
    print("3.5:")
    measure = "|"
    for i in range(1, length + 1):
        measure += "....|"

    measure += "\r\n0"

    for i in range(1, length + 1):
        digits = len(str(i))
        measure += ((5 - digits) * ".")
        measure += str(i)

    print(measure)


def task_3_6(x, y):
    print("3.6:")
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


def task_3_8(first_seq, second_seq):
    new_list = []
    for i in set(first_seq):
        if i in second_seq:
            new_list.append(i)
    print("3.8: a)" + str(new_list) + ", b)" + str(list(set("".join(first_seq + second_seq)))))


def task_3_9(first_seq):
    new_list = []
    for element in first_seq:
        sum_of_elements = 0
        for inner_element in element:
            sum_of_elements += inner_element
        new_list.append(sum_of_elements)
    print("3.9: " + str(new_list))


def task_3_10(roman):
    rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    val = rom_dict[roman[0]]
    for i in range(1, len(roman) - 1):
        if rom_dict[roman[i]] < rom_dict[roman[i + 1]]:
            val -= rom_dict[roman[i]]
        else:
            val += rom_dict[roman[i]]
    val += rom_dict[roman[len(roman) - 1]]
    print("3.10: " + str(val))


def main():
    test1 = ["t", "e", "roman", "t", "1", "2", "3"]
    test2 = ["t", "e", "x", "t", "3", "2", "5"]

    task_3_3()
    task_3_5(19)
    task_3_6(5, 3)
    task_3_8(test1, test2)
    task_3_9([[], [4], (1, 2), [3, 4], (5, 6, 7)])
    task_3_10("MMMCMLXXXVI")


if __name__ == "__main__":
    main()
