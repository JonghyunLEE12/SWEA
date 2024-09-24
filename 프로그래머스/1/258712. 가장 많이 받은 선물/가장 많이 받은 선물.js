// function solution(friends, gifts) {
//     var answer = 0;
    
//     // 두 사람이 선물을 주고받은 기록이 있다면,
//     // 더 많이 선물은 준 사람이 하나 받음
//     // A > B => B -> A
    
//     // 두사람이 기록이 없거나, 주고받은 선물 수가 같다면,
//     // 선물 지수가 더 큰 사람이 더 작은 사람에게 하나 받음
//     // 선물 지수 = 이번 달까지 자신이 친구들에게 준 선물 - 받은 선물
    
//     // 선물을 가장 많이 받을 친구가 받을 선물의 개수
    
//     const nameToGive = {};
//     friends.forEach((friend) => {
//         nameToGive[friend] = {};
//         friends.forEach((otherFriend) => {
//             if (friend !== otherFriend) {
//                 nameToGive[friend][otherFriend] = 0;
//             }
//         });
//     });
    
//     // 선물을 준 사람과 받은 사람을 확인하여 해당 기록을 업데이트
//     gifts.forEach((gift) => {
//         const [giver, receiver] = gift.split(' ');
//         if (giver !== receiver) {
//             nameToGive[giver][receiver] += 1; // 선물을 준 사람의 기록을 업데이트
//         }
//     });
    
//     giftCount(nameToGive, friends);
    
//     return answer;
// }




// function giftCount(nameToGive, friends) {
     
//     const giftScore = {};
    
//     friends.map((name) => giftScore[name] = 0);
        
//     // 선물 주고 받은 기록 확인
//     giftToEach(nameToGive, giftScore, friends);
    
// }



// function giftToEach(nameToGive, giftScore, friends) {
//     console.log(nameToGive);
    
//     // 선물 지수 만들기
//     friends.forEach((name) => {
//         // 준 선물의 수
//         const nameSendGift = Object.values(nameToGive[name]).reduce((a,b) => a + b);
        
//     });
//     //
//     friends.forEach((name) => {
//         for (const friend of Object.keys(nameToGive[name])) {
//             if (nameToGive[name][friend] != 0 && nameToGive[name][friend] != nameToGive[friend][name]) {
//                 if (nameToGive[name][friend] > nameToGive[friend][name]) {
//                     giftScore[name] += 1
//                 } else {
//                     giftScore[friend] += 1
//                 }
//             } 
//             else if ((nameToGive[name][friend] == nameToGive[friend][name])) {
//                 // 선물 지수 확인
//                 // const nameGetGift = Object.values(nameToGive[name]).reduce((a,b) => a + b);
//                 // let nameSendGift = 0;
//                 // console.log(nameGetGift)
//             }
//         }
//     });
    
//     // for (const key of Object.keys(nameToGive)) {
//     //     console.log(nameToGive[key]);
//     // }
// }


// function giftScore(nameToGive, friends) {
    
// }


function solution(friends, gifts) {
  let answer = {}
  let statistic = {}
  let idxStatistic = {}
  for (const name of friends) {
    answer[name] = 0
    statistic[name] = 0
    idxStatistic[name] = {}
    for (const sub of friends) {
      if(name !== sub){
        idxStatistic[name][sub] = 0
      }
    }
  }
  for (const cur of gifts) {
    let [from,to] = cur.split(' ')
    statistic[from] = statistic[from]+1
    statistic[to] = statistic[to]-1
    idxStatistic[from][to] = idxStatistic[from][to]+1
  }
  for (const from in idxStatistic) {
    for (const to in idxStatistic[from]) {
      if(idxStatistic[from][to] === 0 && idxStatistic[to][from] === 0 || idxStatistic[from][to] === idxStatistic[to][from]){
        if(statistic[from] > statistic[to]){
          answer[from] = answer[from]+1
        }
      }else{
        if(idxStatistic[from][to] < idxStatistic[to][from]){
          answer[to] = answer[to]+1
        }else if(idxStatistic[to][from] > idxStatistic[from][to]){
          answer[from] = answer[from]+1
        }
      }
    }
  }
  answer = Math.max(...Object.values(answer))
  return answer
}