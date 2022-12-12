function solution(a, b) {
   if (Number((a/b).toFixed(10)) == a/b) {
       return 1
   } else {
       return 2
   }
}