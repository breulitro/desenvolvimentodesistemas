CREATE TABLE "medical_patient" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"email" varchar(80) NOT NULL UNIQUE,
	"name" varchar(80) NOT NULL,
	"lastname" varchar(80) NOT NULL,
	"occupation" varchar(200) NOT NULL,
	"gender" varchar(1) NOT NULL,
	"date_of_birth" date NULL,
	"nationality" varchar(200) NOT NULL
	);

CREATE TABLE "medical_address" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"zipcode" varchar(9) NOT NULL,
	"address1" varchar(200) NOT NULL,
	"address2" varchar(200) NOT NULL,
	"number" decimal NOT NULL,
	"district" varchar(200) NOT NULL,
	"city" varchar(200) NOT NULL,
	"state" varchar(200) NOT NULL,
	"patient_id" integer NULL UNIQUE REFERENCES "medical_patient" ("id")
	);

CREATE TABLE "medical_accesscounter" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "access_date" date NOT NULL
	);
