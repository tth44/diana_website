$(function() {
	//hide the content. If user does not have JS, he can still see the content by default.
	function init(){
		
		$(".slider-content-hidden").hide();
		
	}
	
	$(".slider-content .toggle").click(function(){
		
		var hiddenContent = $(this).next(".slider-content-hidden");
		
		hiddenContent.slideToggle();
		
		
	});
	
	init();
	
});