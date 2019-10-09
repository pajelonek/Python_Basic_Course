def main():
    new_list = [1, 2, 14, 12, 123, 421, 12, 123, 421, 12, 1, 2]
    new_string = ""
    for i in new_list:
        new_string += str(i).zfill(3)

    print(new_string)


if __name__ == "__main__":
    main()
