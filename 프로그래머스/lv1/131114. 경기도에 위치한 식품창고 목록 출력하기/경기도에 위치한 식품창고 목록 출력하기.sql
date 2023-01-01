-- 코드를 입력하세요
SELECT warehouse_id,
    warehouse_name,
    address,
    case
    WHEN freezer_yn is NULL THEN 'N'
    ELSE freezer_yn
    END AS freezer_yn
FROM FOOD_WAREHOUSE
WHERE address LIKE '경기%'