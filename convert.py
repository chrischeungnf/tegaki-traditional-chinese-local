import io

words = ""

with io.open("wordfreq.txt",'r',encoding='utf8') as wordfreq:
	for line in wordfreq:
		word = line.split("\t")[0]
		words += word

with io.open("words.txt",'w',encoding='utf8') as o:
	o.write(words)
