// back to top button
		// create the back to top button
		$('body').prepend('<a href="#" class="back-to-top"></a>');

		var amountScrolled = 300;

		$(window).scroll(function() {
			if ( $(window).scrollTop() > amountScrolled ) {
				$('a.back-to-top').fadeIn('slow');
			} else {
				$('a.back-to-top').fadeOut('slow');
			}
		});

		$('a.back-to-top, a.simple-back-to-top').click(function() {
			$('html, body').animate({
				scrollTop: 0
			}, 700);
			return false;
		});

$('.carousel').carousel({
touch: true, // default
})
$('.toast').toast('show');


$(function () {
    'use strict';
    $(".up").on("click", function () {
			console.log($(this).siblings());
        var q = parseInt($($(this).siblings()[2]).val());

        q++
        $($(this).siblings()[2]).val(q);

    });

    $(".down").on("click", function () {
			console.log($(this).siblings());
        var q = parseInt($($(this).siblings()[3]).val());
        if (q > 1) {
            q--
            $($(this).siblings()[3]).val(q);
        }else {
            q = 1;
        }

    });
})
