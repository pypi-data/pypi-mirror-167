# -*- coding: GBK -*-

import sys
import os

from docx2python import docx2python
from pathlib import Path
import regex

import pandas as pd
import numpy as np

from . import regex_dictionary
    
class Contract:
    def __init__(self, path):
        self.path = path
        self.product_name = regex.search('����.+(?=\.doc(|x))', path).group()
        self.document = docx2python(path)
        self.full_text = ''
        for table in self.document.body:
            for row in table:
                for cell in row:
                    for para in cell:
                        self.full_text += para
        self.tg = regex.search('��̩|����|����|����|�㷢|��ͨ|����|���|ƽ��|����', path).group()

    # def get_front_page(self):

    # def get_risk_level(self):

    def get_full_text(self):
        return self.full_text

    def get_chapter(self, chapter): #works
        beg_chapter_name = regex_dictionary.get_chapter_beg_end(self.tg, chapter)[0][0]
        end_chapter_name = regex_dictionary.get_chapter_beg_end(self.tg, chapter)[0][1]
        chapter_regex = regex_dictionary.get_chapter_regex(self.tg, beg_chapter_name, end_chapter_name)
        try:
            self.chapter = regex.search(chapter_regex, self.full_text).group()
        except:
            return 'No Regex Matches'
        finally:
            return self.chapter

    def get_section_of_chapter(self, chapter, section):
        chapter = self.get_chapter(chapter)
        beg_section_name = regex_dictionary.get_section_beg_end(self.tg, section)[0][0]
        end_section_name = regex_dictionary.get_section_beg_end(self.tg, section)[0][1]
        section_regex = regex_dictionary.get_section_regex(self.tg, beg_section_name, end_section_name)
        try:
            self.section = regex.search(section_regex, chapter).group()
            if self.section[0] == '��':
                self.section = self.section.replace('��','')
        except:
            return 'No Regex Matches'
        finally:
            return self.section

    # def to_pdf(): under construnction, same as Contracts method, but only exports pdf of one contract document

class Contracts:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.all_files = []
        self.tg = []
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for name in files:
                path = os.path.join(root, name)
                if 'output' not in path and 'docx' in path:
                    self.all_files.append(path)
                    self.tg.append(regex.search('��̩|����|����|����|�㷢|��ͨ|����|���|ƽ��|����', path).group())

    def get_chapters(self, chapter_names):
        out = {}
        for file_path in self.all_files:
            contract = Contract(file_path)
            if contract.tg!='�㷢': out[contract.product_name] = [contract.get_chapter(chapter_name).replace('\t', ' ').replace('\n', '') for chapter_name in chapter_names]
        return out, chapter_names
    
    def get_sections(self, chapter_name, section_names):
        out = {} #dict(per tg) of list(per product) of list(per regex expression)
        for file_path in self.all_files:
            contract = Contract(file_path)
            if contract.tg!='�㷢': out[contract.product_name] = [contract.get_section_of_chapter(chapter_name, section_name).replace('\t', ' ').replace('\n', '') for section_name in section_names]
        return out, sections
        
    def get_df(self, dict):
        data = dict[0]
        names = list(data.keys())
        matrix = np.array([data[product] for product in names])
        df = pd.DataFrame(matrix, index=[names], columns=list(dict[1]))
        return df
    
    def to_excel(self, df, out_path):
        abs_path = Path(out_path).absolute()
        df.to_excel(out_path)
        print(f'Spreadsheet successfully exported to {abs_path}.')
        return df

    # def to_pdf(self, regex): under construction, to include functions from strategy_extract to export pdf of only regexed contents

if __name__=='__main__':
    in_path = sys.argv[1]
    out_path = sys.argv[2]
    chapter = sys.argv[3]
    sections = list(sys.argv[4:])

    ### single contract class
    # contract = Contract('/Users/andy/Desktop/work/ubiquant/��ͬ��ȡ/��ҳ��Ͷ�ʲ�����ȡ/����/�������׾�ѡ2��˽ļ֤ȯͶ�ʻ�������ͬ�йܰ�-���ݵ�һ�β���Э����£�Ͷ�ʶ˺����£�V1.2.8TX-20210302�����壩.docx')
    # print(contract.get_chapter('�����Ͷ��'))
    # print(contract.get_section_of_chapter('�����Ͷ��','Ͷ������'))

    ### folder of contracts class
    contracts = Contracts(in_path)
    contracts.to_excel(contracts.get_df(contracts.get_sections(chapter, sections)), out_path) # works