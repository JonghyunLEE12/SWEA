-- 코드를 입력하세요
SELECT animal_id, name,
IF ( sex_upon_intake LIKE '%Neutered%' OR  sex_upon_intake LIKE '%Spayed%' , 'O', 'X') AS '중성화'
From animal_ins
ORDER BY animal_id
