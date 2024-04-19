# this is a binary search
# this is the array, the numbers must be in the correct order 
array = [1,4,6,34,63,79,99,128,173,181,182,198,201,205]

# initialising variables 
start = 0
end = len(array)
Sort = False
passes = 0
number_to_find = int(input("Wanted Number: ")) # user input for the number to search for

while Sort == False and start < end:
    mid = (start + end) // 2 # makes midpoint within the first loop because it needs to change 
    if number_to_find == array[mid]:
        Sort = True
        print("Found! It took " + str(passes) + " passes")
    elif number_to_find > array[mid]: 
        start = mid - 1
    else:
        end = mid + 1
    passes += 1
