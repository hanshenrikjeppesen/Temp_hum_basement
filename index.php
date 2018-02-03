<!DOCTYPE html>
<html>
<head>
	<title>RaspberryPi - Basement monitoring</title>
</head>
<body>
	<h1>Project: Monitoring data in my home basement</h1>
	<?php
		$myfile =  fopen("/home/hans/temp_log_file.txt", "r") or die("can't finde the file on server");
		while(! feof($myfile))
  			{
  			echo fgets($myfile). "<br />";
  			}
		/* echo fread($myfile,filesize("/home/hans/temp_log_file.txt")); */
		fclose($myfile);
		?>
