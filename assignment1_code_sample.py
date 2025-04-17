import os
import pymysql
from urllib.request import urlopen

db_config = {
    'host': os.environ.get('DB_HOST', 'mydatabase.com'),
    'user': os.environ.get('DB_USER', 'admin'),
    'password': os.environ.get('DB_PASSWORD', 'secret123')
}

def get_user_input():
    user_input = input('Enter your name: ')
    # for making it sure that inout dta is valid 
    if not user_input.isalpha():
        print("input is invalid.")
        exit()
    return user_input


def send_email(to, subject, body):
    os.system(f'echo {body} | mail -s "{subject}" {to}')

def get_data():
    url = 'https://insecure-api.com/get-data' # use https for fetching data make sure that data transmiited securly
    data = urlopen(url).read().decode()
    return data

def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES (%s, %s)" # sql query for insertig the fetch data
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query, (data, 'Another Value'))
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
