function solution(strlist) {
    var answer = [];
    for (let word of strlist) {
        word = word.split("")
        answer.push(word.length)
    }
    return answer;
}