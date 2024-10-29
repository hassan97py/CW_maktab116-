select sq.team as team, sum(sq.women) as female_medalists,
sum(sq.men) as male_medalists,
(case when sum(sq.men)=0 then null else ROUND( sum(sq.women)/(sum(sq.men)+0.0), 2) end ) as female_to_male_ratio 
from (select team, (case when sex='F' and medal is not null then 1 else 0 end) as women, (case when sex='M' and medal is not null then 1 else 0 end) as men from athletes where medal is not null) as sq group by team having sum(sq.women) >=7 order by female_medalists desc,female_to_male_ratio desc limit 22 ;