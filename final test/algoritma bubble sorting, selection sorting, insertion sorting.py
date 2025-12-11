# sorting.py

# =========================
# 1. Bubble Sort
# =========================
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # iterasi membandingkan elemen
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # tukar elemen
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# =========================
# 2. Selection Sort
# =========================
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # anggap elemen pertama sebagai yang terkecil
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # tukar elemen
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# =========================
# 3. Insertion Sort
# =========================
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # geser elemen yang lebih besar dari key ke kanan
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr


# =========================
# Contoh penggunaan
# =========================
if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]

    print("Data asli:", data)
    print("Bubble Sort:", bubble_sort(data.copy()))
    print("Selection Sort:", selection_sort(data.copy()))
    print("Insertion Sort:", insertion_sort(data.copy()))
