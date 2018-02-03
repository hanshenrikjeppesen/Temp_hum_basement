<!DOCTYPE html>
<html>
<head>
	<title>RaspberryPi - Basement monitoring</title>
<style>
	body {background-color: powderblue;}
	h1   {
		
		text-align: center;
		color: blue;
		font-family: 'Ubuntu', sans-serif;
		font-size: 250%;
	}
	p    {color: red;}
	<link href="https://fonts.googleapis.com/css?family=Ubuntu" rel="stylesheet">
</style>
</head>
<body>
	<h1>Project: Monitoring data in my home basement</h1>
	<?php
		$myfile =  fopen("/home/hans/temp_log_file.txt", "r") or die("can't finde the file on server");
		while(! feof($myfile))
  			{
  			echo fgets($myfile). "<br />";
			echo "<hr/ >";
  			}
		/* echo fread($myfile,filesize("/home/hans/temp_log_file.txt")); */
		fclose($myfile);
		?>
