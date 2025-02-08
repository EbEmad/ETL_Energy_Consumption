from extract import extract_data
from transform import transform_data
import psycopg2
import argparse

def load_data(file_path):
    # Connect to PostgreSQL inside Docker
    connection = psycopg2.connect(
        database='energy_consumption',
        host='pgdatabase',  # Use 'localhost' if running outside Docker
        user='postgres',
        password='123456',
        port='5432'
    )
    cursor = connection.cursor()

    print('Loading data...')
    data = extract_data(file_path)

    print('Transforming data...')
    data_transform = transform_data(data)

    column_name = data_transform.columns[-1]

    # Create table if it doesn't exist
    query_create_table = f"""
    CREATE TABLE IF NOT EXISTS {column_name} (
        ID SERIAL PRIMARY KEY,
        continent VARCHAR(50) NOT NULL,
        country VARCHAR(50) NOT NULL,
        {column_name} DECIMAL
    );
    """
    cursor.execute(query_create_table)

    print("Inserting data...")

    for _, row in data_transform.iterrows():
        query_insert_data = f"INSERT INTO {column_name} (continent, country, {column_name}) VALUES (%s, %s, %s)"
        cursor.execute(query_insert_data, (row[0], row[1], row[2]))

    # Commit and close connection
    connection.commit()
    cursor.close()
    connection.close()

    print('ETL process completed successfully.')

    return 'All processes completed'


if __name__ == "__main__":
    # Initialize argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="File path of your dataset")
    
    # Read arguments from command line
    args = parser.parse_args()

    load_data(args.file)
