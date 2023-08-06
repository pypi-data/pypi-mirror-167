#
# Spider, get web page, extract word from the content, download file.
#
# ::
#     # Spider usage examples:
#
#     from net import Spider
#
#
#     # create a Spider object for specified url
#     url = "https://www.python.org/"
#     spider = Spider(url)
#
#
#     # You can user Spider.find_xxx() to find information in the web page
#
#     # find all links in the page
#     link_urls = spider.find_links()
#     print('links:', link_urls)
#
#     # find the links after 'Latest News'
#     link_urls = spider.find_links('Latest News')
#     print('links:', link_urls)
#
#
#     # find the links 'Latest News' and the link's url contains "blog."
#     link_urls = spider.find_links('Latest News', contains="blog.")
#     print('links:', link_urls)
#
#
#     # find the urls of the images in the page
#     img_urls = spider.find_images()
#     print('images:', img_urls)
#
#     if len(img_urls) > 0:
#         # create a new spider to download the first image url, save image to filename 'pic.xxx'
#         # (file extension will be added automatically)
#         filename = Spider(url, img_urls[0]).download("pic")
#         print('file %s downloaded' % repr(filename))
#
#     print("-----------------------------------")
#
#     # find the codes in the page
#     codes = spider.find_codes()
#     if codes:
#         print('code:\n', codes[0])
#
#     print("-----------------------------------")
#
#     # find the list items after 'Latest News'
#     words = spider.find_list_items('Latest News')
#     print('Latest News:', words)
#
#     # find the text of the paragraph after 'Download'
#     text = spider.find_paragraph('Download')
#     print('Download paragraph: ', text)
#
#     tables = Spider("https://www.w3school.com.cn/tags/tag_table.asp").find_tables(text_only=True)
#     if len(tables) > 0:
#         print('table 0:', tables[0].to_list())
#
#
#     # Advanced find example
#     #
#     # understanding the structure of webpage's HTML source code, find words in the HTML
#
#     # example: find the text of menu items
#     begin = ['<ul', 'menu']      # find '<ul' tag and 'menu' class as the beginning
#     end = ['</ul>']              # find '</ul>' tag as the ending
#     # word is the menu item text
#     before = ['<li', '<a', '>']  # find '<li' and '<a' and '>' which is before the word
#     after = ['</a>']             # find '</a>' which is after the word
#     words = spider.find_list(before, after, begin, end)
#     print("menus:", words)   # ['Python', 'PSF', 'Docs', 'PyPI', 'Jobs', 'Community']
#
#     # find the text of menu items and its links
#     # word1 is the link
#     before1 = ['<li', '<a', 'href="']  # find '<li' and '<a' and 'href="' which is before the word1
#     after1 = ['"']     # find '"' which is after the word1
#
#     # word2 is the menu text
#     before2 = ['>']  # find '>' which is before the word2, after word1
#     after2 = ['</a>']  # find '</a>' which is after the word2
#
#     # compose a list definition, each item of the list is a word define (before, after)
#     betweens = [(before1, after1), (before2, after2)]
#
#     # perform finding
#     words_list = spider.find_words_list(betweens, begin, end)
#     print("menus2:", words_list)  # words_list will be a list, each item is a list of two words
#     # the result is  [['/', 'Python'], ['/psf-landing/', 'PSF'], ...
#
#
#
#


from html.parser import HTMLParser
import re
import json
import os

from .util import StrUtil
from .http import Http, Url, UserAgent


# A class to parse HTML to text
class DeHTMLParser(HTMLParser):
    """
    A class to parse HTML to text

    """
    def __init__(self, **kwargs):
        HTMLParser.__init__(self)
        self._text = []
        self._last_tag = None
        self.tag = kwargs.get('tag', None)
        self.tag_attrs = {}
        self.line_break = kwargs.get('line_break', False)

    def handle_data(self, data):
        if self._last_tag == "script":
            return

        text = data.strip()
        if len(text) > 0:
            if self.line_break:
                text = re.sub('[ \t]+', ' ', text)
            else:
                text = re.sub('[ \t\r\n]+', ' ', text)
            self._text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        # print(tag, attrs)
        self._last_tag = tag
        if self.tag and tag == self.tag:
            for attr in attrs:
                self.tag_attrs[attr[0]] = attr[1]
        if tag == 'p':
            self._text.append('\n\n')
        elif tag == 'br':
            self._text.append('\n')
        elif tag == 'script':
            pass

    def handle_startendtag(self, tag, attrs):
        self._last_tag = None
        # if tag == 'br':
        #     self.__text.append('\n\n')

    def text(self):
        if self.line_break:
            s = '\n'
        else:
            s = ''
        return s.join(self._text).strip()


