$("article").hide("slow");
$("#intro").show("slow");

$("nav ul li a").on("click", function() {
    $("nav ul li a").removeClass("active");
    $(this).addClass("active");

    let href = $(this).attr("href");
    $("article").hide("slow");
    $(href).show("slow");
});
