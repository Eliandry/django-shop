$(document).ready(function(){

    //toggle message_body
    $(".message_head").click(function(){
        $(this).next(".message_body").slideToggle(500)
        return false;
    });

});