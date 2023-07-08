SELECT s.name AS student_fullname, sub.subject_name
FROM raiting r
LEFT JOIN students s ON s.id = r.student_id
LEFT JOIN subject sub ON sub.ID = r.subject_id
WHERE s.id = 1;