import heapq

def solution(operations):
    answer = [0,0]
    
    heaq = []
    max_heaq = []
    
    for op in operations:
        current = op.split()
        if current[0] == 'I':
            number =  int(current[1])
            heapq.heappush(heaq,number)
            heapq.heappush(max_heaq,(number*-1,number))
        else:
            if len(heaq) == 0:
                pass
            elif current[1] == '1':
                max_value = heapq.heappop(max_heaq)[1]
                heaq.remove(max_value)
            elif current[1] == '-1':
                min_value = heapq.heappop(heaq)
                max_heaq.remove((min_value*-1,min_value))
                
    
    if heaq:
        return [heapq.heappop(max_heaq)[1],heapq.heappop(heaq)]
    return answer