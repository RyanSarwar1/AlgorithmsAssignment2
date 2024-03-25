#Ryan Sarwar 100825599 INFR2080U Assignment 2

import pygame

# Initialize pygame mixer
pygame.mixer.init()
# Load the sound
swap_sound = pygame.mixer.Sound('swap_sound.wav')

def merge(arr, l, m, r):
    # Create temporary arrays to hold copies of the left and right subarrays
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    # Copy data to temporary arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temporary arrays back into arr[l..r]
    index_one = 0  # Initial index of the first subarray
    index_two = 0  # Initial index of the second subarray
    index_merge = l  # Initial index of the merged subarray

    while index_one < n1 and index_two < n2:
        if L[index_one] <= R[index_two]:
            arr[index_merge] = L[index_one]
            index_one += 1
        else:
            arr[index_merge] = R[index_two]
            index_two += 1
            # Play the swap sound effect
            swap_sound.play()
        index_merge += 1

    # Copy any remaining elements of L[], if there are any
    while index_one < n1:
        arr[index_merge] = L[index_one]
        index_one += 1
        index_merge += 1

    # Copy any remaining elements of R[], if there are any
    while index_two < n2:
        arr[index_merge] = R[index_two]
        index_two += 1
        index_merge += 1

def merge_sort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)

        print(f"Sorting...: {arr[l:r+1]}")  # Print current state of the array

# Driver code to test the corrected code
if __name__ == "__main__":
    arr = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
    print("Inputted Array:", arr)
    merge_sort(arr, 0, len(arr) - 1)
    print("Sorted Array:", arr)

