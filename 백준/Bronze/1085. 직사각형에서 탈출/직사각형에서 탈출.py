x,y,w,h = map(int,input().split())
print(min(min(w-x,h-y),min(abs(0-x),abs(0-y))))