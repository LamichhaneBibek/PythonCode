def largest(arr, n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
            return max
            arr = [5, 10, 15, 2, 3, 12, 55, 23, 34, 45]
            n = len(arr)
            large = largest(arr, n)
            print("Largest in the given array is ", large)
