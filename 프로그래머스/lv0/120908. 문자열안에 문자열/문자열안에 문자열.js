function solution(str1, str2) {
    console.log(str1.indexOf(str2))
    
    return str1.indexOf(str2) == -1 ? 2 : 1
    // return str1.indexOf(str2) != -1 ? 1 : 2;
}