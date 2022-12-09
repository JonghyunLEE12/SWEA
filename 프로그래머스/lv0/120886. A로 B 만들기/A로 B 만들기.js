function solution(before, after) {
    // 정렬하여 각 인덱스를 비교함
    before = [...before].sort()
    after = [...after].sort()
    return before.filter((a,i) => a === after[i]).length === after.length ? 1 : 0
}