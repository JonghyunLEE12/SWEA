function solution(array, n) {
    var answer = 0;
    const set_arr = new Set(array)
    
    const dict = {}
    for (i of set_arr) {
        dict[i] = 0
    }
    
    for (j of array) {
        dict[j] += 1
    }
    
    if (dict[n] ===  undefined ) { return 0 }
    answer = dict[n]
    return answer;
}