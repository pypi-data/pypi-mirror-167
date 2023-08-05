"""for development"""
import numpy as np
from utils import LibManager

lm = LibManager('C:\\Users\\lukas\\PycharmProjects\\spy\\data')
lm.lib_update(period='3mo', new_entries=5)
