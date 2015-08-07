<?php
$target_dir = "uploads/";

$length=$_POST["length"];
$end=$_POST["search"];
$motif=$target_dir ."MotifFile.fasta";
$background= $target_dir ."BackgroundFile.fasta";
move_uploaded_file($_FILES["fileToUploadPSSM"]["tmp_name"],$target_dir."PSSMFile.txt");
move_uploaded_file($_FILES["fileToUploadMotif"]["tmp_name"],$target_dir."MotifFile.fasta"); 
move_uploaded_file($_FILES["fileToUploadBackground"]["tmp_name"],$target_dir."BackgroundFile.fasta"); 
shell_exec("python Sig_calc2.py uploads/MotifFile.fasta uploads/BackgroundFile.fasta uploads/PSSMFile.txt ".$length." ".$end);
#while (!file_exists("uploads/logp.txt")) sleep(1);
header("Location: Results.html"); /* Redirect browser */
exit();
?>