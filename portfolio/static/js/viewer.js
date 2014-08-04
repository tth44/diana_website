$(function(){
		
	function init(){
		
		$(".viewer-nav ul li").first().addClass("selected");
		$(".viewer-panels div").first().removeClass("viewer-panel").addClass("viewer-panel-active");
	}
	
	init()
	$(".viewer-nav ul li").mouseenter(function(e){
		var listMini = $(".viewer-nav ul li");
		var listBig = $(".viewer-panels div");
		var test = $(this).hasClass("selected");
		if (!($(this).hasClass("selected"))){
			
			//if selection, remove it
			var previousMini = $(".selected");
			if(previousMini.length > 0){
				previousMini.removeClass("selected");
				
			}
			$(this).addClass("selected");
			
			var previousBig = $(".viewer-panel-active");
			if(previousBig.length > 0){
				previousBig.removeClass("viewer-panel-active").addClass("viewer-panel");
			}
			
			
			
			//Show the new picture
			// -1 because index count from 1
			var index = $(this).index();
			var bigPic = listBig.eq(index);
			 bigPic.removeClass("viewer-panel").addClass("viewer-panel-active");
		}
	});



});