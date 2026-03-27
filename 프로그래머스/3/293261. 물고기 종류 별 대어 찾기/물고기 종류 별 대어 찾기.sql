-- 코드를 작성해주세요
select b.id, a.fish_name, b.length
from FISH_NAME_INFO a
join FISH_INFO as b on a.fish_type = b.fish_type
where b.fish_type in (
    select fish_type
    from FISH_INFO
    group by fish_type
    having length = max(length)
)
# group by a.FISH_NAME