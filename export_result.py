import csv

def export_result(result_data): 
    file_path = 'data/result.csv'
    text = result_data
    
    with open(file_path, 'w', encoding='utf-8') as f:
        rows = csv.writer(f)
        rows.writerows(result_data)
