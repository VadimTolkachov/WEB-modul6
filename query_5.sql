SELECT teachers.teacher_name, subject.subject_name
FROM teachers
LEFT JOIN subject ON subject.teacher_id = teachers.ID
WHERE teachers.ID = 2;
