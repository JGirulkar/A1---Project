-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: files
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `file_data`
--

DROP TABLE IF EXISTS `file_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `file_data` (
  `hash_values` varchar(255) DEFAULT NULL,
  `file_name` varchar(255) DEFAULT NULL,
  `date_added` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `file_data`
--

LOCK TABLES `file_data` WRITE;
/*!40000 ALTER TABLE `file_data` DISABLE KEYS */;
INSERT INTO `file_data` VALUES ('8b4c2973e47846a2d2efc381518e783aeb12b43508698334b8f00795b11106e2','Arun Sharma - How to Prepare for Quantitative Aptitude for the CAT-McGraw Hill Education (2018).pdf','2023-02-10 20:14:16'),('47fe855ed4b6d5355388ea8879525ba7b2e1ad9296fdac498e4ca29fe648ef3f','doc-corrupted.docx','2023-02-10 20:14:16'),('5368327537e68e6f34fb68249de6810dc4400a39fa52532cd75afe7968c5339b','doc-tampered.docx','2023-02-10 20:14:16'),('9f4ff4aa22ec0a526a164ab73d72f76546c13a753608f00374ed1267c854fb1c','doc.docx','2023-02-10 20:14:16'),('33d0990b64af34d53f36b623595da6653c57a6f9ed3356a2532f08e44ba6fa2f','file_example_JPG_500kB.jpg','2023-02-10 20:14:16'),('41ed54bb8778598c3faf847c18a25c21afae5f5e220a55d7a165433ead859ef8','file_example_MP3_700KB.mp3','2023-02-10 20:14:16'),('5bb3c86ea2ba32e0c6ab344d2bb89fff401293e30c64c7c25f744f3194e0d242','file_example_MP4_480_1_5MG.mp4','2023-02-10 20:14:16'),('ae44064cc9a439127ed4fd98c3395443a4b27fd8789aecc0e61ee9a09e0e4ef3','sample-img1.1.png','2023-02-10 20:14:16'),('fcf166a715e02f8a98c07f2cccf6132a648ced38d32913f1fa1d9fb35373af72','sample-img1.png','2023-02-10 20:14:16'),('f7ecb8cd0f5c755b0bef70a8e89ccc3f321eac36711bf8256a7e0ca0bffeac2c','sampleSubmission.csv','2023-02-10 20:14:16');
/*!40000 ALTER TABLE `file_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-17 22:49:41
