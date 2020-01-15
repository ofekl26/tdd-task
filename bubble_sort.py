def bubble_sort():
    arr = []

    try:
        for i in range(10):
            arr.append(float(input()))
    except ValueError:
        print("only numbers are accepted as valid input.")

    print(arr)


bubble_sort()
