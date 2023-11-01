def solution(k, ranges):
    def get_coords(k):
        ret = []
        while k != 1:
            ret.append(k)
            k = k // 2 if k % 2 == 0 else k * 3 + 1
        ret.append(k)
        return ret

    def get_integrals(coords):
        integrals = []
        for i, coord in enumerate(coords[:-1]):
            y1, y2 = coord, coords[i + 1]
            integrals.append(min(y1, y2) + abs(y1 - y2) / 2)
        return integrals

    answer = []
    coords = get_coords(k)
    integrals = get_integrals(coords)

    n = len(coords)

    for ran in ranges:
        x1, x2 = ran
        x2 = x2 if x2 > 0 else n + x2 - 1
        if x1 > x2:
            answer.append(-1)
            continue
        SUM = 0
        for i in range(x1, x2):
            SUM += integrals[i]
        answer.append(SUM)

    return answer