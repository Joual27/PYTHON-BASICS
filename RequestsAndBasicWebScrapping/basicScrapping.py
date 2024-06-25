from bs4 import BeautifulSoup
import requests

# html_content="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

# soup = BeautifulSoup(html_content, 'html.parser')

# tag_object = soup.h3

# first_sibling = tag_object.next_sibling
# scnd_sibling = first_sibling.next_sibling

# # print(first_sibling ,scnd_sibling )

# #attributes of an element are represented as a dict

# test_tag = tag_object.b
# print(test_tag['id'] , test_tag.attrs , test_tag.get('id') , test_tag.string , type(test_tag.string))


#second example


# table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"


# # trs = soup.find_all('tr')
# # print(trs)

# # for i , row in enumerate(trs):
# #     print(f'row {i} is : {row}')
# #     columns = row.find_all('td')
# #     for j , column in enumerate(columns):
# #        print(f'\t column {j} is {column}')

# trsAndTds = soup.find_all(name=['td','tr'])

# print(trsAndTds , soup.find_all(id='flight'))

# two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"

# soup = BeautifulSoup(two_tables , 'html.parser')

# # find is used to find the first matching tag  , but can also overload args to add specifications
# print(soup.find('table').prettify() , soup.find('table',class_ ='pizza').prettify())


#scrapping a website


# url = "http://www.ibm.com"

# data = requests.get(url).text

# soup = BeautifulSoup(data , 'html.parser')


# # for link in soup.find_all('a', href=True):
# #     print(link['href'])

# for image in soup.find_all('img'):
#     print(image)
#     print(image.get('src'))    

#final example


URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html'

data = requests.get(URL).text

soup = BeautifulSoup(data ,'html.parser')

for row in soup.find_all('tr'):
    columns = row.find_all('td')
    
    color_name = columns[2].string
    color_code = columns[3].string

    print(f'{color_name} ====> {color_code} ')