# A class to parse HTML form
class HtmlForm(HTMLParser):
    """
    A class to parse HTML to text

    """

    class Input(dict):
        def __init__(self, attrs):
            for attr in attrs:
                self[attr[0]] = attr[1]

    def __init__(self, html_text, **kwargs):
        HTMLParser.__init__(self)
        self.attrs = {}
        self.inputs = []
        if html_text:
            self.feed(html_text)

    def handle_data(self, data):
        pass
        # if self._last_tag == "script":
        #     return
        #
        # text = data.strip()
        # if len(text) > 0:
        #     if self.line_break:
        #         text = re.sub('[ \t]+', ' ', text)
        #     else:
        #         text = re.sub('[ \t\r\n]+', ' ', text)
        #     self._text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        # print(tag, attrs)
        if tag == 'input':
            self.inputs.append(HtmlForm.Input(attrs))

    def handle_startendtag(self, tag, attrs):
        pass

    def text(self):
        if self.line_break:
            s = '\n'
        else:
            s = ''
        return s.join(self._text).strip()


# convert html to text
def html2text(html, convert=True, line_break=False):
    """
    Convert html to text.

    :Chinese: 将HTML转化为纯文本

    :param html:   HTML string
    :param convert: (optinal) whether convert to pure text
    :param line_break: (optinal) whether keep line breaks
    :return: str
    """
    if not convert:
        return html
    if html is None:
        return None
    # noinspection PyBroadException
    try:
        parser = DeHTMLParser(line_break=line_break)
        parser.feed(html)
        parser.close()
        return parser.text()
    except Exception:
        return html


class Link(list):
    def __init__(self, url, text):
        self.append(url)
        self.append(text)

    @property
    def url(self):
        return self[0] if len(self) > 0 else None

    @property
    def text(self):
        return self[1] if len(self) >= 1 else None


class Table(list):
    class Row(list):
        pass

    class Cell:
        def __init__(self, text, urls=None):
            self.text = text
            self.urls = urls or []
            self.attrs = {}

        def __repr__(self):
            return '<Cell %s>' % repr(self.text)

    def _regulate(self):
        # TODO: process span row, span col
        pass

    def to_list(self):
        self._regulate()
        result = []
        for row in self:
            r = []
            for cell in row:
                r.append(cell.text)
            result.append(r)
        return result

    def __repr__(self):
        result = '[\n'
        count = 0
        for row in self:
            if count > 0:
                result += ',\n'
            if len(row) > 0:
                result += '    ' + str(row)
                count += 1
        result += '\n]'
        return result


