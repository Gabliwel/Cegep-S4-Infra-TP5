CREATE DATABASE usersDB;
use usersDB;

CREATE TABLE users (
	username VARCHAR(32) NOT NULL,
	isInitialUser BIT DEFAULT 0 NOT NULL,
	UNIQUE(username)
);
