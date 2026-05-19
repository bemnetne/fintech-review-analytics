# Bank Reviews Database Setup

This project uses PostgreSQL to store and analyze cleaned mobile banking app reviews collected from the Google Play Store.

## Prerequisites

- Python 3.x
- PostgreSQL
- pip


## PostgreSQL Setup

1. Install PostgreSQL from:

https://www.postgresql.org/download/

2. Create a database named:

```text
bank_reviews
```

3. Run the schema file located in:

```text
sql/schema.sql
```


## Database Schema

The database contains two tables:

### banks
Stores bank metadata.

| Column |
|---|
| bank_id |
| bank_name |
| app_name |

### reviews
Stores cleaned and processed review data.

| Column |
|---|
| review_id |
| bank_id |
| review_text |
| rating |
| review_date |
| sentiment_label |
| sentiment_score |
| identified_theme |
| source |


## Project Setup

Clone the repository and install dependencies:

```bash
git clone <repository_url>
cd bank_reviews_project
pip install -r requirements.txt
```


## Data Insertion

Before inserting data into the database, thematic analysis and sentiment analysis must first be completed since the processed review data generated from those steps is required for database insertion.

Data insertion can then be performed by running:

```text
database.ipynb
```

The notebook handles:
- Loading processed review data
- Inserting bank metadata
- Inserting review records into PostgreSQL


## Data Validation

SQL queries are used to:
- Count reviews per bank
- Calculate average ratings
- Check for null values


## Technologies Used

- Python
- PostgreSQL
- psycopg2
- SQLAlchemy
- pandas