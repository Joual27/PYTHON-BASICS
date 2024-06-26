import pandas as pd
import glob
import xml.etree.ElementTree as ET
from datetime import datetime


log_file = "logs.txt"
target = 'transformed_data.csv'

def extract_from_csv(file):
    return pd.read_csv(file)

def extract_from_json(file):
    return pd.read_json(file)

def extract_from_xml(file):
    df = pd.DataFrame(columns=['car_model','year_of_manufacture','price','fuel'])
    tree = ET.parse(file)
    root = tree.getroot()

    for car in root :
        car_model = car.find('car_model').text
        year_of_manufacture = car.find('year_of_manufacture').text
        price = float(car.find('price').text)
        fuel = car.find('price').text
        df = pd.concat([df, pd.DataFrame([{ 'car_model' : car_model , 'year_of_manufacture' : year_of_manufacture , 'price' : price , 'fuel' : fuel}])] , ignore_index=True) 
    
    return df

def extract():
    extracted_data = pd.DataFrame(columns=['car_model' , 'year_of_manufacture' , 'price', 'fuel'])

    for csvfile in glob.glob('./dataSource/*.csv'):
        extracted_data = pd.concat([extracted_data , extract_from_csv(csvfile)] , ignore_index=True)
    for jsonfile in glob.glob('./dataSource/*.json'):
        extracted_data = pd.concat([extracted_data , extract_from_json(jsonfile)] , ignore_index=True)
    for xmlfile in glob.glob('./dataSource/*.xml'):
        extracted_data = pd.concat([extracted_data , extract_from_xml(xmlfile)] , ignore_index=True)
    
    return extracted_data   

def transform(data):

    data['price'] = round(data.price , 2)
    return data  

def load(data , target_location):
    data.to_csv(target_location)


def log(message):
    timestamps_format = '%Y-%h-%d-%H:%M:%S'

    now = datetime.now()

    timestamps = now.strftime(timestamps_format)
    
    with open(log_file , 'a') as f:
        f.write(timestamps + ',' + message + '\n')




log('ETL PROCESS START')


log('EXTRACTING STARTED')
data = extract()
log('EXTRACTING ENDED')

log('TRANSFORMING STARTED')

transformed_data = transform(data)
print(transformed_data)

log('TRANSFORMING ENDED')

log('LOADING STARTED')
load(transformed_data , target)
log('LOADING ENDED')

log('ETL PROCESS OVER')


