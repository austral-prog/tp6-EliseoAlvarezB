list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
def remove_elements(list):
    if len(list) == 6:
        list.pop(5)
        list.pop(4)
        list.pop(0)
        return list
    elif len(list) == 5:
        list.pop(4)
        list.pop(0)
        return list
    elif len(list) > 0:
        list.pop(0)
        return list
    
    return list 
    
list = ['Red', 'Green', 'White', 'Black']
def add_elements(list):
    listLen = len(list)
    list.insert(0, "Pink")
    list.insert(listLen+1, "Yellow") # Tambien se puede hacer con list.append(yellow)
    return list

list = ['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White']
list2 = ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']
def is_empty(list):
    if len(list) == 0:
        return True
    else:
        return False
def check_lists(list, list2):
    if len(list) >= 3 and len(list2) >= 3:
        if list[2] == list2[2]:
            return True
        else:
            return False

list = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]
def list_of_lists(list):
    newList = [[],[],[]]
    
    newList[0] = (list[0][0:2])
    newList[1] = (list[1][1:4])
    newList[2] = (list[2][-2:])

    return newList
list_of_lists(list)