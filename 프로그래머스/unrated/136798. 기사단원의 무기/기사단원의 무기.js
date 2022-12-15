// function solution(number, limit, power) {
//     var answer = 0;
//     // console.log(Number.isInteger(15/3))
    
//     let arr = []
//     function check(i) {
//         let cnt = 0
//         for (let j = 1 ; j < i+1 ; j ++) {
//             if (Number.isInteger(i/j)) {
//                 cnt += 1
//             }
//         }
//         arr.push(cnt)
//     }
//     for (let i = 1; i < number+1; i ++) {
//         let cnt = 1
//         for (let j = 1 ; j < i/2 ; j ++) {
//             if (i % j === 0) {
//                 cnt += 1
//             }
//         }
//         arr.push(cnt)
//     }
    
//     console.log(arr)
//     for (let num of arr) {
//         if (num > limit) {
//             answer += power
//         } else{
//             answer += num
//         }
//     }
//     return answer;
// }

function solution(number, limit, power) {
  const nums = [];

  // 1부터 number 까지 순차적으로 약수의 개수를 확인한다.
  for (let cur = 1; cur <= number; cur++) {
    let divisor = 0;

    // 1부터 현재 수의 절반 까지만 반복문을 돌린다.
    // 약수는 본래 값을 제외하고 n/2보다 클 수 없기 때문이다.

    for (let i = 1; i <= cur / 2; i++) {

      // i로 나누어 나머지가 0이면 약수이므로
      // 약수면 1을 더해준다.
      if (cur % i === 0) {
        divisor += 1;
      }
    }

    // 위에서 본래 값을 제외하고 반절만 돌렸기 때문에
    // 본래 값을 넣어준다 생각 하고 1을 더 더해준다.
    nums.push(divisor + 1);
  }

  // 위 작업을 통해 나온 개수의 배열을 map과 reduce를 통해 정답을 구한다.
  // num === [1, 2, 2, 3, 2]
  return nums
    .map((n) => {

      // n이 limit보다 크게되면 협약기관에서 정한 공격력을 가지는 무기를
      // 그렇지 않으면 그대로 n을 구매한다.
      return n > limit ? power : n;
    })
    .reduce((acc, cur) => acc + cur, 0);
}
