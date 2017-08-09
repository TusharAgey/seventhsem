-- phpMyAdmin SQL Dump
-- version 4.6.6
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 09, 2017 at 01:16 AM
-- Server version: 5.7.17
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE TABLE `word_count` (
  `time_it` varchar(25) NOT NULL COMMENT 'To milestone the data',
  `file_name` varchar(100) NOT NULL COMMENT 'name of the file processed',
  `unique_word` varchar(200) NOT NULL COMMENT 'the unique word',
  `count_it` int(3) NOT NULL COMMENT 'count of occurance'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `word_count`
--

--
-- Indexes for dumped tables
--

--
-- Indexes for table `word_count`
--
ALTER TABLE `word_count`
  ADD PRIMARY KEY (`time_it`,`file_name`,`unique_word`,`count_it`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
