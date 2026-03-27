-- 코드를 입력하세요
select MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
from MEMBER_PROFILE 
where month(Date_of_birth) = 3 and TLNO is not null and gender = 'W'