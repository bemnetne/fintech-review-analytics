# Fintech Review Analytics – Web Scraping

## Overview

This module is responsible for collecting customer reviews from the Google Play Store for selected Ethiopian mobile banking applications. The scraped reviews are used for sentiment analysis, thematic analysis, and customer experience evaluation.

The scraping process was implemented in a Jupyter Notebook (`.ipynb`) using the `google-play-scraper` Python library.


## Target Applications

The following banking applications were included in the analysis:

| Bank | App ID |
|---|---|
| Commercial Bank of Ethiopia | `com.combanketh.mobilebanking` |
| Bank of Abyssinia | `com.boa.boaMobileBanking` |
| Dashen Bank | `com.cr2.amolelight` |


## Tools and Libraries

Required Python libraries:

```bash
pip install google-play-scraper pandas
```

Libraries used:
- `google-play-scraper`
- `pandas`

## Data Collected

The scraper extracts the following fields:

| Column | Description |
|---|---|
| `review_id` | Unique review identifier |
| `review_text` | Customer review text |
| `rating` | Rating score (1–5) |
| `review_date` | Date review was posted |
| `bank_name` | Bank/application name |
| `source` | Data source (`Google Play`) |


## Scraping Methodology

The scraping workflow:
1. Connects to Google Play Store using `google-play-scraper`
2. Retrieves reviews for each banking application
3. Collects up to 400 reviews per bank
4. Stores reviews in a Pandas DataFrame
5. Exports the dataset as a CSV file

Reviews were collected using:
- `lang='en'`
- `country='et'`
- `Sort.NEWEST`

The implementation was performed inside:

```text
notebooks/scrape_reviews.ipynb
```

## Collection Results

| Bank | Reviews Collected |
|---|---|
| Commercial Bank of Ethiopia | 400 |
| Bank of Abyssinia | 400 |
| Dashen Bank | 400 |
| **Total** | **1,200** |


## Preprocessing Summary

The collected dataset was cleaned before analysis:
- Duplicate reviews removed using `review_id`
- Missing review text and ratings checked
- Dates normalized to `YYYY-MM-DD`

### Findings
- Duplicate reviews removed: `0`
- Missing rows removed: `0`

This indicates the dataset was complete and clean after scraping.

## Output Files

Generated datasets:

```text
bank_reviews_google_play.csv
cleaned_bank_reviews.csv
```


## Running the Notebook

Open the notebook using Jupyter:

```bash
jupyter notebook
```

Then run:

```text
notebooks/scrape_reviews.ipynb
```

## Project Structure

```text
FINTECH-REVIEW-ANALYTICS/
│
├── .github/
│   └── workflows/
│       └── unittests.yml
│
├── data/
│   ├── processed/
│   │   ├── bank_reviews_sentiment.csv
│   │   └── cleaned_bank_reviews.csv
│   │
│   └── raw/
│       └── bank_reviews.csv
│
├── notebooks/
│   ├── full_output.csv
│   ├── README.md
│   ├── scrapping.ipynb
│   ├── sentimentanalysis.ipynb
│   └── thematic.ipynb
│
├── scripts/
│
├── src/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── analysis.py
│   └── dataprocessing.py
│
├── tests/
│
├── venv/
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Notes

- CSV datasets are excluded from Git tracking using `.gitignore`
- The scraper depends on publicly available Google Play reviews
- Review availability may vary over time depending on Google Play Store updates
