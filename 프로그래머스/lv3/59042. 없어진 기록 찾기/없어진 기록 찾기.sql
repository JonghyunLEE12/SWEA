SELECT A.animal_id, A.name
FROM ANIMAL_OUTS AS A
LEFT JOIN ANIMAL_INS AS B
ON A.animal_id = B.animal_id
WHERE B.animal_id IS NULL
ORDER BY animal_id



