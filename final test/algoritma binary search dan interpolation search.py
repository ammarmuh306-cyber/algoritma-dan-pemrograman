#binary search
def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Contoh penggunaan
if __name__ == "__main__":
    data = [5, 8, 12, 15, 20, 28, 33, 40]
    cari = 20

    hasil = binary_search(data, cari)
    print("Hasil:", hasil)
  

#inter polation search
def interpolation_search(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right and x >= arr[left] and x <= arr[right]:

        # Menghindari pembagian nol
        if arr[left] == arr[right]:
            if arr[left] == x:
                return left
            return -1

        # Rumus interpolasi
        pos = left + ((x - arr[left]) * (right - left)) // (arr[right] - arr[left])

        if pos < 0 or pos >= len(arr):
            return -1

        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            left = pos + 1
        else:
            right = pos - 1

    return -1


# Contoh penggunaan
if __name__ == "__main__":
    data = [5, 8, 12, 15, 20, 28, 33, 40]
    cari = 28

    hasil = interpolation_search(data, cari)
    print("Hasil:", hasil)
