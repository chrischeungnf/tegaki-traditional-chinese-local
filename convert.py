import io

words = ""
bwords = b""

with io.open("wordfreq.txt",'r',encoding='utf8') as wordfreq:
	for line in wordfreq:
		word = line.split("\t")[0]
		words += word
		bwords += word.encode('utf8')

with io.open("words.txt",'w',encoding='utf8') as o:
	o.write(words)

with io.open("bwords.txt",'wb') as o:
	o.write(bwords)
