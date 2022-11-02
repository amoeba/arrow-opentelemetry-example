# From https://arrow.apache.org/docs/python/compute.html#table-and-dataset-joins

import pyarrow as pa

table1 = pa.table({'id': [1, 2, 3],
                   'year': [2020, 2022, 2019]})

table2 = pa.table({'id': [3, 4],
                   'n_legs': [5, 100],
                   'animal': ["Brittle stars", "Centipede"]})

joined_table = table1.join(table2, keys="id")
