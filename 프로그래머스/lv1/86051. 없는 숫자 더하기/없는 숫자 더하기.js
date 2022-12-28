function solution(numbers) {
    var answer = -1;
    
    let rlt = 0
    for (let i = 0 ; i < 10 ; i ++) {
        if (numbers.includes(i)) continue
        else {
            rlt += i
        }
    }

    return rlt
}