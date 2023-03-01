import requests
from bs4 import BeautifulSoup
import time
import csv

vietnamese_letters = ['a', 'á', 'à', 'ã', 'ả', 'ă', 'ắ', 'ằ', 'ẵ', 'ẳ', 'â', 'ấ', 'ầ', 'ẫ', 'ẩ', 'b', 'c', 'd', 'đ', 'e', 'é', 'è', 'ẽ', 'ẻ', 'ê', 'ề', 'ế', 'ễ', 'ể', 'g', 'h', 'i', 'í', 'ì', 'ĩ', 'ỉ', 'k', 'l', 'm', 'n', 'o', 'ó', 'ò', 'õ', 'ỏ', 'ô', 'ố', 'ồ', 'ỗ', 'ổ', 'ơ', 'ớ', 'ờ', 'ỡ', 'ở', 'p', 'q', 'r', 's', 't', 'u', 'ú', 'ù', 'ũ', 'ủ', 'ư', 'ứ', 'ừ', 'ữ', 'ử', 'v', 'x', 'y', 'ý', 'ỳ', 'ỹ', 'ỷ']

url = 'https://vtudien.com/dstu'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}
data = {
    'tu': 'a',
    'src': 'viet',
    'tgt': 'viet',
    'tudien': 'dictionary'
}
n=0
previous_target = None  # Store the previous target value
with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Index', 'Target', 'Response'])
    while url:
        response = requests.post(url, headers=headers, data=data)
        response = response.text
        response = response.split("||")
        target = response[-1]  # Use list indexing instead of len() function
        if target == previous_target:  # Check if current target is same as previous target
            target = vietnamese_letters[n]  # Update the target value
            n+=1 
        # Write the index and target to the CSV file
        writer.writerow([n, target, response])  
        # Print the response body
        print(target)
        data = {
            'tu': target,
            'src': 'viet',
            'tgt': 'viet',
            'tudien': 'dictionary'
        }
        previous_target = target  # Update the previous target value