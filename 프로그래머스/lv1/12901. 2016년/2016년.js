function solution(a, b) {
    return new Date(2016, a-1, b).toString().slice(0,3).toUpperCase();
}

// 다른 방법
function solution(a, b) {
    // 윤년은 2월이 29일까지 있고, 1년이 366일이다.
    // 4, 100, 400으로 나누어지는 년도는 윤년이다.
    const weekToDay = ['SUN','MON','TUE','WED','THU','FRI','SAT'];
    const leapYearMonths = [31,29,31,30,31,30,31,31,30,31,30,31]; 
    let day = b+4; // 1월 1일은 FRI, b가 1일 때 인덱스로는 5가 되어야한다.
    // 1월은 이전 월의 일수를 더하지 않음으로 a-1 조건으로 해야한다.
    for(let i = 0; i < a-1; ++i){
        day += leapYearMonths[i];
    }
    return weekToDay[day%7];
}