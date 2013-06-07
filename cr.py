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
#     print "%s added to directory list" % previous_directory_url

# print"directorly list successfully loaded."

def inner_page_url(directory_url):
    raw_html = urlopen(directory_url).read()
    # <a class="permalink" rel="bookmark" href="http://unmatchedstyle.com/gallery/magician-slider.php">Magician Slider</a>
    url_pattern = re.compile(r'''<a class="permalink" rel="bookmark" href="(http://unmatchedstyle.com/gallery/.+\.php)"''')
    inner_url_list = url_pattern.findall(raw_html)

#     for i in inner_url_list:
#         print i

# inner_page_url("http://unmatchedstyle.com/gallery")  

# def imgdown(url):

#     out_folder = re.findall(r'\d+-(.+)', url)[0].strip()

#     if not os.path.exists(out_folder):
#         os.makedirs(out_folder)

#     raw = urlopen(url).read()

#     all_img_url = re.findall(r'''src="/(.+?)" style''', raw)
#     for img_url in all_img_url:
#         real_img_url = "http://models.sight-management.com/" + img_url.strip()
#         img_name = img_url.strip()[20:-11]
#         outpath = os.path.join(out_folder, img_name)
#         try:
#             urlretrieve(real_img_url, outpath)
#         except:
#             continue

# raw = urlopen(url).read()
# all_model_url = re.findall(r"href='/models/(.+?)'", raw)

# for model_url in all_model_url:
#     real_model_url = "http://models.sight-management.com/models/" + model_url.strip()
#     print "downloading images from %s" % real_model_url
#     try:
#         imgdown(real_model_url)
#     except:
#         continue