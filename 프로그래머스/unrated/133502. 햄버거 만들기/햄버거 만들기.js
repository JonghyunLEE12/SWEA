function solution(ingredient) {
    const stack = [];
    let cnt = 0;
    
    ingredient.forEach((ing,idx) => {
        
        stack.push(ing)
        if (stack.length >= 4) {
            const find = stack.slice(-4).join('')
            if (find === '1231') {
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                cnt ++
            }
        }
    })
    return cnt;
}
