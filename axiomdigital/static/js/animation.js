$(document).ready(function () {
    resizeDiv();
    navbarController();
    main(loadPage(type));
    responsiveNav();
});

$(window).resize(function () {
    resizeDiv();
});

function resizeDiv() {
    vph = $(window).height();
    if (vph > 500) {
        $(".auto-resize").css({"height": vph + "px"});

    }
}

function displaySuccess(callback) {
    setTimeout(function () {
        $('.success-text').css('visibility', 'visible').hide().fadeIn('slow', callback);
    }, 500);
}

function displayButton() {
    setTimeout(function () {
        $('.main-btn').css('visibility', 'visible').hide().fadeIn(function () {
            $(this).addClass('main-btn-transition');
        });
    }, 1000);
}

function main(callback) {
    setTimeout(function () {
        $('body').css('visibility', 'visible').hide().fadeIn(600, callback);
    }, 1000);

}

function loadPage(callback) {
    setTimeout(function () {
        $(".background-vid").vide({
            'mp4': '/static/vid/bg-vid.mp4',
            'ogv': '/static/vid/bg-vid.ogv'
        });
        $('.main-content').css('visibility', 'visible').hide().fadeIn(callback);
    }, 1200);
}

function type() {
    $(".typed").typed({
        strings: ["Ideas", "Products", "^500 Dreams"],
        typeSpeed: 20,
        callback: function () {
            displaySuccess(displayButton);
        }
    });
}

var OFFSET = 0;
function navbarController() {
    var triggerPosition = $('.nav-trigger').position().top + OFFSET;
    $(window).on("scroll", function () {
            var scrollPosition = scrollY || pageYOffset;
            if (scrollPosition > triggerPosition) {
                nav = $('.nav');
                nav.addClass('nav-fixed');
            } else {
                $('header').removeClass('nav-fixed');
            }


        }
    );
}

function responsiveNav() {
    $('.menu-icon').click(function () {
        $('.nav').toggleClass('opened')
        // console.log("toggled nav")
    });
}
