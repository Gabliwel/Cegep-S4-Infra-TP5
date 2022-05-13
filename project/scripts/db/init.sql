CREATE DATABASE usersDB;
use usersDB;

CREATE TABLE users (
	username VARCHAR(32) NOT NULL,
	isInitialUser BIT DEFAULT 0 NOT NULL,
	UNIQUE(username)
);

INSERT INTO users (
	username,
	isInitialUser
)

VALUES (
	'Bob',
	1
);

INSERT INTO users (
	username,
	isInitialUser
)

VALUES (
	'Bill',
	0
);

INSERT INTO users (
	username,
	isInitialUser
)

VALUES (
	'Body',
	1
);

INSERT INTO users (
	username,
	isInitialUser
)

VALUES (
	'Joe',
	0
);

INSERT INTO users (
	username,
	isInitialUser
)

VALUES (
	'Jack',
	0
);