for t in (1,11):
    N=int(input())
    buildings=list(map(int,input().split()))
    view=0
    # (-) 가 되면 안되기 때문에 range를 2 부터 N-2
    for i in range(2,N-2):
        def_2=buildings[i]-buildings[i-2]
        def_1=buildings[i]-buildings[i-1]
        def1=buildings[i]-buildings[i+1]
        def2=buildings[i]-buildings[i+2]

        if def_2 >0 and def_1 >0 and def1 >0 and def2 > 0:
            view+=min(def_2,def_1,def1,def2)
    print(f'#{t} {view}')




