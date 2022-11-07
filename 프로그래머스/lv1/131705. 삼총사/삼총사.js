function solution(number) {
    let result = 0;

    const combination = (current, start) => {
        if (current.length === 3) {
            result += current.reduce((acc, cur) => acc + cur, 0) === 0 ? 1 : 0;
            return;
        }

        for (let i = start; i < number.length; i++) {
            combination([...current, number[i]], i + 1);
        }
    }
    combination([], 0);
    return result;
}

// function solution(number) {
//     var answer = 0;
//     // 학교 학생 3명의 정수를 더했을 때 0 이 되면 삼총사
    
//     const combination = (current, start) => {
//        if (current.length === 3) {
//            if (current.reduce((a,b) => a+b,0) === 0) {
//                answer += 1
//            }
//        }
//         for (let i = 0 ; i < number.length ; i ++) {
//             combination([...current, number[i]],i+1)
//         }
//     }
//     combination([],0)
//     return answer;
// }