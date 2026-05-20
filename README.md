# Fintech Mobile Banking Review Analytics Project

## Overview

This project focuses on collecting, processing, analyzing, and storing customer reviews from Ethiopian mobile banking applications. The workflow includes data scraping, sentiment analysis, PostgreSQL database implementation, and business insight generation.

The project was completed in four major tasks:

1. Task 1 — Data Collection and Preprocessing
2. Task 2 — Sentiment and Thematic Analysis
3. Task 3 — Store Cleaned Data in PostgreSQL
4. Task 4 — Insights and Recommendations

---

# Task 1: Data Collection and Preprocessing

## Objective

Collect customer reviews from mobile banking applications and prepare clean datasets for downstream sentiment analysis and database storage.

---

## Data Sources

Customer reviews were collected from Google Play Store applications for:

* Bank of Abyssinia (BoA Mobile)
* Dashen Bank (Dashen Super App)
* Commercial Bank of Ethiopia (CBE Mobile)

---

## Tools and Libraries Used

* Python
* pandas
* google-play-scraper
* numpy
* matplotlib

---

## Data Collection Process

Reviews were scraped programmatically using Python scripts.

Example metadata collected:

* Review text
* Rating score
* Review date
* App metadata
* User feedback

---

## Data Cleaning and Preprocessing

The following preprocessing steps were performed:

* Removed duplicate reviews
* Removed missing/null values
* Standardized column names
* Converted review dates to datetime format
* Cleaned unnecessary symbols and whitespace
* Combined review datasets into a unified CSV

---

## Output

Final cleaned datasets were stored as CSV files for further analysis.

Example files:

```text
all_reviews.csv
cleaned_reviews.csv
```

---

# Task 2: Sentiment and Thematic Analysis

## Objective

Analyze customer sentiment and identify recurring themes from bank reviews.

---

## Sentiment Analysis Techniques

The project applied multiple sentiment analysis techniques:

* VADER Sentiment Analysis
* TextBlob Sentiment Analysis
* Transformer-based Sentiment Classification

---

## Generated Features

The following features were added to the processed dataset:

| Feature                     | Description                  |
| --------------------------- | ---------------------------- |
| vader_compound              | VADER sentiment score        |
| tb_polarity                 | TextBlob polarity score      |
| tb_subjectivity             | TextBlob subjectivity score  |
| sentiment                   | Final sentiment label        |
| transformed_sentiment_label | Transformer sentiment label  |
| transformed_sentiment_score | Transformer confidence score |

---

## Theme Identification

Keyword-based thematic classification was implemented to categorize reviews into:

* Authentication
* Stability
* Transactions
* Performance
* User Experience
* Other

---

## Key Findings

### Positive Drivers

* Fast money transfers
* Convenient mobile banking access
* User-friendly interfaces

### Common Pain Points

* OTP and login failures
* Application crashes
* Slow performance during peak usage

---

# Task 3: Store Cleaned Data in PostgreSQL

## Objective

Design and implement a relational database schema in PostgreSQL to persistently store cleaned and processed bank review data. The task simulates a real-world data engineering workflow involving database setup, schema creation, data insertion, and SQL validation.

---

# Project Setup

## Technologies Used

* Python 3
* PostgreSQL
* pgAdmin 4
* pandas
* psycopg2
* Git & GitHub

---

# Database Setup

## Step 1: Install PostgreSQL

PostgreSQL and pgAdmin 4 were installed on Windows.

## Step 2: Create Database

A PostgreSQL database named:

```sql
bank_reviews
```

was created using pgAdmin 4.

---

# Database Schema Design

Two relational tables were created:

## 1. banks Table

Stores metadata about the banks and their mobile applications.

### Columns

| Column    | Type               | Description             |
| --------- | ------------------ | ----------------------- |
| bank_id   | SERIAL PRIMARY KEY | Unique bank identifier  |
| bank_name | VARCHAR(100)       | Bank name               |
| app_name  | VARCHAR(100)       | Mobile application name |

---

## 2. reviews Table

