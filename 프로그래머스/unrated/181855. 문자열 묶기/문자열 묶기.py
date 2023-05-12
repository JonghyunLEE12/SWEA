def solution(strArr):
    answer = 0
    
    dp = [0]*len(strArr)
    
    for i in range(len(strArr)):
        dp[i] = len(strArr[i])
    
    
    countDict = {}
    for num in dp:
        countDict[num] = 0
    
    for num in dp:
        countDict[num] += 1
    
    answer = max(countDict.values())
    return answer