function solution(array) {
    var answer = 0;
    
    let count = {}
    
    for (let num of array) {
        count[num] = 0
    }
    
    for (let num of array) {
        count[num] += 1
    }
    
    let max = [0,0]
    for (let num of Object.entries(count)) {
        if (num[1] > max[1]) { max = num}
        else if (num[1] === max[1]) { max = [-1,-1] }
    }
    return Number(max[0])
}