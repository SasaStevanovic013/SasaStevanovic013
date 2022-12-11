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

