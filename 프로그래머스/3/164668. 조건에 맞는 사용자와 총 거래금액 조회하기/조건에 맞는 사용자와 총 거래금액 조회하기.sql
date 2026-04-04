-- 코드를 입력하세요
SELECT u.USER_ID, u.NICKNAME, sum(b.price) as TOTAL_SALES
from USED_GOODS_BOARD as b
join USED_GOODS_USER as u
on u.user_id = b.writer_id
where b.STATUS = 'DONE'
group by u.user_id
having 700000 <= sum(b.price)
order by TOTAL_SALES

# select *
# from USED_GOODS_BOARD