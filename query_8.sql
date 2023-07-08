SELECT t.teacher_name, sub.subject_name, Round(AVG(r.raiting),2) AS rait
FROM subject sub
LEFT JOIN teachers t ON t.ID = sub.teacher_id
LEFT JOIN raiting r ON r.subject_id = sub.ID
WHERE t.ID = 2
GROUP BY t.teacher_name, sub.subject_name;