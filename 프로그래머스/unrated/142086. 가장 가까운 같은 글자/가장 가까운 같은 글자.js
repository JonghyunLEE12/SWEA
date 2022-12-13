function solution(s) {

    var answer = [];
    let word_stack = []
    s = s.split("")
    
    for ( let w of s) {
        if ( word_stack.includes(w) === false) {
            word_stack.push(w)
            answer.push(-1)
        } else {
            let idx = 1
            for (let i = word_stack.length -1 ; i > -1 ; i --) {
                if (word_stack[i] === w) {
                    word_stack.push(w)
                    answer.push(idx)
                    break
                } else {
                    idx += 1
                }
            }
        }
    }
    
    return answer;
}