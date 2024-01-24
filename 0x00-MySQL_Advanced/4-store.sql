-- Create a trigger that decreases the quantity of an item
-- After adding a new order

DELIMITER // ;

CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON orders FOR EACH ROW

-- BODY OF THE TRIGGER

BEGIN
    -- Update the item quantiy by decreasing from the order number
    UPDATE items SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END//
