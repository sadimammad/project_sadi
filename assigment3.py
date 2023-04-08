import os

directory='fayl31'

yeni_fayl='/home/sadimammad'

path=os.path.join(yeni_fayl,directory)

os.mkdir(path)
print('Directory %s created' %directory)
