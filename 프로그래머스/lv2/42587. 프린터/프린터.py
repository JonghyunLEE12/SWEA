def solution(priorities, location):
    answer = 0
    
    arr1 = [ a for a in range(len(priorities))]
    arr2 = priorities.copy()
    i = 0
    while True:
        if arr2[i] < max(arr2[i+1:]):
            arr1.append(arr1.pop(i))
            arr2.append(arr2.pop(i))
        else:
            i += 1
        
        if arr2 == sorted(arr2, reverse=True):
            break
    return arr1.index(location) + 1