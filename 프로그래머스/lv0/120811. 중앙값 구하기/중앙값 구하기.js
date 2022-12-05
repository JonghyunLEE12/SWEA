function solution(array) {
    var answer = 0;
    
    array = array.sort((a,b) => a - b )
    
    answer = array[parseInt(array.length/2)]
    return answer;
}