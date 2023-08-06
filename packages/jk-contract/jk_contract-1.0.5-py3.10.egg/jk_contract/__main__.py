import sys

from jk_contract import Contracts

in_path = sys.argv[1]
out_path = sys.argv[2]
chapter = sys.argv[3]
sections = list(sys.argv[4:])

def main():
    contracts = Contracts(in_path)
    contracts.to_excel(contracts.get_df(contracts.get_sections(chapter, sections)), out_path) # works

if __name__=='__main__':

    ### single contract class
    # contract = Contract('/Users/andy/Desktop/work/ubiquant/��ͬ��ȡ/��ҳ��Ͷ�ʲ�����ȡ/����/�������׾�ѡ2��˽ļ֤ȯͶ�ʻ�������ͬ�йܰ�-���ݵ�һ�β���Э����£�Ͷ�ʶ˺����£�V1.2.8TX-20210302�����壩.docx')
    # print(contract.get_chapter('�����Ͷ��'))
    # print(contract.get_section_of_chapter('�����Ͷ��','Ͷ������'))

    ### folder of contracts class
    
    main()
  