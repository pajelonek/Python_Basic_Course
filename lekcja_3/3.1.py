def main():

# Case a):
    x = 2; y = 3;
    if(x > y):
        result = x;
    else:
        result = y;
    print(result)
# Tak, sredniki sa warningami, mozna je stosowac


#   for i in "qwerty": if ord(i) < 100: print i

# Nie, for + instrukcje wewnetrzne musza znajdowac sie w innych rzedach po 4 spacjach i print(i)

    for i in "axby": print ord(i) if ord(i) < 100 else i


if __name__ == "__main__":
    main()