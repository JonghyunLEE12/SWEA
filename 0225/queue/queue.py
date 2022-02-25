import queue # q 자료형이 내장 되어 있음

# queue = []
#
# queue.append(1)
# queue.append(2)
# queue.append(3)
#
# print(queue)
# # queue 는 선입선출
# queue.pop(0)        # 맨앞이 반환
# print(queue)

########################################

my_Q = queue.Queue      # Queue 생성
my_Q.put(1)
my_Q.put(2)
my_Q.put(3)

elem = my_Q.get()
print(elem)