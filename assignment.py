"""
This is if the array is of length greater than 2 because otherwise there will not be an upper and lower bound
since its not mentioned whether its just a positive or negative integer array and even after that there will be
some concerns. So, I will be returning the array as it is.

Also, in case there is no element in the array I will be returning an empty array.

We can not simply use list comprehension as in Python 3 a generator object is generated instead of list.

So I went for the longer solution.
"""


def missing_range(arr):
    missing_ele_arr = []
    if len(arr) > 1:
        for i in range(len(arr)-1):
            if arr[i+1] > arr[i]+1:
                for j in range(arr[i]+1, arr[i+1], 1):
                    missing_ele_arr.append(j)
    else:
        missing_ele_arr = arr
    return missing_ele_arr


if __name__ == '__main__':
    array = [0, 1, 3, 5, 21]
    print(missing_range(array))
