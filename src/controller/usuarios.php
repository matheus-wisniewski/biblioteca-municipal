import os
import sys

sys.path.append(os.path.abspath('../'))
from model import get_usuarios

query = get_usuarios()

print(query)