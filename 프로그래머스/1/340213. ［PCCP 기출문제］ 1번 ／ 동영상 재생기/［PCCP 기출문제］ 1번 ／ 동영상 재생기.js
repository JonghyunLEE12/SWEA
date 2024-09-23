// function solution(video_len, pos, op_start, op_end, commands) {
//     var answer = '';
    
//     let posToSec = convertTime(pos);
//     const videoLen = convertTime(video_len);
//     const opStartToSec = convertTime(op_start);
//     const opEndToSec = convertTime(op_end);
//     posToSec = findTime(posToSec, videoLen, opStartToSec, opEndToSec);
//     if (opStartToSec <= posToSec && opEndToSec >= posToSec ) {
//         posToSec = opEndToSec;
//     }
    
//     for (let cmd of commands) {
//         if (cmd == "next") {
//             posToSec += 10;
//             posToSec = findTime(posToSec, videoLen, opStartToSec, opEndToSec);
//         } else {
//             posToSec -= 10;
//             posToSec = findTime(posToSec, videoLen, opStartToSec, opEndToSec);
//         }
//     }
//     posToSec = findTime(posToSec, videoLen, opStartToSec, opEndToSec);
    
//     if (opStartToSec <= posToSec && opEndToSec >= posToSec ) {
//         posToSec = opEndToSec;
//     }
//     return convertAnswer(posToSec);
// }


// function convertTime(time) {
//     let timeList = time.split(':');
//     timeList = timeList.map((clock) => Number(clock));
//     return timeList[0] * 60 + timeList[1];
// }


// function findTime(time, videoLen, opStartToSec, opEndToSec) {
//     if (time < 10) return 0;
//     if (videoLen - time < 10) return videoLen;
//     if (opStartToSec <= time && opEndToSec >= time ) return opEndToSec;
//     return time;
// }

// function convertAnswer(time) {
//     let front = Math.floor(time/60);
//     let back = time % 60;
    
//     front = front.toString().padStart(2, '0');  
//     back = back.toString().padStart(2, '0');    

//     return `${front}:${back}`;
// }



// // 입력값 〉 "30:00", "00:08", "00:00", "00:05", ["prev"]
// // 기댓값 〉 "00:05"


function solution(video_len, pos, op_start, op_end, commands) {
    let cur_s = convertToSec(pos)
    const end_s = convertToSec(video_len)

    if(is_inside_op(cur_s, op_start, op_end)){
        cur_s = convertToSec(op_end)
    }

    commands.forEach(command=>{
        if(command === 'next'){
            cur_s = next(cur_s, end_s)
        }else{
            cur_s = prev(cur_s, end_s)
        }
        if(is_inside_op(cur_s, op_start, op_end)){
           cur_s = convertToSec(op_end)
        }
    })


    return convertToFormatString(cur_s);
}

function next(cur_sec, end_sec){
    const result = cur_sec + 10

    if(result >= end_sec){
        return end_sec
    }
    return result
}

function prev(cur_sec){
    const result = cur_sec - 10
    if(result < 0){
        return 0
    }
    return result
}

function is_inside_op(cur_sec, op_start, op_end){
    const ops = convertToSec(op_start)
    const opend = convertToSec(op_end)
    return ops<= cur_sec && cur_sec <= opend
}

function convertToSec(formatString){
    const [m,s] = formatString.split(':').map(Number)

    return 60*m+s
}

function convertToFormatString(sec){
    const m = String(Math.floor(sec / 60)).padStart(2,"0")
    const s = String(sec % 60).padStart(2,"0")

    return m + ':' + s
}

