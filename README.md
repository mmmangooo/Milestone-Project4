# Green toys webshop

This site is the Milestone Project 4 for the Software Development Diploma course at Code Institute. The project is aimed at displaying my 
understanding of full stack development with Django framework and building upon all previous learning in the course to put together a fully functional
website.

[A live version of the website can be virwed here]()

(Image of the site on differents viewports)


The purpose of this site is to provide means for parents and others to buy eco-friendly toys for their children. The reasoning behind this is that children (at least in societal
contexts where economical conditions are strong) often have an abundance of toys, and these are more often than not made of different sort of plastics. As the manufacturing of plastics 
results in negative effects on the environment, many people find it important to try to avoid contributing to this by limiting or avoiding their use of plastic materials. When it comes
to toys, avoiding plastics can be percieved as important both for the sake of minimizing negative effects on the environment and because plastic toys can contain potentially harmful
substances. Because of this, many people find it especially important that the things that children use are made of environment-friendly materials that are free from harmful substances,
and there is therefore a need for providing such things as toys that are guaranteed to be tested for substances that can be harmful to children and that are made out of material that 
cause as little harm as possible to the environment. This website is aimed at providing an easy way for parents and others interested to purchase these kind of eco-friendly toys.


## UX

### Ideal client

The ideal client for this website is:

* Someone environmentally conscious

* A parent or someone else with children in their social circle

### Visitors to this site are looking for

* Buying a gift to a child

* Buying toys with a minimized negative impact on the environment

* Buying toys that are free from substances that can be harmful to children

* Finding more information about why eco-friendly toys are important and what effect different materials have on the environment

### This site is the best way to help them achieve this because:

* It only contains toys that fill the above criteria

* It provides user-friendly ways of searching and sorting the articles to find an eco-friendly toy of interest

* It provides easily accessed check-out options and register, login and logout of account

* It contains a blog with posts about eco-friendly toys, information about different materials toys can be made of and their impact on the environment

* The site is easy to navigate and well-designed to provide a positive user experience


### User stories

![Image of all user stories for the site](/static/readme-assets/readme-images/user_stories.png)

### Wireframes

1. As a site user, I want to be able to immediately get an overview of what products this site offers so that I can decide if it contains what I am looking for

![Image of wireframe showing mobile home page](/static/readme-assets/readme-images/home_mobile.png)
![Image of wireframe showing web home page](/static/readme-assets/readme-images/home_web.png)

2. As a shopper, I want to be able to view a list of products so that I can select some to purchase

![Image of wireframe showing product page on mobile](/static/readme-assets/readme-images/all_products_mobile.png)
![Image of wireframe showing product page on web](/static/readme-assets/readme-images/all_products_web.png)

3. As a shopper, I want to be able to view details about a specific product so that I can see a detailed description, larger image, price and rating of the product

![Image of wireframe showing product details on mobile page](/static/readme-assets/readme-images/product_detail_mobile.png)

![Image of wireframe showing product details on web page](/static/readme-assets/readme-images/product_detail_web.png)

4. As a shopper, I want to be able to easily view deals and special offers on products so that I can take advantage of special prizes on products that I am interested in buying

![Image of wireframe showing campaign section](/static/readme-assets/readme-images/campaigns.png)

5. As a shopper, I want to be able to Easily see the total of all items in my shopping cart from all parts of the site so that I can avoid spending more money than I was planning to

![Image of wireframe showing shopping cart](/static/readme-assets/readme-images/shopping_cart.png)

6. As as a shopper I want to be able to easily see what rating different products have gotten so that i can see what others think of the product that I am interested in

![Image of wireframe showing close up of product icon on product page](/static/readme-assets/readme-images/product_closeup.png)

7. As a shopper I want to be able to easily see what products have got the highest ratings so that I can find the most popular products

![Image of wireframe showing popular products section on home page](/static/readme-assets/readme-images/popular.png)

8. As a site user, I want to be able to find information about eco-friendly toys so that I can learn more about different materials and their impact on environment and why eco-friendly toys are important

![Image of wireframe showing blog page on mobile](/static/readme-assets/readme-images/blog_mobile.png)

![Image of wireframe showing blog page on web](/static/readme-assets/readme-images/blog_web.png)

9. As a site user I want to be able to comment on blog posts so that I ca ask questions and share my opinions on matters discussed in the blog post

![Image of wireframe showing individual blog post with comment field](/static/readme-assets/readme-images/blog_comment.png)

