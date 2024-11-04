"""
This code will identify the biggest subarray containing the same number of
0s and 1s.
"""


def Longest_subarray(array):
    length = 0

    if len(array) < 2: #Base case to avoid errors
        return 0

    for size in range(2, len(array) + 1): #First loop for different subarray sizes

        for i in range(len(array) - size + 1): # Second loop for setting start and finish of each subarray within the main array. 
            counter = 0 # Counter to help us identify whether digit is 0 or 1.

            for j in range(i,size+i): # Third loop for iterating through each element
                if array[j] == 0:
                    counter += 1
                else:
                    counter -= 1

            if counter == 0:
                length = size # Setting the length based on the number of 1s and 0s.

    return length


# In this exercise I am using a different appraoch to entering the array of numbers.
# this approach is not optimal as it may present runtime errors.

n = input("Please enter your array of 0s and 1s: ")
array = []
for i in n:
    array.append(int(i))

print(f"Your array: {array}")
print(f"The largest subarray's length is {Longest_subarray(array)}")
