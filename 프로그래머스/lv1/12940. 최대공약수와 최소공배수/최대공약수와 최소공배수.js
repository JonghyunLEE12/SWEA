// function solution(n, m) {
//     var answer = [];
//     let G = 0
//     let L = 0
    
//     let num = n < m ? n : m
    
//     for (let i = 1; i <= num ; i ++) {
//         if (num % i === 0 && m % i === 0) {
//             G = i
//         }
//     }
    
//     L = n * m / G
//     answer = [G,L]
//     return answer
// }

function solution(n, m) {
    let max = (a, b) => a%b===0 ? b : max(b, a%b);
    let gcd = max(n,m);
    return [gcd, n*m/gcd];
}