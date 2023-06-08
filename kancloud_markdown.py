import requests
from bs4 import BeautifulSoup
import os
import re
import urllib.parse
import shutil

# 请求目录页面
url = "https://www.kancloud.cn/maliming/leetcode/content"
response = requests.get(url)

# 解析HTML
soup = BeautifulSoup(response.text, 'html.parser')

# 找到目录元素
catalog = soup.find('div', {'class': 'catalog'})

# 提取所有文章的ID
article_ids = [a['href'] for a in catalog.find_all('a')]

# 确保asset文件夹存在
if not os.path.exists('asset'):
    os.makedirs('asset')

# 遍历所有文章
for article_id in article_ids:
    # 请求文章页面
    article_url = f"https://www.kancloud.cn/maliming/leetcode/{article_id}"
    article_response = requests.get(article_url)

    # 解析HTML
    article_soup = BeautifulSoup(article_response.text, 'html.parser')

    # 找到文章标题和内容
    title = article_soup.find('title').text
    content = article_soup.find('div', {'class': 'content'}).text

    # 找到所有的图片链接
    img_urls = re.findall(r'!\[.*?\]\((.*?)\)', content)

    # 下载图片并替换链接
    for img_url in img_urls:
        # 下载图片
        img_response = requests.get(img_url, stream=True)
        img_response.raise_for_status()

        # 保存图片到本地
        img_name = os.path.basename(urllib.parse.urlparse(img_url).path)
        img_path = os.path.join('asset', img_name)
        with open(img_path, 'wb') as f:
            img_response.raw.decode_content = True
            shutil.copyfileobj(img_response.raw, f)

        # 替换链接
        content = content.replace(img_url, img_path)

    # 将文章标题和内容保存为Markdown文件
    with open(f"{title}.md", 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n{content}")
