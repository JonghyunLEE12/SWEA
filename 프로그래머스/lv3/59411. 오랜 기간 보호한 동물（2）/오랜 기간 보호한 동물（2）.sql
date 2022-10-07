-- 코드를 입력하세요
# SELECT A.ANIMAL_ID, A.NAME
# FROM ANIMAL_INS A, ANIMAL_OUTS B
# WHERE A.ANIMAL_ID = B.ANIMAL_ID
# ORDER BY B.DATETIME-A.DATETIME DESC
# LIMIT 2


SELECT A.animal_id, A.name
FROM animal_ins A, animal_outs B
WHERE A.animal_id = B.animal_id
ORDER BY B.datetime - A.datetime DESC
LIMIT 2