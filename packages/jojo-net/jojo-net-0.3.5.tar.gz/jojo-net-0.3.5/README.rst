net module 0.3.2 documentation

Author: JoStudio, Date: 2022/9/1

net Module
======================

This net package provides tools to perform net ping, scan port, send email, http, web spider,
access web API.







net.mail submodule
-----------------------------------------------



e-mail sender



::

    # Send e-mail example



    from net import Mail



    # Set parameters

    username = 'xxxxxxx@host.com'  # username to login SMTP server

    password = 'xxxxxxxxxx'      # password to login SMTP server

    receiver = 'xxxxxxxx@host.com'  # receiver e-mail address



    mail = Mail(username, password)  # Create mail object



    # Send mail with attachment file '1.jpg'

    mail.send([receiver], 'My Subject', "This is body", ['1.jpg'])









net.scan submodule
-----------------------------------------------



Network ping and scan functions

::

    # Net ping and scan examples



    from net import Net



    # ping a server(or an IP)

    t = Net.ping("www.bing.com")  # return milliseconds, return -1 means not available

    print('milliseconds', t)



    # get IP address of this computer

    my_ip = Net.local_ip()



    # create an IP range (a list of IP address

    ip_list = Net.ip_range(my_ip, 1, 100)

    print(ip_list)



    # Scan the IPs, return list of pingable IPs

    exists_ips = Net.ip_scan(ip_list)

    print(exists_ips)



    # whether a port of specified IP is opened

    if Net.is_port_open(my_ip, 80):

        print('port 80 of', my_ip, 'opened')

    else:

        print('port 80 of', my_ip, 'not opened')





    # scan a list of port on specified IP address, return opened port list

    port_list = Net.port_scan(my_ip, [80, 8080, 21, 22, 443, 445])

    print('opened ports', port_list)







net.spider submodule
-----------------------------------------------

Spider, get web page, extract word from the content, download file.



::

    # Spider usage examples:



    from net import Spider





    # create a Spider object for specified url

    url = "https://www.python.org/"

    spider = Spider(url)





    # You can user Spider.find_xxx() to find information in the web page



    # find all links in the page

    link_urls = spider.find_links()

    print('links:', link_urls)



    # find the links after 'Latest News'

    link_urls = spider.find_links('Latest News')

    print('links:', link_urls)





    # find the links 'Latest News' and the link's url contains "blog."

    link_urls = spider.find_links('Latest News', contains="blog.")

    print('links:', link_urls)





    # find the urls of the images in the page

    img_urls = spider.find_images()

    print('images:', img_urls)



    if len(img_urls) > 0:

        # create a new spider to download the first image url, save image to filename 'pic.xxx'

        # (file extension will be added automatically)

        filename = Spider(url, img_urls[0]).download("pic")

        print('file %s downloaded' % repr(filename))



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



    tables = Spider("https://www.w3school.com.cn/tags/tag_table.asp").find_tables(text_only=True)

    if len(tables) > 0:

        print('table 0:', tables[0].to_list())





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














