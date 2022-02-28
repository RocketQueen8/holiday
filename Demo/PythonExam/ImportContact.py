# coding:utf-8
import os
import re
import quopri
def csv2vcf(csv_filename, encoding='gbk'):
    """csv格式文件转换为vcf格式文件"""
    # 1.读取csv文件
    with open(csv_filename, 'r', encoding='gbk') as f:
        ftext_list = f.readlines()
        f.close()
    # 2.将cvs转换为vcf格式
    vcards = ''
    for line in ftext_list[1:]:
        tel_numbers = ''
        name_tel_list = line.strip().split(',')
        if name_tel_list[0]:
            tel_name = name_tel_list[0]  # 姓名
            for tel in name_tel_list[1:]:  # 电话
                tel_numbers += f'TEL;CELL:{tel}\n'
            vcard = f'BEGIN:VCARD\nN:{tel_name}\n{tel_numbers}END:VCARD\n'
            vcards += vcard
    # 3.保存转换后的vcf格式文件
    (fpath, temp_fname) = os.path.split(csv_filename)
    (fname, fextension) = os.path.splitext(temp_fname)
    with open(f'{fpath}{fname}.vcf', "w", encoding=encoding) as f:
        try:
            f.write(vcards)
        finally:
            f.close()
def vcf2csv(vcf_filename, encoding="gbk"):
    """vcf格式文件转换为csv格式文件"""
    # 1.读取vcf文件
    with open(vcf_filename, 'r', encoding='utf-8') as f:
        try:
            ftext = f.read()
        finally:
            f.close()
    # 2.正则替换清洗数据
    re_dic = {
        r"(EMAIL;)(.*)(\n)": "",
        r"(ADR;)(.*)(\n)": "",
        r"(ORG;)(.*)(\n)": "",
        r"(NOTE:)(.*)(\n)": "",
        r"(\n)(VERSION:2.1)": "",
        r"\nEND:VCARD\nBEGIN:VCARD": "",
        r"\nEND:VCARD": "",
        r"BEGIN:VCARD\n": "",
        r"(;;;)([\s\S]*?)(TEL;CELL:)": ",",
        r"N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:": "",
        r"(\nTEL;)(.*?)(:)": ",",
        r"N:;": "",
        r";": "",
        r" ": "",
        r"=\n": ""
    }
    for re_rule, replace_str in re_dic.items():
        p1 = re.compile(re_rule)
        ftext = p1.sub(replace_str, ftext)
    # 3.解码quopri编码
    #ftext = quopri.decodestring(ftext).replace(" ", "")
    ftext = "".join([s for s in ftext.splitlines(True) if s.strip()])
    # 4.保存cvs文件
    csv_str = f'姓名,手机\n{ftext}'
    (fpath, temp_fname) = os.path.split(vcf_filename)
    (fname, fextension) = os.path.splitext(temp_fname)
    with open(f'{fpath}{fname}.csv', "w", encoding=encoding) as f:
        try:
            f.write(csv_str)
        finally:
            f.close()

# vcf2csv(vcf_filename="00001.vcf")
csv2vcf(csv_filename="00001.csv")