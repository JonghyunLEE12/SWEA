function solution(numbers, direction) {
    var answer = [];
    
    if (direction === 'right') {
        numbers.unshift(numbers.pop())
    } else if (direction === 'left') {
        numbers.push(numbers.shift())
    }
    return numbers
}