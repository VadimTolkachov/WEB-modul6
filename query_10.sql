SELECT s.name, t.teacher_name, sub.subject_name
FROM raiting r
LEFT JOIN students s ON s.id = r.student_id
LEFT JOIN subject sub ON sub.ID = r.subject_id
LEFT JOIN teachers t ON t.ID = sub.teacher_id
WHERE s.id = 1 AND t.ID = 2;