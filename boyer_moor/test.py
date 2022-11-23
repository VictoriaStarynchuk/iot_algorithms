import time
from boyer_moor.boyer_moor_algorithm import main

def test_avarage():
    with open("resources/avarage_case.txt", "r") as file:
        text = str(file.read())
    search_pattern = "absababab"

    start = time.time()
    main(text, search_pattern)
    end = time.time()

    print("Normal case")
    print(f"Time complexity is : {(end-start) * 10**3:.03f}ms \n")


def test_worst():
    with open("resources/worst_case.txt", "r") as file:
        text = str(file.read())
    search_pattern = "kkkkkkk"

    start = time.time()
    main(text, search_pattern)
    end = time.time()

    print("Worst case")
    print(f"Time complexity is: {(end-start) * 10**3:.03f}ms \n")


def test_best():
    with open("resources/best_case.txt", "r") as file:
        text = str(file.read())
    search_pattern = "abbddmnkk"

    start = time.time()
    main(text, search_pattern)
    end = time.time()

    print("Best case")
    print(f"Time complexity is : {(end-start) * 10**3:.03f}ms \n")


if __name__ == '__main__':
    test_avarage()
    test_worst()
    test_best()