def question_1(filename):
    with open(filename) as my_file:

        count = 0
        for line in my_file:
            if line.startswith("From:"):
                count += 1
        return count


def main():
    fariha = {}
    fariha["I"] = 4
    fariha["F"] = 1
    fariha["A"] = 6
    fariha["A"] = 2
    fariha["R"] = 3
    fariha["H"] = 5


    key_list = fariha.keys()
    print(key_list)

    for key in fariha.keys():
        print(fariha[key])

    print(fariha)
    print(fariha["F"])

main()