-- digit. kandidater (KL 2019)
select c.name, s.code||'/'||u.ref, u.year_from||'-'||u.year_to, x.n, case when c.county is null then '?' else c.county end
from creator c, series s, unit u,
(select r.unit_id uid, count(*) n from request r where r.status not in ('rejected','cancelled','done') and r.requested >= '2024-01-01' group by r.unit_id) x
where s.creator_id=c.id and u.series_id=s.id and x.uid=u.id and u.digitised=0 and u.restricted<>1
and (u.year_to < 1960 or c.id in (select s2.creator_id from series s2 where s2.code='A'))
and x.n > (select count(*)*1.0/count(distinct unit_id) from request where status='open') - 1
order by 4 desc, 3
