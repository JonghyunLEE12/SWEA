function solution(my_string, n) {
    var answer = '';
    my_string = my_string.split("")
    
    
    function makeWord (w , n) {
        let word = ''
        for (let i = 0 ; i < n ; i ++) {
            word += w 
        }
        return word
    }
    for (let i of my_string) {
        answer += makeWord(i,n)
    }
    return answer;
}