# net spider
class Spider:
    """
    Net Spider, get web page, extract word from the content.

    :Chinese: 网络爬虫类, 抓取网页，分析提取其中的数据

    Usage：

    # create a Spider object for url

    w = Spider("https://www.python.org/")

    # find links

    links = w.find(Spider.LINKS)

    """

    BING = "https://cn.bing.com/search?q={0}"
    BAIDU = "https://www.baidu.com/s?wd={0}"

    def __init__(self, url: str = None, sub_url: str = None):
        self.pure_text = True  # whether return pure text
        self._user_agent = UserAgent.chrome
        self._url = Url.join(url, sub_url)
        self._page = None

        if url is None:
            self._url = Spider.BING

    def user_agent(self, keyword):
        keyword = str(keyword).strip().lower()
        if keyword == 'android':
            self._user_agent = UserAgent.android
        elif keyword == 'ios':
            self._user_agent = UserAgent.ios
        elif keyword == 'iphone':
            self._user_agent = UserAgent.ios
        elif keyword == 'chrome':
            self._user_agent = UserAgent.chrome
        elif keyword == 'ie':
            self._user_agent = UserAgent.ie
        else:
            raise ValueError("unknown UserAgent keyword %s" % repr(keyword))
        return self

    def search(self, word=None):
        """ search a word """
        self._page = Http.get(self._url, word).text
        return self

    def download(self, filename):
        """ download and save to file """
        return Http.get(self._url, '').save_to_file(filename)

    # noinspection PyMethodMayBeStatic
    def _stop_chars(self):
        """ return stop chars """
        chars = [
            '，',
            '；',
            '。',
            '</div',
            '</td',
            '</li',
            '</h',
            '</p',
            ',',
        ]
        return tuple(chars)

    def _ensure_page(self):
        """ ensure self._page has content """
        if self._url and not self._page:
            self._page = Http.get(self._url).text

    def find(self, before, after=None, begin=None, end=None):
        """
        find information on the web page

        :param before: texts which is before the finding text.  could be a string or a list of string.
        :param after: (optional) texts which is after the finding text, could be a string or a list of string
        :param begin: (optional) texts from where to begin the finding, could be a string or a list of string or an offset int
        :param end: (optional) texts from where to end the finding, could be a string or a list of string or an offset int
        :return:  return string
        """
        self._ensure_page()

        if not self._page:
            return None

        if after is None:
            after = self._stop_chars()

        start = 0
        if begin:
            start, _ = StrUtil.match_offset_length(self._page, begin)
        if start < 0:
            return None

        s = StrUtil.get_word(self._page, before, after, start)
        return html2text(s, self.pure_text)

    def find_pairs(self, begin, pair='{}'):
        self._ensure_page()

        if not self._page:
            return None

        s = StrUtil.find_pair(self._page, begin, pair=pair)
        return s

    def find_links(self, begin=None, end=None, contains=None, regex=False):
        """
        find links in the webpage. A link is a tag like '<a href="url">text</a>' in HTML.

        :param begin: (optional) texts from where to begin the finding, could be a string or a list of string or an offset int
        :param end: (optional) texts from where to end the finding, could be a string or a list of string or an offset int
        :param contains: (optional) the substring that the link's url should contains
        :param regex: (optional) whether contains is a regex pattern
        :return: return a list, each item of the list is a tuple of (url, text) of a link.
        """
        self._ensure_page()
        before1 = ['<a', 'href="']
        after1 = '"'
        before2 = '>'
        after2 = '</a'
        betweens = [(before1, after1), (before2, after2)]
        words = self.find_words_list(betweens, begin, end)

        # convert to list of Link
        links = []
        for item in words:
            links.append(Link(item[0], item[1]))

        # filter the links
        if contains:
            result = []
            for u in links:
                if regex:
                    if re.search(contains, u[0]) is not None:
                        result.append(u)
                elif u[0].find(contains) >= 0:
                    result.append(u)
            return result
        else:
            return links

    def find_images(self, begin=None, end=None, contains=None, regex=False):
        """
        find images in the webpage. An image is a tag like '<img src="url">' in HTML.

        :param begin: (optional) texts from where to begin the finding, could be a string or a list of string or an offset int
        :param end: (optional) texts from where to end the finding, could be a string or a list of string or an offset int
        :param contains: (optional) the substring that the image's url should contains
        :param regex: (optional) whether contains is a regex pattern
        :return: return a list, each item of the list is url of image.
        """
        before = ['<img', 'src="']
        after = '"'
        betweens = [[before, after]]
        urls = self.find_words_list(betweens, begin, end)

        # filter the links
        if contains:
            result = []
            for url in urls:
                if regex:
                    if re.search(contains, url) is not None:
                        result.append(url)
                elif url.find(contains) >= 0:
                    result.append(url)
            return result
        else:
            return urls

    def find_codes(self, begin=None, end=None):
        """
        find codes in the webpage. code is the text between '<code>' and '</code>' in HTML

        :param begin: (optional) texts from where to begin the finding, could be a string or a list of string or an offset int
        :param end: (optional) texts from where to end the finding, could be a string or a list of string or an offset int
        :return: return a list, each item of the list is a piece of code.
        """
        before = ['<code', '>']
        after = ['</code', '>']
        betweens = [[before, after]]
        return self.find_words_list(betweens, begin, end, line_break=True)

    def find_paragraph(self, begin=None, end=None):
        """
        find paragraph text in the webpage. A paragraph is a tag like '<p>text</p>' in HTML.

        :param begin: (optional) texts from where to begin the finding, could be a string or a list of string or an offset int
        :param end: (optional) texts from where to end the finding, could be a string or a list of string or an offset int
        :return: return a list, each item of the list is a paragraph text.
        """
        before = '<p>'
        after = '</p'

        # convert begin to start
        start = 0
        if begin:
            start, _ = StrUtil.match_offset_length(self._page, begin)
        if start < 0:
            return None
        s = StrUtil.get_word(self._page, before, after, start)

        return html2text(s, self.pure_text)

    def find_forms(self, begin=None, end=None):
        self._ensure_page()
        text = self._page

        forms = self._get_texts(text, '<form', '</form', begin, end)

        result = []
        for form in forms:
            result.append(HtmlForm(form))
        return result

    def set_text(self, text):
        """ set text of the web page """
        self._page = text
        return self

    def _get_texts(self, page, before, after, begin=None, end=None, append_char='>'):
        """ get text from page """
        result = []
        s, offset = StrUtil.get_word(page, before, after, begin, return_offset=True)
        while s is not None:
            if append_char is not None:
                result.append(before + s + after + append_char)
            else:
                result.append(s)
            s, offset = StrUtil.get_word(page, before, after, offset, return_offset=True)
        return result

    def find_tables(self, begin=None, end=None, text_only=False):
        """
        find paragraph text in the webpage. A paragraph is a tag like '<p>text</p>' in HTML.

        :param begin: (optional) texts from where to begin the finding, could be a string or a list of string or an offset int
        :param end: (optional) texts from where to end the finding, could be a string or a list of string or an offset int
        :return: return a list, each item of the list is table.
            A table is a list, each item is a row. A row is a list each item is a cell.
            A cell is a tuple, first element is cell text, second element is the links in the cell.
            A link is a
        """
        self._ensure_page()
        result = []
        # find tables in '<table> ... </table>'
        tables = self._get_texts(self._page, '<table', '</table', begin, end)
        for table in tables:
            table_obj = Table()
            # find row in '<tr> ... </tr>'
            rows = self._get_texts(table, '<tr', '</tr')
            for row in rows:
                row_obj = Table.Row()
                # find cell in '<td> .. </td>'
                if row.find('<th') >= 0:
                    cells = self._get_texts(row, '<th', '</th')
                else:
                    cells = self._get_texts(row, '<td', '</td')
                # for each cell
                for cell in cells:
                    # get urls in the <td>
                    urls = []
                    if cell.find('<a') >= 0:
                        urls = Spider().set_text(cell).find_links()
                    # get cell text
                    parser = DeHTMLParser(tag='td', line_break=True)
                    parser.feed(cell)
                    cell_text = parser.text()
                    if text_only:
                        cell_obj = Table.Cell(cell_text)
                    else:
                        cell_obj = Table.Cell(cell_text, urls)
                    cell_obj.attrs = parser.tag_attrs
                    # append cell to the row
                    row_obj.append(cell_obj)
                # append row to the table
                table_obj.append(row_obj)
            # append table to tables
            result.append(table_obj)
        return result

    @staticmethod
    def _get_begin_condition(b, prefix):
        # convert word to list
        if prefix and (not isinstance(prefix, list) and not isinstance(prefix, tuple)):
            prefix = [str(prefix)]
        if not prefix:
            prefix = []

        # join word, begin
        if isinstance(b, list) or isinstance(b, tuple):
            b = list(prefix) + list(b)
        elif isinstance(b, str):
            b = list(prefix).append(b)
        elif b is None:
            b = list(prefix)
        else:
            b = list(prefix).append(str(b))

        return b

    def find_list_items(self, begin=None, is_ol=False):
        """
        find list items in the webpage. list items are within '<ul> <li></li> </ul>' in HTML

        :param begin: (optional) texts from where to begin the finding, could be a string or a list of string or an offset int
        :param end: (optional) texts from where to end the finding, could be a string or a list of string or an offset int
        :param is_ol: (optional) whether the list is order list which tag is '<ol>'
        :return: return a list, each item is an item which is a list of [url, text]
        """
        self._ensure_page()
        tag_begin = ['<ul'] if not is_ol else ['<ol']
        end = ['</ul'] if not is_ol else ['</ol']
        begin = self._get_begin_condition(tag_begin, begin)
        # word1 is the link url
        before1 = ['<li', '<a', 'href="']
        after1 = '"'
        # word1 is the text
        before2 = '>'
        after2 = '</a'
        betweens = [(before1, after1), (before2, after2)]
        words_list = self.find_words_list(betweens, begin, end)
        if not words_list:
            betweens = [(['<li', '>'], '</li>')]
            words_list = self.find_words_list(betweens, begin, end)
        return words_list

    def find_text(self, before, after=None, begin=None):
        """
        find words

        :param before: texts which is before the finding text.  could be a string or a list of string.
        :param after: (optional) texts which is after the finding text, could be a string or a list of string
        :param begin: (optional) texts from where to begin the finding, could be a string or a list of string or an offset int
        :return:  return string
        """
        self._ensure_page()

        if not self._page:
            return None

        if after is None:
            after = self._stop_chars()

        text = html2text(self._page)
        # print(text)

        start = 0
        if begin:
            start, _ = StrUtil.match_offset_length(text, begin)
        if start < 0:
            return None

        s = StrUtil.get_word(text, before, after, start)
        return html2text(s, self.pure_text)

    def find_list(self, before, after=None, begin=None, end=None):
        """
        find a list of word

        :param before: texts which is before the finding text.  could be a string or a list of string.
        :param after: (optional) texts which is after the finding text, could be a string or a list of string
        :param begin: (optional) texts from where to begin the finding, could be a string or a list of string or an offset int
        :param end: (optional) texts from where to end the finding, could be a string or a list of string or an offset int
        :return:  return string
        """
        self._ensure_page()

        if after is None:
            after = self._stop_chars()

        if self._page:
            betweens = [(before, after)]
            words = StrUtil.get_word_list(self._page, begin, betweens, end=end)
            ret = []
            for item in words:
                ret.append(html2text(item, self.pure_text))
            return ret

    def find_words_list(self, betweens, begin=None, end=None, line_break=False):
        """
        Find a list of words, each item of list may have serveral words.

        :Chinese: 查找一个列表, 每一个列表项有多个词.

        :param betweens:  betweens list, each item is a tuple of (before, after)
        :param begin: (optional) texts from where to begin the finding, could be a string or a list of string or an offset int
        :param end: (optional) texts from where to end the finding, could be a string or a list of string or an offset int
        :param line_break:  (optional) whether keep line breaks
        :return: return a list
        """
        self._ensure_page()

        if not isinstance(betweens, list) and not isinstance(betweens, tuple):
            raise ValueError("betweens must be a list")
        else:
            for item in betweens:
                if not (isinstance(item, list) or isinstance(item, tuple)) or len(item) != 2:
                    msg = "item of betweens must be a list of two elements: before, after"
                    raise ValueError(msg)

        if self._page:
            words = StrUtil.get_word_list(self._page, begin, betweens, end=end)
            if self.pure_text:
                for index, item in enumerate(words):
                    if isinstance(item, tuple):
                        item = list(item)
                        words[index] = item
                    if isinstance(item, list):
                        for i in range(0, len(item)):
                            item[i] = html2text(item[i], line_break=line_break)
                    elif isinstance(item, str):
                        words[index] = html2text(item, line_break=line_break)

            return words

    @property
    def html(self):
        self._ensure_page()
        return self._page

    @property
    def text(self):
        self._ensure_page()
        return html2text(self._page)