Stores cleaned customer reviews and sentiment analysis results.

### Columns

| Column           | Type               | Description                         |
| ---------------- | ------------------ | ----------------------------------- |
| review_id        | SERIAL PRIMARY KEY | Unique review identifier            |
| bank_id          | INT                | Foreign key referencing banks table |
| review_text      | TEXT               | Customer review text                |
| rating           | INT                | Review rating score                 |
| review_date      | TIMESTAMP          | Date and time of review             |
| sentiment_label  | VARCHAR(50)        | Sentiment classification            |
| sentiment_score  | FLOAT              | Sentiment confidence/score          |
| identified_theme | VARCHAR(100)       | Extracted review theme              |
| source           | VARCHAR(100)       | Review source platform              |

---

# SQL Schema

```sql
CREATE TABLE banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(100) NOT NULL,
    app_name VARCHAR(100)
);

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
```

---

# Insert Bank Metadata

```sql
INSERT INTO banks (bank_name, app_name)
VALUES
('Bank of Abyssinia', 'BoA Mobile'),
('Dashen Bank', 'Dashen Super App'),
('Commercial Bank of Ethiopia', 'CBE Mobile');
```

---

# Data Insertion Using Python

A Python script named:

```text
insert_reviews.py
```

was created to:

* Load cleaned CSV review data
* Connect to PostgreSQL
* Map reviews to corresponding banks
* Insert review records into the reviews table
* Automatically generate themes from review content

---

# Theme Identification

A simple keyword-based function was implemented to classify reviews into themes such as:

* Authentication
* Stability
* Transactions
* Performance
* User Experience
* Other

Example:

```python
def identify_theme(review):
    review = str(review).lower()

    if any(word in review for word in ['login', 'password', 'otp']):
        return 'Authentication'

    elif any(word in review for word in ['crash', 'bug', 'freeze']):
        return 'Stability'

    elif any(word in review for word in ['transfer', 'payment']):
        return 'Transactions'

    elif any(word in review for word in ['slow', 'lag']):
        return 'Performance'

    elif any(word in review for word in ['ui', 'design', 'interface']):
        return 'User Experience'

    else:
        return 'Other'
```

---

# Database Verification Queries

## 1. Count Reviews Per Bank

```sql
SELECT b.bank_name, COUNT(r.review_id) AS total_reviews
FROM banks b
JOIN reviews r
ON b.bank_id = r.bank_id
GROUP BY b.bank_name;
```

---

## 2. Average Rating Per Bank

```sql
SELECT b.bank_name, AVG(r.rating) AS average_rating
FROM banks b
JOIN reviews r
ON b.bank_id = r.bank_id
GROUP BY b.bank_name;
```

---

## 3. Check for NULL Values

```sql
SELECT *
FROM reviews
WHERE review_text IS NULL
OR sentiment_label IS NULL;
```

---

# Project Structure

```text
fintech-review-analytics/
│
├── notebooks/
├── data/
├── insert_reviews.py
├── db_test.py
├── schema.sql
├── README.md
├── requirements.txt
└── .github/workflows/ci.yml
```

---

# Git Workflow

## Create Task Branch

```bash
git checkout -b task-3
```

## Commit Changes

```bash
git add .
git commit -m "Complete Task 3 PostgreSQL implementation"
```

## Push Branch

```bash
git push origin task-3
```

---

# CI Pipeline

A GitHub Actions CI pipeline was added to:

* Validate Python setup
* Install dependencies
* Run a basic Python verification step automatically on push

---

# Key Achievements

* PostgreSQL database successfully configured
* Relational schema designed and implemented
* Python-to-PostgreSQL connection established
* Review data inserted into database
* Sentiment and theme data stored successfully
* SQL verification queries executed
* GitHub CI workflow configured

---

# Conclusion

This task successfully demonstrated the implementation of a complete PostgreSQL data storage workflow for fintech mobile banking reviews. The project integrates Python data processing, sentiment analysis results, relational database design, SQL validation, and Git-based development practices into a reproducible data engineering pipeline.
