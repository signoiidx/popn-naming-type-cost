import csv
import pykakasi

def parse_name(csv_text):
    csvResult = []
    
    for pair_text in csv_text: 
        kks = pykakasi.kakasi()
        result = kks.convert(pair_text)
        
        pairResult = []
        index = 0
     
        for item in result: 
            typingCount = 0
            sentenseRoman = ''
            chunkRoman = item['hepburn']
            chunkLength = len(chunkRoman)

            sentenseRoman += chunkRoman
            typingCount += chunkLength
            
            pairResult.extend([sentenseRoman, typingCount])
            
            index += 1
            
        csvResult.append(pairResult)
        