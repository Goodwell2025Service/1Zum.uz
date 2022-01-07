/* Project specific Javascript goes here. */

$(document).ready(function() {
    // adding to cart functionality
    $('.btn-cart').off().on('click', function(e){
        e.preventDefault();
        let count = $('.qty').val()
        // console.log('clicked', count, $('.cart-count'))
        $.ajax({
            method: "GET",
            url: $(this).attr("href"),
            data: {'count': count},
            dataType: 'json',
            success: function (data) {
                if (data.success) {
                    console.log(data.message)
                    $('#header-cart').text(data.count)
                    $('#success_msg').text(data.message)
                } else {
                    console.log(data.message)
                    $('#success_msg').text(data.message)
                    $('#success_msg').css('color', 'red')
                }
            }
        });
    })

    // Yetkazib berish turini tanlash
    $('#shipping-method input[type="radio"]').on('change', function(e) {
        e.preventDefault();
        $('input[name="shipping-method"]').val($(this).next().text())
    })

    // To'lov turini tanlash
    $('#payment_method .card-header a').on('click', function(e) {
        e.preventDefault();
        $('input[name="payment-method"]').val($(this).text())
    })

    // update quantity and price functions
    $('.quantity-plus').off().click(function(e){
        e.preventDefault()
        let productId = $(this).attr("product-id")
        console.log($(this).attr('class'), productId)
        let productQuantity = $(this).prev('.qty')
        if (Number(productQuantity.val()) < 20) {
            productQuantity.val(Number(productQuantity.val()) + 1);
        }
        console.log("quantity now", productQuantity.val())

        let elem = $(this)

        $.ajax({
            method: "GET",
            url: $(this).attr("url"),
            dataType: 'json',
            data: {'id': productId, 'quantity': productQuantity.val()},
            success: function (data) {
                if (data) {
                    elem.parent().parent().next().children('.amount').text(data.product_price)
                    $("#total-price").text(`${data.total_price} UZS`)
                }
            }
        });
    })

    // update quantity and price functions
    $('.quantity-minus').off().click(function(e){
        e.preventDefault()
        let productId = $(this).attr("product-id")
        console.log($(this).attr('class'), productId)
        let productQuantity = $(this).prev().prev()
        if (Number(productQuantity.val()) > 1) {
            productQuantity.val(Number(productQuantity.val()) - 1);
        }
        
        console.log("quantity now", productQuantity.val())

        let elem = $(this)
        $.ajax({
            method: "GET",
            url: $(this).attr("url"),
            dataType: 'json',
            data: {'id': productId, 'quantity': productQuantity.val()},
            success: function (data) {
                if (data) {
                    elem.parent().parent().next().children('.amount').text(`${data.product_price} UZS`)
                    $("#total-price").text(`${data.total_price} UZS`)
                }
            }
        });
    });

    // submit pagination form
    $('select[name="paginate"]').off().on('change', function(e) {
        console.log("changed");
        $("#left-filter").submit();
    });

    $('input[type="checkbox"]').off().on('click', function(e) {
        console.log("changed");
        $("#left-filter").submit();
    });

    $('input[name="min_price"], input[name="max_price"]').on('focusout', function(e){
        $("#left-filter").submit();
    })

    // function manipulating the compare functionality
    $('.btn-compare').off().on('click', function(e){
        e.preventDefault();
        let count = $('.qty').val()
        let compare_link = $(this).attr("href")
        // console.log('clicked', count, $('.cart-count'))
        $.ajax({
            method: "GET",
            url: $(this).attr("href"),
            data: {'count': count},
            dataType: 'json',
            success: function (data) {
                if (data.success) {
                    console.log(data.message)
                    $('#success_msg').text(data.message)
                    $(this).removeClass('w-icon-compare')
                } else {
                    console.log(data.message)
                    $('#success_msg').text(data.message)
                }
            }
        });
    })

    // function manipulating the whishlist functionality
    $('.btn-wishlist').off().on('click', function(e){
        e.preventDefault();
        console.log("Bosildi")
        $.ajax({
            method: "GET",
            url: $(this).attr("href"),
            data: {'data': 1},
            dataType: 'json',
            success: function (data) {
                if (data.success) {
                    console.log("Success boldi")
                } else {
                    console.log("Muammo boldi")
                }
            }
        });
    })

    // event saving ratings
    $('.fa-star').click(function(){
        $(this).prevAll().addClass('checked');
        $(this).addClass('checked');
        $(this).nextAll().removeClass('checked');
        const rate = $(this).prevAll().length + 1;
        $('input[name="review[rating]"]').val(rate)
        if ($('input[name="review[rating]"]').val()) {
            $('#submitComment').attr('disabled', false)
            $('#rateWarning').fadeOut()
        } else {
            $('#submitComment').attr('disabled', true)
            $('#rateWarning').show()
        }
    })

})

// https://app.slack.com/client/T02PM4HGUUX/C02Q41YLH2Q

