# -- 코드를 입력하세요
# SELECT animal_ins.name, animal_ins.datetime
# from animal_ins
# left join animal_outs
# on animal_ins.animal_id = animal_outs.animal_id
# where animal_outs.animal_id is null
# order by animal_ins.datetime
# limit 3


# SELECT animal_ins.name , animal_ins.datetime
# FROM animal_ins
# LEFT JOIN animal_outs
# ON animal_ins.animal_id = animal_outs.animal_id
# WHERE animal_outs.animal_id IS NULL
# ORDER BY animal_ins.datetime
# limit 3





# SELECT animal_ins.name , animal_ins.datetime
# FROM animal_ins
# LEFT JOIN animal_outs
# ON animal_ins.animal_id = animal_outs.animal_id
# WHERE animal_outs.animal_id IS NULL
# ORDER BY animal_ins.datetime
# limit 3



# SELECT animal_ins.name , animal_ins.datetime
# FROM animal_ins
# LEFT JOIN animal_outs
# ON animal_ins.animal_id = animal_outs.animal_id
# WHERE animal_outs.animal_id IS NULL
# ORDER BY animal_ins.datetime
# limit 3




SELECT INS.NAME,INS.DATETIME
FROM ANIMAL_INS AS INS
LEFT JOIN ANIMAL_OUTS AS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE OUTS.ANIMAL_ID IS NULL
ORDER BY INS.DATETIME
LIMIT 3