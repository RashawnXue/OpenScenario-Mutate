import xmltodict
import json
import re
import os

def xml2json(src, dest):
    '''
    将xml解析为json
    '''
    my_dict = xml2dict(src)
    dict2json(my_dict, dest)

def xml2dict(src): 
    with open(src) as f:
        my_dict = xmltodict.parse(f.read())
    return my_dict

def dict2json(my_dict, dest):
    with open(dest, 'w', encoding='utf-8') as f:
        json.dump(my_dict, f, indent=2, sort_keys=False, ensure_ascii=False)

def json2xml(src, dest):
    '''
    将json逆向解析为xml
    '''
    my_dict = json2dict(src)
    dict2xml(my_dict, dest)

def json2dict(src):
    with open(src, 'r', encoding='utf-8') as f:
        my_dict = json.loads(f.read())
    return my_dict

def dict2xml(my_dict, dest):
    my_xml = xmltodict.unparse(my_dict, pretty=True, indent='  ')
    regex = re.compile(r'></.*>')
    my_xml = regex.sub('/>', my_xml)
    with open(dest, 'w', encoding='utf-8') as f:
        f.write(my_xml)

def trans_examples_to_json():
    '''
    将examples转换为json   
    '''
    for item in os.scandir('./ParseXOSC/xml/examples'):
        xml2json(item.path, './ParseXOSC/json/examples/'+item.path.split('/')[-1].split('.')[-2]+'.json')

def trans_catalogs_to_json():
    '''
    将catalogs转换为json
    '''
    for path, dir_lst, file_lst in os.walk('./ParseXOSC/xml/Catalogs'):
        for file_name in file_lst:
            file_path = os.path.join(path, file_name)
            xml2json(file_path, file_path.replace('xml', 'json').replace('xosc', 'json'))

def trans_oxdr_to_json():
    '''
    将xodr文件转换为json
    '''
    for path, dir_lst, file_lst in os.walk('./ParseXOSC/Databases'):
        for file_name in file_lst:
            if not file_name.endswith('xodr'):
                continue
            file_path = os.path.join(path, file_name)
            xml2json(file_path, file_path.replace('Databases', 'json/Databases').replace('xodr', 'json'))

if __name__ == '__main__':
#    trans_examples_to_json()
#    trans_catalogs_to_json() 
    # trans_oxdr_to_json()
    xml2json('ParseXOSC/mutate/Pedestrain/pedestrian.xosc', 'ParseXOSC/mutate/Pedestrain/pedestrain.json')