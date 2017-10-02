import numpy as np
import xlrd

doc = xlrd.open_workbook('../Data/au2.xlsx').sheet_by_index(0)

kLabels = doc.col_values(7, 1, 393)
y = np.mat([kLabels]).T
print(len(y))