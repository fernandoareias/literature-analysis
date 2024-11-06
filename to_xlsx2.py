import pandas as pd
import os
import time
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

    # Limpar os nomes das colunas removendo espaços em branco e padronizando para maiúsculas
    data.columns = data.columns.str.strip().str.upper()
    
    # Renomear as colunas usando o dicionário de tradução
    data.rename(columns=translation_dict, inplace=True)

    # Verificar se alguma coluna não foi renomeada
    missing_columns = [col for col in data.columns if col in translation_dict and col == data.columns[col]]
    if missing_columns:
        logging.warning(f"Colunas não renomeadas: {missing_columns}")
    return data

input_file = 'datasets/atividade02/q5.txt'
if not os.path.exists(input_file):
    raise FileNotFoundError(f"Arquivo '{input_file}' não encontrado. Verifique o caminho.")

start_time = time.time()

data_frame = load_file(input_file)

output_file = 'datasets/atividade02/Q5.xlsx'
data_frame.to_excel(output_file, index=False)

end_time = time.time()

execution_time = end_time - start_time
total_migrated_lines = len(data_frame)
file_size = os.path.getsize(output_file) / (1024 * 1024)

logging.info(f"Dados combinados salvos em {output_file}")
logging.info(f"Tempo total de execução: {execution_time:.2f} segundos")
logging.info(f"Total de linhas migradas: {total_migrated_lines}")
logging.info(f"Tamanho do arquivo final: {file_size:.2f} MB")
