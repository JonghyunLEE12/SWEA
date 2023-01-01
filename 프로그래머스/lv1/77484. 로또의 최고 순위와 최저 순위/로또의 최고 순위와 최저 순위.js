// def solution(lottos, win_nums):
//     answer = []
//     cnt = 0
//     for i in lottos:
//         if i in win_nums:
//             cnt += 1
//     cnt_0 = lottos.count(0)
    
//     rank = {
//         '6' : 1,
//         '5' : 2,
//         '4' : 3,
//         '3' : 4,
//         '2' : 5,
//         '1' : 6,
//         '0' : 6,
//     }
    
//     ans1 = str(cnt)
//     ans2 = str(cnt+cnt_0)
//     answer.append(rank[ans2])
//     answer.append(rank[ans1])
 
//     return answer

function solution(lottos, win_nums) {
    var answer = [];
    let cnt = 0
    let count_0 = 0
    
    for (let i of lottos) {
        if (i === 0) { count_0 += 1 }
        if (win_nums.includes(i)) {
            cnt += 1
        }
    }
    
    let rank = {
        '6' : 1,
        '5' : 2,
        '4' : 3,
        '3' : 4,
        '2' : 5,
        '1' : 6,
        '0' : 6
    }

    let ans1 = String(cnt)
    let ans2 = String(cnt+count_0)

    answer = [rank[ans2],rank[ans1]]
    
    return answer;
}