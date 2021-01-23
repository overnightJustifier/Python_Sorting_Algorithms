def insertion_sort(InputList, inputLength):
    for i in range(1, inputLength):
        j = i-1
        next_element = InputList[i]
# Compare the current element with next one
        while (InputList[j] > next_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
        InputList[j+1] = nxt_element
# you can add list of any numbers
list = [6, 5, 3, 1, 8]
insertion_sort(list)
print(list)
