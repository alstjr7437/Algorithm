-- https://school.programmers.co.kr/learn/courses/30/lessons/151136 
-- round 부분
SELECT round(avg(daily_fee),0) as AVERAGE_FEE
from CAR_RENTAL_COMPANY_CAR 
where car_type = "SUV";

-- https://school.programmers.co.kr/learn/courses/30/lessons/144853
-- date_format 부분, year부분ㄴ
SELECT BOOK_ID, 
    date_format(PUBLISHED_DATE, "%Y-%m-%d") as PUBLISHED_DATE 
from BOOK 
where year(published_Date) = 2021 
    and category = "인문" 
order by published_date asc;

-- https://school.programmers.co.kr/learn/courses/30/lessons/132201
-- ifnull 부분, 문제 잘 읽어보기
SELECT PT_NAME, 
    PT_NO, 
    GEND_CD, 
    AGE, 
    ifnull(TLNO, "NONE") as TLNO 
from PATIENT 
where AGE <= 12 and GEND_CD = "W"
order by age desc, PT_NAME asc;

-- https://school.programmers.co.kr/learn/courses/30/lessons/131120
-- ISNOTNULL 부분
SELECT MEMBER_ID, 
    MEMBER_NAME, 
    GENDER, 
    date_format(date_of_birth, "%Y-%m-%d") as DATE_OF_BIRTH
from MEMBER_PROFILE
where month(date_of_birth) = 3 
    and TLNO IS NOT NULL 
    and gender = "W"
order by member_id asc;

-- https://school.programmers.co.kr/learn/courses/30/lessons/133024
-- 여러개 정렬
SELECT flavor
from FIRST_HALF
order by total_order desc, shipment_id asc;
