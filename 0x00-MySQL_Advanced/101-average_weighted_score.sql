-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  UPDATE users
    SET average_score = (
        SELECT 
            SUM(c.score * p.weight) / SUM(p.weight)
        FROM corrections c
        JOIN projects p ON p.id = c.project_id
        WHERE c.user_id = users.id
    );
END $$

DELIMITER ;
