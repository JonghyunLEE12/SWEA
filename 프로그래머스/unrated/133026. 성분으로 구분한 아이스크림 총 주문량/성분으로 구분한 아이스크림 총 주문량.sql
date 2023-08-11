-- 코드를 입력하세요
# SELECT A.ingredient_type , sum(B.total_order) AS 'TOTAL_ORDER'
# FROM ICECREAM_INFO AS A , FIRST_HALF AS B
# WHERE A.flavor = B.flavor
# GROUP BY A.ingredient_type
# ORDER BY B.TOTAL_ORDER

SELECT A.ingredient_type , sum(B.total_order) AS 'TOTAL_ORDER'
FROM ICECREAM_INFO AS A , FIRST_HALF AS B
WHERE A.flavor = B.flavor
GROUP BY A.ingredient_type
ORDER BY B.TOTAL_ORDER