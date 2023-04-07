CREATE TABLE phonebook (
	id NUMBER PRIMARY KEY,
	name VARCHAR2(50) NOT NULL,
	phone VARCHAR2(100),
	email VARCHAR2(100),
	age NUMBER DEFAULT 21,
	memo CLOB,
	regDate DATE
);