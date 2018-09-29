<html>
	<head>
		<title>
			Welcome to INFSCI 2710
		</title>
	</head>
	<body>
		Hello, world!
		<?php
			$servername = "localhost";
			$username = "root";
			$password = "mysql";

			// Create connection
			$conn = new mysqli($servername, $username, $password);

			// Check connection
			if ($conn->connect_error) {
			    die("Connection failed: " . $conn->connect_error);
			} 
			echo "<p><font color=\"red\">Connected successfully</font></p>";

			// Run a sql
			$sql = "show databases;";
			$result = $conn->query($sql);
			while($row = $result->fetch_assoc()) {
				echo $row["Database"]."<br/>";
			}
			$result->free();

			// Close connection
			mysqli_close($conn);
		?>
	</body>
</html>
