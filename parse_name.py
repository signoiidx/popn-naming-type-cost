import csv
import pykakasi

def parse_name(csv_text):
    csv_result = []
    
    for pair_text in csv_text: 
        kks = pykakasi.kakasi()
        result = [kks.convert(pair_text[0]), kks.convert(pair_text[1])]
        
        pair_result = []
        
        for category in result: 
            sentence_roman = ''
            
            for item in category: 
                chunk_Roman = item['hepburn']
                sentence_roman += ''.join(chunk_Roman)
                
            typing_count = len(sentence_roman)
            pair_result.extend(tuple([sentence_roman, typing_count]))

        csv_result.append(pair_result)
        print(pair_result)
        
    return csv_result
