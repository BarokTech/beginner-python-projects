'''
BinarySearch program
It checks the exsistence of a number in a list and displays 
its positon if it exists

'''
num = input("Input the number you want to search: ")
n = int(num)
array = [2, 3, 5, 8, 13, 18, 42]

def search(array, n):
    #declaring the upper and the lower indices in the array
    low = 0
    up = len(array) - 1
    

    while low <= up:
        #calculating the mid value with floor division to avoid decimals
        mid = (up + low) // 2

        if array[mid] == n:
            #declaring the position varible as global for it to be used outside the function
            global pos
            pos = mid + 1
            return True

        elif array[mid] < n:
            #updates the lower value to ignore the lower half
            low = mid + 1

        else:
            #updates the upper value to ignore the upper half
            up = mid - 1
    #returns false if the value is not in the list
    return False




#Takes the return value from the function
rep = search(array, n)
#checking the returns and displaying the output to the user
if rep:
    print(f"The number is found at position {pos}")
else:
    print("The number is not found!")
