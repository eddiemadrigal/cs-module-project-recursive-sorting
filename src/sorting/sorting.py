# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):                                      # define merge function
    if arrA and arrB:                                       # if arrA and arrB are present
        if arrA == [] and arrB == []:                       # if arrA and arrB are both empty
            return []                                       # return nothing (exit)
        if arrA[0] > arrB[0]:                               # if array A at position 0 is greater than B at the same 0
            arrA, arrB = arrB, arrA                         # swap the arrays B is on the left (less than) and A is on the right (greater than)
        return [arrA[0]] + merge(arrA[1:], arrB)            # return element at position 0 and run the function again, moving to the right at each iteration
    return arrA + arrB                                      # when nothing is left to iterate, concat and return both arrays

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):                                        # define the merge_sort function
    if len(arr) <= 1:                                       # if arr(ay) has no or one piece of content
        return arr                                          # return the arr(ay) as is
    x = len(arr) // 2                                       # find the middle of the array
    return merge(merge_sort(arr[:x]), merge_sort(arr[x:]))  # call the merge function. while there, call the merge_sort function to continue sorting, always halfing the array and figuring out what goes to the right and what value goes to the left

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    pass
    # Your code here

