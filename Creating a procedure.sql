CREATE SCHEMA `radnici` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci ;
USE radnici;
#kreiranje i popunjavanje tabele korisnici
CREATE TABLE `radnici`.`korisnici` (
  `korisnik` INT NOT NULL AUTO_INCREMENT,
  `ime` VARCHAR(45) NOT NULL,
  `prezime` VARCHAR(60) NOT NULL,
  `datum_rođenja` DATE NOT NULL,
  `korisničko_ime` VARCHAR(60) NOT NULL,
  `e_mail` VARCHAR(70) NOT NULL,
  `biografija` VARCHAR(8000) NOT NULL,
  `fotografija` BLOB NULL,
  PRIMARY KEY (`korisnik`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;
INSERT INTO korisnici (ime,prezime,datum_rođenja,korisničko_ime,e_mail,biografija)
VALUES ('Pera','Perić','1991-03-04','korisnik1','peraperic@gmail.com','Ro]en u Ni[u 1991. godine. Ravr[en Poljoprivredni fakultet u Beogradu. Završena srednja Mašinska škola u Nišu. Poznavanje rada na računaru. Znanje Engleskog jezija.');
INSERT INTO korisnici (ime,prezime,datum_rođenja,korisničko_ime,e_mail,biografija)
VALUES ('Mika','Mikić','1992-04-06','korisnik2','mikamikic@gmail.com','Ro]en u Pančevu 1992. godine. Ravr[en Elektrotehnički fakultet u Beogradu. Završena srednja Elektrotehnička škola u Pančevu. Poznavanje rada na računaru. Znanje Engleskog jezija.');
INSERT INTO korisnici (ime,prezime,datum_rođenja,korisničko_ime,e_mail,biografija)
VALUES ('Joca','Jocić','1993-07-08','korisnik2','jojajocic@gmail.com','Ro]en u Somboru 1993. godine. Ravr[en Tehnološki fakultet u Beogradu. Završena srednja Tehnička škola u Somboru. Poznavanje rada na računaru. Znanje Nemačkog jezija. ');
#kreiranje i popunjavanje tabele plata
CREATE TABLE `radnici`.`plata` (
  `plataid` INT NOT NULL AUTO_INCREMENT,
  `korisnik` INT NOT NULL,
  `iznos_plate` DECIMAL(7,2) NOT NULL,
  `datum_plate` DATE NOT NULL,
  `isplaćena_ili_ne` VARCHAR(45) NOT NULL,
  `ugovor` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`plataid`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;
INSERT INTO plata (korisnik,datum_plate,iznos_plate,isplaćena_ili_ne,ugovor)
VALUES (3,'2022-03-04',78978.89,'isplaćena','na neodređeno');
INSERT INTO plata (korisnik,datum_plate,iznos_plate,isplaćena_ili_ne,ugovor)
VALUES (2,'2022-03-04',69778.80,'isplaćena','na neodređeno');
INSERT INTO plata (korisnik,datum_plate,iznos_plate,isplaćena_ili_ne,ugovor)
VALUES (1,'2022-03-04',81978.00,'isplaćena','na neodređeno');
#kreiranje i popunjavanje tabele poruke
CREATE TABLE `radnici`.`poruke` (
  `porukeid` INT NOT NULL AUTO_INCREMENT,
  `pošiljalac` INT NOT NULL,
  `primalac` INT NOT NULL,
  `poruka` VARCHAR(5000) NOT NULL,
  `datum_poruke` DATE NOT NULL,
  `status_poruke` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`porukeid`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;
INSERT INTO  poruke (pošiljalac,primalac,poruka,datum_poruke,status_poruke)
VALUES (1,2,'Da li ideš u bioskop?','2022-05-06','pročitano');
INSERT INTO  poruke (pošiljalac,primalac,poruka,datum_poruke,status_poruke)
VALUES (2,1,'Moram da se dogovorim sa  Jocom. Obećao sam mu.','2022-05-06','pročitano');
INSERT INTO  poruke (pošiljalac,primalac,poruka,datum_poruke,status_poruke)
VALUES (2,3,'Hoćemo li ići u bioskop?','2022-05-06','pročitano');
INSERT INTO  poruke (pošiljalac,primalac,poruka,datum_poruke,status_poruke)
VALUES (3,2,'Može.','2022-05-06','pročitano');
INSERT INTO  poruke (pošiljalac,primalac,poruka,datum_poruke,status_poruke)
VALUES (3,1,'Idemo u bioskop. Hoceš li sa nama?','2022-05-06','pročitano');
INSERT INTO  poruke (pošiljalac,primalac,poruka,datum_poruke,status_poruke)
VALUES (1,3,'Hoću.','2022-05-06','pročitano');
#povezivanje tabela
ALTER TABLE `radnici`.`korisnici` 
ADD CONSTRAINT `fk_plata`
  FOREIGN KEY (`korisnik`)
  REFERENCES `radnici`.`plata` (`plataid`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_posiljalac`
  FOREIGN KEY (`korisnik`)
  REFERENCES `radnici`.`poruke` (`porukeid`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_primalac`
  FOREIGN KEY (`korisnik`)
  REFERENCES `radnici`.`poruke` (`porukeid`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
  #kreiranje kompozitnog indeksa za pretragu po imenu , prezimeneu i korisničkom imenu tebele korisnici
  ALTER TABLE `radnici`.`korisnici` 
 ADD INDEX `idx_ime_prezime` (`ime` ASC, `prezime` ASC, `korisničko_ime` ASC);
 #kreiranje kompozitnog indeksa za pretragu po korisniku i datumu plate tebele plata
 ALTER TABLE `radnici`.`plata` 
ADD INDEX `idx_korisnik_datum` (`korisnik` ASC, `datum_plate` ASC);
#kreiranje kompozitnog indeksa za pretragu po pošiljaovcu i primaovcu i full text po porukama tebele poruke
ALTER TABLE `radnici`.`poruke` 
ADD INDEX `idx_posiljalac_primalac` (`pošiljalac` ASC, `primalac` ASC) ,
ADD FULLTEXT INDEX `idx_poruka` (`poruka`);
# kreiranje pogleda sa podacima o korisnicima
CREATE VIEW `podaci` AS SELECT ime, prezime,datum_rođenja, biografija FROM korisnici;
#procedura za unos korisnika u tabelu korisnici
DROP procedure IF EXISTS `unos_korisnika`;
DELIMITER $$
USE `radnici`$$
CREATE PROCEDURE `unos_korisnika` (parm1 varchar(60),parm2 varchar(60), parm3 date, parm4 varchar(60),parm5 varchar(60),
parm6 varchar (5000))
BEGIN
INSERT INTO korisnici (ime,prezime,datum_rođenja,korisničko_ime,e_mail,biografija)
VALUES (parm1,parm2,parm3,parm4,parm5,parm6);
END$$
DELIMITER ;
# izmena korisnika u tabeli korisnici
DROP procedure IF EXISTS `izmena_korisnika`;
DELIMITER $$
USE `radnici`$$
CREATE PROCEDURE `izmena_korisnika` (korisnikid int,parm1 varchar(60),parm2 varchar(60), parm3 date, parm4 varchar(60),parm5 varchar(60),parm6 varchar (5000))
BEGIN
UPDATE korisnici SET ime=parm1, prezime=parm2, datum_rođenja=parm3, korisničko_ime=parm4, e_mail=parm5, biografija=parm6
 WHERE  korisnik=korisnikid;
END$$
DELIMITER ;
#brisanje korisnika iz tabele korisnici
DROP procedure IF EXISTS `brisanje_korisnika`;
DELIMITER $$
USE `radnici`$$
CREATE PROCEDURE `brisanje_korisnika` (id int)
BEGIN
DELETE FROM korisnici   WHERE  korisnik=id;
END$$
DELIMITER ;
# unos podataka o platama
DROP procedure IF EXISTS `unos_plate`;
DELIMITER $$
USE `radnici`$$
CREATE PROCEDURE `unos_plate` (p1 int,p2 decimal(7,2), p3 date, p4 varchar(60), p5 varchar(60))
BEGIN
INSERT INTO plata (korisnik,iznos_plate,datum_plate,isplaćena_ili_ne,ugovor)
VALUES (p1,p2,p3,p4,p5);
END$$
DELIMITER ;
#brisanje podataka o platama
DROP procedure IF EXISTS `brisanje_plate`;
DELIMITER $$
USE `radnici`$$
CREATE PROCEDURE `brisanje_plate` (idplata int)
BEGIN
DELETE FROM plata WHERE plataid=idplata;
END$$
DELIMITER ;
#izmena u tabeli plata
DROP procedure IF EXISTS `izmena_plata`;
DELIMITER $$
USE `radnici`$$
CREATE PROCEDURE `izmena_plata` (idx int,pr1 int, pr2 decimal(7,2),pr3 date,pr4 varchar(60),pr5 varchar(60) )
BEGIN
UPDATE plata SET korisnik=pr1, iznos_plate=pr2, datum_plate=pr3, isplaćena_ili_ne=pr4,ugovor=pr5
 WHERE plataid=idx ;
END$$
DELIMITER ;
#dodavanje poruka u tabeli poruke
DROP procedure IF EXISTS `unos_poruke`;
DELIMITER $$
USE `radnici`$$
CREATE PROCEDURE `unos_poruke` ( par1 int,par2 int, par3 varchar(3000), par4 date, par5 varchar(60))
BEGIN
INSERT INTO poruke (pošiljalac,primalac,poruka,datum_poruke,status_poruke)
VALUES (par1,par2,par3,par4,par5);
END$$
DELIMITER ;
#brisanje poruka iz tabele poruke
DROP procedure IF EXISTS `brisanje_poruke`;
DELIMITER $$
USE `radnici`$$
CREATE PROCEDURE `brisanje_poruke` (idporuke int)
BEGIN
DELETE FROM poruke WHERE porukeid=idporuke;
END$$
DELIMITER ;
#izmena poruka u tabeli poruke
DROP procedure IF EXISTS `izmena_poruke`;
DELIMITER $$
USE `radnici`$$
CREATE PROCEDURE `izmena_poruke` (idx int,pr1 int, pr2 int,pr3 varchar(3000),pr4 date,pr5 varchar(60) )
BEGIN
UPDATE poruke SET pošiljalac=pr1, primalac=pr2,poruka=pr3, datum_poruke=pr4,status_poruke=pr5
 WHERE porukeid=idx ;
END$$
DELIMITER ; 
#broj poslatih poruka po korisniku
DROP function IF EXISTS `poslate_poruke`;
DELIMITER $$
USE `radnici`$$
CREATE FUNCTION poslate_poruke(id int)
RETURNS INTEGER
BEGIN
RETURN (SELECT COUNT(pošiljalac) FROM poruke WHERE pošiljalac=id);
END$$
DELIMITER ;
















 
 

  
  
  


