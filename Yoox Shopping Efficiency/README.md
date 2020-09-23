# Final Project at IronHack

### Introduction :  
For this final project at IronHack, I decided to work on a fashion customer problem : find the best deals in the least amount of time!
So, as you might have understood, I have created a recommandation model, based on the market place Yoox.
We had 6 days to create this project and the presentation.

### Initial goal :
The aim of this porject was for the user to pick a product on Yoox, which is a luxury marketplace, so obviously not in everyone's budget, and the model would find a similar product on Vestiaire Collective or Vide Dressing, which are luxury item's second hand marketplaces.
What this little porject would do basically is reduice the user's environemental impact, help them save some time and money!


### The project itself :
I've scraped Yoox marketplace in two times :
1. All the products with the basics informations like price, designer, category, URL
2. Inside each product, the composition and the color

Then I've cleaned my data and created my recommandation model using the paired cosined distance, after having transformed my data with PCA.

The next step was to create the app using spider.


### Difficulties :
- It took me a lot of time trining to scrape the data from VideDressing.com, trying to get the API, bypassing the firewalls, scraping through HTML, getting kicked out...
Finally, I managed to get 3000 product, which was ridiculously small for this project, so I decided to focus on Yoox for this presentation
- Also, I didn't manage to get the color information without using Selenium which is super long to process as well, considering the number of products, so I dindn't have the proper time to clean the color infomation, which makes it not super precise (I have some "Purple", "Mauve", "Lilac" etc...)

### Improvements :
- Use the second hand database and being able to update it frequently,
- Instead of scraping the whole Yoox database, scrape only the page of the product picked by the client,
- Use image recognition to get a better precision of the colors, patterns, intensity, shapes, length... on the original product (because all the images are following the same template)
- Use NLP and RegEx to get more information from the titles and descriptions of the second hand data.


### Presentation :
Please find [here](https://docs.google.com/presentation/d/1Fk9RNem-E23IARosBCWDSDJG_LQzDdEFVBoo2U3GTpc/edit?usp=sharing) the presentation of this project, that I've had the chance to present at the Hack Show (for a public that is not necessarily from the data field)
