-- SELECT REPLACE(ColumnName, Character/String to be change, New String/Character)
-- FROM TableName; 

select StudentID, Email, replace(Email, 'yahoo', 'gmail') as New_Email from students;