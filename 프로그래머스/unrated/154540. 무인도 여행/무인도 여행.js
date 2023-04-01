function solution(maps) {
    var answer = [];
    
    // 델타 상 하 좌 우
    let dr = [-1,1,0,0]
    let dc = [0,0,-1,1]
    
    let visited = []
    
    for ( let a = 0 ; a < maps.length ; a++){
        let arr = new Array(maps[0].length).fill(0)
        visited.push(arr)
    }

    
    function bfs(r,c) {
        let queue = [r,c]
        let num = Number(maps[r][c])
        visited[r][c] = 1
        
        while (queue.length > 0) {
            let row = queue.shift()
            let col = queue.shift()
            
            for (let i = 0; i < dr.length ; i ++) {
                let nr = row + dr[i]
                let nc = col + dc[i]
                
                if ( 0 <= nr && nr < maps.length && 0 <= nc && nc < maps[0].length ) {
                    if ( maps[nr][nc] !== 'X' && visited[nr][nc] === 0 ) {
                        queue.push(nr)
                        queue.push(nc)
                        num += Number(maps[nr][nc])
                        visited[nr][nc] = 1
                    }
                } 
            }
        }
        return num
    }
    for (let r = 0; r < maps.length ; r++) {
        for (let c = 0; c < maps[0].length ; c ++) {
            if (maps[r][c] !== 'X' && visited[r][c] === 0) {
                answer.push(bfs(r,c))
            }
        }
    }
    
    if (answer.length === 0) {
        answer = [-1]
    } else {
        answer = answer.sort((a,b) => a-b)
    }
    return answer;
}