/* Code mostly from https://stripe.com/docs/payments/integration-builder
and https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/f5880efee43b3b9ea1276a09ca972f4588001c59/checkout/static/checkout/js/stripe_elements.js
*/

var stripePublicKey = document.getElementById('id_stripe_public_key').toString().slice(1, -1);
var clientSecret = document.getElementById('id_client_secret').toString().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
  base: {
    color: '#5a5a5a',
    fontFamily: '"Quicksand", sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '1rem',
    padding: '1rem',
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

  } else {
    errorDiv.textContent = '';
  }
})

card.on("change", function (event) {
  // Disable the Pay button if there are no card details in the Element
  document.querySelector("button").disabled = event.empty;
});

var form = document.getElementById("payment-form");
form.addEventListener("submit", function (event) {
  event.preventDefault();
  // Complete payment when the submit button is clicked
  payWithCard(stripe, card, data.clientSecret);
});

// Calls stripe.confirmCardPayment
// If the card requires authentication Stripe shows a pop-up modal to
// prompt the user to enter authentication details without leaving your page.
var payWithCard = function (stripe, card, clientSecret) {
  loading(true);
  stripe
    .confirmCardPayment(clientSecret, {
      payment_method: {
        card: card
      }
    })
    .then(function (result) {
      if (result.error) {
        // Show error to customer, in error-div
        var errorDiv = document.getElementById('card-errors');
        var html = `
          <span class="icon" role="alert">
          <i class="fas fa-times"></i></span>
          <span>${result.error.message}</span> `;
        $(errorDiv).html(html);
        $(errorDiv).html(html);
        card.update({ 'disabled': false });
        $('#checkout-button').attr('disabled', false);
      } else {
        if (result.paymentIntent.status === 'succeeded') {
          form.onsubmit();

        }
        // The payment succeeded!
        orderComplete(result.paymentIntent.id);
      }
    });
};

// Show a spinner on payment submission
var loading = function (isLoading) {
  if (isLoading) {
    // Disable the button and show a spinner
    document.querySelector("button").disabled = true;
    document.querySelector("#spinner").classList.remove("hidden");
    document.querySelector("#button-text").classList.add("hidden");
  } else {
    document.querySelector("button").disabled = false;
    document.querySelector("#spinner").classList.add("hidden");
    document.querySelector("#button-text").classList.remove("hidden");
  }
};