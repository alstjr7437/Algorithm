-- 코드를 입력하세요
SELECT a.flavor
from FIRST_HALF a
join ICECREAM_INFO b on a.flavor = b.flavor
where b.INGREDIENT_TYPE = 'fruit_based'
    and a.TOTAL_ORDER > 3000