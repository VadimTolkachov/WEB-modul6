SELECT sub.subject_name, s.name, ROUND(AVG(r.raiting), 2) AS avg_raiting
FROM raiting r
LEFT JOIN students s ON s.id = r.student_id
LEFT JOIN subject sub ON sub.ID = r.subject_id
WHERE sub.ID = 1
GROUP BY s.id
ORDER BY avg_raiting DESC
LIMIT 1;