-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 08, 2021 at 12:55 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cvms`
--

-- --------------------------------------------------------

--
-- Dumping data for table `covidvms_ug`
--

INSERT INTO `covidvms_ug` (`dist_id`, `name`) VALUES
(1, 'Abim'),
(2, 'Adjumani'),
(3, 'Agago'),
(4, 'Alebtong'),
(5, 'Amolatar'),
(6, 'Amudat'),
(7, 'Amuria'),
(8, 'Amuru'),
(9, 'Apac'),
(10, 'Arua'),
(11, 'Binyin'),
(12, 'Bombo'),
(13, 'Bududa'),
(14, 'Bugiri'),
(15, 'Buikwe'),
(16, 'Bukedea'),
(17, 'Bukomansimbi'),
(18, 'Bukwo'),
(19, 'Bulambuli'),
(20, 'Bulisa'),
(21, 'Bundibugyo'),
(22, 'Bupoto'),
(23, 'Busesa'),
(24, 'Bushenyi'),
(25, 'Busia'),
(26, 'Butalangu'),
(27, 'Butaleja'),
(28, 'Butebo'),
(29, 'Buyende'),
(30, 'city'),
(31, 'Dokolo'),
(32, 'Entebbe'),
(33, 'Fort Portal'),
(34, 'Gombe'),
(35, 'Gulu'),
(36, 'Hoima'),
(37, 'Ibanda'),
(38, 'Iganga'),
(39, 'Isingiro'),
(40, 'Jinja'),
(41, 'Kaabong'),
(42, 'Kabale'),
(43, 'Kaberamaido'),
(44, 'Kagadi'),
(45, 'Kakumiro'),
(46, 'Kalaki'),
(47, 'Kalangala'),
(48, 'Kaliro'),
(49, 'Kalungu'),
(50, 'Kampala'),
(51, 'Kamuli'),
(52, 'Kamwenge'),
(53, 'Kanoni'),
(54, 'Kanungu'),
(55, 'Kapchorwa'),
(56, 'Kasaali'),
(57, 'Kasanda'),
(58, 'Kasese'),
(59, 'Katakwi'),
(60, 'Kayunga'),
(61, 'Kibiito'),
(62, 'Kibingo'),
(63, 'Kiboga'),
(64, 'Kibuku'),
(65, 'Kinoni'),
(66, 'Kiruhura'),
(67, 'Kiryandongo'),
(68, 'Kisoro'),
(69, 'Kitamilo'),
(70, 'Kitgum'),
(71, 'Koboko'),
(72, 'Kole'),
(73, 'Kotido'),
(74, 'Kumi'),
(75, 'Kyankwanzi'),
(76, 'Kyegegwa'),
(77, 'Kyenjojo'),
(78, 'Lamwo'),
(79, 'Lira'),
(80, 'Luuka Town'),
(81, 'Luwero'),
(82, 'Lwengo'),
(83, 'Lyantonde'),
(84, 'Manafwa'),
(85, 'Maracha'),
(86, 'Masaka'),
(87, 'Masindi'),
(88, 'Mayuge'),
(89, 'Mbale'),
(90, 'Mbarara'),
(91, 'Mitoma'),
(92, 'Mityana'),
(93, 'Moroto'),
(94, 'Moyo'),
(95, 'Mparo'),
(96, 'Mpigi'),
(97, 'Mubende'),
(98, 'Mukono'),
(99, 'Nabilatuk'),
(100, 'Nakapiripirit'),
(101, 'Nakasongola'),
(102, 'Namayingo'),
(103, 'Namutumba'),
(104, 'Napak'),
(105, 'Nebbi'),
(106, 'Ngora'),
(107, 'Nsiika'),
(108, 'Ntara'),
(109, 'Ntoroko'),
(110, 'Ntungamo'),
(111, 'Nwoya'),
(112, 'Otuke'),
(113, 'Oyam'),
(114, 'Pader'),
(115, 'Pakwach'),
(116, 'Palenga'),
(117, 'Pallisa'),
(118, 'Rakai'),
(119, 'Rubanda'),
(120, 'Rubirizi'),
(121, 'Rukungiri'),
(122, 'Sembabule'),
(123, 'Serere'),
(124, 'Sironko'),
(125, 'Soroti'),
(126, 'Tororo'),
(127, 'Wakiso'),
(128, 'Yumbe'),
(129, 'Zombo');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `covidvms_ug`
--
ALTER TABLE `covidvms_ug`
  ADD PRIMARY KEY (`dist_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `covidvms_ug`
--
ALTER TABLE `covidvms_ug`
  MODIFY `dist_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=130;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
