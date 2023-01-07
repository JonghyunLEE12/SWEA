-- 코드를 입력하세요
# SELECT *
# FROM BOOK_SALES AS C
# WHERE SALES_DATE LIKE '2022-01%'


SELECT A.AUTHOR_ID,A.AUTHOR_NAME,B.CATEGORY,sum(SALES*PRICE) AS TOTAL_SALES
FROM AUTHOR AS A
JOIN BOOK AS B
ON A.AUTHOR_ID = B.AUTHOR_ID
JOIN BOOK_SALES AS C
ON B.BOOK_ID  = C.BOOK_ID
WHERE C.SALES_DATE LIKE '2022-01%'
GROUP BY 1,2,3
ORDER BY AUTHOR_ID , CATEGORY DESC