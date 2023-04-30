$(function () {
    // $("#toggle-sidebar").click(function(){
    //     $(".sidebar").toggleClass("toggled");
    // });
    var CURRENT_URL = window.location.href.split('#')[0].split('?')[0];
    $('.sidebar-nav li').find('a').each(function () {
           if($(this).attr('href') == CURRENT_URL || CURRENT_URL.search($(this).attr('href')) >= 0){
               $(this).parent().siblings('li').removeClass('active');
               $(this).parent().addClass('active');
           }
    });

});