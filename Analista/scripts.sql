--
-- File generated with SQLiteStudio v3.0.6 on qui jun 11 16:39:02 2015
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: medical_address
CREATE TABLE "medical_address" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "zipcode" varchar(9) NOT NULL, "address1" varchar(200) NOT NULL, "address2" varchar(200) NOT NULL, "number" decimal NOT NULL, "district" varchar(200) NOT NULL, "city" varchar(200) NOT NULL, "state" varchar(200) NOT NULL, "patient_id" integer NULL UNIQUE REFERENCES "medical_patient" ("id"));
INSERT INTO medical_address (id, zipcode, address1, address2, number, district, city, state, patient_id) VALUES (1, '99223-002', 'Rua do Limoeiro', '502', 324, 'Jardim Botânico', 'Porto Alegre', 'RS', 1);
INSERT INTO medical_address (id, zipcode, address1, address2, number, district, city, state, patient_id) VALUES (2, '73872-023', 'Rua Ferreira da Silva', '209', 2345, 'Bela Vista', 'Porto Alegre', 'RS', 2);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
