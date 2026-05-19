import pandas as pd
import psycopg2

# Load CSV
df = pd.read_csv("notebooks/dataprocessed/all_reviews3.csv")

# PostgreSQL connection
conn = psycopg2.connect(
    host="localhost",
    database="bank_reviews",
    user="postgres",
    password="123456",
    port="5432"
)

cur = conn.cursor()

# Theme identification function
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


# Loop through rows
for _, row in df.iterrows():

    # Get bank_id from bank_name
    cur.execute(
        """
        SELECT bank_id FROM banks
        WHERE bank_name = %s
        """,
        (row['bank'],)
    )

    result = cur.fetchone()

    if result:
        bank_id = result[0]

        cur.execute(
            """
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
            """,
            (
                bank_id,
                row['content'],
                row['score'],
                row['at'],
                row['transformer_sentiment_label'],
                row['transformer_sentiment_score'],
                # AUTO GENERATED THEME
                identify_theme(row['content']),
                "Google Play Store"
            )
        )

# Save changes
conn.commit()

print("Reviews inserted successfully!")

cur.close()
conn.close()