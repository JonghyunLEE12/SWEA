function solution(my_string) {
    var answer = '';
    my_string = my_string.split("")
    let my_set = new Set(my_string)
    
    for (let i of my_set) {
        answer += i
    }
    return answer;
}