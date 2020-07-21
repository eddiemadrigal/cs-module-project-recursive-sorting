# TO-DO: Implement a recursive implementation of binary search
def binary_search(A, key, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if key == A[mid]:
            return True
        elif key < A[mid]:
            return binary_search(A, key, low, mid-1)
        else:
            return binary_search(A, key, mid+1, high)

Arr = [2, 4, 22, 54, 76, 99, 108, 166]

found = binary_search(Arr, 108, 0, 8)

print(found)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass
    # Your code here

