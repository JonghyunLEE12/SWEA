function solution(age) {
    var answer = '';
    
    
    age = String(age).split("")
    
    for (let i of age ) {
        num = 97+Number(i)
        answer += String.fromCharCode(num)
    }
    return answer;
}