-- 코드를 입력하세요
SELECT A.product_code AS 'PRODUCT_CODE', SUM(A.price * B.sales_amount) AS 'SALES'
FROM PRODUCT AS A JOIN OFFLINE_SALE AS B
ON A.product_id = B.product_id
GROUP BY A.product_code
ORDER BY  SALES DESC , PRODUCT_CODE
