-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema python_exam
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema python_exam
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `python_exam` DEFAULT CHARACTER SET utf8 ;
USE `python_exam` ;

-- -----------------------------------------------------
-- Table `python_exam`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `python_exam`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `alias` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(150) NULL,
  `birthday` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `python_exam`.`quotes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `python_exam`.`quotes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `quote` VARCHAR(200) NULL,
  `quote_by` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_quotes_users_idx` (`users_id` ASC),
  CONSTRAINT `fk_quotes_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `python_exam`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `python_exam`.`favorite_quote`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `python_exam`.`favorite_quote` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `user_id` INT NOT NULL,
  `quote_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_favorite_quote_users1_idx` (`user_id` ASC),
  INDEX `fk_favorite_quote_quotes1_idx` (`quote_id` ASC),
  CONSTRAINT `fk_favorite_quote_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `python_exam`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_favorite_quote_quotes1`
    FOREIGN KEY (`quote_id`)
    REFERENCES `python_exam`.`quotes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
