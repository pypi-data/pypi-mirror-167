# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 17:01:22 2022

@author: wujian
"""

name = "risk_model_maidou"

import copy
import statsmodels.api as sm
from sklearn.metrics import roc_curve,roc_auc_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from itertools import combinations


from risk_model_maidou.build_model import *

from risk_model_maidou.fenbin import *

from risk_model_maidou.model_train import *


