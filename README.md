# desc-dc2-dm-data
Providing consistent access to DC2 DM data products in DESC Python environments.

## Usage
```python
from desc_dc2_dm_data import get_butler, REPOS

butler = get_butler('1.2i')

print('Repo path to 1.2p', REPOS['1.2p'])
```
