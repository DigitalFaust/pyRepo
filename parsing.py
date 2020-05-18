from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen("https://codeby.net/")
html = req.read()

soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('div', class_='porta-article-item')

results = []

for i in news:
    author = i.find('a', class_='u-concealed').get_text(strip=True)
    title = i.find('a').get_text(strip=True)
    content = i.find('div', class_='bbWrapper').get_text(strip=True)
    results.append({
        'author': author,
        'title': title,
        'content': content,
        })

f = open("practice_asm.txt", 'w', encoding='utf-8')
count = 1
for i in results:
    f.write(f'Comments # {count}\n\nAuthor: {i["author"]}\n\nTitle: {i["title"]}\n\nContent: {i["content"]}\n\n********************\n\n')
    count += 1
f.close()
