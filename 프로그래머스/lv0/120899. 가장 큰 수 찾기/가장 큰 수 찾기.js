function solution(array) {
    var answer = [];
    const max_v = Math.max(...array)
    console.log(max_v)
    array.forEach((value,index) => {
        if (value === max_v) {
            answer = [max_v,index]
        }
    })
    return answer;
}