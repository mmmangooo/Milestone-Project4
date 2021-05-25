# Milestone Project 4 - Green Toys - Testing details

## Manual testing

The site has been manually tested on the functionality of the following:

* Navigation links:

  - Links in navigation bar

  - Links in footer

  - Links to toy details and blog details from index page

  - Links to toy details and blog details from toys and blog pages respectively

  - Links back to previous pages from details pages, bag page and checkout page

* Toys pages:

  - Category and sort selectors on toys page

  - Add, edit and delete toy functionality working on frontend and in database

  - Search form for toys returning correct result

* Blog pages:

  - Add, edit and delete blog posts functionality working on frontend and in database

  - Add blog comments

  - Added blog comments showing on blog details page

  - Search form for blogposts returning correct result

* Bag and checkout:  

  - Add to bag functionality

  - Adjust quantity in bag functionality

  - Remove item from bag functionality

  - Checkout purchase with Stripe and webhooks 

  - Receiving confirmation email

  - Order being created in database

* Personal account:

  - Sign up for account

  - Login and logout of account

  - Reset forgotten password

  - Profile page showing saved information and previous order

  - Edit saved information in profile page 

* Contact form: 

  - Showing signed in users emailaddress prefilled

  - Sending email to default site owner

* Toasts showing success, warning, information and error messages

* All forms validating input


## User stories testing

1. As a site user, I want to be able to immediately get an overview of what products this site offers so that I can decide if it contains what I am looking for
   
   - The landing page shows a full-height image of a child playing with a wooden toy and a big header saying "Green Toys" and a call to action button saying  "Shop now", which together clearly tells the user what the site offers

   ![Screenshot of landing page](static/readme-assets/user-stories-testing/landing.png)

2. As a shopper, I want to be able to view a list of products so that I can select some to purchase

   - The toys page by default shows all toys sold on the site

   ![Screenshot of toys page](static/readme-assets/user-stories-testing/all-toys.png)

3. As a shopper, I want to be able to view details about a specific product so that I can see a detailed description, larger image, price and rating of the product

   - By clicking the link on a toy card on the toys page, the user gets to the toy details page where they can see detailed description, larger image, price and rating

   ![Screenshot of toy details page](static/readme-assets/user-stories-testing/toy_details.png)

4. As a shopper, I want to be able to easily view deals and special offers on products so that I can take advantage of special prizes on products that I am interested in buying

   - The landing page shows the three latest toys with campaign prices

   ![Screenshot of campaign section on landing page](static/readme-assets/user-stories-testing/campaign.png)

5. As a shopper, I want to be able to easily see the total of all items in my shopping cart from all parts of the site so that I can avoid spending more money than I was planning to

   - A summary of the total sum of items in user's bag and delivery cost is shown beside the bag icon in the navbar, present on all pages on the site

    ![Screenshot of bag total](static/readme-assets/user-stories-testing/bag-total.png)

6. As as a shopper I want to be able to easily see what rating different products have gotten so that i can see what others think of the product that I am interested in

   - Rating of each toy is shown on toy card on toys page and on toy details page

   ![Screenshot of rating](static/readme-assets/user-stories-testing/rating.png)

7. As a shopper I want to be able to easily see what products have got the highest ratings so that I can find the most popular products

   - The landing page shows the three most popular products on the site

   ![Screenshot of popular products section on landing page](static/readme-assets/user-stories-testing/popular.png) 

8. As a site user, I want to be able to find information about eco-friendly toys so that I can learn more about different materials and their impact on environment and why eco-friendly toys are important

   - The site has a blog page where the user can find blogposts about eco-friendly toys and different materials

    ![Screenshot of blog page](static/readme-assets/user-stories-testing/blog.png) 

9. As a site user I want to be able to comment on blog posts so that I ca ask questions and share my opinions on matters discussed in the blog post

   - When clicking a blogpost, the user gets to a blog details page where they can leave comments on the blogpost, if logged in

   ![Screenshot of blog details page with comment form ](static/readme-assets/user-stories-testing/blog_comment.png) 

10. As a site user I want to be able to easily register for an account so that I can have a personal account to come back to and view my profile

   - A link to signup form is available from the navbar, where the user easily can sign up for an account

  ![Screenshot of sign up form](static/readme-assets/user-stories-testing/signup.png) 

11. As a site user I want to be able to easily log in or out so that I can access my personal account information

   - A link to login and logout respectively is available in the navbar so that the user easily can login or out

   ![Screenshot of login](static/readme-assets/user-stories-testing/nav-login.png) 

   ![Screenshot of logout](static/readme-assets/user-stories-testing/nav-logout.png) 

12. As a site user I want to be able to easily recover my password in case I forget it so that I can regain access to my account

  - From the login page, the user can click a link for resetting a forgotten password

   ![Screenshot of password reset](static/readme-assets/user-stories-testing/password-reset.png) 

13. As a site user I want to be able to recieve a confirmation email after registering an account so that I can know that my account registration was successful

  - The user receives a confirmation email after signing up for an account

    ![Screenshot of email verification](static/readme-assets/user-stories-testing/verify-email.png) 

