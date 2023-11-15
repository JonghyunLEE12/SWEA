function solution(info, query) {

  const infoDict = {'cpp': 'c', 'java': 'j', 'python': 'p', 'backend': 'b', 'frontend': 'f', 'junior': 'j', 'senior': 's', 'chicken': 'c', 'pizza': 'p', '-': '-'};

  const infoList = {};
  
  info.map((v) => {
    const arr = v.split(' ');
    const score = +arr.pop();
    const word = arr.map((v) => infoDict[v]).join('');
    if(infoList[word]) {
      infoList[word].push(score);
    } else {
      infoList[word] = [score];
    }
  });


  const infoArray = Object.entries(infoList).map((v) => [v[0], v[1].sort((a, b) => a - b)]);

  return query.map((v) => {
    const arr = v.replace(/and\s/, '').split(' ');
    const qscore = +arr.pop();
    const word = arr.map((v) => infoDict[v]).join('');
    return infoArray.reduce((a, v) => {
      const temp = v[0];
      const iscore = v[1];

      if(iscore[iscore.length - 1] < qscore) return a;
      for(let i = 0 ; i <word.length ; i++) {
        if(word.charAt(i) !== temp.charAt(i) && word.charAt(i) !== '-') {return a}
      }
      let start = 0;
      let end = iscore.length; 
      while (start < end) {
        const mid = Math.floor((start + end) / 2);

        if(iscore[mid] >= qscore) {
          end = mid;
        } else {
          start = mid + 1;
        }
      }
      return a + (iscore.length - start);
    }, 0);
  });
}