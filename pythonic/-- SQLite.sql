-- SQLite
SELECT id, fname, lname, username, email, image_file, bio, password
FROM user;
CREATE TABLE User (
    id INTEGER PRIMARY KEY,
    fname VARCHAR(80) NOT NULL,
    lname VARCHAR(80) NOT NULL,
    username VARCHAR(80) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    image_file VARCHAR(255),
    bio TEXT,
    password VARCHAR(80) NOT NULL
);