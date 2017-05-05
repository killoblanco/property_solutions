<?php

// Define some constants
define( "RECIPIENT_NAME", "John Doe" );
define( "RECIPIENT_EMAIL", "mail@mail.com" );

// Read the form values
$success = false;
$senderName = isset( $_POST['name'] ) ? preg_replace( "/[^\.\-\' a-zA-Z0-9]/", "", $_POST['name'] ) : "";
$senderEmail = isset( $_POST['email'] ) ? preg_replace( "/[^\.\-\_\@a-zA-Z0-9]/", "", $_POST['email'] ) : "";
$phone = isset( $_POST['phone'] ) ? preg_replace( "/[^\.\-\' a-zA-Z0-9]/", "", $_POST['phone'] ) : "";
$city = isset( $_POST['city'] ) ? preg_replace( "/[^\.\-\' a-zA-Z0-9]/", "", $_POST['city'] ) : "";



// If all values exist, send the email
if ( $senderName && $senderEmail && $phone && $city ) {
	$recipient = RECIPIENT_NAME . " <" . RECIPIENT_EMAIL . ">";
	$headers = "From: " . $senderName . " <" . $senderEmail . ">";
	// fromating message body 
	$message =   'Sender Name: '. $senderName . '\r\n'
			   . 'Sender Email: '. $senderEmail . '\r\n'
			   . 'Sender Phone: '. $phone . '\r\n'
			   . 'Sender City: '. $city;
	$success = mail( $recipient, $subject, $message, $headers );
	echo "<p class='success'>Thanks for contacting us. We will contact you ASAP!</p>";
}

?>