14. As a site user I want to be able to have a personalized user profile so that I can view my order history and see that my orders are confirmed and save my payment information

  - From the navigation bar, the user can access the "My Profile" page, which contains personal info that can be updated and order history

  ![Screenshot of profile page](static/readme-assets/user-stories-testing/profile.png)

15. As a shopper I want to be able to select which category of products to show so that I can easily find a product within the category that I am interested in

  - The toys page contains a selector dropdown where the user can choose a category of which to show toys

  ![Screenshot of categories select dropdown](static/readme-assets/user-stories-testing/categories-select.png)

16. As a shopper I want to be able to sort each chosen category of product by different parameters so that I can easily find the products with the best rating or lowest price in that category

  - The toys page contains a selector dropdown where the user can choose by which parameter to sort the toys shown

  ![Screenshot of sort select dropdown](static/readme-assets/user-stories-testing/sort-select.png)

  ![Screenshot of categories and sort select dropdown](static/readme-assets/user-stories-testing/category_sort.png)

17. As a shopper I want to be able to search for a product by name or description so that I can easily find a specific product that I am looking to buy

  - A search input field is available in the navigation bar, where the user can search for toys on the site

  ![Screenshot of search toys input](static/readme-assets/user-stories-testing/search-toys.png)

18. As a shopper I want to be able to easily see what I have searched for and the number of results so that I can identify miss-spellings in my search string and quickly overview the search result

   - The search toys results are shown on the toys page with a header telling the user what they have searched for and how many results where found

  ![Screenshot of search toys results](static/readme-assets/user-stories-testing/search-result.png)

19. As a shopper I want to be able to easily select a quantity of the product when adding it to my shopping bag, so that I an ensure I don't accidently select the wrong quantity

   - The toy details page have a quantity select input just above the add to bag button, to ensure that the add to bag functionality is clear to the user
  
  ![Screenshot of select quantity of toys input](static/readme-assets/user-stories-testing/select-qty.png)

20. As a shopper I want to be able to easily view all items in my shopping bag so that I can identify the total cost and overview the items to be ordered

  - The shopping bage page clearly shows a summary of the order items, quantity and shipping cost

  ![Screenshot of shopping bag page](static/readme-assets/user-stories-testing/shoppingbag.png)

21. As a shopper I want to be able to change the quantity of a product in my shopping bag so that I can correct any mistakes in quantity of products before I order

  - The shopping bag page has a quantity select inoput available for each item in the shopping bag, where the user can change quantity or delete a toy in the bag

  ![Screenshot of shopping bag quantity input](static/readme-assets/user-stories-testing/bag-qty-select.png)

22. As a shopper I want to be able to easily enter my payment information so that I can checkout quickly and easily

  - The checkput page contains a user friendly payment form 

  ![Screenshot of payment info form](static/readme-assets/user-stories-testing/payment-info.png)

23. As a shopper I want to know that my personal and payment information is secure so that I can feel confident when providing the information needed to make a purchase

  - The payment form on checkout page contains info about secure payment

  ![Screenshot of payment form secure checkout info](static/readme-assets/user-stories-testing/secure-checkout.png)

24. As a shopper I want to be able to view an order confirmation after checkout so that I can see that I haven't made any mistakes in my order

  - After checkout, the user is sent to a checkput success page which shows order info

  ![Screenshot of checkout success page](static/readme-assets/user-stories-testing/order-confirmation.png) 

25. As a shopper I want to be able to recieve a confirmation email after ordering so that I can keep the information about what I have ordered and when for future needs

  - A confirmation email is sent to the user after ordering

  ![Screenshot of checkout success page showing email confirmation sent](static/readme-assets/user-stories-testing/order-confirmation-email.png) 

26. As a registered user I want to be able to have my address and billing information prefilled on the checkout page so that I can checkout quicker

  - The payment info form has the user's saved information prefilled

  ![Screenshot of prefilled info in payment info form](static/readme-assets/user-stories-testing/prefilled-info.png) 

27. As a store owner I want to be able to add a product to the site so that I can add new items to be sold in my store

  - The site owner, logged in with superuser credentials, can access a form for adding toys via the navigation bar

  ![Screenshot of add toy form](static/readme-assets/user-stories-testing/add-toy.png) 

28. As a store owner I want to be able to edit/update a product so that I can make changes to the products' images or descriptions when needed

  - The site owner, logged in with superuser credentials can access an edit toy form via a link on toy card on toys page 

  ![Screenshot of edit toy form](static/readme-assets/user-stories-testing/edit-toy.png) 

29. As a store owner I want to be able to delete a product so that I can remove items that I am no longer selling

  - The site owner, logged in with superuser credentials can access delete toy functionality via a link on toy card on toys page 

  ![Screenshot of delete toy functionality](static/readme-assets/user-stories-testing/delete-toy.png) 

30. As a store owner I want to be able to add, update and delete blog posts so that I can write and maintain a blog about products-related topics

  - The site owner, logged in with superuser credentials, can access a form for adding blogposts via the navigation bar, edit blogpost form and delete blogpost functionality via links on blog post card on blog page



