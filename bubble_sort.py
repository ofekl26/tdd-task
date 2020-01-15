def bubble_sort():
    arr = []

    try:
        for i in range(10):
            arr.append(float(input()))
    except ValueError:
        print("only numbers are accepted as valid input.")
    print(arr)
    for i in range(10):
        for j in range(0, 10 - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


bubble_sort()
