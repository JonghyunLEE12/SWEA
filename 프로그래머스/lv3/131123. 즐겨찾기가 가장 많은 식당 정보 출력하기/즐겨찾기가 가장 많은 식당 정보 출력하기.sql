-- 코드를 입력하세요
# SELECT * FROM REST_INFO
# food_type,rest_id,rest_name,favorites

SELECT food_type,rest_id,rest_name,favorites FROM REST_INFO
WHERE (food_type,favorites) in (
    SELECT food_type,max(favorites) FROM REST_INFO
    GROUP BY food_type
)
ORDER BY FOOD_TYPE desc