10. As a site user I want to be able to easily register for an account so that I can have a personal account to come back to and view my profile

![Image of wireframe showing registration page on mobile](/static/readme-assets/readme-images/register_mobile.png)

![Image of wireframe showing registration page on web](/static/readme-assets/readme-images/register_web.png)

11. As a site user I want to be able to easily log in or out so that I can access my personal account information

![Image of wireframe showing login page on mobile](/static/readme-assets/readme-images/login_mobile.png)

![Image of wireframe showing login page on web](/static/readme-assets/readme-images/login_web.png)

12. As a site user I want to be able to easily recover my password in case I forget it so that I can regain access to my account

![Image of wireframe showing close up of recreate password on login](/static/readme-assets/readme-images/recreatepassword_closeup.png)

13. As a site user I want to be able to recieve a confirmation email after registering an account so that I can know that my account registration was successful

![Image of wireframe showing registration confirmation message](/static/readme-assets/readme-images/registration_confirmation.png)

14. As a site user I want to be able to have a personalized user profile so that I can view my order history and see that my orders are confirmed and save my payment information

![Image of wireframe showing user profile page on mobile](/static/readme-assets/readme-images/user_profile_mobile.png)

![Image of wireframe showing user profile page on web](/static/readme-assets/readme-images/user_profile_web.png)

15. As a shopper I want to be able to select which category of products to show so that I can easily find a product within the category that I am interested in

16. As a shopper I want to be able to select to show only products with a special prize offer so that I can find only the products with the most favoureable prizes

![Image of wireframe showing close up of dropdown with choice of category to show](/static/readme-assets/readme-images/categories.png)

17. As a shopper I want to be able to sort each chosen category of product by different parameters so that I can easily find the products with the best rating or lowest price in that category

![Image of wireframe showing close up of dropdown with choice of parameter to sort the product list by](/static/readme-assets/readme-images/sortby_closeup.png)

18. As a shopper I want to be able to search for a product by name or description so that I can easily find a specific product that I am looking to buy

![Image of wireframe showing close up of search field](/static/readme-assets/readme-images/search.png)

19. As a shopper I want to be able to easily see what I have searched for and the number of results so that I can identify miss-spellings in my search string and quickly overview the search result

![Image of wireframe showing search results page](/static/readme-assets/readme-images/search_results.png)

20. As a shopper I want to be able to easily select a quantity of the product when adding it to my shopping bag, so that I an ensure I don't accidently select the wrong quantity

![Image of wireframe showing close up of quantity choose field on product details page](/static/readme-assets/readme-images/quantity_closeup.png)

21. As a shopper I want to be able to easily view all items in my shopping bag so that I can identify the total cost and overview the items to be ordered

![Image of wireframe of shopping bag page on mobile](/static/readme-assets/readme-images/shopping_bag_mobile.png)

![Image of wireframe of shopping bag page on web](/static/readme-assets/readme-images/shopping_bag_web.png)

22. As a shopper I want to be able to change the quantity of a product in my shopping bag so that I can correct any mistakes in quantity of products before I order

![Image of wireframe showing close up of change quantity field in shopping bag](/static/readme-assets/readme-images/change_quantity_closeup.png)

23. As a shopper I want to be able to easily enter my payment information so that I can checkout quickly and easily

![Image of wireframe of checkout page on mobile](/static/readme-assets/readme-images/checkout_mobile.png)

![Image of wireframe of checkout page on web](/static/readme-assets/readme-images/checkout_web.png)

24. As a shopper I want to know that my personal and payment information is secure so that I can feel confident when providing the information needed to make a purchase

![Image of closeup of info about secure checkout](/static/readme-assets/readme-images/secure_checkout.png)

25. As a shopper I want to be able to view an order confirmation after checkout so that I can see that I haven't made any mistakes in my order

26. As a shopper I want to be able to recieve a confirmation email after ordering so that I can keep the information about what I have ordered and when for future needs

![Image of wireframe of order confirmation page on mobile](/static/readme-assets/readme-images/order_confirmation_mobile.png)

![Image of wireframe of order confirmation page on web](/static/readme-assets/readme-images/order_confirmation_web.png)

27. As a registered user I want to be able to have my address and billing information prefilled on the checkout page so that I can checkout quicker

