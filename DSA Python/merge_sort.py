def split(list):
    a = len(list)//2
    list1 = list[a:]
    list2 = list[:a] 
    return list1, list2
    
def merge(list1, list2):
    return list1 + list2          
def merge_sort(list):
    #we are sorting a list
    #so returns the sorted list
    #Divide the the list at its mid point
    #conquer:recursively sort the sub list.
    #merge the sublist all together
    if len(list) <= 1:
        return print(list)
    else:
        list_1, list_2 = split(list)    
        left1 = merge_sort(list_1)
        right2 = merge_sort(list_2)
        return print(merge(left1, right2))

list = [10, 5, 3, 2, 1]  
merge_sort(list)   
