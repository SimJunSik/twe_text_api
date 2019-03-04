import codecs
from konlpy.tag import Twitter
import os, fnmatch

twitter = Twitter()
results = []
cates = []
pass_cates = []
listOfFiles = os.listdir('./cates')
pattern = "*.txt"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        cate = entry[8:entry.index(".txt")]
        if cate not in pass_cates :
            cates.append(cate)

for cate in cates :
    print(cate)
    file_name = "./cates/twitter_" + cate + ".txt"
    fp = codecs.open(file_name, "r", encoding="utf-8")
    text = fp.read()

    lines = text.split('\n')
    for line in lines :
        malist = twitter.pos(line, norm=True, stem=True)
        r = []
        for word in malist :
            if not word[1] in ["Josa", "Eomi", "Punctuation"] :
                r.append(word[0])
        rl = (" ".join(r)).strip()
        results.append(rl)
        print(rl)

    fp.close()

wakati_file = 'twitter.wakati'
with open(wakati_file, 'w', encoding='utf-8') as fp :
    fp.write("\n".join(results))

print("ok")