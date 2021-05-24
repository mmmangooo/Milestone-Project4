# Milestone Project 4 - Green Toys - Testing details

## Manual testing

The site has been manually tested on the functionality of the following:


## User stories testing


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


