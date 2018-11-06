# desc-dc2-dm-data
Providing consistent access to DC2 DM data products in DESC Python environments.

## Usage
```python
from desc_dc2_dm_data import REPOS
import lsst.daf.persistence as dafPersist

butler = dafPersist.Butler(REPOS['1.2i'])
```
