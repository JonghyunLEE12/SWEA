function solution(babbling) {
    // 해당 풀이는 StarBlitz님의 풀이를 해석하였음을 미리 밝힙니다.
    let count = 0;
    // 연속되는 경우
    let dup = ['ayaaya', 'yeye', 'woowoo', 'mama'];
    while (babbling.length) {
        let b = babbling.pop();
        // 연속되는 발음은 패스
        if (dup.some(v=>b.includes(v))) continue;
        // 가능한 발음을 모두 숫자로 바꾸어
        b = b.replaceAll('aya','1').replaceAll('ye','2').replaceAll('woo','3').replaceAll('ma','4');
        // 숫자는 공백으로 변환
        b = b.replace(/[1234]/g, '');
        // 모두 가능한 발음의 경우 count++
        if (b.length === 0) count++;
    }

    return count;
}