<?php

$host="localhost";

$username="b1908333";

$password="b1908333";

$db_name="test";

$tbl_name="user";

$conn = mysqli_connect($host, $username, $password)or die("cannot connect");

mysqli_select_db($conn, $db_name)or die("cannot select DB");

$username=$_POST['username'];

$password=$_POST['password'];

#$username = stripslashes($username);

#$password = stripslashes($password);

#$username = mysql_real_escape_string($username);

#$password = mysql_real_escape_string($password);

$sql="select * from $tbl_name where username='$username' AND password='$password'";

$result=mysqli_query($conn,$sql);

$count=mysqli_num_rows($result);

if ($count == 0)
{
echo "Invalid Username Or Password!";
}

else 
{
echo "Login Sucessfully!";
}

?>

