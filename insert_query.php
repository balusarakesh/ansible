<?php

ini_set('display_errors', 1);

ini_set('display_startup_errors', 1);

error_reporting(E_ALL);

$email= $_GET["email"];
$name = $_GET["name"];
$profession = $_GET["profession"];
$dbconn3 = pg_connect("host=hostname port=5432 dbname=dbname user=username password=password");
#$result = pg_query($conn, "create table people (email varchar(100), name varchar(100), profession varchar(100))");
$result = pg_query($dbconn3, "insert into people values( '$email', '$name', '$profession')");
echo $result;

exit;

?>

