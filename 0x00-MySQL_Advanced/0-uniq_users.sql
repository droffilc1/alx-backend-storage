-- creates a table users with id, email, name attributes
-- can be executed on any database
CREATE TABLE IF NOT EXISTS users (
	id INT AUTO_INCREMENT PRIMARY KEY,
       	email VARCHAR(255) NOT NULL UNIQUE,
       	name VARCHAR(255)
);
