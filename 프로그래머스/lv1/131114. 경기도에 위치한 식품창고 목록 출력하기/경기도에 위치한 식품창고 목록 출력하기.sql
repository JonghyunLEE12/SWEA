-- 코드를 입력하세요
# SELECT warehouse_id,
#     warehouse_name,
#     address,
#     case
#     WHEN freezer_yn is NULL THEN 'N'
#     ELSE freezer_yn
#     END AS freezer_yn
# FROM FOOD_WAREHOUSE
# WHERE address LIKE '경기%'



SELECT WAREHOUSE_ID, WAREHOUSE_NAME,ADDRESS,
(
    CASE
        WHEN FREEZER_YN IS NULL THEN 'N'
        ELSE FREEZER_YN
    END
) AS FREEZER_YN

FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '경기%'










