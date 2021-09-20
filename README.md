# tegaki-traditional-chinese-local
## Create better traditional Chinese handwriting recognition system by locals

*This project will not be updated in foreseeable future since the owner has taken up a full-time job with very limited down time. I recommend people interested in creating open source Chinese handwriting recognition system to join this GitHub project: [hanzi_lookup](https://github.com/gugray/hanzi_lookup).*

Old Plan for development:
I plan to use tesseract to recognize Chinese handwriting as it is better trained. I will integrate tesseract into tegaki. I plan to talk about my progress in [HKOSCon 2017](https://hkoscon.org/2017/) Day 2 Lightning Talks (3:00pm - 3:25pm, Function Room 1 and 2)

Problem:
[Current traditional Chinese handwriting model](https://github.com/tegaki/tegaki/releases/download/v0.3/tegaki-zinnia-traditional-chinese-0.3.zip) of [Tegaki Project](https://tegaki.github.io/) is bad as it seems to be trained with rare Chinese characters

Solution:
Create a better traditional Chinese handwriting recognition system using tesseract with the help of Hong Kong people and Taiwanese

Files in this folder:
* wordfreq.txt: Common Chinese (traditional) characters scrapped from [Chinese Character Frequency Statistics for Hong Kong, Mainland China and Taiwan](http://humanum.arts.cuhk.edu.hk/Lexis/chifreq/)
* convert.py: Transform wordfreq.txt into words.txt and bwords.txt
* words.txt: UTF-8 common Chinese (traditional) characters file
* numbers.xml: Character collection file for Arabic numerals (As a test)
* test.xml: Character collection file for common Chinese (traditional) characters
* present.pdf: Introduction to this project, which was presented in Open Source Developer Meetup #1 organized by Open Source Hong Kong
