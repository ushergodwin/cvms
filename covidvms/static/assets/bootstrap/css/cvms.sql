-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 06, 2021 at 06:29 PM
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
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add auth', 1, 'add_auth'),
(2, 'Can change auth', 1, 'change_auth'),
(3, 'Can delete auth', 1, 'delete_auth'),
(4, 'Can view auth', 1, 'view_auth'),
(5, 'Can add log entry', 2, 'add_logentry'),
(6, 'Can change log entry', 2, 'change_logentry'),
(7, 'Can delete log entry', 2, 'delete_logentry'),
(8, 'Can view log entry', 2, 'view_logentry'),
(9, 'Can add permission', 3, 'add_permission'),
(10, 'Can change permission', 3, 'change_permission'),
(11, 'Can delete permission', 3, 'delete_permission'),
(12, 'Can view permission', 3, 'view_permission'),
(13, 'Can add group', 4, 'add_group'),
(14, 'Can change group', 4, 'change_group'),
(15, 'Can delete group', 4, 'delete_group'),
(16, 'Can view group', 4, 'view_group'),
(17, 'Can add user', 5, 'add_user'),
(18, 'Can change user', 5, 'change_user'),
(19, 'Can delete user', 5, 'delete_user'),
(20, 'Can view user', 5, 'view_user'),
(21, 'Can add content type', 6, 'add_contenttype'),
(22, 'Can change content type', 6, 'change_contenttype'),
(23, 'Can delete content type', 6, 'delete_contenttype'),
(24, 'Can view content type', 6, 'view_contenttype'),
(25, 'Can add session', 7, 'add_session'),
(26, 'Can change session', 7, 'change_session'),
(27, 'Can delete session', 7, 'delete_session'),
(28, 'Can view session', 7, 'view_session'),
(29, 'Can add citizen model', 8, 'add_citizenmodel'),
(30, 'Can change citizen model', 8, 'change_citizenmodel'),
(31, 'Can delete citizen model', 8, 'delete_citizenmodel'),
(32, 'Can view citizen model', 8, 'view_citizenmodel'),
(33, 'Can add feed back', 9, 'add_feedback'),
(34, 'Can change feed back', 9, 'change_feedback'),
(35, 'Can delete feed back', 9, 'delete_feedback'),
(36, 'Can view feed back', 9, 'view_feedback'),
(37, 'Can add user model', 10, 'add_usermodel'),
(38, 'Can change user model', 10, 'change_usermodel'),
(39, 'Can delete user model', 10, 'delete_usermodel'),
(40, 'Can view user model', 10, 'view_usermodel');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$216000$wVJerV1yJHPW$WItEFSSg9CVXBN5pjd54CoEEBOo9LLuu/tVmY+MQdBI=', NULL, 1, 'david', '', '', 'ojokdavid68@gmail.com', 1, 1, '2021-03-15 11:21:26.721450');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `citizen`
--