# BaiDu Chinese Wiki 百度百科
class BaiKe(Spider):
    """
    百度百科
    ===========
    使用方法示例：

    # 创建对象, 百科条目是: 爱在深秋，
    # (可选)辅助注释是：谭咏麟
    b = BaiKe("爱在深秋", "谭咏麟")

    # 打印内容目录
    print( b.catalog )

    # 如果目录中有歌词, 打印歌词内容
    if '歌词' in b:
        print(b['歌词'])

    """

    def __init__(self, word=None, finding=None):
        self.base_url = "https://baike.baidu.com"
        super().__init__(self.base_url + "/item/{0}")
        self._explain = None  # 解释
        self._catalog = []  # 百科的目录
        self._synonyms = []  # 同义词数据

        if word:
            self.load(word, finding)

    @property
    def explain(self):
        """ 解释文字 """
        return self._explain

    @property
    def catalog(self):
        """ 目录列表 """
        return self._catalog

    def _get_explain(self):
        if self._page:
            self._explain = StrUtil.get_word(self._page, ['<meta', '"description"', 'content="'], ['">'])
            self._load_catalog()

    def _load_synonyms(self):
        if self._page:
            betweens = [
                (['<li', '<a', "href='"], "'>"),
                (None, '</a')
            ]
            others_list = StrUtil.get_word_list(self._page, 'polysemantList-wrapper', betweens)
            if len(others_list) == 0:
                betweens = [(['<li', '<a', 'href="'], '"'), ('>', '</a')]
                others_list = StrUtil.get_word_list(self._page, 'custom_dot', betweens)
            for item in others_list:
                if isinstance(item, list) and len(item) == 2:
                    self._synonyms.append([item[1], self.base_url + item[0]])

    def _load_url(self, url):
        self._page = Http.get(url)
        self._get_explain()

    def _load_catalog(self):
        if self._page:
            betweens = [
                (['<li', '<a', 'href=', '>'], '</a'),
            ]
            # begin = '<div class="catalog-list'
            begin = 'catalog-list'
            self._catalog = StrUtil.get_word_list(self._page, begin,
                                                  betweens, end='anchor-list')

    def _find_catalog(self, item):
        """ find a item in the catalog """
        if isinstance(item, tuple):
            for e in item:
                r = self._find_catalog(e)
                if r >= 0:
                    return r
            return -1
        else:
            for index, elem in enumerate(self._catalog):
                if elem == item:
                    return index
            for index, elem in enumerate(self._catalog):
                if StrUtil.match(elem, item):
                    return index
        return -1

    def load(self, word, finding=None):
        """
        读取一个词的百科

        :param word:  一个词
        :param finding: （可选)限定语，用于寻找同义词
        :return: 返回对象本身
        """
        self.search(word)
        self._get_explain()
        self._load_synonyms()

        if finding:
            self.find_others(finding)
        return self

    def find_others(self, finding):
        """ 寻找同义词,  如找到则返回对象本身, 如找不到返回None"""
        for item in self._synonyms:
            if StrUtil.match(item[0], finding):
                self._load_url(item[1])
                return self
        if len(self._synonyms) > 0 and self._page.find('custom_dot') > 0:
            item = self._synonyms[0]
            self._load_url(item[1])
            return self
        return None

    def count(self):
        """ 返回同义词的数量 """
        return len(self._synonyms)

    def others(self, index):
        """
        跳转到指定序号index的同义词。

        :param index:  序号index
        :return: 返回一个BaiKe对象，指向序号index的同义词
        """
        if 0 <= index < len(self._synonyms):
            item = self._synonyms[index]
            obj = BaiKe()
            obj._load_url(item[1])
            obj._synonyms = self._synonyms
            obj.word = item[0]
            return obj
        else:
            raise IndexError('index %s out of bound' % index)

    def __contains__(self, item):
        return self._find_catalog(item) >= 0

    def __getitem__(self, item):
        if item is None or item == '':
            index = 0
        else:
            index = self._find_catalog(item)

        if index < 0:
            raise StopIteration()

        paragraph = self._catalog[index]
        before = ['<div class="para-title', paragraph, '</div>']
        after = '<div class="anchor-list'
        start = 0
        text = StrUtil.get_word(self._page, before, after, start)

        # 如果找不到
        if len(html2text(text)) < 5:
            # 接下一个段落
            before.append(after)
            before.append('</div>')
            text = StrUtil.get_word(self._page, before, after, start)
        # 如果找到
        if text:
            text = text.replace("</div>", "</div><br>")
        return html2text(text, self.pure_text)


