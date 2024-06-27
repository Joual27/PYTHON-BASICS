import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import sqlite3

URL_TO_SCRAP = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ['Rank','Bank_Name', 'MC_USD_BILLION']
exchange_rate_csv = 'exchange_rate.csv'
target_csv_file = 'TOP_10_BANKS_MC.csv'
TABLE_NAME = 'Largest_Banks'


def log(message): 
    now = datetime.now()
    timestamps = now.strftime('%Y-%h-%d-% H:%M:%S')
    with open('code_log.txt','a') as f:
        f.write(timestamps + ',' + message + '\n')

   
def extract(url, table_attribs): 
    df = pd.DataFrame(columns=table_attribs)
    html_content = requests.get(URL_TO_SCRAP).text
    data = BeautifulSoup(html_content , 'html.parser')
    table_body = data.find('tbody')
    table_rows = table_body.find_all('tr')
    for row in table_rows:
        cols = row.find_all('td')
        if(len(cols) != 0):
            data_dict = {
                table_attribs[0] : cols[0].string.strip(),
                table_attribs[1] : cols[1].find_all('a')[1].string,
                table_attribs[2] : float(cols[2].string.strip())
            }
            df = pd.concat([df , pd.DataFrame(data_dict , index=[0])], ignore_index=True)
    return df

def transform(df, csv_path):
    exchange_data = pd.read_csv(csv_path)
    exchange_rate = exchange_data.set_index('Currency').to_dict()['Rate']
    df['MC_GBP_BILLION'] = round(df['MC_USD_BILLION'] * float(exchange_rate['GBP']) ,2)
    df['MC_EUR_BILLION'] = round(df['MC_USD_BILLION'] * float(exchange_rate['EUR']) ,2)
    df['MC_INR_BILLION'] = round(df['MC_USD_BILLION'] * float(exchange_rate['INR']) ,2)
    return df

def load_to_csv(df, output_path):

    df.to_csv(output_path)

def load_to_db(df, sql_connection, table_name):

    df.to_sql(table_name,sql_connection,if_exists='replace',index=False)

def run_query(query_statement, sql_connection):
    return pd.read_sql(query_statement,sql_connection)


log('Preliminaries complete. Initiating ETL process')
df = extract(URL_TO_SCRAP , table_attribs)
log('Data extraction complete. Initiating Transformation process')
df = transform(df , exchange_rate_csv)
log('Data transformation complete. Initiating Loading process')
load_to_csv(df,target_csv_file)
log('Data saved to CSV file')

conn = sqlite3.connect('Banks.db')
log('SQL Connection initiated')
load_to_db(df,conn,TABLE_NAME)
log('Data loaded to Database as a table, Executing queries')

print(run_query('SELECT * FROM Largest_banks',conn))
print(run_query('SELECT AVG(MC_GBP_Billion) FROM Largest_banks',conn))
print(run_query('SELECT Bank_Name from Largest_banks LIMIT 5',conn))

log('Process Complete')

conn.close()
log('Server Connection closed')


