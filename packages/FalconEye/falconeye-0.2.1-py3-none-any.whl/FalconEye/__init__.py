from .walk import Walk
from .flatten import Flatten

obj = {"hello":{"Hi": 5, "why": {"Energy": "Efficiency"}}}
print(Flatten(obj).items)