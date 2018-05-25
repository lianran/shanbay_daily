# coding=utf-8
import json
import xlwt

file = open("./data/daily.json")
workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet("words")


cnt = 0
while 1:
    line = file.readline()
    if not line:
        break;
    #print(line)
    #to json
    obj = json.loads(line);
    print(obj['defn'])
    word = u"%s" % obj['word']#.encode("utf-8")
    pr = u"%s" % obj["pronunciation_us"]#.encode("utf-8")
    chs = u"%s" % obj['defn']#.encode('utf-8')
    print(word, pr, chs)
    worksheet.write(cnt, 0, str(cnt+1))
    worksheet.write(cnt, 1, word)
    worksheet.write(cnt, 2, pr)
    worksheet.write(cnt, 3, chs)
    cnt += 1
#     if cnt > 1 :
#         break
file.close()
workbook.save('my words.xls')
