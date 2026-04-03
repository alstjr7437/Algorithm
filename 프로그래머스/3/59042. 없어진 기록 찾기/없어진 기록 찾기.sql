-- 코드를 입력하세요
SELECT b.ANIMAL_ID, b.NAME
from ANIMAL_INS as a
right join animal_outs as b
on b.ANIMAL_ID = a.ANIMAL_ID
where isnull(a.ANIMAL_ID)