import sys


def task_2_10(line):
    result = str(len(line.split()))
    print("2.10: " + result)


def task_2_11(word):
    sys.stdout.write("2.11: ")
    for i in range(0, len(word) - 1):
        sys.stdout.write(word[i] + "_")
    sys.stdout.write(word[len(word) - 1] + "\r\n")


def task_2_12(line):
    string_from_first_letters = ''
    string_from_last_letters = ''
    for word in line.split():
        string_from_first_letters += word[0]
        string_from_last_letters += word[len(word) - 1]
    print("2.12: " + string_from_first_letters + " " + string_from_last_letters)


def task_2_13(line):
    print("2.13: " + str(len("".join(line.split()))))


def task_2_14(line):
    longest = max(line.split(), key=len)
    size_of_longest = len(longest)
    print("2.14: longest = " + longest + ", size of longest " + str(size_of_longest))


def task_2_15(new_list):
    new_string = ""
    for i in new_list:
        new_string += str(i)
    print("2.15: " + new_string)


def task_2_16(line):
    print("2.16: " + line.replace("GvR", "Guido van Rossum"))


def task_2_17(line):
    length = sorted(line.split(), key=len)
    alphabet = sorted(line.split())
    print("2.17: dlugosc = " + str(length) + ", alfabet = " + str(alphabet))


def task_2_18(big_number):
    result = len(str(big_number)) - len(str(big_number).replace('0', ''))
    print("2.18: " + str(result))


def task_2_19(new_list_2):
    new_string = ""
    for i in new_list_2:
        new_string += str(i).zfill(3)

    print("2.19: "+new_string)


def main():
    line = "am\t i\n python\tlong_word\ns"
    line_for_sub = "I\t GvR\n python"
    new_list = [1, 15, 23, 51, 23]
    new_list_2 = [1, 2, 14, 12, 123, 421, 12, 123, 421, 12, 1, 2]
    big_number = 1234012301230130103120310

    task_2_10(line)
    task_2_11("word")
    task_2_12(line)
    task_2_13(line)
    task_2_14(line)
    task_2_15(new_list)
    task_2_16(line_for_sub)
    task_2_17(line)
    task_2_18(big_number)
    task_2_19(new_list_2)


if __name__ == "__main__":
    main()
