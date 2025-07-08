--confirm we are working in the correct database
SELECT current_database();

drop table if exists membership, client, benefit cascade;

--create table
CREATE TABLE IF NOT EXISTS membership (
	membership_id SERIAL PRIMARY KEY,
	name TEXT UNIQUE,
	price INT NOT NULL
);

--create a second table
CREATE TABLE IF NOT EXISTS client (
	client_id SERIAL PRIMARY KEY,
	name TEXT NOT NULL,
	membership INT NOT NULL REFERENCES membership(membership_id)
);

--create a third table
CREATE TABLE IF NOT EXISTS benefit (
	benefit_id SERIAL PRIMARY KEY,
	name TEXT NOT NULL,
	membership INT NOT NULL REFERENCES membership(membership_id)
);

--CRUD OPERATIONS

--CREATE
INSERT INTO membership (name, price) VALUES
  ('Basic', 10),
  ('Premium', 20),
  ('VIP', 30);

SELECT * FROM membership;

INSERT INTO client (name, membership) VALUES
  ('Alice', (SELECT membership_id FROM membership WHERE name='Basic')),
  ('Bob',   (SELECT membership_id FROM membership WHERE name='Premium')),
  ('Carol', (SELECT membership_id FROM membership WHERE name='VIP')),
  ('Dave',  (SELECT membership_id FROM membership WHERE name='Basic')),
  ('Eve',   (SELECT membership_id FROM membership WHERE name='Premium'));

SELECT * FROM client;

INSERT INTO benefit (name, membership) VALUES
  ('Free Shipping lvl 1',     (SELECT membership_id FROM membership WHERE name='Basic')),
  ('Priority Support lvl 1',  (SELECT membership_id FROM membership WHERE name='Basic')),
  ('Free Shipping lvl 2',     (SELECT membership_id FROM membership WHERE name='Premium')),
  ('Priority Support lvl 2',  (SELECT membership_id FROM membership WHERE name='Premium')),
  ('Free Shipping lvl 3',     (SELECT membership_id FROM membership WHERE name='VIP')),
  ('Priority Support lvl 3',  (SELECT membership_id FROM membership WHERE name='VIP'));

--READ
SELECT membership_id, price
  FROM membership
 WHERE price > 20;

--UPDATE
UPDATE membership
   SET price = price * 1.20
 WHERE name = 'Premium';

UPDATE client
   SET membership = (SELECT membership_id FROM membership WHERE name='Premium')
 WHERE name = 'Dave';

--DELETE
DELETE FROM benefit
 WHERE name = 'Priority Support lvl 1'
   AND membership = (SELECT membership_id FROM membership WHERE name='Basic');

SELECT * FROM benefit;

--JOIN
SELECT c.client_id, c.name AS client_name,
       m.name AS membership_name, m.price
  FROM client AS c
  INNER JOIN membership AS m
    ON c.membership = m.membership_id;

SELECT * FROM benefit;

SELECT b.name AS benefit_name,
	m.name as membership_name, m.price
	FROM benefit as b
	INNER JOIN membership as m
	ON b.membership = m.membership_id;

--LEFT OUTER JOIN
SELECT m.membership_id, m.name AS membership_name,
       b.name AS benefit_name
  FROM membership AS m
  LEFT OUTER JOIN benefit AS b
    ON b.membership = m.membership_id;

--CROSS JOIN (permutations)
SELECT c.name, m.name as membership_name
  FROM client AS c
  CROSS JOIN membership AS m;