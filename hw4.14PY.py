def print_list(lst, i):
    if i < len(lst):
        print(lst[i])
        print_list(lst, i+1)
    else:
        print("Конец списка")

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print_list(my_list, 0)