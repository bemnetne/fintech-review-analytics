-- =====================================
-- Create Database
-- =====================================
from src.database.connection import get_connection
conn = get_connection()
cursor = conn.cursor()
CREATE DATABASE bank_reviews;

-- Connect to database before running below
-- \c bank_reviews

-- =====================================
-- Banks Table
-- =====================================

CREATE TABLE banks (

    bank_id SERIAL PRIMARY KEY,

    bank_name VARCHAR(255) NOT NULL UNIQUE,

    app_name VARCHAR(255) NOT NULL
);

-- =====================================
-- Reviews Table
-- =====================================

CREATE TABLE reviews (

    review_id SERIAL PRIMARY KEY,

    bank_id INTEGER NOT NULL,

    review_text TEXT NOT NULL,

    rating INTEGER CHECK (
        rating >= 1 AND rating <= 5
    ),

    review_date DATE,

    sentiment_label VARCHAR(50),

    sentiment_score NUMERIC(5,4),

    identified_theme VARCHAR(255),

    source VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_bank
        FOREIGN KEY(bank_id)
        REFERENCES banks(bank_id)
        ON DELETE CASCADE
);

-- =====================================
-- Indexes
-- =====================================

CREATE INDEX idx_bank_id
ON reviews(bank_id);

CREATE INDEX idx_sentiment
ON reviews(sentiment_label);