# Apriori algorithm

Wikipedia 2019 defined "Aprori is an algorithm for mining frequent itemsets and learning association on relational databases"

## Declaration

### Import libraries

- [**mlxtend**]()

```python
import numpy as np
import pandas as pd
import matplotlib.pylot as plt
from mlextend.frequent_patterns import apriori, association_rules
```

#### Working on [dataset.csv](https://github.com/DacCute/Data_mining_EX/blob/main/Apriori%20algorithm/Data/dataset.csv)

* Pre-processing data

```python
df = pd.read_csv('./dataset.csv', sep= ',') #read data before read
df.head(10) # print the first 10 rows
items = df['0'].unique # create an array include unique element
```

* Checking the input data

```python
df.info()
```

* Applying [_One Hot Encoding_](https://en.wikipedia.org/wiki/One-hot) for data

```python
itemset = set(items)
envals = []
for idx, row in df.iterrows():
    rowset = set(row)
    labels = {}
    uncomms = list(itemset - rowset)
    commons = list(itemset.intersection(rowset))
    for uc in uncomms:
        labels[uc] = 0
    for cm in commons:
        labels[cm] = 1
    envals.append(labels)
```

 > Final result will look like [Ouput](https://github.com/DacCute/Data_mining_EX/blob/main/Apriori%20algorithm/Illustration/OHE.output)

This encoding turn each row of the data, such as {non, 'Bagel, 'Wine', 'Bread', 'Meat'} 

Where non is not available value, into a corresponding list, such as {'Milk': 0, 'Diaper': 0, 'Pencil': 0, 'Cheese': 0, 'Bagel': 1, ’Eggs’: 1, ’Wine’: 1, ’Bread’: 1, ’Meat’: 1}. The resulting array of lists is _envals_

* Applying association_rules for mining association rules
