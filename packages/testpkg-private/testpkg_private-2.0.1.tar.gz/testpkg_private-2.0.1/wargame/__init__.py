import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path)
print("in __init__.py sys.path: ", sys.path)