## Further Testing

* HTML code has been validated using the [WC3 Markup Validation Tool](https://validator.w3.org/) with no errors found

* CSS code has been validated using the [WC3 CSS Validator Tool Jigsaw](https://jigsaw.w3.org/css-validator/) with no errors found

* Javascript code has been validated using [JSHint](https://jshint.com/) with no errors or warnings, except for warnings shown for undeclared variables Stripe and Bootstrap,
  which is because these variables being sent through Stripe and Bootstrap API:s

* Python code has been validated using [Pep8 Online](http://pep8online.com/) with no errors showing, except for some warnings for too long lines that couldn't be fixed without breaking the code. This reagards the following files:
    checkout app: models.py, line 59
                  webhook_handler.py, line 81 and 82
                  webhooks.py, line 47
    toys app: widgets.py, line 12
    settings.py, line 147, 150, 153, 156


## Usability and performance testing


## Bugs

* During development, a number of smaller issues associated with typing mistakes and miss-spelled urls have occured and have all been solved by looking into the error messages shown by Django and searching back to the appointed areas in the code where the issues should be deriving from. A few times issues have also occurred from accidently moving a file out of its parenting folder, which of course has been solved by checking the file structure and finding the out of place file or folder.


* When setting up Bootstrap toasts a bug occured, where the the toasts would show when triggered by appearing in the DOM (seen in Chrome Develeoper Tools) but not show on the page because they has opacity:0 set by bootstrap classes. 
  - This opacity value should not be 0 after the toast has been triggered, and it could be overridden by setting the classes opacity value to 1 manually in the custom CSS file, but this would not fix the underlying issue causing the error. 
  - I tried several different ways of writing the code for triggering the toasts, including using jQuery and not using jQuery, but the result was the same
  - Eventually I asked for help in tutor support and while looking through the issue together, the tutor eventually came across the real issue which was that I had accidently put a script inide the postloadjs block in another template without setting {{ block.super }} above it, which caused the toast triggering script in the postloadjs block on base template to be overriden by this other script and therefor not work
  - The issue was solved by ensuring that all scripts in postloadjs blocks on other templates than base had {{block.super }} set so that they were added to this block rather than overriding other scripts in it loaded from base template


* The campaign prices for some toys where originally set through a separate Campaign model, associated with the Toy model through a foreign key. Since there was no need for having different campaign prices set to different toys or sets of toys in this project I later decided to simplify the functionality of campaign prices by removing the separate Campaign model and change foreign key field campaign field on the toy model to a boolean-field that the superuser can set to True on those toys that should have a campaign price. In the Toy model, I added a function for calulation a campaign price with a 20% discount. This was done after deploying the product to Heroku and setting up a Postgres database and the model changes where therefor to be migrated to both Django in-built database sQlite (used only for development in this project) and to Heroku Postgres database. Migrating to sQlite was successful but when trying to migrate to Postgres, the following error occured in the CLI: 

"django.db.utils.ProgrammingError: cannot cast type bigint to boolean
LINE 1: ...ER COLUMN "campaign" TYPE boolean USING "campaign"::boolean,... "

  - I searched on Google for this error and found several threads on Stack Overflow concerning the issue of PostgresSQL not being to able to cast a field to a different type
    and that it could potentially be solved by manually (from Postgres) setting the field to the other type  
  - Because I was unsure how to alter database model fields from Postgres I contacted tutor support 
  - Together we found that the altered 'campaign' field on the toy model was interpreted as still pointing toward a model that no longer existed (the campaign model)
  - The issue was solved by commenting out the campaign field and deleting the migrations for renaming that field, migrating the deletion of campaign model and then setting  back the campaign field on toy model and migrating again

* After successfully setting up AWS S3 Bucket for storing static and media files, a few days later I received an email from AWS saying that I had used more than 85 percent of the free space on my S3 Bucket for the month of May. As it was still the beginning of May, I came to the conclusion that the free space would definetly be exceeded and I decided to disconnect the S3 Bucket and setup storing with Cloudinary and Whitenoise instead. The setup of these was successful in the case of static files but media files did not render on the deployed version. Because of the deadline to submit the project was drawing up and there were other functionalities to finish, I decided to not pursue debugging the Cloudinary and Whitenoise setup but instead reconnect the AWS S3 Bucket.


* On the 'Toys' page there is a dropdown where the user can choose a category of toys to be shown on the page (Wooden toys or Rubber toys). The dropdown works as far as that  when the user clicks 'Wooden Toys', only wooden toys are shown on the page, and same goes for rubber toys. However, when the user clicks the default value 'All categories' after having chosen either wooden or rubber toys, the page does not go back to showing toys in all categories on the page but remans showing only the latest chosen category. The desired functionality would be to reset the page to showing toys in all categories when 'All Categories' is chosen. Due to lack of time however, I chose not to put additional time into solving this at this point in favor of being able to submit the project on time. This issue therefor remains to be solved. 


