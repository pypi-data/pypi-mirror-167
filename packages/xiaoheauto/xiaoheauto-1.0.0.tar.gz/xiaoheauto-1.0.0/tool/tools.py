import json
import os

import xlrd

from tool.config import Config


def params_to_dict(s):
    d={}
    try:
        json.loads(s)
    except:
        pass
    else:
        return d
    # if "=" not in d:
    #     return {}
    # else:
    kvs=s.split('&')
    for kv in kvs:
        d[kv.split('=')[0]]=kv.split('=')[1]
    return d



def headers_to_dict(s):
    d={}
    s=s.strip()
    try:
        json.loads(s)
    except:
        pass
    else:
        return d

    dict_list=s.split('\n')
    for kvs in dict_list:
        kvs=kvs.strip()
        k,v=kvs.split(': ')
        d[k]=v
    return d



def read_excel(path):
    root_path=Config().get_rootpath()
    excel=xlrd.open_workbook(os.path.join(root_path,path))
    sheets=excel.sheets()    #读取所以sheet
    ids=[]
    case_list=[]
    for sheet in sheets:
        rows=sheet.nrows
        if rows<1:
            continue
        rows_1=sheet.row_values(0)   #读取第一行数据
        for i in range(1,rows):
            row=sheet.row_values(i)
            d={}
            for n in range(len(row)):
                d[rows_1[n]] = None if row[n]=="" else row[n]
            if d['is_run']=='否':
                continue
            ids.append(d['title'])
            case_list.append(d)
    return ids,case_list




def scan_excel(root_path,excel_list):        #扫描项目下的所有Excel文件
    files_list=os.listdir(root_path)
    for f in files_list:
        file=os.path.join(root_path,f)
        if os.path.isdir(file) and f not in ['.idea', '.pytest_cache', '__pycache__']:
            scan_excel(file,excel_list)
        elif os.path.isfile(file) and (file.endswith(".xls")) or (file.endswith(".xlsx")):        #判断是否是Excel文件
            excel_list.append(file)
        else:
            pass

def get_cases():
    root_path=Config().get_rootpath()
    excel_list=[]
    scan_excel(root_path,excel_list)
    # 批量读取Excel文件里面的数据
    ids=[]
    cases=[]
    for e in excel_list:
        titles,case_list=read_excel(e)
        ids.extend(titles)
        cases.extend(case_list)
    return ids,cases



