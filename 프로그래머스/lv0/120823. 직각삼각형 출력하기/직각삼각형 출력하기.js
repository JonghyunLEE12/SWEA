const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    // console.log(Number(input[0]));
    
    let num = Number(input[0])
    
    function star(i){
        let star = ''
        for (let j = 0 ; j < i ; j ++) {
            star += '*'
        }
        console.log(star)
    }
    
    for (let i = 1 ; i < num+1 ; i ++){
        star(i)
    }
});