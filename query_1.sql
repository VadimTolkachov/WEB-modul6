select s.name, round(AVG(raiting), 2) as average_grade
FROM raiting g
left join students s on s.id = g.student_id
group by s.name
order by average_grade DESC
limit 5;