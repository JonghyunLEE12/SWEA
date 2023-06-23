-- 코드를 입력하세요

# SELECT animal_type, count(animal_type)
# FROM animal_ins
# GROUP BY animal_type
# ORDER BY animal_type


# SELECT animal_type , count(animal_type)
# FROM animal_ins
# GROUP BY animal_type
# ORDER BY animal_type


# SELECT ANIMAL_TYPE , COUNT(ANIMAL_TYPE) AS 'count'
# FROM ANIMAL_INS
# GROUP BY ANIMAL_TYPE
# ORDER BY ANIMAL_TYPE



SELECT ANIMAL_TYPE , COUNT(ANIMAL_TYPE) AS 'Count'
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE