-- ----------------------------------------------------------------------------
-- MySQL Workbench Migration
-- Migrated Schemata: project
-- Source Schemata: project
-- Created: Tue Sep 21 20:58:09 2021
-- Workbench Version: 8.0.26
-- ----------------------------------------------------------------------------

SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------------------------------------------------------
-- Schema project
-- ----------------------------------------------------------------------------
DROP SCHEMA IF EXISTS `project` ;
CREATE SCHEMA IF NOT EXISTS `project` ;
USE `project` ;

-- ----------------------------------------------------------------------------
-- Table project.booking
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`booking` (
  `PNR_no` INT NOT NULL AUTO_INCREMENT ,
  `Username` VARCHAR(45) NULL DEFAULT NULL,
  `Journey_date` VARCHAR(45) NULL DEFAULT NULL,
  `Start_Station` VARCHAR(45) NULL DEFAULT NULL,
  `End_Station` VARCHAR(45) NULL DEFAULT NULL,
  `Train_no` INT NULL DEFAULT NULL,
  `Train_name` VARCHAR(45) NULL DEFAULT NULL,
  `Class` VARCHAR(45) NULL DEFAULT NULL,
  `Seats` INT NULL DEFAULT NULL,
  `Price` INT NULL DEFAULT NULL,
  PRIMARY KEY (`PNR_no`));




-- ----------------------------------------------------------------------------
-- Table project.day1
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`day1` (
  `Class` VARCHAR(45) NOT NULL,
  `Intercity` INT NULL DEFAULT NULL,
  `Vindhyachal_Exp` INT NULL DEFAULT NULL,
  `Shatabdi_Exp` INT NULL DEFAULT NULL,
  `Taj_Exp` INT NULL DEFAULT NULL,
  `Gatiman_Exp` INT NULL DEFAULT NULL,
  `Malwa_Exp` INT NULL DEFAULT NULL,
  PRIMARY KEY (`Class`));


INSERT INTO `day1` VALUES ('1AC',12,12,12,12,12,12),('2AC',27,27,27,27,27,27),('2S',53,53,53,53,53,53),('3AC',32,32,32,32,32,32),('CC',39,39,39,39,39,39),('SL',40,40,40,40,40,40);

-- ----------------------------------------------------------------------------
-- Table project.day2
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`day2` (
  `Class` VARCHAR(45) NOT NULL,
  `Intercity` INT NULL DEFAULT NULL,
  `Vindhyachal_Exp` INT NULL DEFAULT NULL,
  `Shatabdi_Exp` INT NULL DEFAULT NULL,
  `Taj_Exp` INT NULL DEFAULT NULL,
  `Gatiman_Exp` INT NULL DEFAULT NULL,
  `Malwa_Exp` INT NULL DEFAULT NULL,
  PRIMARY KEY (`Class`));


INSERT INTO `day2` VALUES ('1AC',12,12,12,12,12,12),('2AC',27,27,27,27,27,27),('2S',53,53,53,53,53,53),('3AC',32,32,32,32,32,32),('CC',39,39,39,39,39,39),('SL',40,40,40,40,40,40);

-- ----------------------------------------------------------------------------
-- Table project.day3
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`day3` (
  `Class` VARCHAR(45) NOT NULL,
  `Intercity` INT NULL DEFAULT NULL,
  `Vindhyachal_Exp` INT NULL DEFAULT NULL,
  `Shatabdi_Exp` INT NULL DEFAULT NULL,
  `Taj_Exp` INT NULL DEFAULT NULL,
  `Gatiman_Exp` INT NULL DEFAULT NULL,
  `Malwa_Exp` INT NULL DEFAULT NULL,
  PRIMARY KEY (`Class`));


INSERT INTO `day3` VALUES ('1AC',12,12,12,12,12,12),('2AC',27,27,27,27,27,27),('2S',53,53,53,53,53,53),('3AC',32,32,32,32,32,32),('CC',39,39,39,39,39,39),('SL',40,40,40,40,40,40);
-- ----------------------------------------------------------------------------
-- Table project.day4
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`day4` (
  `Class` VARCHAR(45) NOT NULL,
  `Intercity` INT NULL DEFAULT NULL,
  `Vindhyachal_Exp` INT NULL DEFAULT NULL,
  `Shatabdi_Exp` INT NULL DEFAULT NULL,
  `Taj_Exp` INT NULL DEFAULT NULL,
  `Gatiman_Exp` INT NULL DEFAULT NULL,
  `Malwa_Exp` INT NULL DEFAULT NULL,
  PRIMARY KEY (`Class`));


INSERT INTO `day4` VALUES ('1AC',12,12,12,12,12,12),('2AC',27,27,27,27,27,27),('2S',53,53,53,53,53,53),('3AC',32,32,32,32,32,32),('CC',39,39,39,39,39,39),('SL',40,40,40,40,40,40);
-- ----------------------------------------------------------------------------
-- Table project.day5
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`day5` (
  `Class` VARCHAR(45) NOT NULL,
  `Intercity` INT NULL DEFAULT NULL,
  `Vindhyachal_Exp` INT NULL DEFAULT NULL,
  `Shatabdi_Exp` INT NULL DEFAULT NULL,
  `Taj_Exp` INT NULL DEFAULT NULL,
  `Gatiman_Exp` INT NULL DEFAULT NULL,
  `Malwa_Exp` INT NULL DEFAULT NULL,
  PRIMARY KEY (`Class`));


INSERT INTO `day5` VALUES ('1AC',12,12,12,12,12,12),('2AC',27,27,27,27,27,27),('2S',53,53,53,53,53,53),('3AC',32,32,32,32,32,32),('CC',39,39,39,39,39,39),('SL',40,40,40,40,40,40);

-- ----------------------------------------------------------------------------
-- Table project.day6
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`day6` (
  `Class` VARCHAR(45) NOT NULL,
  `Intercity` INT NULL DEFAULT NULL,
  `Vindhyachal_Exp` INT NULL DEFAULT NULL,
  `Shatabdi_Exp` INT NULL DEFAULT NULL,
  `Taj_Exp` INT NULL DEFAULT NULL,
  `Gatiman_Exp` INT NULL DEFAULT NULL,
  `Malwa_Exp` INT NULL DEFAULT NULL,
  PRIMARY KEY (`Class`));


INSERT INTO `day6` VALUES ('1AC',12,12,12,12,12,12),('2AC',27,27,27,27,27,27),('2S',53,53,53,53,53,53),('3AC',32,32,32,32,32,32),('CC',39,39,39,39,39,39),('SL',40,40,40,40,40,40);

-- ----------------------------------------------------------------------------
-- Table project.day7
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`day7` (
  `Class` VARCHAR(45) NOT NULL,
  `Intercity` INT NULL DEFAULT NULL,
  `Vindhyachal_Exp` INT NULL DEFAULT NULL,
  `Shatabdi_Exp` INT NULL DEFAULT NULL,
  `Taj_Exp` INT NULL DEFAULT NULL,
  `Gatiman_Exp` INT NULL DEFAULT NULL,
  `Malwa_Exp` INT NULL DEFAULT NULL,
  PRIMARY KEY (`Class`));


INSERT INTO `day7` VALUES ('1AC',12,12,12,12,12,12),('2AC',27,27,27,27,27,27),('2S',53,53,53,53,53,53),('3AC',32,32,32,32,32,32),('CC',39,39,39,39,39,39),('SL',40,40,40,40,40,40);

-- ----------------------------------------------------------------------------
-- Table project.schedule
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`schedule` (
  `Day` INT NOT NULL,
  `Date` VARCHAR(45) NULL DEFAULT NULL,
  `Intercity` VARCHAR(45) NULL DEFAULT NULL,
  `Vindhyachal_Exp` VARCHAR(45) NULL DEFAULT NULL,
  `Shatabdi_Exp` VARCHAR(45) NULL DEFAULT NULL,
  `Taj_Exp` VARCHAR(45) NULL DEFAULT NULL,
  `Gatiman_Exp` VARCHAR(45) NULL DEFAULT NULL,
  `Malwa_Exp` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`Day`));



INSERT INTO `schedule` VALUES (1,'2021-09-23','Bhopal - BPL_Jhansi - JHS','','New Delhi - NDLS_Bhopal - BPL','','Jhansi - JHS_New Delhi - NDLS','New Delhi - NDLS_Agra Cantt - AGC'),(2,'2021-09-24','Jhansi - JHS_Bhopal - BPL','Bhopal - BPL_Agra Cantt - AGC','','Agra Cantt - AGC_Jhansi - JHS','',''),(3,'2021-09-25','','Agra Cantt - AGC_Bhopal - BPL','Bhopal - BPL_New Delhi - NDLS','','New Delhi - NDLS_Jhansi - JHS','Agra Cantt - AGC_New Delhi - NDLS'),(4,'2021-09-26','Bhopal - BPL_Jhansi - JHS','','','Jhansi - JHS_Agra Cantt - AGC','',''),(5,'2021-09-27','Jhansi - JHS_Bhopal - BPL','Bhopal - BPL_Agra Cantt - AGC','New Delhi - NDLS_Bhopal - BPL','','Jhansi - JHS_New Delhi - NDLS','New Delhi - NDLS_Agra Cantt - AGC'),(6,'2021-09-28','','Agra Cantt - AGC_Bhopal - BPL','','Agra Cantt - AGC_Jhansi - JHS','','Agra Cantt - AGC_New Delhi - NDLS'),(7,'2021-09-29','','','Bhopal - BPL_New Delhi - NDLS','Jhansi - JHS_Agra Cantt - AGC','New Delhi - NDLS_Jhansi - JHS','');
-- ----------------------------------------------------------------------------
-- Table project.seat_price
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`seat_price` (
  `Class` VARCHAR(45) NOT NULL,
  `Price` INT NULL DEFAULT NULL,
  PRIMARY KEY (`Class`));


INSERT INTO `seat_price` VALUES ('1AC',1500),('2AC',1000),('2S',500),('3AC',800),('CC',900),('SL',600);

-- ----------------------------------------------------------------------------
-- Table project.trains
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`trains` (
  `Train_no` INT NOT NULL,
  `Train_name` VARCHAR(45) NULL DEFAULT NULL,
  `Timing` VARCHAR(45) NULL DEFAULT NULL,
  `Route` VARCHAR(45) NULL DEFAULT NULL,
  `1AC` INT NULL DEFAULT NULL,
  `2AC` INT NULL DEFAULT NULL,
  `3AC` INT NULL DEFAULT NULL,
  `SL` INT NULL DEFAULT NULL,
  `2S` INT NULL DEFAULT NULL,
  `CC` INT NULL DEFAULT NULL,
  PRIMARY KEY (`Train_no`));


INSERT INTO `trains` VALUES (1,'Intercity','09:00-13:00','Bhopal - BPL_Jhansi - JHS',12,27,32,40,53,39),(2,'Vindhyachal_Exp','09:00-15:15','Bhopal - BPL_Agra Cantt - AGC',12,27,32,40,53,39),(3,'Shatabdi_Exp','09:00-20:00','Bhopal - BPL_New Delhi - NDLS',12,27,32,40,53,39),(4,'Taj_Exp','13:00 - 15:30','Jhansi - JHS_Agra Cantt - AGC',12,27,32,40,53,39),(5,'Gatiman_Exp','13:00 - 19:30','Jhansi - JHS_New Delhi - NDLS',12,27,32,40,53,39),(6,'Malwa_Exp','15:30-19:30','Agra Cantt - AGC_New Delhi - NDLS',12,27,32,40,53,39);
-- ----------------------------------------------------------------------------
-- Table project.users
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`users` (
  `User_ID` INT NOT NULL AUTO_INCREMENT,
  `Username` VARCHAR(45) NOT NULL,
  `User_Type` VARCHAR(45) NULL DEFAULT NULL,
  `F_name` VARCHAR(45) NULL DEFAULT NULL,
  `L_name` VARCHAR(45) NULL DEFAULT NULL,
  `Mobile_no` VARCHAR(45) NULL DEFAULT NULL,
  `Email` VARCHAR(45) NULL DEFAULT NULL,
  `Password` VARCHAR(45) NULL DEFAULT NULL,
  `DOB` VARCHAR(45) NULL DEFAULT NULL,
  `Wallet` INT NULL DEFAULT '0',
  PRIMARY KEY (`User_ID`),
  UNIQUE INDEX `Username_UNIQUE` (`Username` ASC),
  UNIQUE INDEX `L_name_UNIQUE` (`L_name` ASC) ,
  UNIQUE INDEX `Mobile_no_UNIQUE` (`Mobile_no` ASC))
AUTO_INCREMENT = 5;




INSERT INTO `users` VALUES (1,'G_coder','Admin','Gatij','Shakyawar','9893620986','gatij.shakya.29.11@gmail.com','gatij@2911','11/29/03',50000),(2,'Swastik117','Admin','Swastik','Bansal','7024069004','swastikbansal0@gmail.com','abcd1234','11/06/04',50000),(3,'a','','a','a','5086604150','a','a','1/1/04',26125),(4,'b',NULL,'b','b','1234567890','b','b','1/4/00',50000);
