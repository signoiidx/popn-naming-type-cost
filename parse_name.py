import csv
import pykakasi

def parse_name(csv_text):
    csvResult = []
    
    for pair_text in csv_text: 
        kks = pykakasi.kakasi()
        result = [kks.convert(pair_text[0]), kks.convert(pair_text[1])]
        
        pairResult = []
        
        for category in result: 
            sentenseRoman = ''
            
            for item in category: 
                chunkRoman = item['hepburn']
                sentenseRoman += ''.join(chunkRoman)
                
            typingCount = len(sentenseRoman)
            pairResult.extend(tuple([sentenseRoman, typingCount]))

        csvResult.append(pairResult)
        print(pairResult)
        
    return csvResult
