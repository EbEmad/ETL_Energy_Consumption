from extract import extract_data
from transform import transform_data
import psycopg2
import argparse


def load_data(file_path):
    connection=psycopg2.connect(database='energy_consumption',host='localhost',user='postgres',password='123456',port='5434')
    cursor=connection.cursor()

    print('loading data.....')
    data=extract_data(file_path)

    print('transforming data.....')

    data_transform=transform_data(data)

    column_name=data_transform.columns[-1]


    query_create_table=f"CREATE TABLE IF NOT EXISTS {column_name}(\
        ID SERIAL PRIMARY KEY,\
            conteinent varchar(50) NOT NULL,\
                country varchar(50) NOT NULL,\
                    {column_name} decimal\);"

    cursor.execute(query_create_table)

    # start loading
    print("loading data....")

    for index,row in data_transform.iterrows():
        query_create_table=f"INSERT INTO {column_name} (contient,country ,{column_name} )
        VALUES (' {row[0]},\
            {row[1]},{row[2]}')"
        cursor.execute(query_create_table)
    cursor.colse()
    connection.close()

    print('etl sucess ....\n')

    return 'all process completed'


if __name__=="__main__":

    # initialize parser
    
    parser=argparse.ArgumentParser()

    parser.add_argument("-f","--file",help="file path 0f your dataset")
    
    # read arguments from command line
    args=parser.parse_args()

    load_data(args.file)

