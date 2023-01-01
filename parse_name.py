import csv
import pykakasi

def parse_name(csv_text):
    csv_result = []
    
    for pair_text in csv_text: 
        kks = pykakasi.kakasi()
        result = [kks.convert(pair_text[0]), kks.convert(pair_text[1])]
        
        pair_result = []
        
        for category in result: 
            sentense_Roman = ''
            
            for item in category: 
                chunk_Roman = item['hepburn']
                sentense_Roman += ''.join(chunk_Roman)
                
            typing_count = len(sentense_Roman)
            pair_result.extend(tuple([sentense_Roman, typing_count]))

        csv_result.append(pair_result)
        print(pair_result)
        
    return csv_result
