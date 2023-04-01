# # -- 코드를 입력하세요
# SELECT 
# CONCAT('/home/grep/src',FILE.BOARD_ID ,'/',FILE.FILE_ID,FILE.FILE_NAME,FILE.FILE_EXT) AS FILE_PATH
# FROM USED_GOODS_BOARD AS BOARD
# JOIN USED_GOODS_FILE AS FILE
# ON BOARD.BOARD_ID = FILE.BOARD_ID
# WHERE BOARD.VIEWS = ( SELECT MAX(b1.views) FROM USED_GOODS_BOARD b1)
# ORDER BY FILE.FILE_ID DESC

# SELECT concat('/home/grep/src/',f.board_id,'/',f.file_id, f.file_name, f.file_ext) as file_path
# from used_goods_file f 
# join used_goods_board b
# on f.board_id = b.board_id
# where b.views = (select max(b1.views) from used_goods_board b1 )
# order by f.file_id desc


SELECT 
CONCAT('/home/grep/src/',FL.BOARD_ID,'/',FL.FILE_ID,FL.FILE_NAME,FL.FILE_EXT)
AS FILE_PATH
FROM USED_GOODS_FILE AS FL
JOIN USED_GOODS_BOARD AS BD
ON FL.BOARD_ID = BD.BOARD_ID
WHERE BD.VIEWS = (SELECT MAX(B1.VIEWS) FROM USED_GOODS_BOARD B1)
ORDER BY FL.FILE_ID DESC












