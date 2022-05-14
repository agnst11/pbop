-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 14, 2022 at 01:40 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sewa`
--

-- --------------------------------------------------------

--
-- Table structure for table `data_sewa`
--

CREATE TABLE `data_sewa` (
  `idSewa` int(3) NOT NULL,
  `nik` varchar(10) NOT NULL,
  `nama` varchar(25) NOT NULL,
  `noHp` varchar(15) NOT NULL,
  `idSepeda` varchar(5) NOT NULL,
  `harga` int(6) NOT NULL,
  `durasi` int(1) NOT NULL,
  `waktuSewa` datetime NOT NULL,
  `waktuKembali` datetime DEFAULT NULL,
  `tagihan` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `data_sewa`
--

INSERT INTO `data_sewa` (`idSewa`, `nik`, `nama`, `noHp`, `idSepeda`, `harga`, `durasi`, `waktuSewa`, `waktuKembali`, `tagihan`) VALUES
(4, '234567', 'Esa', '21424124', 'ab123', 12000, 1, '2022-05-14 18:03:05', '2022-05-14 18:34:50', 12000),
(5, '234567', 'Esa', '2312412123', 'ab234', 9000, 1, '2022-05-14 18:08:45', '2022-05-14 18:37:25', 9000);

-- --------------------------------------------------------

--
-- Table structure for table `sepeda`
--

CREATE TABLE `sepeda` (
  `id` varchar(5) NOT NULL,
  `warna` varchar(10) NOT NULL,
  `harga` int(6) NOT NULL,
  `status` enum('tersedia','disewa','rusak') NOT NULL DEFAULT 'tersedia'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sepeda`
--

INSERT INTO `sepeda` (`id`, `warna`, `harga`, `status`) VALUES
('123as', 'biru', 10000, 'tersedia'),
('ab123', 'hitam', 12000, 'tersedia'),
('ab234', 'hijau', 9000, 'tersedia'),
('bc123', 'merah', 15000, 'rusak');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data_sewa`
--
ALTER TABLE `data_sewa`
  ADD PRIMARY KEY (`idSewa`);

--
-- Indexes for table `sepeda`
--
ALTER TABLE `sepeda`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `data_sewa`
--
ALTER TABLE `data_sewa`
  MODIFY `idSewa` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
