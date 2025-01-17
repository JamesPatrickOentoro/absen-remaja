from datetime import datetime
from pytz import timezone
from backend.models import Jemaat
import pandas as pd
# Read data from the Excel file
csv_file_path = 'data_remaja_edited.csv'  # replace with your file path
df = pd.read_csv(csv_file_path)




