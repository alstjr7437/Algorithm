-- 코드를 입력하세요
SELECT year(SALES_DATE) as YEAR, month(SALES_DATE) as MONTH, count(DISTINCT u.user_id) as PURCHASED_USERS,
    round(count(distinct u.user_id) / (
        SELECT COUNT(*) FROM USER_INFO WHERE joined LIKE '2021%'
    ), 1) as PUCHASED_RATIO
from USER_INFO as u
join ONLINE_SALE as o
on u.user_id = o.user_id
where year(u.JOINED) = 2021
group by year, month

# select *
# from ONLINE_SALE