# BaiDu Chinese Wiki 百度知道
class ZhiDao(Spider):
    """
    百度知道
    =======
    使用方法示例：

    # 创建对象, 提出问题: 李白 出生地
    b = ZhiDao("李白 出生地")

    # 答案的数量
    b.count()

    # 打印第0条答案
    print( b.answer(0) )

    """

    def __init__(self, word):
        super().__init__("https://zhidao.baidu.com/search?word={0}")
        self._answers = []  # 答案, 每一个元素是一个tuple, 第一个元素是标题，第二个是url
        self.search(word)

    def answer(self, index=0):
        """
        返回答案文字

        :param index (可选)第几条答案
        """
        if 0 <= index < len(self._answers):
            item = self._answers[index]
            # title = item[0]
            page = Http.get(item[1])  # url = item[1]
            before = ['<div', 'answer', '>', 'content-container', '>']
            after = ['<div', 'quality-content']
            word = StrUtil.get_word(page, before, after)
            return html2text(word)

    def count(self):
        """ 返回答案的数量 """
        return len(self._answers)

    def search(self, word):
        """ 提出一个问题 """
        self._answers = []
        super().search(word)
        if self._page:
            begin = 0
            betweens = [
                (['<dt', 'result', '<a', 'href="'], '"'),
                (['>'], '</a'),
            ]
            words = StrUtil.get_word_list(self._page, begin, betweens)
            for item in words:
                if len(item) == 2:
                    self._answers.append((html2text(item[1]), item[0]))
        return self


