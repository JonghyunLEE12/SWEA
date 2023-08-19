-- 코드를 입력하세요
# SELECT hour(datetime) as HOUR, count(datetime) as COUNT
# from animal_outs
# where hour(datetime) >= 9 and hour(datetime) <= 19
# group by hour
# order by hour


SELECT HOUR(DATETIME) AS HOUR, COUNT(DATETIME) AS COUNT
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) <= 19
GROUP BY HOUR 
ORDER BY HOUR;