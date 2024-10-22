def selection_sort(N, array):
    
    for index in range(0, N):
        minimum_index = index
        for index1 in range(index+1, N):
            if array[index1] < array[minimum_index]:
                minimum_index = index1
            array[index], array[minimum_index] = array[minimum_index], array[index]
    return array            

    
    
    
    

n = 6
array = [13,46,24,52,20,9]
 
print(selection_sort(n, array))



    
