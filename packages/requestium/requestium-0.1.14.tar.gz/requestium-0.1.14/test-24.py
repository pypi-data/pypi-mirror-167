#!/usr/bin/env python3

import requestium

s = requestium.Session(
    webdriver_path='./chromedriver',
    browser='chrome',
    default_timeout=15,
    webdriver_options={'arguments': ['headless']},
)

a = s.get('https://www.baidu.com/')

#print(a.encoding)
#print(a.text)

a.encoding = 'utf-8'

#print(a.encoding)
#print(a.text)

print(a.text)
print(a.xpath('//text()[normalize-space() and not(ancestor::script | ancestor::style)]').extract())
