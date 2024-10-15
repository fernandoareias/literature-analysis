import openpyxl

workbook = openpyxl.load_workbook('datasets/artigos.xlsx')
sheet = workbook.active  

for row in sheet.iter_rows():
    for cell in row:
        if isinstance(cell.value, str):  
            cell.value = cell.value.replace('?', '/?')

workbook.save('datasets/artigos_processado.xlsx')
