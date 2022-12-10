function solution(emergency) {
    var answer = [];

    let copy = JSON.parse(JSON.stringify(emergency))
    let sorted = emergency.sort((a,b) => b-a)
    
    let check = {}
    sorted.forEach((num,idx) => {
        check[num] = idx
    })
    
    for (let num of copy) {
        answer.push(check[num]+1)
    }
    return answer;
}