$(document).ready(function(){
	
	$("#H1").click(function(){
		
		$(function(){
			$.ajax({
				url: "localhost:9000/Hello",
				type: "POST",
				dataType: "text",
				success: function(data){
					console.log(data);
				}
			});
		});
	});
	
});