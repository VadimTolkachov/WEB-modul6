SELECT s.group_id, sub.subject_name, s.name, r.raiting 
FROM raiting r
LEFT JOIN students s ON s.id = r.student_id
LEFT JOIN subject sub ON sub.ID = r.subject_id
WHERE s.group_id =2 AND sub.ID = 1;