CREATE TABLE `citizen` (
  `nin_number` varchar(15) NOT NULL,
  `sur_name` varchar(30) NOT NULL,
  `given_name` varchar(45) NOT NULL,
  `nationality` varchar(15) NOT NULL,
  `gender` enum('M','F') NOT NULL,
  `date_of_birth` date NOT NULL,
  `card_no` int(11) NOT NULL,
  `expiry_date` date NOT NULL,
  `village` varchar(100) NOT NULL,
  `parish` varchar(100) NOT NULL,
  `sub_county` varchar(100) NOT NULL,
  `county` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `phone_number` varchar(14) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `citizen`
--

INSERT INTO `citizen` (`nin_number`, `sur_name`, `given_name`, `nationality`, `gender`, `date_of_birth`, `card_no`, `expiry_date`, `village`, `parish`, `sub_county`, `county`, `district`, `phone_number`, `email`) VALUES
('CM96061102UEPA', 'TUMUHIMBISE', 'GODWIN', 'UGA', 'M', '1997-12-06', 14617215, '2025-07-31', 'MISHOZI II', 'KAKATSI', 'BISHESHE', 'BISHESHE', 'IBANDA', '+256754438448', 'godwintumuhimbise96@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `covidvms_auth`
--

CREATE TABLE `covidvms_auth` (
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `covidvms_covid19vaccines`
--

CREATE TABLE `covidvms_covid19vaccines` (
  `vaccine_id` varchar(8) NOT NULL,
  `name` varchar(100) NOT NULL,
  `dozes` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `covid_19_vaccination`
--

CREATE TABLE `covid_19_vaccination` (
  `vaccination_id` int(11) NOT NULL,
  `citizen_nin` varchar(15) NOT NULL,
  `no_of_dozes` int(1) NOT NULL DEFAULT 0,
  `vaccine_type` int(11) DEFAULT NULL,
  `taken_at` datetime DEFAULT NULL,
  `next_doze_on` datetime DEFAULT NULL,
  `doze_status` enum('PARTIAL','COMPLETE') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `covid_19_vaccination`
--

INSERT INTO `covid_19_vaccination` (`vaccination_id`, `citizen_nin`, `no_of_dozes`, `vaccine_type`, `taken_at`, `next_doze_on`, `doze_status`) VALUES
(45859536, 'CM96061102UEPA', 0, NULL, NULL, NULL, 'PARTIAL');

-- --------------------------------------------------------

--
-- Table structure for table `covid_19_vaccines`
--

CREATE TABLE `covid_19_vaccines` (
  `vaccine_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `dozes` int(1) NOT NULL DEFAULT 2
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `covid_19_vaccines`
--

INSERT INTO `covid_19_vaccines` (`vaccine_id`, `name`, `dozes`) VALUES
(54815, 'Oxford–AstraZeneca', 2),
(247896, 'Pfizer-BioNTech', 2),
(578954, 'Moderna', 2),
(796482, 'Johnson & Johnson', 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(2, 'admin', 'logentry'),
(4, 'auth', 'group'),
(3, 'auth', 'permission'),
(5, 'auth', 'user'),
(6, 'contenttypes', 'contenttype'),
(1, 'covidvms', 'auth'),
(8, 'covidvms', 'citizenmodel'),
(9, 'covidvms', 'feedback'),
(10, 'covidvms', 'usermodel'),
(7, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-03-15 11:05:39.017186'),
(2, 'auth', '0001_initial', '2021-03-15 11:05:40.477139'),
(3, 'admin', '0001_initial', '2021-03-15 11:05:47.096751'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-03-15 11:05:48.911850'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-03-15 11:05:48.943093'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-03-15 11:05:49.536959'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-03-15 11:05:50.334180'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-03-15 11:05:50.428165'),
(9, 'auth', '0004_alter_user_username_opts', '2021-03-15 11:05:50.459407'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-03-15 11:05:51.078345'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-03-15 11:05:51.109555'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-03-15 11:05:51.140830'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-03-15 11:05:51.281390'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-03-15 11:05:52.033517'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-03-15 11:05:52.283426'),
(16, 'auth', '0011_update_proxy_permissions', '2021-03-15 11:05:52.330450'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-03-15 11:05:52.548988'),
(18, 'covidvms', '0001_initial', '2021-03-15 11:05:52.800480'),
(19, 'sessions', '0001_initial', '2021-03-15 11:05:53.003561');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('g1ep74jeprv33b91jcwof6v961lpk9sx', 'e30:1m0li3:njrE6dvBzL0ngEc1tgYhKywayZO8YDYF-K33Uduj6U8', '2021-07-20 14:05:59.368372');

-- --------------------------------------------------------

--
-- Table structure for table `ug`
--

CREATE TABLE `ug` (
  `name` varchar(13) NOT NULL,
  `population` varchar(10) DEFAULT NULL,
  `population_per_srqt` varchar(17) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `ug`
--

INSERT INTO `ug` (`name`, `population`, `population_per_srqt`) VALUES
('Abim', '', ''),
('Adjumani', '34700', '34700'),
('Agago', '', ''),
('Alebtong', '', ''),
('Amolatar', '', ''),
('Amudat', '', ''),
('Amuria', '', ''),
('Amuru', '', ''),
('Apac', '', ''),
('Arua', '250000', '59400'),
('Binyin', '', ''),
('Bombo', '75000', '21000'),
('Bududa', '', ''),
('Bugiri', '', ''),
('Buikwe', '', ''),
('Bukedea', '', ''),
('Bukomansimbi', '', ''),
('Bukwo', '', ''),
('Bulambuli', '', ''),
('Bulisa', '', ''),
('Bundibugyo', '', ''),
('Bupoto', '', ''),
('Busesa', '', ''),
('Bushenyi', '', ''),
('Busia', '47100', '47100'),
('Butalangu', '', ''),
('Butaleja', '', ''),
('Butebo', '', ''),
('Buyende', '', ''),
('city', 'population', 'population_proper'),
('Dokolo', '', ''),
('Entebbe', '69958', '69958'),
('Fort Portal', '42670', '42670'),
('Gombe', '', ''),
('Gulu', '146858', '142003'),
('Hoima', '', ''),
('Ibanda', '', ''),
('Iganga', '45024', '45024'),
('Isingiro', '', ''),
('Jinja', '72931', '72931'),
('Kaabong', '1137', '1137'),
('Kabale', '44600', '44600'),
('Kaberamaido', '3400', '3400'),
('Kagadi', '', ''),
('Kakumiro', '', ''),
('Kalaki', '', ''),
('Kalangala', '5200', '5200'),
('Kaliro', '', ''),
('Kalungu', '', ''),
('Kampala', '1659600', '1659600'),
('Kamuli', '12764', '12764'),
('Kamwenge', '', ''),
('Kanoni', '', ''),
('Kanungu', '', ''),
('Kapchorwa', '', ''),
('Kasaali', '', ''),
('Kasanda', '', ''),
('Kasese', '67269', '67269'),
('Katakwi', '8400', '8400'),
('Kayunga', '21704', '21704'),
('Kibiito', '', ''),
('Kibingo', '', ''),
('Kiboga', '14512', '14512'),
('Kibuku', '', ''),
('Kinoni', '', ''),
('Kiruhura', '', ''),
('Kiryandongo', '', ''),
('Kisoro', '12900', '12900'),
('Kitamilo', '', ''),
('Kitgum', '56891', '8680'),
('Koboko', '', ''),
('Kole', '', ''),
('Kotido', '', ''),
('Kumi', '13000', '13000'),
('Kyankwanzi', '', ''),
('Kyegegwa', '', ''),
('Kyenjojo', '', ''),
('Lamwo', '', ''),
('Lira', '135445', '119323'),
('Luuka Town', '', ''),
('Luwero', '', ''),
('Lwengo', '', ''),
('Lyantonde', '', ''),
('Manafwa', '', ''),
('Maracha', '', ''),
('Masaka', '65373', '65373'),
('Masindi', '31486', '31486'),
('Mayuge', '', ''),
('Mbale', '402368', '91800'),
('Mbarara', '83700', '83700'),
('Mitoma', '', ''),
('Mityana', '41131', '33710'),
('Moroto', '371', '371'),
('Moyo', '22434', '22434'),
('Mparo', '', ''),
('Mpigi', '11082', '11082'),
('Mubende', '18936', '176'),
('Mukono', '', ''),
('Nabilatuk', '', ''),
('Nakapiripirit', '', ''),
('Nakasongola', '6921', '6921'),
('Namayingo', '', ''),
('Namutumba', '', ''),
('Napak', '', ''),
('Nebbi', '30354', '30354'),
('Ngora', '', ''),
('Nsiika', '', ''),
('Ntara', '', ''),
('Ntoroko', '', ''),
('Ntungamo', '16400', '16400'),
('Nwoya', '', ''),
('Otuke', '', ''),
('Oyam', '', ''),
('Pader', '', ''),
('Pakwach', '17541', '17541'),
('Palenga', '', ''),
('Pallisa', '30745', '30745'),
('Rakai', '', ''),
('Rubanda', '', ''),
('Rubirizi', '', ''),
('Rukungiri', '', ''),
('Sembabule', '', ''),
('Serere', '', ''),
('Sironko', '14100', '14100'),
('Soroti', '1038', '1038'),
('Tororo', '150000', '43700'),
('Wakiso', '', ''),
('Yumbe', '', ''),
('Zombo', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `email` varchar(65) NOT NULL,
  `names` varchar(65) NOT NULL,
  `password` varchar(255) NOT NULL,
  `img_url` varchar(255) DEFAULT NULL,
  `account_type` int(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`email`, `names`, `password`, `img_url`, `account_type`) VALUES
('godwintumuhimbise96@gmail.com', 'tumuhimbise godwin', 'pbkdf2_sha256$216000$lsG72RJBXAR1$gpkCms3npKSfWJFFdYIrifmbgv9n5AEBVajtpeiJnNU=', NULL, 0),
('ojokdavid68@gmail.com', 'Ojok David', 'pbkdf2_sha256$216000$rVtX0IpWoJrc$qy/86j/XcOMY4o4ulK9IHktZUMdNFjhuE3KKFINLJec=', NULL, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `citizen`
--
ALTER TABLE `citizen`
  ADD PRIMARY KEY (`nin_number`);

--
-- Indexes for table `covidvms_auth`
--
ALTER TABLE `covidvms_auth`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `covidvms_covid19vaccines`
--
ALTER TABLE `covidvms_covid19vaccines`
  ADD PRIMARY KEY (`vaccine_id`);

--
-- Indexes for table `covid_19_vaccination`
--
ALTER TABLE `covid_19_vaccination`
  ADD PRIMARY KEY (`vaccination_id`),
  ADD KEY `citizen_nin` (`citizen_nin`),
  ADD KEY `vaccine_type` (`vaccine_type`);

--
-- Indexes for table `covid_19_vaccines`
--
ALTER TABLE `covid_19_vaccines`
  ADD PRIMARY KEY (`vaccine_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `ug`
--
ALTER TABLE `ug`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `covidvms_auth`
--
ALTER TABLE `covidvms_auth`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `covid_19_vaccination`
--
ALTER TABLE `covid_19_vaccination`
  ADD CONSTRAINT `covid_19_vaccination_ibfk_1` FOREIGN KEY (`citizen_nin`) REFERENCES `citizen` (`nin_number`),
  ADD CONSTRAINT `covid_19_vaccination_ibfk_2` FOREIGN KEY (`vaccine_type`) REFERENCES `covid_19_vaccines` (`vaccine_id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
