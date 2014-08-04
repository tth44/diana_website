$(function() {

	$("nav >ul >li").hover(function(e){
		
			//target the sub menu and do the animation
			var $subs = $(this).children(".sub-menu");
				if($subs.length == 1){
				
					var sub = $subs.first();
					sub.stop( true, true).slideDown("fast");
				}	
	
	}, function(e) {
			//target the sub menu and do the animation
           var $subs = $(this).children(".sub-menu");
			if($subs.length == 1){
				var sub = $subs.first();
				//only one "true" to avoid flickering
				sub.stop( true).slideUp("fast");
			}
		}
	);
	

});