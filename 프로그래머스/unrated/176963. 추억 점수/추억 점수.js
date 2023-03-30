function solution(name, yearning, photo) {
    var answer = [];
    
    let dict = {}
    
    for (let i = 0 ; i < name.length; i ++) {
        dict[name[i]] = yearning[i]
    }
    
    function check(arr) {
        let score = 0
        
        for (let ph of arr) {
            if (name.includes(ph)) { score += dict[ph] }
        }
        
        return score
    }
    for ( let ph of photo) {
        let score = check(ph)
        answer.push(score)
    }
    return answer;
}