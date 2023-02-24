# SELECT animal_id, name , DATE_FORMAT(datetime , '%Y-%m-%d') AS '날짜'
# FROM animal_ins
# ORDER BY animal_id


# SELECT animal_id, name, DATE_FORMAT(datetime, '%Y-%m-%d') AS '날짜'
# FROM animal_ins
# ORDER BY animal_id


SELECT ANIMAL_ID , NAME , DATE_FORMAT(DATETIME, '%Y-%m-%d')
FROM ANIMAL_INS
ORDER BY ANIMAL_ID