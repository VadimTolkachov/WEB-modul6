SELECT g.group_name, sub.subject_name, ROUND(AVG(r.raiting),2) AS rait
FROM raiting r
LEFT JOIN students s ON s.id = r.student_id
LEFT JOIN subject sub ON sub.ID = r.subject_id
LEFT JOIN groups g ON g.ID = s.group_id
WHERE sub.ID = 3
GROUP BY g.group_name, sub.subject_name;