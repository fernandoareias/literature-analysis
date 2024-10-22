import pandas as pd

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

def process_file(file_path):
    data = []
    record = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line == "ER":  
                data.append(record)
                record = {}
            elif line == "EF":  
                break
            else:
                if line[:2] in translation_dict:
                    key = translation_dict[line[:2]]
                    value = line[3:].strip()
                    if key in record:
                        record[key] += f" {value}"
                    else:
                        record[key] = value
                elif line[:2] == "  ": 
                    if record:
                        record[list(record.keys())[-1]] += f" {line.strip()}"

    df = pd.DataFrame(data)
    return df

file_path = 'datasets/atividade02/504_registros.txt'

df = process_file(file_path)

print(df)
 