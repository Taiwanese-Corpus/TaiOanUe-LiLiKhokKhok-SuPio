from 臺灣言語工具.語音辨識.數字 import 台語數字
from csv import DictWriter

from tauphahji_cmd import tàuphahjī


def main():
#     a = []
#     print(a)
    
    with open('sooji.csv', 'w') as csvfile:
        fieldnames = ['漢字', '羅馬字']
        writer = DictWriter(csvfile, fieldnames=fieldnames)
    
        writer.writeheader()
        
        for sooji in range(11, 100):
            漢字=台語數字().轉數量(sooji)
            羅馬字=tàuphahjī(漢字)['多元書寫'][0]['臺羅斷詞']
            writer.writerow({'漢字': 漢字, '羅馬字': 羅馬字})
        writer.writerow({'漢字': 'Lovely', '羅馬字': 'Spam'})
        writer.writerow({'漢字': 'Wonderful', '羅馬字': 'Spam'})



if __name__ == '__main__':
    main()
