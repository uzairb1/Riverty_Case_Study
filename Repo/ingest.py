import pandas as pd
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL

def fetch_data():
    url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/United%20States.csv'
    df = pd.read_csv(url,index_col=0,parse_dates=[0])
    df = df.fillna(0)
    df = df.astype({'vaccine':str, 'source_url':str, 'total_vaccinations':int, 'people_vaccinated':int, 'people_fully_vaccinated':int,
                    'total_boosters':int, 'date':str})
    #df['date'] = pd.to_datetime(df['date'])
    return df
def upload_to_snowflake():
    try:
        engine = create_engine(URL(  
            user="",
            password="",
            account="",
            warehouse="COMPUTE_WH",
            database="",
            schema=""
        ))
            # Step 1: Create a Snowflake session
        # Connect to Snowflake
        connection = engine.connect()

        # Create a sample DataFrame
        df = fetch_data()
        print(df)
        # Write DataFrame to Snowflake
        df.to_sql('data_US', con=connection, index=False, if_exists='replace')

        # Close the connection
        connection.close()
    except OSError as e:
        print(e)
upload_to_snowflake()