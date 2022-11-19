function solution(food) {
    var answer = '';
    
    function check(food) {
        if (food === 1) return 'PASS'
        if (food !== 1 && food % 2 === 1) {
            return (food-1) /2 
        } else {
            return food/2
        }
    }
    
    function makeAnswer(index,time){
        let plusWord = ''
        for (let i = 0; i < time ; i ++) {
            plusWord += String(index)
        }
        return plusWord
    }
    
    let word = ''
    for (let i = 0 ; i < food.length ; i ++ ) {
        if (i === 0) { continue }
        if (check(food[i]) === 'PASS') { continue }
        word += makeAnswer(i,check(food[i]),word)        
    }
    const reversed = word.split("").reverse().join("")
    answer = word + '0' + reversed
    return answer;
}