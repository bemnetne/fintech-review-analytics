from psycopg2.extras import execute_batch
from src.database.connection import get_connection

def insert_banks(df):

    conn = get_connection()
    cursor = conn.cursor()

    unique_banks = df["bank"].unique()

    insert_query = """
    INSERT INTO banks (bank_name, app_name)
    VALUES (%s, %s)
    ON CONFLICT (bank_name) DO NOTHING
    """

    for bank in unique_banks:

        cursor.execute(
            insert_query,
            (bank, bank)
        )

    conn.commit()

    cursor.close()
    conn.close()

    print("Banks inserted successfully!")



def insert_reviews(df):

    conn = get_connection()
    cursor = conn.cursor()
    # cursor.execute("DELETE FROM reviews")
    # conn.commit()
    # =========================
    # Fetch Bank Mapping
    # =========================

    cursor.execute(
        "SELECT bank_id, bank_name FROM banks"
    )

    bank_mapping = {
        bank_name: bank_id
        for bank_id, bank_name in cursor.fetchall()
    }

    # =========================
    # Prepare Records
    # =========================

    review_records = []

    for _, row in df.iterrows():

        review_records.append(
            (
                bank_mapping[row["bank"]],
                row["review_text"],
                int(row["rating"]),
                row["date"],
                row["sentiment_label"],
                float(row["sentiment_score"]),
                row["identified_theme"],
                row["source"]
            )
        )

    # =========================
    # Insert Query
    # =========================

    insert_query = """
    INSERT INTO reviews (
        bank_id,
        review_text,
        rating,
        review_date,
        sentiment_label,
        sentiment_score,
        identified_theme,
        source
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    execute_batch(
        cursor,
        insert_query,
        review_records
    )
    
    conn.commit()

    cursor.close()
    conn.close()

    print("Reviews inserted successfully!")

def count_reviews_per_bank():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT
        b.bank_name,
        COUNT(r.review_id) AS total_reviews
    FROM banks b
    LEFT JOIN reviews r
    ON b.bank_id = r.bank_id
    GROUP BY b.bank_name
    ORDER BY total_reviews DESC;
    """

    cursor.execute(query)

    results = cursor.fetchall()

    print("\nReviews Per Bank\n")

    for row in results:
        print(row)

    cursor.close()
    conn.close()


def average_rating_per_bank():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT
        b.bank_name,
        ROUND(AVG(r.rating), 2) AS average_rating
    FROM banks b
    JOIN reviews r
    ON b.bank_id = r.bank_id
    GROUP BY b.bank_name
    ORDER BY average_rating DESC;
    """

    cursor.execute(query)

    results = cursor.fetchall()

    print("\nAverage Rating Per Bank\n")

    for row in results:
        print(row)

    cursor.close()
    conn.close()


def check_null_values():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT
        COUNT(*) AS total_reviews,

        COUNT(review_text) AS non_null_review_text,

        COUNT(rating) AS non_null_ratings,

        COUNT(sentiment_label) AS non_null_sentiments

    FROM reviews;
    """

    cursor.execute(query)

    result = cursor.fetchone()

    print("\nNull Value Check\n")
    print("\nNull Value Check\n")
    print(result)
    print(f"Total Reviews: {result[0]}")
    print(f"Non-null Review Texts: {result[1]}")
    print(f"Non-null Ratings: {result[2]}")
    print(f"Non-null Sentiment Labels: {result[3]}")

    cursor.close()
    conn.close()