# Spider usage examples:
import re

from net import Spider

# create a Spider object for specified url
url = "https://www.python.org/"
url = "https://www.qq.com"
spider = Spider(url)
print(spider.text)
# print(str(bytes(spider.text, "utf-8"), encoding="gbk"))
exit()

# get the web-page content
spider = spider.get()

# s = spider.find_tables()
# print(s)
#
# exit()

# You can user find_xxx() to find information in the web page


# tables = Spider("https://www.w3school.com.cn/tags/tag_table.asp").find_tables(text_only=True)
# print(tables)


# find_form
words = Spider("http://www.baidu.com").find_forms()
print('form', words)
exit()

# find the links in the page
link_urls = spider.find_links('Latest News')
print('links:', link_urls)


# find the links whose url contains "blog."
link_urls = spider.find_links('Latest News', contains="blog.")
print('links:', link_urls)


# find the urls of the images in the page
img_urls = spider.find_images()
print('images:', img_urls)

if len(img_urls) > 0:
    # create a new spider to download the first image url, save image to filename 'pic.xxx'
    # (file extension will be added automatically)
    filename = Spider(url, img_urls[0]).download("pic")

    # open image file using PIL
    # from PIL import Image
    # Image.open(filename).show()

print("-----------------------------------")

# find the codes in the page
codes = spider.find_codes()
if codes:
    print('code:\n', codes[0])

print("-----------------------------------")

# find the list items after 'Latest News'
words = spider.find_list_items('Latest News')
print('Latest News:', words)

# find the text of the paragraph after 'Download'
text = spider.find_paragraph('Download')
print('Download paragraph: ', text)

# Advanced find example
#
# understanding the structure of webpage's HTML source code, find words in the HTML

# example: find the text of menu items
begin = ['<ul', 'menu']      # find '<ul' tag and 'menu' class as the beginning
end = ['</ul>']              # find '</ul>' tag as the ending
# word is the menu item text
before = ['<li', '<a', '>']  # find '<li' and '<a' and '>' which is before the word
after = ['</a>']             # find '</a>' which is after the word
words = spider.find_list(before, after, begin, end)
print("menus:", words)   # ['Python', 'PSF', 'Docs', 'PyPI', 'Jobs', 'Community']

# find the text of menu items and its links
# word1 is the link
before1 = ['<li', '<a', 'href="']  # find '<li' and '<a' and 'href="' which is before the word1
after1 = ['"']     # find '"' which is after the word1

# word2 is the menu text
before2 = ['>']  # find '>' which is before the word2, after word1
after2 = ['</a>']  # find '</a>' which is after the word2

# compose a list definition, each item of the list is a word define (before, after)
betweens = [(before1, after1), (before2, after2)]

# perform finding
words_list = spider.find_words_list(betweens, begin, end)
print("menus2:", words_list)  # words_list will be a list, each item is a list of two words
# the result is  [['/', 'Python'], ['/psf-landing/', 'PSF'], ...
