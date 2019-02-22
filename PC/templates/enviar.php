<?php

	// definimos el mensaje
	$mensaje="";
	$mensaje.="Contactado por: ". "\n\n";
	$mensaje.="Nombre: ".$_POST['nombre']."\n";
	$mensaje.="Email: ".$_POST['email']."\n";
	$mensaje.="Telefono: ".$_POST['telefono']."\n";
	$mensaje.="Mensaje: ".$_POST['mensaje']."\n";
	// definimos a quien se lo enviamos
	$email_destiny="info@webpcx.cl";
	$subject="Mensaje de: ";


	header("Location:Gracias.html")
?>