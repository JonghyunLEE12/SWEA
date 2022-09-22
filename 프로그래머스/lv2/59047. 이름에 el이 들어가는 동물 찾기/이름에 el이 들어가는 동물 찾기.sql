-- 코드를 입력하세요
# SELECT animal_id , name from animal_ins
# where animal_type = "Dog" and name like "%el%"
# order by name


SELECT animal_id , name FROM animal_ins
WHERE animal_type = 'Dog' AND name LIKE "%el%"
ORDER BY name