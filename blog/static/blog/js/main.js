$(document).ready(function(){
  var owl = $('#owl-1');
  var owl2 = $('#owl-2');

  //Init first Slider Carousel
  owl.owlCarousel({
    loop: true,
    dots: false,
    nav: true,
		itemClass: 'owl-item',
    responsiveClass:true,
    responsive:{
        0:{
            items:2,
        },
        600:{
            items:3,
        },
        1200:{
            items:4,
        }
    }
  });


$().fancybox({
  selector : '.owl-item:not(.cloned) a', //a Reference to <a></a>
  hash   : false,
  thumbs : {
    autoStart : true
  }
});

  //Init second Slider Carousel
  owl2.owlCarousel({
    loop: true,
    dots: false,
    nav: true,
		itemClass: 'owl-item2',
    responsiveClass:true,
    responsive:{
        0:{
            items:1,
        },
        600:{
            items:3,
        },
        1200:{
            items:4,
        }
    }
  });

$().fancybox({
  selector : '.owl-item2:not(.cloned) a', //a Reference to <a></a>
  hash   : false,
  thumbs : {
    autoStart : true
  }
});


});
