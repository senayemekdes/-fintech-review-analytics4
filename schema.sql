-- Create banks table
CREATE TABLE banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(100) NOT NULL,
    app_name VARCHAR(100)
);

-- Create reviews table
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,

    bank_id INT REFERENCES banks(bank_id),

    review_text TEXT NOT NULL,

    rating INT,

    review_date TIMESTAMP,

    sentiment_label VARCHAR(50),

    sentiment_score FLOAT,

    identified_theme VARCHAR(100),

    source VARCHAR(100)
);