import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

def csv_to_parquet(csv_file, parquet_file, options):

  # Read the CSV file into a Pandas DataFrame
  # with open(csv_filename,'r') as csv_file:
  df = pd.read_csv(csv_file, **options)

  # Convert the DataFrame to a PyArrow Table
  table = pa.Table.from_pandas(df)

  # Write the table to a Parquet file
  pq.write_table(table, parquet_file)