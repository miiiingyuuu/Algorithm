-- 코드를 입력하세요
SELECT P.PRODUCT_ID, P.PRODUCT_NAME, SUM(P.PRICE * O.AMOUNT) AS TOTAL_SALES
FROM FOOD_PRODUCT P
JOIN FOOD_ORDER O ON P.PRODUCT_ID = O.PRODUCT_ID
WHERE O.PRODUCE_DATE BETWEEN '2022-05-01' AND '2022-05-31'
GROUP BY P.PRODUCT_ID, P.PRODUCT_NAME
ORDER BY TOTAL_SALES DESC, P.PRODUCT_ID ASC