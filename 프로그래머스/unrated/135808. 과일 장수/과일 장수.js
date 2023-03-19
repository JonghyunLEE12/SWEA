function solution(k, m, score) {
    let answer = 0
    score.sort((a,b) => b - a)
    
    let box = []
    let rlt = []
    function cal(box) {
        let min_num = Math.min(...box)
        rlt.push(min_num*box.length)
    }
    
    for ( let apple of score) {
        if ( box.length == m ) {
            cal(box)
            box = [apple]
        } else { box.push(apple) }
    }
    
    if ( box.length === m ) { cal(box) }
    
    answer = rlt.reduce((a,b) => a+b,0)
    
    
    return answer
}
