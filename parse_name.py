import csv
import pykakasi

def parse_name(csv_text):
    for pair_text in csv_text: 
        kks = pykakasi.kakasi()
        result = kks.convert(pair_text)

        totalTypeCount = [0, 0]
        index = 0
        
        for item in result: 
            chunkRoman = item['hepburn']
            chunkLength = len(chunkRoman)
            print("{}".format(item['hepburn']))
            totalTypeCount[index] += chunkLength
            index += 1
        