def iterate_set(set):
    for val in set:
        print(val, end = "")

def main():
    a = set()
    a.add(True)
    a.add("Poop")
    print(a)
    
    b = {"Apollo XXI", "Atlanta Millionaires Club"}
    print("Length of Album Set:", len(b))
    b.remove("Apollo XXI")
    print(b)
    
    c = set("Christian")
    for _ in range(10):
        iterate_set(c)
        print()

if __name__ == "__main__":
    main()