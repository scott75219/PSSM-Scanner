<?php
ini_set('set_time_limit', 3000);

$PSSM_out=file_get_contents("uploads/PSSM2.txt");
$Confidence_out=file_get_contents("uploads/logp.txt");
$post_data = json_encode(array('PSSM' => $PSSM_out, 'Confidence'=>$Confidence_out), JSON_FORCE_OBJECT);
echo $post_data;
#unlink("uploads/PSSMFile.txt")
#unlink("uploads/MotifFile.txt")
#unlink("uploads/BackgroundFile.txt")
#unlink("uploads/PSSM2.txt")

?>