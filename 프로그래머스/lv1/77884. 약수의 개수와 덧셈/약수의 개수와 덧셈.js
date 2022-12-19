function solution(left, right) {
    var answer = 0;
    
    function check(num) {
        let cnt = 0
        for (let i = 1; i < num+1; i ++) {
            if (num % i === 0) { cnt +=1 }
        }
        if (cnt % 2 === 0) { return 0 }
        else { return 1 }
    }
    
    for (let i = left ; i < right+1 ; i ++) {
        check(i)
        if (check(i) === 1) { answer -= i}
        else if(check(i) === 0) { answer += i}
    }
    return answer;
}