from urllib2 import urlopen
from urllib import urlretrieve
import os
import re
import socket

timeout = 10
socket.setdefaulttimeout(timeout)

directory_list = ['http://unmatchedstyle.com/gallery/']

for i in range(2, 11):
    previous_directory_url = "http://unmatchedstyle.com/gallery/page/" + str(i)
    directory_list.append(previous_directory_url)

def inner_page_url(directory_url):
    raw_html = urlopen(directory_url).read()
    # <a class="permalink" rel="bookmark" href="http://unmatchedstyle.com/gallery/magician-slider.php">Magician Slider</a>
    url_pattern = re.compile(r'''<a class="permalink" rel="bookmark" href="(http://unmatchedstyle.com/gallery/.+\.php)"''')
    inner_url_list = url_pattern.findall(raw_html)

    return inner_url_list

def get_info(url):
    url = url.strip()
    # url: http://unmatchedstyle.com/gallery/magician-slider.php
    out_folder = re.findall(r'com/gallery/(.+)\.php$', url)[0].strip()
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)

    raw_html = urlopen(url).read()

    # <h2 class="post-title">Magician Slider</h2> and <img src="http://unmatchedstyle.com/wp-content/uploads/2013/05/magicianslider.jpg" alt="" />

    extraction_pattern = re.compile(r'''<h2 class="post-title">(.+)</h2>.*?<li class="visit"><a href="(.+)">Visit Site</a></li>.*?<img src="(http://unmatchedstyle.com/wp-content/uploads/\d{4}/\d{2}/.+?\.(jpg|png))" alt="" />''', re.DOTALL)
    extracted_info = extraction_pattern.search(raw_html)

    try:
        site_title = extracted_info.group(1)
    except:
        site_title = "Error"

    try:
        site_url = extracted_info.group(2)
    except:
        site_url = url

    try:
        img_url = extracted_info.group(3)
    except:
        img_url = "http://unmatchedstyle.com/wp-content/uploads/2013/04/Converge-smallgraphic.jpg"

    txt_filename = "info.txt"
    with open(os.path.join(out_folder, txt_filename), 'w') as txt_file:
        txt_file.write(site_title+"\n"+site_url+"\n"+img_url)
        txt_file.close()

    img_name = img_url.strip()[53:]
    outpath = os.path.join(out_folder, img_name)
    urlretrieve(img_url, outpath)

counter = 0
for i in directory_list:
    for j in inner_page_url(i):
        counter += 1
        print "No.%s downloading %s" % (counter, j)
        get_info(j)

