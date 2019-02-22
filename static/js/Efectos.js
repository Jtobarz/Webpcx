 jQuery(document).ready(function( $ ) 
 {

  /*INICIAR WOW*/
    wow = new WOW( {
        animateClass: 'animated',
        offset:       100
    });
    wow.init();
  /*INICIAR WOW*/
  
  /*ROTADOR TEXTO*/
  	$(" .rotador").Morphext(
  	{
   	 animation: "flipInX",
   	 separator: ",",
  	 speed: 4000
  	});
  /*ROTADOR TEXTO*/

  /*MODAL*/
   $(window).load(function(){        
   $('#myModal').modal('show');
    }); 
  /*MODAL*/

  /*NAVBAR*/
    $(window).scroll(function() {
        if ($(".navbar-default").offset().top > 50) {
            $(".navbar-fixed-top").addClass("top-nav-collapse");
        } else {
            $(".navbar-fixed-top").removeClass("top-nav-collapse");
        }
    });
  /*NAVBAR*/

  /*VELOCIDAD SLIDER*/
     $('.carousel').carousel(
    {
        interval: 3000
    }
    )
  /*VELOCIDAD SLIDER*/

 });

