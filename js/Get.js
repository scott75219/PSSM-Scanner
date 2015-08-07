Scores=[];
function Get(){
	jQuery.ajax(
	    {
	        url:'get_INFO.php',
			type:'GET',
			success: function(response){
				var results=JSON.parse(response);
				var PSSM=results.PSSM;
				Scores=results.Confidence.split("\n");
				PSSM = PSSM.split(" ").join("\n");
				PSSM = PSSM.replace(/^\s+[\r\n]/gm,'');
				console.log(PSSM)
				var PSSM_matrix=[];
				var Graph_data=[];
				var weights=PSSM.split("\n");
				var motif_length=(weights.length-2)/4

	            for(var i = 0; i < motif_length; i++){ //parsing through pssm file and making a matrix to send tothe make logo function to draw it
	                    PSSM_matrix[i]=[{letter:"A",bits:weights[i]},{letter:"C",bits:weights[i+motif_length]},{letter:"G",bits:weights[i+motif_length*2]},{letter:"T",bits:weights[i+motif_length*3]}];
	            }
	            Make_Logo(PSSM_matrix);
	          //  drawMultSeries(Scores);          
	        }
         });
}
