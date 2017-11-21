# -*- coding: utf-8 -*-
import urllib
import urllib.request
import urllib.parse
from google import search
import re
import ssl



def google_search(query):
    for url in search(query,start=0, stop=1, lang="jp", num=5, pause=2.0):
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            print('url: ' + url)
            print('')
            regex = r'<h[23].*?/h[23]>'
            pattern = re.compile(regex, re.MULTILINE | re.DOTALL)
            match_h2 = pattern.findall(html)
            for h2 in match_h2:
                print(h2)
                print('')
            print('')

def url_search(url):
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            print('url: ' + url)
            print('')
            regex = r'<h2.*?/h2>'
            pattern = re.compile(regex, re.MULTILINE | re.DOTALL)
            match_h2 = pattern.findall(html)
            for h2 in match_h2:
                print(h2)
            print('')
            print('')


def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    google_search("bitcoin使い方")
    

if __name__ == '__main__':
    main()

