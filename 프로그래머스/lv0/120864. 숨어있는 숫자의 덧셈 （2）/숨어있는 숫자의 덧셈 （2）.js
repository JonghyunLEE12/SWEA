function solution(my_string) {
    return (my_string.match(/\d+/g)||[0]).reduce((a,b) => a*1+b*1, 0)
}