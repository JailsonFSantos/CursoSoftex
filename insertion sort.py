def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1       
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


data = [19,23,53,43,51,11,37,59,3,9,35,25,27,33,5,31,57,17,59,45,1,15,13,29,39,49,41,55,21,7,47,]
insertionSort(data)
print(data)