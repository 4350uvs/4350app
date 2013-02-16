$(document).ready(function(){
	$('#fadeframe').fadeIn(500);
});

$(".sessEven, .sessOdd").hover(function() {
	$(this).stop().delay(100).animate({
		'background-position' : '99%'
	}, 400);
},function() {
	$(this).stop().delay(100).animate({
		'background-position' : '97%'
	}, 400);
});

$(".sessEven, .sessOdd").click(function(){
	$('.container-fluid').animate({'width' : '0%'}, 400);
}).click(function(){
	$(".sessEven, .sessOdd").find('hover').unbind('mouseenter');
}).click(function(){
	$('.sessEven:hover, .sessOdd:hover').css('background-image', 'none');
	$(".sessEven, .sessOdd").find('.sessInfo').css("display", "none");
});