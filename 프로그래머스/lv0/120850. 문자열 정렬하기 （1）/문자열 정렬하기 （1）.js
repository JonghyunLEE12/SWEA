function solution(my_string) {
    var answer = [];
    for (let i of my_string) {
        i = Number(i)
        if (Number.isInteger(i)) { answer.push(i)}
    }
    answer = answer.sort((a,b) => a - b)
    return answer;
}