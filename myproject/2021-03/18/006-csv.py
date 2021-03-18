import csv

path = __file__
path = path[:path.rfind('\\')][:path.rfind('/')]+"\\"

with open(path+'file.csv', 'w', newline='', encoding='utf-8') as fp:
    write = csv.writer(fp, delimiter=',')
    header = ["姓名", "學號"]
    write.writerow(["魯路修", "564884"])
    write.writerow(["美海", "794564"])
    write.writerow(["紗霧", "484684"])
    write.writerow(["士織", "654815"])

fp.close()
