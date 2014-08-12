$(function(){
	
	var timeoutShow
	var timeoutHide
	$(".sum-portfolio a").hover(function(){
		var caption = $(this).find(".sum-portfolio-caption");
		
		//remove time out if necessary
		if (timeoutHide != undefined || timeoutHide != null){
			clearTimeout(timeoutHide)
		}
		
		timeoutShow = setTimeout(function(){
			
			caption.stop(true,true).show("slide", {direction: "down" ,easing:"linear"}, "fast" );
			
		}, 1000);
	}, function(){
		var caption = $(this).find(".sum-portfolio-caption");
		
		if (timeoutShow != undefined || timeoutShow != null){
			clearTimeout(timeoutShow)
		}
		timeoutHide = setTimeout(function(){
			
			
			caption.stop(true,true).hide("slide", {direction: "down" ,easing:"linear"}, "fast");
			
		}, 1000);
	
		
		
	});
	
	
	
});