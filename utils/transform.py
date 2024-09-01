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


def excel_to_yaml(excel_file, yaml_file):
  """Converts an Excel file to a YAML file, using the first column for levels and lists.

  Args:
    excel_file: Path to the Excel file.
    yaml_file: Path to the output YAML file.
  """

  # Read the Excel file into a Pandas DataFrame
  df = pd.read_excel(excel_file)

  # Create a YAML dictionary
  yaml_dict = {}

  # Iterate over the rows of the DataFrame
  for index, row in df.iterrows():
    current_dict = yaml_dict

    # Create nested dictionaries based on the first column (levels)
    for level in row.dropna().tolist()[:-1]:
      if level not in current_dict:
        current_dict[level] = {}
      current_dict = current_dict[level]

    # Add the last value as a list item
    last_value = row.dropna().tolist()[-1]
    if last_value not in current_dict:
      current_dict[last_value] = []
    current_dict[last_value].append(row.tolist()[1:])

  # Write the YAML dictionary to a file
  with open(yaml_file, 'w') as f:
    yaml.dump(yaml_dict, f, default_flow_style=False)
