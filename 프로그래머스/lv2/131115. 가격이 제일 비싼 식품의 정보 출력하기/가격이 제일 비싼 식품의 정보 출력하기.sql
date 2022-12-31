-- 코드를 입력하세요
# SELECT product_id , product_name , product_cd , category, price
# FROM food_product
# where price in ( select max(price) from food_product)




# SELECT product_id , product_name , product_cd , category , price
# FROM food_product
# WHERE price IN ( SELECT MAX(price) FROM food_product)

SELECT product_id , product_name, product_cd, category, price
FROM food_product
WHERE price IN ( SELECT max(price) FROM food_product)