// function solution(babbling) {
//     let count = 0
//     let dup = ['ayaaya', 'yeye', 'woowoo', 'mama']
    
//     function check(word) {
//         for (let d of dup) {
//             if (word.includes(d)) { return 1}
//         }
//         return 0
//     }
    
//     while (babbling.length) {
//         let word = babbling.pop()
//         if (check(word) === 1) { count += 1 } 
//     }

//     return count;
// }

function solution(babbling) {
    let answer = 0
    
    for (let bab of babbling){
        if (/(aya|ye|woo|ma)\1+/g.test(bab)) continue
        if (/^(aya|ye|woo|ma)+$/g.test(bab)) answer++
    }
    return answer++
}