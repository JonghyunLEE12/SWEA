

function solution (a,b,n){
    let total = 0
    while(n/a >= 1) {
        let newCoke = Math.floor(n/a)*b
        total += newCoke
        n = n%a + newCoke
    }
    return total
}

