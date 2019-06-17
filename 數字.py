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
        for 漢字, 羅馬字 in 全部資料():
            writer.writerow({'漢字': 漢字, '羅馬字': 羅馬字})
        


def 全部資料():
    for sooji in range(11, 100):
        漢字 = 台語數字().轉數量(sooji)
        羅馬字 = 產生羅馬字(漢字)
        yield 漢字, 羅馬字


def 產生羅馬字(漢字):
    return 整理羅馬字(tàuphahjī(漢字)['多元書寫'][0]['臺羅斷詞'])


def 整理羅馬字(羅馬字):
    羅馬字.replace(' ', '-')
    羅馬字.lower()
    return 羅馬字


if __name__ == '__main__':
    main()
