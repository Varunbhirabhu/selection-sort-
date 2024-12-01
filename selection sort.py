def selectionsort (a):
    for i in range(0,len(a)-1):
        smallest = i
        for j in range(i+1,len(a)):
            if a[j]< a[smallest]:
                smallest = j

        temp = a[smallest]
        a[smallest] = a[i]
        a[i] = temp

a=[10,5,65,34,3,2]
selectionsort(a)
print(a)

             
        
