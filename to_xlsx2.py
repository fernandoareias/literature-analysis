import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def load_file(file):
    logging.info(f"Lendo arquivo: {file}")
    data = pd.read_csv(file, sep='\t', header=0, names=["Affiliations", "Record Count", "% of 9.977"])
    return data

file_path = 'datasets/analyze (3).txt'
data = load_file(file_path)

output_file = 'datasets/affiliations_output.xlsx'
data.to_excel(output_file, index=False)

logging.info(f"Dados combinados salvos em {output_file}")
