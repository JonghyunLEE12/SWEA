-- 코드를 입력하세요
# SELECT animal_ins.animal_id , animal_ins.animal_type , animal_ins.name
# from animal_ins
# left join animal_outs
# on animal_ins.animal_id = animal_outs.animal_id
# where animal_ins.sex_upon_intake like "Intact %"and (animal_outs.sex_upon_outcome like "%Spayed%" or animal_outs.sex_upon_outcome like " %Neuterted%")
# order by animal_ins.animal_id

SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
FROM ANIMAL_INS AS A
LEFT JOIN ANIMAL_OUTS AS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.SEX_UPON_INTAKE LIKE 'Intact %'and (B.SEX_UPON_OUTCOME LIKE '%Spayed%' or
B.SEX_UPON_OUTCOME LIKE '%Neutered%')
ORDER BY A.ANIMAL_ID