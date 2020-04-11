$(document).ready(function () {
  var owl = $('#owl-1');
  var owl2 = $('#owl-2');
  var owl3 = $('#owl-3');
  var owl4 = $('#owl-4');
  var owl5 = $('#owl-5');

  //Init first Slider Carousel
  owl.owlCarousel({
    loop: true,
    dots: false,
    nav: true,
    itemClass: 'owl-item',
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
    selector: '.owl-item:not(.cloned) a', //a Reference to <a></a>
    hash: false,
    thumbs: {
      autoStart: true
    }
  });

  //Init second Slider Carousel
  owl2.owlCarousel({
    loop: true,
    dots: false,
    nav: true,
    itemClass: 'owl-item2',
    responsiveClass: true,
    responsive: {
      0: {
        items: 1,
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
    selector: '.owl-item2:not(.cloned) a', //a Reference to <a></a>
    hash: false,
    thumbs: {
      autoStart: true
    }
  });

  //Init third Slider Carousel
  owl3.owlCarousel({
    loop: true,
    dots: false,
    nav: true,
    itemClass: 'owl-item3',
    responsiveClass: true,
    responsive: {
      0: {
        items: 1,
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
    selector: '.owl-item3:not(.cloned) a', //a Reference to <a></a>
    hash: false,
    thumbs: {
      autoStart: true
    }
  });
  //Init fourth Slider Carousel
  owl4.owlCarousel({
    loop: true,
    dots: false,
    nav: true,
    itemClass: 'owl-item4',
    responsiveClass: true,
    responsive: {
      0: {
        items: 1,
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
    selector: '.owl-item4:not(.cloned) a', //a Reference to <a></a>
    hash: false,
    thumbs: {
      autoStart: true
    }
  });
  //Init fivth Slider Carousel
  owl5.owlCarousel({
    loop: true,
    dots: false,
    nav: true,
    itemClass: 'owl-item5',
    responsiveClass: true,
    responsive: {
      0: {
        items: 1,
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
    selector: '.owl-item5:not(.cloned) a', //a Reference to <a></a>
    hash: false,
    thumbs: {
      autoStart: true
    }
  });

});