# ImageData
class ImageData:
    """ ImageData"""

    def __init__(self, data):
        self.url = None  # 图片rul
        self.thumb_url = None  # 缩略图rul
        self.filename = None  # 文件扩展名
        self.file_ext = None  # 文件名
        self.ref_url = None  # 图片源头的网页url
        self.title = None  # 图片源头的网页标题
        self._load(data)

    # noinspection PyMethodMayBeStatic
    def valid_format(self, fmt):
        """ fmt 是否是有效的图片格式 """
        if fmt in ['.jpg', '.jpeg', '.gif', '.bmp', '.png', '.webp']:
            return True
        return False

    def valid(self):
        """ 图片是否有效 """
        if self.file_ext:
            return True
        return False

    def _set_format(self, fmt):
        if fmt:
            fmt = fmt.lower()
            fmt = ImageData._cut_char(fmt, '?')
            fmt = ImageData._cut_char(fmt, '!')
            # if fmt.find('?') >= 0:
            #     fmt = fmt[:fmt.find('?')]
            # if fmt.find('!') >= 0:
            #     fmt = fmt[:fmt.find('!')]
            # if fmt == '.jpeg':
            #     fmt = '.jpg'

            if self.valid_format(fmt):
                self.file_ext = fmt
            else:
                self.file_ext = None

    def _load(self, data):
        """ 从 data 中读入图片数据 """
        if isinstance(data, dict):
            if 'murl' in data:
                self.url = data['murl']
                self._set_format(ImageData.get_file_ext(self.url))
                self.filename = ImageData.get_file_name(self.url)
            if 'turl' in data:
                self.thumb_url = data['turl']
            if 't' in data:
                self.title = data['t']
            if 'purl' in data:
                self.ref_url = data['purl']

    @staticmethod
    def _cut_char(url, c):
        """ 切除 url 中 字符c 后面的部分 """
        if url.find(c) >= 0:
            url = url[:url.find(c)]
        return url

    @staticmethod
    def get_file_ext(url):
        """ 取得 url 中的文件扩展名 """
        url = ImageData._cut_char(url, '?')
        url = ImageData._cut_char(url, '!')

        pos = url.rfind('.')
        if pos >= 0:
            url = url[pos:]
            return url
        else:
            return ''

    @staticmethod
    def get_file_name(url):
        """ 取得 url 中的文件名 """
        url = ImageData._cut_char(url, '?')
        url = ImageData._cut_char(url, '!')

        pos = url.rfind('/')
        if pos >= 0:
            url = url[pos + 1:]

        return url

    def download(self, filename=None):
        """
        下载图片, 保存到文件.

        :param filename: (可选)存盘文件名.
                文件名可以不带扩展名， 如: file1,
                本函数将根据图片类型自动添加扩展名， 并返回实际存盘的文件名， 如: file1.jpg。

        :return: 如果失败，则返回None。<br>
                如果成功存盘，返回存盘文件名。<br>
                如果参数filename缺省，则不存盘，返回图片数据(bytes)。
        """
        # noinspection PyBroadException
        try:
            response = Http.get(self.url)
        except Exception:
            return None

        if not response:
            return

        if filename:
            # noinspection PyBroadException
            try:
                filename = str(filename)
                ext = ImageData.get_file_ext(filename)
                if ext != self.file_ext:
                    filename += self.file_ext
                f = open(filename, 'wb')
                f.write(response.content)
                f.close()
                return filename
            except Exception:
                pass
        else:
            return response.content


