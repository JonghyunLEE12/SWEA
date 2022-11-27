function solution(s) {
    var answer = '';
    s = s.split(" ")
    
    function change(word){
        let change_word = ''
        word = word.split("")
        word.forEach((value,idx) => {
            if (idx % 2 === 0) {
                value = value.toUpperCase()
                change_word += value
            } else {
                value = value.toLowerCase()
                change_word += value
            }
        })
        return change_word
    }
    
    const result = []
    for (word of s ) {
        let newWord = change(word)
        result.push(newWord)
    }
    return result.join(" ")
}