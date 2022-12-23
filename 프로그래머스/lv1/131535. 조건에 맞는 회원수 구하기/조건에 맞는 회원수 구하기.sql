-- 코드를 입력하세요
SELECT count(user_id) AS 'USERS' from user_info
WHERE AGE >= 20 and AGE <= 29 and YEAR(JOINED) = '2021'