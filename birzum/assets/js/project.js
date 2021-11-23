/* Project specific Javascript goes here. */

$(document).ready(function() {
    $('.btn-cart').on('click', function(e){
        e.preventDefault();
        console.log("fucking shit")
        $.ajax({
            method: "GET",
            url: $(this).attr("href"),
            dataType: 'json',
            success: function (data) {
                if (data) {
                   console.log(data.success) 
                }
            }
        });
    })
})
