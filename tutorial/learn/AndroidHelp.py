__author__ = 'bj'
import re

f = open(
    'D:\\workspace\\svn\\android\\trunk\\travel\\app\\src\\main\\res\\layout\\adapter_journey_list_card.xml')
read = f.read()
pattern = re.compile(r'@\+id/[a-z0-9_]+');
match = pattern.findall(read, 0, len(read))
print ("        SparseArray<View> vh = new SparseArray<>();       ");
record = ""
if (match):
    for id in match:
        outPut = "R.id." + id[id.find("/") + 1:len(id)]
        if (record.find( ";" + outPut + ";")  >= 0 ):
            continue
        else:
            print(
                "        vh.put(" + outPut + ",convertView.findViewById(" + outPut + "));              ")
            record  =record+ ";" + outPut + ";"

print ("return vh;");
