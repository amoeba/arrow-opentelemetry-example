import pyarrow as pa
import pyarrow.dataset as ds

taxi = ds.dataset("~/data/nyc-taxi", format="parquet", partitioning=["year"])

# Read just ten batches
count = 10

for batch in taxi.to_batches():
    if count <= 0:
        break
    count -= 1

