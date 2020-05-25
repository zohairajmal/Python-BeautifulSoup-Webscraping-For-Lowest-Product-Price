import sys
from easeTec import EaseTec
from indusTech import IndusTech
from makeExcel import MakeWorkbook

# Purpose of this file:
# 1) Call all the website classes and store their results in their corresponding class names
# 2) Call the class to export the results to an excel workbook

# Ensure search arguments are taken
if len(sys.argv[1]) > 1:
	print('fit')
else:
	print('error')

# Search argument list
search = sys.argv[1:]

# ====== IndusTech ======
print('Searching IndusTech...')
indusTech = IndusTech(search) # Class created which contains the results of the search
print('Done!\n')


# ====== EaseTec ======
print('Searching EaseTec...')
easeTec = EaseTec(search) # Class created which contains the results of the search
print('Done!\n')


# ====== EXCEL/CSV ======
print('Making Excel Workbook...')
MakeWorkbook(search, easeTec, indusTech) # Export results to an excel sheet
print('Done! \n\nOpen:', '_'.join(search) + '.xlsx')

if len(easeTec.name) == 0:
	print('\nEaseTec found no results..\nTry something else?')

if len(indusTech.name) == 0:
	print('\n\nIndusTech found no results..\nTry something else?')

