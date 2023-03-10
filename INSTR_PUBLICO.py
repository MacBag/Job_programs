import  xml.etree.ElementTree as ET

tree = ET.parse(r'C:\Users\maciej.baginski\Desktop\Podyplomowe Big Data\Public INSTR\INSTR\ALIOR_INSTR_20230306.xml')
root=tree.getroot()

krok = 0
l=[]

for security in root.iter('Security'):

    if security.find('TURNOVERADMITTED').text == '0':
        l.append(security)
    for i in root.iter('PrimaryMarket'):
        i.find('FundName').text = 'EAI'
        # print((security.find('TURNOVERADMITTED').text=='0'))
        # root.remove(root[krok])
        # root.remove(security)
        # l.append(krok)
    # elif security.find('TURNOVERADMITTED').text == '1':
        # root.remove(root[krok])
    #     # root.remove(security)
    # else:
    #     krok += 1
for i in l:
    root.remove(i)
# root.remove(root(l))
# print(len(l))

tree.write(r'C:\Users\maciej.baginski\Desktop\Podyplomowe Big Data\Public INSTR\INSTR\eques_INSTR_20230302.xml', encoding='utf-8', xml_declaration=True)