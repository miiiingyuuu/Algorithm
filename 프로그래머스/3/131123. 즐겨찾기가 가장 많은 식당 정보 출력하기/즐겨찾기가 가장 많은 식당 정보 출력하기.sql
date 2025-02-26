SELECT T.FOOD_TYPE, T.REST_ID, T.REST_NAME, T.FAVORITES
FROM REST_INFO T
    JOIN (
        SELECT FOOD_TYPE, MAX(FAVORITES) AS MAX_FAVORITES
        FROM REST_INFO
        GROUP BY FOOD_TYPE
    ) M ON T.FOOD_TYPE = M.FOOD_TYPE AND T.FAVORITES = M.MAX_FAVORITES
ORDER BY T.FOOD_TYPE DESC