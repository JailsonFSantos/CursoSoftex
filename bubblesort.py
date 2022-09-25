def bubble_sort(ulist):
    for j in range(len(ulist) - 1):
        for i in range(len(ulist) - 1):
            if ulist[i] > ulist[i+1]:
                ulist[i], ulist[i+1] = ulist[i+1], ulist[i]
                print(ulist)
    return ulist
 
bubble_sort([9, 25, 34, 529, 51, 44, 29, 91, 84, 2])