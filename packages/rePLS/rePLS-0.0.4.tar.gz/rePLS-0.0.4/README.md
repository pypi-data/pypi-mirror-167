# rePLS


## Examples 

```python
from rePLS import rePLS, rePCR, reMLR
import numpy as np

n_samples, n_features, n_outcomes, n_confounders = 100, 10,5,2
n_components = 2
rng = np.random.RandomState(0)

Y = rng.randn(n_samples,n_outcomes)
X = rng.randn(n_samples, n_features)
Z = rng.randn(n_samples, n_confounders)

reg = rePLS(Z=Z,n_components=n_components)
reg.fit(X,Y)
Y_pred = reg.predict(X,Z)
```