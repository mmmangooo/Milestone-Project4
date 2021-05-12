/* Code mostly from https://stripe.com/docs/payments/integration-builder	
and https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/f5880efee43b3b9ea1276a09ca972f4588001c59/checkout/static/checkout/js/stripe_elements.js	
*/
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
  base: {
    color: '#5a5a5a',
    fontFamily: '"Quicksand", sans-serif',
    fontSmoothing: 'antialiased',
  },
  invalid: {
    color: '#f55742',
    iconColor: '#f55742'
  }
};
// Create a card element and insert it into a div 	
// in the checkout template	
var card = elements.create('card', { style: style });
card.mount('#card-element');

// Show validation errors on the card element in a div by the card	
card.addEventListener('change', function (event) {
  var errorDiv = document.getElementById('card-errors');
  if (event.error) {
    var html = `	
          <span class="icon" role="alert">	
          <i class="fas fa-times"></i></span>	
          <span>${event.error.message}</span> `;
    errorDiv.innerHTML = html;
  } else {
    errorDiv.textContent = '';
  }
})

// Handle form submit	
var form = document.getElementById("payment-form");
form.addEventListener("submit", function (event) {
  event.preventDefault();
  card.update({ 'disabled': true });
  $('#checkout-button').attr('disabled', true);

  var saveInfo = Boolean($('#save-user-info').attr('checked'));
  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  var postData = {
    'csrfmiddlewaretoken': csrfToken,
    'client_secret': clientSecret,
    'save_info': saveInfo,
  };
  var url = '/checkout/cache_checkout_data/';
  $.post(url, postData).done(function () {
    stripe.confirmCardPayment(clientSecret, {
      payment_method: {
        card: card,
        billing_details: {
          firstName: $.trim(form.first_name.value),
          lastName: $.trim(form.last_name.value),
          phone: $.trim(form.phone_number.value),
          email: $.trim(form.email.value),
          address: {
            line1: $.trim(form.street_address1.value),
            line2: $.trim(form.street_address2.value),
            city: $.trim(form.town_or_city.value),
            country: $.trim(form.country.value),
            state: $.trim(form.county.value),
          }
        }
      },
      shipping: {
        firstName: $.trim(form.first_name.value),
        lastName: $.trim(form.last_name.value),
        phone: $.trim(form.phone_number.value),
        address: {
          line1: $.trim(form.street_address1.value),
          line2: $.trim(form.street_address2.value),
          city: $.trim(form.town_or_city.value),
          country: $.trim(form.country.value),
          postal_code: $.trim(form.postcode.value),
          state: $.trim(form.county.value),
        }
      },
    }).then(function (result) {
      if (result.error) {
        // Show error to customer, in error-div 
        var errorDiv = document.getElementById('card-errors');
        var html = `  
            <span class="icon" role="alert">  
            <i class="fas fa-times"></i></span> 
            <span>${result.error.message}</span> `;
        $(errorDiv).html(html);
        card.update({ 'disabled': false });
        $('#submit-button').attr('disabled', false);
      } else {
        if (result.paymentIntent.status === 'succeeded') {
          form.submit();
        }
      }
    });
  }).fail(function () {
    // If the payment fails, reload the page  
    location.reload();
  })
});
