import os
import re
import subprocess

with open("url_database.html", "r") as file:
    html_content = file.read()

url_pattern = re.compile(r'href="(.*?\.gif)"')

gif_urls = url_pattern.findall(html_content)

if not os.path.exists("contents"):
    os.makedirs("contents") 

for url in gif_urls:
    file_name = os.path.join("contents", os.path.basename(url))
    subprocess.run(["wget", url, "-O", file_name])
