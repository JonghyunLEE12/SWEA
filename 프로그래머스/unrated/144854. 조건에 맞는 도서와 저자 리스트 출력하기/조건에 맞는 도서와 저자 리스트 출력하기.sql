# -- 코드를 입력하세요

# SELECT A.BOOK_ID, B.AUTHOR_NAME,
# DATE_FORMAT(A.PUBLISHED_DATE,'%Y-%m-%d') AS PUBLISHED_DATE
# FROM BOOK AS A
# JOIN AUTHOR AS B
# ON A.AUTHOR_ID = B.AUTHOR_ID
# WHERE A.CATEGORY LIKE '경제'
# ORDER BY A.PUBLISHED_DATE


# SELECT BOOK.BOOK_ID,AUTHOR.AUTHOR_NAME,
# DATE_FORMAT(BOOK.PUBLISHED_DATE,'%Y-%m-%d') AS PUBLISHED_DATE
# FROM BOOK AS BOOK
# JOIN AUTHOR AS AUTHOR
# ON BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID
# WHERE BOOK.CATEGORY LIKE '경제'
# ORDER BY BOOK.PUBLISHED_DATE













SELECT BOOK.BOOK_ID, AUTHOR.AUTHOR_NAME, 
DATE_FORMAT(BOOK.PUBLISHED_DATE , '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK AS BOOK
JOIN AUTHOR AS AUTHOR
ON BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID
WHERE BOOK.CATEGORY LIKE '경제'
ORDER BY BOOK.PUBLISHED_DATE
