$(document).ready(function () {
  var owlold = $('#owl-1');
  var owl2 = $('#owl-2');
  var i;
  var owl = '#owl-';
  var itemname = 'owl-item';
  for (i = 1; i < 10; i++) {


    //Init first Slider Carousel
    $('#owl-' + i).owlCarousel({
      loop: true,
      dots: false,
      nav: true,
      navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>   ',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>   '
      ],
      itemClass: 'owl-item' + i,
      responsiveClass: true,
      responsive: {
        0: {
          items: 2,
        },
        600: {
          items: 3,
        },
        1200: {
          items: 4,
        }
      }
    });

    $().fancybox({
      selector: '.owl-item' + i + ':not(.cloned) a', //a Reference to <a></a>
      hash: false,
      thumbs: {
        autoStart: true
      }
    });

  }

});
