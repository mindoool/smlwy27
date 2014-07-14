$(document).ready(function(){
	
	$('#myModal').modal('hide');

	$('#TV').hide();
	$('#minseok').click(function(){
		$('#minseok').hide();
	})

	$('#hobby').click(function(){
		$('#TV').toggle();
	});
	$('.dropdown-toggle').dropdown();
	$('.popover-dismiss').popover({
		trigger: 'focus'
	});
	$('body').scrollspy({target:'.navbar-collapse'});
	$('#me').hover(function(){
		$('#me').css("color","red")
	},function(){
		$('#me').css("color","black");
	});
})