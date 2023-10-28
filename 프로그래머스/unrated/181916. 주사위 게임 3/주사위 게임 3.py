def solution(a, b, c, d):

    dice = [a, b, c, d] # 주사위의 숫자들을 리스트에 저장
    abcd = dict() # 각 숫자의 등장 횟수를 저장할 딕셔너리를 생성
   
    # 주사위의 숫자들을 하나씩 확인하면서
    for num in dice:
        if num not in abcd: # 해당 숫자가 딕셔너리에 없다면 새로 추가하고,
            abcd[num] = 1
        else: # 있다면 등장 횟수를 1 증가
            abcd[num] += 1

    # 딕셔너리의 키를 등장 횟수에 따라 정렬
    abcd = sorted(abcd, key=lambda x:abcd[x])

    if len(abcd) == 1: # 주사위에서 나온 숫자가 모두 같을 때,
        return 1111 * a
   
    elif len(abcd) == 2: # 주사위에서 나온 숫자가 3개 일 때,
        if dice.count(abcd[0]) in [1, 3]: # 세 주사위에서 같은 값을 가지는 경우
            return (10 * abcd[1] + abcd[0]) ** 2
       
        else: # 주사위가 2개씩 같은 값을 가지는 경우
            return (abcd[0] + abcd[1]) * abs(abcd[0] - abcd[1])
       
    elif len(abcd) == 3: # 주사위에서 나온 숫자가 3개 일 때,
        return abcd[0] * abcd[1]
   
    # 주사위에서 나온 숫자가 모두 다를 때, 가장 작은 값을 반환
    return min(dice)