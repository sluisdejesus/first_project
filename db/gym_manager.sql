DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  age INT
);

CREATE TABLE classes(
    id SERIAL PRIMARY KEY,
    class_name VARCHAR(255),
    instructor VARCHAR(255),
    weekday VARCHAR(255),
    time VARCHAR(255)
);

CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    class_id INT REFERENCES classes(id) ON DELETE CASCADE
);