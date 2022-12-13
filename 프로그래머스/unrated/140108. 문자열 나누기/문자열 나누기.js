function solution(s) {
    var answer = 0;
    
    let arr = []
    let x = 0
    let y = 0

    while (s.length > 0) {
        let count = 0
        for (let i = 0; i < s.length ; i ++) {
            s[0] === s[i] ? x += 1 : y += 1
            if ( x === y) {
                count = i + 1
                break
            }
        }
        arr.push(s.slice(0,count))
        s = s.slice(count)
        if (count === 0) {break}
    }
    return arr.length;
}