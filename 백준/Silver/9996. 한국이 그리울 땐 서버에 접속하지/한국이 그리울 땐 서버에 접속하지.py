n = int(input())

word = input().split('*')
length = len(word[0]) + len(word[1])

for _ in range(n):
    check = input()
    if length > len(check):
        print("NE")
    
    else:
        if word[0] == check[:len(word[0])] and word[1] == check[-len(word[1]):]:
            print("DA")
        else:
            print("NE")