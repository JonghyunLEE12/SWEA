-- 코드를 입력하세요
# SELECT animal_id, name,
# IF ( sex_upon_intake LIKE '%Neutered%' OR  sex_upon_intake LIKE '%Spayed%' , 'O', 'X') AS '중성화'
# From animal_ins
# ORDER BY animal_id



# SELECT animal_id , name ,
# IF ( sex_upon_intake LIKE '%Neutered%' OR sex_upon_intake LIKE '%Spayed%','O','X')
# AS '중성화'
# FROM animal_ins
# ORDER BY animal_id



SELECT ANIMAL_ID,NAME,(
    CASE
        WHEN ANIMAL_ID IN (
            SELECT ANIMAL_ID
            FROM ANIMAL_INS
            WHERE SUBSTR(SEX_UPON_INTAKE,1,1) LIKE 'N' OR
            SUBSTR(SEX_UPON_INTAKE,1,1) LIKE 'S'
        ) THEN 'O'
        ELSE 'X'
    END
) AS '중성화'

FROM ANIMAL_INS
ORDER BY ANIMAL_ID








