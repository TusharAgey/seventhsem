-- phpMyAdmin SQL Dump
-- version 4.6.6
-- https://www.phpmyadmin.net/

CREATE TABLE `word_count` (
  `time_it` varchar(25) NOT NULL COMMENT 'To milestone the data',
  `file_name` varchar(100) NOT NULL COMMENT 'name of the file processed',
  `unique_word` varchar(200) NOT NULL COMMENT 'the unique word',
  `count_it` int(3) NOT NULL COMMENT 'count of occurance'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `word_count`
  ADD PRIMARY KEY (`time_it`,`file_name`,`unique_word`,`count_it`);

