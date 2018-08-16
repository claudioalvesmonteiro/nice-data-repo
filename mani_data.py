
# importar modules
import pandas as pd

# read and select columns
QOGdata = pd.read_csv('/home/pacha/Documents/git_projects/aulas_analisededados/aulas_particulares/dados/qog_std_cs_jan18.csv')
QOGdataSave = QOGdata[['epi_wastecxn','epi_eh', "epi_epi","wdi_export"]]

# rename columns
QOGdataSave.columns = ["waster_water_treatment", "environmental_health", "environmental_performance_index" "total_export", ]

# save select data
QOGdataSave.to_csv("QOGdataSave.csv", sep=';', encoding='utf-8')

#############################################

# importar modules
import pandas as pd

# read and select columns
QOGdata = pd.read_csv('/home/pacha/Documents/git_projects/aulas_analisededados/aulas_particulares/dados/qog_std_cs_jan18.csv')
QOGdataSave = QOGdata[['epi_wastecxn','epi_eh', "epi_epi","wdi_export"]]
