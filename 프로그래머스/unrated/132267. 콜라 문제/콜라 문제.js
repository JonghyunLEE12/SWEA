function solution(a, b, n) {
  //총 받은 콜라 수
    let totalcokes=0
    //교환 가능한 수량이 아닐 때까지 반복
   while(n/a>=1){
     //콜라 n개를 줄 때 받게 되는 콜라 수
       let newcokes=Math.floor(n/a)*b;
     //받은 콜라들을 totalcokes에 더한다
        totalcokes+=newcokes;
     //n은 교환하고 남은 콜라와 새로 받은 콜라의 합이 된다
        n=n%a+newcokes;
    }
    return totalcokes;
}