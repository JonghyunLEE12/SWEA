-- 코드를 입력하세요

# SELECT ins.animal_id , ins.name
# FROM animal_ins ins
# LEFT OUTER JOIN animal_outs outs
# ON ins.animal_id = outs.animal_id
# WHERE outs.datetime < ins.datetime
# ORDER BY ins.datetime


SELECT A.animal_id , A.name
# SELECT *
FROM ANIMAL_INS AS A
LEFT JOIN ANIMAL_OUTS AS B
ON A.animal_id = B.animal_id
WHERE A.DATETIME > B.DATETIME
ORDER BY A.datetime
