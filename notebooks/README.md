------Scraping Methodology and Limitations----------

Customer reviews were collected from the Google Play Store using the google-play-scraper Python library. Reviews were scraped for the mobile banking applications of Commercial Bank of Ethiopia, Bank of Abyssinia, and Dashen Bank. The scraper retrieved review text, ratings, review dates, review IDs, bank names, and source information.

The scraping process used the following configuration:

Language: English (lang='en')
Country: Ethiopia (country='et')
Sorting method: Newest reviews first (Sort.NEWEST)
Target: Minimum of 400 reviews per bank

The collected reviews covered the range of reviews made publicly accessible by Google Play at the time of scraping, primarily focusing on the most recent reviews returned by the API