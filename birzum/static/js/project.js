/* Project specific Javascript goes here. */

$(document).ready(function() {
    // adding to cart functionality
    $('.btn-cart').off().on('click', function(e){
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
        let productId = $(this).attr("product-id")
        let productQuantity = $(this).prev('.qty')
        if (Number(productQuantity.val()) < 20) {
            productQuantity.val(Number(productQuantity.val()) + 1);
        }
        console.log($(this).attr("url"))

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
                    return
                }
            }
        });
    })

    // update quantity and price functions
    $('.quantity-minus').off().click(function(e){
        let productId = $(this).attr("product-id")
        let productQuantity = $(this).prev().prev()
        if (Number(productQuantity.val()) > 1) {
            productQuantity.val(Number(productQuantity.val()) - 1);
        }
        
        console.log($(this).attr("url"))
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
                    return
                }
            }
        });

    })

})


