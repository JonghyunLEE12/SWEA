// function solution(array, commands) {
//     var answer = [];
//     for (cmd of commands) {
//         let sliceArr = array.slice(cmd[0]-1,cmd[1])
//         answer.push(sliceArr.sort()[cmd[2]-1])
//     }
//     return answer;
// }

function solution(array, commands) {
    var answer = [];
    
    for(var i=0; i<commands.length;i++){
        var list = array.slice(commands[i][0]-1, commands[i]
        							[1]).sort((a,b)=>{return a-b});
        
        answer.push(list[commands[i][2]-1]);
    }

    return answer;
}