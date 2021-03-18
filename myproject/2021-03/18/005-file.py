path = __file__
path = path[:path.rfind('\\')][:path.rfind('/')]+"\\"

fp = open(path+'workfile.txt', 'w')
fp.write('Hello123')
fp.close()
