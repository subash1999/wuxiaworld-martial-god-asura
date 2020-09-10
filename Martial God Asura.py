from lxml import html
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time
import random
import os
os.chdir(os.path.dirname(__file__))


chap_start = 3765
chap_end = 4405

file_name = "Martial God Asura [Chapter "+str(chap_start)+" - Chapter "+str(chap_end)+"].html"
style = "<style>@media print {  section {    page-break-before: always;  } } </style>"
style = ""
html_begin= "<html><head><title>Martial God Asura : chap_"+str(chap_start)+" to chap_"+str(chap_end)+"</title>"+style+"</head><body>"
html_end = "</body></html>"
all_chapters_html = ""
bookmarks = "<h1>Table Of Contents</h1>"

with open(file_name, "w", encoding="utf-8") as f:
        f.write("")

for x in range(chap_start,chap_end+1):
    # sleep to avoid ddos attack detection    
    # sleep_sec = random.randint(7,22)    
    # print("Current Sleep Time : ",sleep_sec)
    # time.sleep(sleep_sec)

    chap_no = str(x)
    section_start = '<section id="chapter_'+chap_no+'" name="chapter_'+chap_no+'">'
    section_end = "</section>"

    req = Request('https://www.wuxiaworld.com/novel/martial-god-asura/mga-chapter-'+chap_no+'/',headers={'User-Agent' : 'Mozila/5.0'})

    page = urlopen(req).read()

    soup = BeautifulSoup(page, 'html.parser')    

    title_text = soup.find('div',id="chapter-outer").find('div',class_="caption clearfix").find('h4').get_text().strip()

    
    
    title = '<h1 style="text-align:center;"> Chapter: '+chap_no+'</h1>'
    title = title+'\n<div style="text-align:center;font-size: 140%;font-weight: bold;">'+title_text+'</div>'

    bookmarks = bookmarks + '<a href="#chapter_'+chap_no+'">'+title_text+'</a><br>'


    content = soup.find('div', id="chapter-content",class_="fr-view")
    val = ""
    for div in content.find_all("p"): 
        val = val+str(div)
        
    total_chapter = title + str(val)

    # all_chapters_html = all_chapters_html + "\n<br><br><br><hr><hr><hr><hr>" + section_start + total_chapter + section_end

    all_chapters_html =  section_start + total_chapter +"<br><hr><hr>"+ section_end

    with open(file_name, "a", encoding="utf-8") as f:
        f.write(all_chapters_html)
    
    print("Chapter "+chap_no+" Done")

all_info = ""
with open(file_name, "r", encoding="utf-8") as f:
    all_info = f.read()
with open(file_name, "w+", encoding="utf-8") as f:
    f.write(html_begin + bookmarks+"<hr><hr>"+all_info + html_end )