![Image of wireframe of checkout page with user's info prefilled](/static/readme-assets/readme-images/users_info_prefilled.png)


28. As a store owner I want to be able to add a product to the site so that I can add new items to be sold in my store

![Image of wireframe of add product page](/static/readme-assets/readme-images/add_product.png)

29. As a store owner I want to be able to edit/update a product so that I can make changes to the products' images or descriptions when needed

![Image of wireframe of products page when superuser is logged in](/static/readme-assets/readme-images/products_page_superuser.png)

![Image of wireframe of products edit page](/static/readme-assets/readme-images/edit_product.png)

30. As a store owner I want to be able to delete a product so that I can remove items that I am no longer selling

![Image of close up of delete product link on products page](/static/readme-assets/readme-images/delete_product_closeup.png)


31. As a store owner I want to be able to add, update and delete blog posts so that I can write and maintain a blog about products-related topics

![Image of wireframe of blog page when superuser is logged in](/static/readme-assets/readme-images/blog_page_superuser.png)

![Image of wireframe of add blog post page](/static/readme-assets/readme-images/add_blog_post.png)

![Image of wireframe of edit blog post page](/static/readme-assets/readme-images/edit_blog_post.png)

![Image of close up of delete blog link on blog page](/static/readme-assets/readme-images/delete_blogpost_closeup.png)

## Database design

![Image of database design schema](/static/readme-assets/readme-images/MS4_database_design.png)

## Security

An env.py file is used for storing details about database and Stripe connections. This file is not uploaded to Github.

## Design

* Color schema:
  The background color used on the site is a regular plain white, #fffff, which is chosen for creating an impression of airyness on the background by keeping it a color that goes by rather unnoticed. A brown umber nuance, #6D564D is used for headers and links in nav bar. It is chosen to create associations with nature and eco-friendliness, while also being a very warm color that aids in giving a sort of calm an friendly impression to the site. Buttons, shopping bag icon and hero header has a bright green nuance, #81E157, that is chosen to create an impression of playfulness and hapiness and associate with the sites target group - children. This is also the purpose of the light green complementary color #DEF188 that is used on the header banner and on button hovers. The p elements on the site use a dark grey/light black color, #383636, that is chosen to create a softer impression and be easier on the eyes than a regular black color. 

![Color scheme pallette](/static/readme/readme-images/color-scheme.png)

* Imagery:
  The hero image - a closeup of a child's hand playing with a wooden toy, is chosen to create associations to robust and environmentally friendly toys that catches a child's interest (by showing a child engaged in play with this type of toy). The brown colors in the image also aid in creating associations with nature and naturalness that goes well with the site's 
  purpose. The drawn image of a green leaf appering on different pages on the site is chosen to represent an association to nature and environmental friendliness. The drawn images of toys and animals are chosen to create a feeling of playfulness and associate with kids and playing.

* Typography:
  The main header on the hero section on landing page, p elements and all headers on the site except for the subheader on the hero section has the font Quicksand. This font is chosen for its
  rounded shapes that create an impression of friendliness and somewhat of an association to childhood, while not being so round-shaped that it gets hard to read. The subheader on the hero section has the font Roboto, which is chosen to give a more serious impression (by its narrow shape) to accomodate well with this header's promoting message.


### Differences between wireframes and implemented design


## Features

Navigation bar is present on all pages to ensure easily accessed navigation on the site. In the navbar is also a search bar where the user can search for toys on the site. Banner below navbar showing the free shipping threshold, and shortcut to shopping cart are also present on all pages to make sure that the customer easily can keep track of their shopping. There is also a footer with copyright info present on all pages.

### Index page

The index page consists of a hero section covering the full height of the screen, showing a large image with a header and a subheader on it clearly stating the name
of the site and with a call for action button below leading to the all toys page. Below the hero section on index page, the user finds a selection of toys that can be bought on this site - the four toys with the highest rating and four toys that are on campaign right now with lower prices. This is made to create an interest in looking at some of the toys sold on the site. The user also finds the four latest blog posts displayed here which is made to envoke an interest in exploring the blog. In this section there are also links to the all toys page and the blog page for easily accessed navigation.

### Toys page

On this page the user can find all toys for sale on the website, and choose to show only toys in the category 'wooden' or 'rubber', and sort toys by price or rating, highest to lowest or the opposite. On the card for each toy, there is an image of the toy (or a 'no image found' generic image if that toy has no image) a "read more"-button that takes the user to the toy details page. For superuser, the cards also contains an edit- and a delete- link that takes the superuser to an edit form for that toy, or to a confirmation page for deleting that toy.

### Search results page

If the user has searched for a toy on the site using the search bar in the navigation menu, the result is shown on the toys page along with a header saying what the user has searched for and how many results were found.

### Toy details page

The toy details page contains details about the toy that the user has clicked the "read more"-button on from the toys page. This page contains an image of the toy, a description of it and a button for adding the toy to the user's shopping cart, along with an input for choosing the amount of toys to add to the bag. Clicking the add to shopping bag-button will trigger a toast message that shows the user a feedback for the action. 

### Add toy page

This page is only available for superuser, and is accessed from the navigation bar (where it is only showed for signed in superuser). This page contains a form where the superuser can fill in name, description, rating and image and add a toy to the database by clicking "add toy". The page also contains a "cancel"-link that leads back to the toys-page when clicked.

### Edit toy page

This page is only available for superuser, and is accessed from the navigation bar (where it is only showed for signed in superuser). This page contains a form where the superuser can edit name, description, rating and image and add the updates to the database by clicking "edit toy". The page also contains a "cancel"-link that leads back to the toys-page when clicked.

### Confirm deletion page

This page is shown when superuser clicks the "delete"-link on a toy card. This page only contains a question "Are you sure you want to delete (name of the toy) ? and the choices yes or no. Clicking no takes the user back the toys page and clicking yes deletes the toy from the database.

### Shopping bag page

If the user has not added any toy to their bag, this page contains an info text saying that the user does not have any items in their bag yet, and a link to the toys page for a shortcut to shopping. If the user has added any items to their bag, this page shows what items are in the bag, the amount of them added and their price each and totally, along with shipping price and info about how much more the user has to by for to get free shipping (if that amount is not already exceeded). The shopping bag page contains a link back to the toys page in case the user wants to do more shopping, and a button that takes the user to the checkout page when clicked.

### Checkout page

The checkout page contains a summary of the users order with title of the items, price of each, amount of each, total of each, shipping cost and total cost. It also contains a form where the user fills in their shipping and payment details. For signed in users with this information saved to their profile, it is prefilled in this form. The page contains a link back to the toys page if the user wants to add more items to their bag, and a button for paying and checking out the order. 

### Blog page
The blog page contains a list of blog posts shown in the order of most recently added. The page also has a search box above the blog post where the user can search for a blog post either by title or by a word in the content. Each blogpost has a "read more"-link that when clicked takes the user to the blog details page. For a signed in superuser, there are also two additional links on each blogpost. One for editing, that takes the superuser to an edit blogpost page, and one for delete that takes the superuser for a confirm deletion page.

### Blog details page

The blog details page contains the entire text content of the blogpost shown, and if the user is signed in to their account a button saying "comment blogpost" is shown. If the user is not signed in, a text informing the user that they has to be signed in to comment is shown instead, along with a link to the login page and a link to the sign up-page to make it easy for the user to login or to create an account if they doesn't have one.




### Add blog page

This page is only available for superuser, and is accessed from the navigation bar (where it is only showed for signed in superuser). This page contains a form where the superuser can fill in title and content and add a blogpost to the database by clicking "add blogpost". The page also contains a "cancel"-link that leads back to the blogs-page when clicked.

### Edit blog page

This page is only available for superuser, and is accessed from the navigation bar (where it is only showed for signed in superuser). This page contains a form where the superuser can edit title and content and update a blogpost in the database by clicking "edit blogpost". The page also contains a "cancel"-link that leads back to the blogs-page when clicked.

### Confirm deletion page

This page is shown when superuser clicks the "delete"-link on a blogpost on the blog page. This page only contains a question "Are you sure you want to delete (title of the blogpost) ? and the choices yes or no. Clicking no takes the user back the blogs page and clicking yes deletes the toy from the database.


## Credits

Unsplash

Sigmund
  

Code:
Setting up signup and login, this tutorial: https://www.youtube.com/watch?v=q4jPR-M0TAQ&t=1377s


Blog comments, this tutorial: https://www.youtube.com/watch?v=hZrlh4qU4eQ
and https://djangocentral.com/creating-comments-system-with-django/


404 and 500 custom template setup:

https://github.com/GBrachetta/guillermo/blob/master/guillermo/


Code credits for send email view:
https://docs.djangoproject.com/en/3.2/topics/email/
and https://www.youtube.com/watch?v=4b3yvjcPLnk&list=PLXcnmXd-db_hO1v3SLAzVcNieoS_Tcn-6