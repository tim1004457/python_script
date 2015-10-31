# -*-coding:utf-8-*-

__author__ = 'bj'
f = open("D:\\countryCode.data")
read = f.read()
split = read.split('\n')
fout = open("D:\\out.data", "w")
content = ""
for city in split:
    detail = city.split(' ')
    if detail.__len__() > 3:
        content += (
            'countryModuleList.add(new CountryModule(\"' + detail[0] + '\",\"' + detail[
                1] + '\",\"' + detail[
                2] + '\", Character.valueOf(\'' + detail[3] + '\')) );\n');
    print (content)
fout.write(content)