mod_requests = None


# import requests package
def get_requests():
    """ import requests package """
    global mod_requests

    if mod_requests is None:
        mod_requests = __import__('requests')

    return mod_requests


# bing.com image search
class WebImage(Spider):
    """
    bing.com image search

    :Chinese: 图片搜索 (使用 bing.com)
    ==============
    Usage:

    # Create object，search for png image of baby, image count is 5
    b = WebImage('baby', 'png', count=5)

    # download all images to subdirectory images
    b.download_all("images")

    # another download style: for each image
    for index, img in enumerate(b.images):

        # print url, filename, file extension of the image
        print(img.url, img.filename, img.file_ext)

        # download image to file
        img.download('images/' + str(index))

    """
    MAX_IMAGES = 50  # max count of images for one search

    def __init__(self, word, file_ext=None, size=None, count=20, first=0):
        url = 'https://cn.bing.com/images/async?q={0}&first={1}&count={2}&relp={3}&lostate=r&mmasync=1'
        super().__init__(url)
        self.word = ''
        self.images = []
        if word:
            self.load(word, file_ext, size, count, first)

    # noinspection PyMethodMayBeStatic
    def _parse_json(self, json_str):
        # noinspection PyBroadException
        try:
            data = json.loads(json_str)
            return data
            pass
        except Exception:
            pass

        data = {}
        # noinspection PyBroadException
        try:
            s = json_str.strip()
            s = s.replace(',', '\n')
            s = s.replace('{', '')
            s = s.replace('}', '')
            lines = s.split('\n')
            for line in lines:
                if line.find(':') > 0:
                    key, value = StrUtil.split2(line, ':')
                    key = StrUtil.trim_quote(key)
                    value = StrUtil.trim_quote(value)
                    data[key] = value
        except Exception:
            pass
        return data

    def load(self, word, file_ext=None, size=None, count=20, first=0):
        """
        search keyword

        :param word:    keyword
        :param file_ext: (optional) file extension of image, such as 'jpg' 'png'  'gif'
        :param count:    (optional) count of image
        :param first:   (optional) skip first some images
        :return: self
        """
        # process file extension
        if file_ext:
            file_ext = str(file_ext).lower()
            if not file_ext.startswith('.'):
                file_ext = '.' + file_ext
            search_word = word + ' ' + file_ext
        else:
            search_word = word

        self.word = word
        self.images = []

        # create a session using requests
        req = get_requests()
        session = req.Session()

        retry = 1
        while len(self.images) < count and retry < 10000:
            retry += 1
            # get web page
            number_per_page = WebImage.MAX_IMAGES
            url = Http._compose_get_url(self._url, [search_word, first, number_per_page, number_per_page])
            r = session.get(url=url, timeout=(3.05, 10))
            self._page = r.text

            first += number_per_page

            # analysis web page
            betweens = [
                (['<a class="iusc"', 'm="'], '"')
            ]
            words = StrUtil.get_word_list(self._page, 0, betweens)

            # convert to images
            for word in words:
                word = word.replace('&quot;', '"')
                data = self._parse_json(word)
                img = ImageData(data)
                if img.valid():
                    if file_ext is None or img.file_ext == file_ext:
                        self.images.append(img)
                if len(self.images) >= count:
                    break
        return self

    def count(self):
        """ return count of images """
        return len(self.images)

    def download_all(self, path=None):
        """
        download all image, save file to specified path

        :param path:  save path
        :return: return count of downloaded files
        """
        success = 0
        for index, img in enumerate(self.images):
            if path:
                filename = os.path.join(str(path), str(index))
            else:
                filename = str(index)
            if img.download(filename):
                success += 1
        return success
