-- 코드를 입력하세요
# SELECT * FROM REST_INFO
# food_type,rest_id,rest_name,favorites

# SELECT food_type,rest_id,rest_name,favorites FROM REST_INFO
# WHERE (food_type,favorites) in (
#     SELECT food_type,max(favorites) FROM REST_INFO
#     GROUP BY food_type
# )
# ORDER BY FOOD_TYPE desc



SELECT FOOD_TYPE,REST_ID,REST_NAME,FAVORITES
FROM REST_INFO
WHERE (FOOD_TYPE,FAVORITES) in (
    SELECT FOOD_TYPE,MAX(FAVORITES)
    FROM REST_INFO
    GROUP BY FOOD_TYPE
)
ORDER BY FOOD_TYPE DESC

