import pyarrow.parquet as pq
import pandas


def download_parquet():
    trips = pq.read_table('yellow_tripdata_2022-01.parquet')
    trips = trips.to_pandas()
    print(trips.head())

if __name__=="__main__":
    download_parquet()