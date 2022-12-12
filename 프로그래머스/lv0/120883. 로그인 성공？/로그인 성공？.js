function solution(id_pw, db) {
    var answer = 'fail';
    for (let id of db) {
        if ( id[0] === id_pw[0]) {
            if (id[1] === id_pw[1]) {
                answer = 'login'
            } else {
                answer = 'wrong pw'
            }
        }
    }
    return answer;
}