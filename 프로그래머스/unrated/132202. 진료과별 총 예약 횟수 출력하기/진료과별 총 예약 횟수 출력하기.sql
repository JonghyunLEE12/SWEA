-- 코드를 입력하세요
# SELECT mcdp_cd AS '진료과코드', count(mcdp_cd) AS '5월예약건수'
# FROM appointment
# WHERE APNT_YMD LIKE '2022-05%'
# GROUP BY mcdp_cd
# ORDER BY count(mcdp_cd) ASC, mcdp_cd ASC



SELECT MCDP_CD AS '진료과코드' , COUNT(MCDP_CD) AS '5월예약건수'
FROM APPOINTMENT
WHERE APNT_YMD LIKE '2022-05%'
GROUP BY MCDP_CD
ORDER BY COUNT(MCDP_CD) ASC , MCDP_CD ASC