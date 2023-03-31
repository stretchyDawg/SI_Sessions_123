def sum_135(list):
    new_list = list[1:6:2]
    num = 0
    for number in new_list:
        num+=number
    return num

def even_string(list):
    new_list = list[0:len(list):2]
    new_str = ""
    for string in new_list:
        new_str += string
    return new_str


def main():
    lista = [10, 30, 25, 48, 91, 10]
    print(lista)
    print("First 3:", lista[0:3])
    print("Odd values:", lista[0:6:2])
    print("Even values:", lista[1:6:2])

    print("sum of indices 1, 3, 5:", sum_135(lista))
    print()

    listb = ["a", "b", "a", "b","a", "b", "a", "b","a", "b", "a", "b"]
    print(even_string(listb))



main()