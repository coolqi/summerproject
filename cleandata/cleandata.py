import re,string,csv
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize 
# from nltk.stem.snowball import SnowballStemmer

# stoplist = stopwords.words("english")
# print stoplist1
# clean = re.compile(r'[.*]+')
stoplist = open('stoplist.txt').read()
# clean = re.compile('[%s]' % re.escape(string.punctuation))

originalstring = open('newpost.csv').read().lower()
#remove all urls start with https or http
removeURL = re.sub('(https?:\/\/.[a-z0-9\.\/]+)', '', originalstring)
removeName = re.sub('@[a-z0-9\.]+',' ',removeURL)
open('cleandata.csv','w+').write(removeName)

with open('cleandata.csv','r') as infile, open('abc.csv','w+')as outfile:
    dialect = csv.Sniffer().sniff(infile.read(1024))
    infile.seek(0)
    reader = csv.reader(infile)
    writer = csv.writer(outfile, dialect)
    new_c = []
    for row in reader:
        new_row = ([c.translate(None, string.punctuation) for c in row])
        writer.writerow(new_row)
# infile.close()
# outfile.close()
 
with open('abc.csv','w+') as csvfile, open('stoplist.txt') as stoplist:
    newstr = []
    line = csvfile.readline()
    while line:
        words = line.split()
        line = csvfile.readline()
        for c in row:
            words = c.split()
            resultwords = [word for word in words if word not in stoplist]
            result = ' '.join(resultwords)
            writer.writerow([result])
#             