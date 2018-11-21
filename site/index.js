function navega(id) {
    $("article").hide('slow');
    $("article").removeClass("active")
    $("#" + id).show('slow');
    $("#" + id).addClass('active');
}

navega("post1");