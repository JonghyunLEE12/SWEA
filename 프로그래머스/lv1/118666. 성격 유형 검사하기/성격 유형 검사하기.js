function solution(survey, choices) {
    var answer = '';
    
    let perObj = {
        'R' : 0,'T' : 0,
        'C' : 0,'F' : 0, 
        'J' : 0,'M' : 0, 
        'A' : 0,'N' : 0  
        
    }
    // 매우 동의 or 매우 비동의 : 3점
    //  1               7
    // 동의 or 비동의 : 2점
    //  2               6
    // 약간 동의 or 약간 비동의 : 1점
    //  3.              5 
    // 모르겠음 : 0점
    // 4

    
    survey.forEach((sur,idx) => {
        let agree = [5,6,7]
        let disagree = [1,2,3]
        
        if (agree.includes(choices[idx])) {
            // 동의 => 두번째 
            if (choices[idx] === 7) { perObj[sur[1]] += 3 }
            if (choices[idx] === 6) { perObj[sur[1]] += 2 }
            if (choices[idx] === 5) { perObj[sur[1]] += 1 }

        } else if (disagree.includes(choices[idx])) {
            // 비동의 => 첫번째
            if (choices[idx] === 1) { perObj[sur[0]] += 3 }
            if (choices[idx] === 2) { perObj[sur[0]] += 2 }
            if (choices[idx] === 3) { perObj[sur[0]] += 1 }   
        }
    })
    
        
    let stack = []
    for (let i of Object.entries(perObj)) {
        stack.push(i)
        if (stack.length === 2) {
            check(stack)
            stack = []
        }
    }
    
    function check(arr){
        if (arr[0][1] > arr[1][1]) { answer += arr[0][0] }
        else if (arr[0][1] < arr[1][1]) { answer += arr[1][0] }
        else { answer += arr[0][0]}
    }
    

    return answer;
}