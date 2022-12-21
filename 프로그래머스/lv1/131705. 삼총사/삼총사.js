function solution(number) {
    let result = 0;
    
    
    const combination = (current,start) => {
        if (current.length === 3){
            if (current.reduce((a,b) => a+b, 0) === 0) {
                result += 1
            }
            return
        }
        for (let i = start ; i < number.length ; i ++) {
            combination([...current,number[i]],i+1)
        }
    }
    combination([],0)
    return result;
}
