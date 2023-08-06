Notes from an investigation into this.

We currently have a method called block_from_labels, which will create all the record pairs for a set of labels

For example

```
from splink.duckdb.duckdb_linker import DuckDBLinker
import pandas as pd

linker = DuckDBLinker(df, settings, connection=":memory:")

labels = [
    {"unique_id_l": 1, "unique_id_r":2, "clerical_match_score": 0.99}
]

labels = pd.DataFrame(labels)
linker._con.register("labels", labels)
linker._initialise_df_concat_with_tf()
from splink.block_from_labels import block_from_labels

sqls = block_from_labels(linker, "labels")

for sql in sqls:
    linker._enqueue_sql(sql["sql"], sql["output_table_name"])

linker._execute_sql_pipeline().as_pandas_dataframe()
```

We can then add in the Splink scores.

So we probably want:

- A list of all true positive matches with associated Splink score
  - That give you True Positives
  - And False Negative

To get - False positive - True Negative

You also need the results of df_predict. You could concatenate

Or, you could cluster the labels to derive a 'person_id', and join on the the

So you want to concatenate the two

This is actually the same way we'd probably want to create charts for false positives and false negatives.

User to provide a list of
