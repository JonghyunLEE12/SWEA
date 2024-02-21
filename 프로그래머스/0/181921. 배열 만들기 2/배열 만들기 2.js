function solution(l, r) {

    let result = []
    for(let i = l ; i <= r ; i++){
        let intoString = i.toString();
        let j = 0;
        let total = 0;
        while(j !== intoString.length){
            if(intoString[j].includes("5") || intoString[j].includes("0"))
            total++;
            if(total === intoString.length){
                result.push(Number(intoString));
                break;
            }
            j++;    
        }
    }
    if(result.length === 0) result.push(-1);
    return result;
}