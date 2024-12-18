function solution(topping) {
  let answer = 0;
  const right = new Map(); // 전체에서 감소 토핑을 하나씩 뺄 예정
  const left = new Set(); // 하나씩 토핑을 추가할 예정

  // 각 토핑이 몇 개씩 있는지 확인
  for (let index = 0; index < topping.length; index++) {
    const key = topping[index];
    if (right.has(key)) {
      const value = right.get(key);
      right.set(key, value + 1);
    } else {
      right.set(key, 1);
    }
  }

  // 왼쪽부터 하나씩 추가,삭제하며 좌우 토핑수 비교하기
  for (let index = 0; index < topping.length; index++) {
    const targetTopping = topping[index];

    left.add(targetTopping);

    const value = right.get(targetTopping);
    if (value === 1) {
      right.delete(targetTopping);
    } else {
      right.set(targetTopping, value - 1);
    }

    if (left.size === right.size) {
      answer += 1;
    }
  }

  return answer;
}