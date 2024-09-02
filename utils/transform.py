import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import yaml

def csv_to_parquet(csv_file, parquet_file, file_date, options):

  # Read the CSV file into a Pandas DataFrame
  # with open(csv_filename,'r') as csv_file:
  df = pd.read_csv(csv_file, **options)

  df = df.rename(columns={'Setor': 'setor','Código': 'cod','Ação': 'acao','Tipo':'tipo' ,'Qtde. Teórica':'qtde_teorica','Part. (%)':'part_perc','Part. (%)Acum.':'part_perc_acum'})
  df['data_pregao'] = file_date
  # Convert the DataFrame to a PyArrow Table
  table = pa.Table.from_pandas(df)

  # Write the table to a Parquet file
  pq.write_table(table, parquet_file)