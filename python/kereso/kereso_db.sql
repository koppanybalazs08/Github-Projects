CREATE DATABASE  IF NOT EXISTS `kereso_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `kereso_db`;
-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: kereso_db
-- ------------------------------------------------------
-- Server version	8.0.46

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `fizetes`
--

DROP TABLE IF EXISTS `fizetes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fizetes` (
  `id` int NOT NULL DEFAULT '0',
  `brutto` int DEFAULT NULL,
  `bonus` double DEFAULT NULL,
  `netto` int GENERATED ALWAYS AS ((`brutto` * `bonus`)) STORED,
  PRIMARY KEY (`id`),
  CONSTRAINT `fizetes_ibfk_1` FOREIGN KEY (`id`) REFERENCES `szemelyek` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fizetes`
--

LOCK TABLES `fizetes` WRITE;
/*!40000 ALTER TABLE `fizetes` DISABLE KEYS */;
INSERT INTO `fizetes` (`id`, `brutto`, `bonus`) VALUES (1,500,1.05),(2,450,1),(3,455,1.2),(4,450,1.35),(5,450,0.98),(6,694,1.05),(7,712,1),(8,1288,1.1),(9,50,1.5);
/*!40000 ALTER TABLE `fizetes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `szemelyek`
--

DROP TABLE IF EXISTS `szemelyek`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `szemelyek` (
  `id` int NOT NULL AUTO_INCREMENT,
  `keresztnev` varchar(30) DEFAULT NULL,
  `vezeteknev` varchar(30) DEFAULT NULL,
  `beosztas` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `szemelyek`
--

LOCK TABLES `szemelyek` WRITE;
/*!40000 ALTER TABLE `szemelyek` DISABLE KEYS */;
INSERT INTO `szemelyek` VALUES (1,'Ica','Kukor','Hr Manager'),(2,'József','Kovács','Junior dev'),(3,'Dénes','Gábor','Junior dev'),(4,'János','Kiss','Junior dev'),(5,'Dénes','Gábor','Junior dev'),(6,'Sándor','Kovács','Medior dev'),(7,'Ágoston','Keleti','Medior dev'),(8,'János','Nagy','Senior dev/Project Manager'),(9,'Benő','Szegedi','Intern'),(10,'Béla','Tiszta','takarító');
/*!40000 ALTER TABLE `szemelyek` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-08-18 13:03:34
