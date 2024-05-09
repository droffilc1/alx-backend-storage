-- creates a trigger that decreses the quanity of an item
-- afyter adding a new order
DELIMITER $$ 
CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON `orders`
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END;

$$
DELIMITER ;
