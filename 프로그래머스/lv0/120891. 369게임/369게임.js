function solution(order) {
    var answer = 0;
    order = String(order).split("")
    for (let i of order ) {
        if (parseInt(i) % 3 === 0 && parseInt(i) !== 0 ) {
            answer += 1
        }
    }
    return answer;
}