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
    # contract = Contract('/Users/andy/Desktop/work/ubiquant/合同提取/首页和投资策略提取/申万/九坤交易精选2号私募证券投资基金基金合同托管版-根据第一次补充协议更新（投资端含打新）V1.2.8TX-20210302（清洁稿）.docx')
    # print(contract.get_chapter('基金的投资'))
    # print(contract.get_section_of_chapter('基金的投资','投资限制'))

    ### folder of contracts class
    
    main()
  