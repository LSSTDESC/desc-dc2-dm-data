# desc-dc2-dm-data
Providing consistent access to DC2 DM data products in DESC Python environments.

## Usage
```python
from desc_dc2_dm_data import get_butler, REPOS

butler = get_butler('1.2p')

print('Repo path to 2.1i', REPOS['2.1i'])
```
