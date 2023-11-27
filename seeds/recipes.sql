-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Create a table to store recipes
CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  recipe_name text,
  cooking_time int,
  rating int
);

INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Spaghetti Carbonara', 30, 4);
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Chicken Kiev', 45, 5);
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Vegetable Stir-Fry', 20, 3);
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Beef Tacos', 35, 4);
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Chocolate Brownies', 40, 5);
