# SELECT outs.animal_id , outs.name
# FROM animal_outs outs
# LEFT OUTER JOIN animal_ins ins
# ON outs.animal_id = ins.animal_id
# WHERE ins.animal_id IS NULL
# ORDER BY outs.animal_id


 

# SELECT A.ANIMAL_ID, A.NAME
# FROM ANIMAL_OUTS A LEFT JOIN ANIMAL_INS B ON A.ANIMAL_ID = B.ANIMAL_ID
# WHERE B.ANIMAL_ID IS NULL
# ORDER BY A.ANIMAL_ID

SELECT A.animal_id , A.name
FROM ANIMAL_OUTS AS A LEFT JOIN ANIMAL_INS AS B
ON A.animal_id = B.animal_id
WHERE B.animal_id IS NULL
ORDER BY A.animal_id
