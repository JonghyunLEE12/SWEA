function solution(n, k) {
    var answer = 0;
    
    let food = 12000*n
    let drink = 2000*k
    let service = 2000 * parseInt(n / 10) 
    answer = (food + drink) - service
    return answer;
}