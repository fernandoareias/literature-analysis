import pandas as pd
import glob
import os
import time
from concurrent.futures import ThreadPoolExecutor
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

translation_dict = {
    "PT": "Publication Type",
    "AU": "Authors",
    "BA": "Book Authors",
    "BE": "Book Editors",
    "GP": "Book Group Authors",
    "AF": "Author Full Names",
    "BF": "Book Author Full Names",
    "CA": "Group Authors",
    "TI": "Article Title",
    "SO": "Source Title",
    "SE": "Book Series Title",
    "BS": "Book Series Subtitle",
    "LA": "Language",
    "DT": "Document Type",
    "CT": "Conference Title",
    "CY": "Conference Date",
    "CL": "Conference Location",
    "SP": "Conference Sponsor",
    "HO": "Conference Host",
    "DE": "Author Keywords",
    "ID": "Keywords Plus",
    "AB": "Abstract",
    "C1": "Addresses",
    "C3": "Affiliations",
    "RP": "Reprint Addresses",
    "EM": "Email Addresses",
    "RI": "Researcher Ids",
    "OI": "ORCIDs",
    "FU": "Funding Orgs",
    "FP": "Funding Name Preferred",
    "FX": "Funding Text",
    "CR": "Cited References",
    "NR": "Cited Reference Count",
    "TC": "Times Cited, WoS Core",
    "Z9": "Times Cited, All Databases",
    "U1": "180 Day Usage Count",
    "U2": "Since 2013 Usage Count",
    "PU": "Publisher",
    "PI": "Publisher City",
    "PA": "Publisher Address",
    "SN": "ISSN",
    "EI": "eISSN",
    "BN": "ISBN",
    "J9": "Journal Abbreviation",
    "JI": "Journal ISO Abbreviation",
    "PD": "Publication Date",
    "PY": "Publication Year",
    "VL": "Volume",
    "IS": "Issue",
    "PN": "Part Number",
    "SU": "Supplement",
    "SI": "Special Issue",
    "MA": "Meeting Abstract",
    "BP": "Start Page",
    "EP": "End Page",
    "AR": "Article Number",
    "DI": "DOI",
    "DL": "DOI Link",
    "D2": "Book DOI",
    "EA": "Early Access Date",
    "PG": "Number of Pages",
    "WC": "WoS Categories",
    "WE": "Web of Science Index",
    "SC": "Research Areas",
    "GA": "IDS Number",
    "PM": "Pubmed Id",
    "OA": "Open Access Designations",
    "HC": "Highly Cited Status",
    "HP": "Hot Paper Status",
    "DA": "Date of Export",
    "UT": "UT (Unique WOS ID)",
}

def load_file(file):
    logging.info(f"Lendo arquivo: {file}")
    data = pd.read_csv(file, sep='\t', header=0)
    
    data.rename(columns=translation_dict, inplace=True)
    
    return data

input_files = glob.glob('datasets/savedrecs*')
if not input_files:
    raise FileNotFoundError("Nenhum arquivo encontrado com o padrão '/datasets/savedrecs*'. Verifique o caminho ou o padrão.")
else:
    total_files_size = sum(os.path.getsize(f) for f in input_files) / (1024 * 1024)
    logging.info(f"Arquivos encontrados: {input_files}")
    logging.info(f"Tamanho total dos arquivos: {total_files_size:.2f} MB")

total_lines = 0
for file in input_files:
    with open(file, 'r') as f:
        total_lines += sum(1 for line in f) - 1 

data_frames = []

start_time = time.time()

with ThreadPoolExecutor() as executor:
    futures = executor.map(load_file, input_files)

    processed_lines = 0
    for data_frame in futures:
        data_frames.append(data_frame)
        processed_lines += len(data_frame)

        progress = (processed_lines / total_lines) * 100
        logging.info(f"Progresso: {progress:.2f}% ({processed_lines} linhas processadas de {total_lines})")

combined_data = pd.concat(data_frames, ignore_index=True)

output_file = 'datasets/combined_output.xlsx'
combined_data.to_excel(output_file, index=False)

end_time = time.time()

execution_time = end_time - start_time

total_migrated_lines = len(combined_data)

file_size = os.path.getsize(output_file) / (1024 * 1024) 

logging.info(f"Dados combinados salvos em {output_file}")
logging.info(f"Tempo total de execução: {execution_time:.2f} segundos")
logging.info(f"Total de linhas migradas: {total_migrated_lines}")
logging.info(f"Tamanho do arquivo final: {file_size:.2f} MB")
