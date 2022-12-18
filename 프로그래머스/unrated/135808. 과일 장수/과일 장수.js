// function solution(k, m, score) {
//     let answer = 0
    
//     let box = []
//     // box 에 m 개 씩 담아 포장
//     // 사과 상자의 가격은 가장 낮은 점수 p * m
    
//     let score_rlt = []
//     score = score.sort().reverse()
    
//     for (let i of score) {
//         if (box.length === m){
//             let sum = Math.min(...box) * m
//             score_rlt.push(sum)
//             box = [i]
//         } else {
//             box.push(i)
//         }
//     }
    
//     if (box.length === m) {
//         let plus = Math.min(...box) * m
//         score_rlt.push(plus)
//     }
//     answer = score_rlt.reduce((a,b) => a+b)
//     return answer
// }

function solution(k, m, score) {
    var answer = 0;
   score.sort((a, b) => b - a); //1.
    let arr=[];
  for(let i=0; i<score.length; i+=m) {
      arr.push(score.slice(i, i+m)); //2.
  }
    for(let j=0; j<arr.length; j++){// 3.
        if(arr[j].length ===m){ //4.
           answer+= arr[j][m-1]*m; //5.
        }
    }
    return answer;
}
