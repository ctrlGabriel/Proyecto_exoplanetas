#Importar Librerias
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn import svm 
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.neighbors import KNeighborsRegressor
