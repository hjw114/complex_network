import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

def data_read(path):
    df_data = pd.read_csv(path, usecols=[2, 3, 4, 5])
    data = df_data.values.tolist()
    c_data = np.array(data, dtype='float64')
    df_label = pd.read_csv(path, usecols=[7])
    label = df_label.values.tolist()
    label = [i for item in label for i in item]
    c_label = np.array(label, dtype='float64')
    return  c_data, c_label

def svm(data, label):
    x_train, x_test, y_train, y_test = train_test_split(data, label, test_size=0.2, random_state=None)
    svc = SVC(kernel='linear')  # 线性核函数
    svc.fit(x_train, y_train)
    coef = svc.coef_[0]
    intercept = svc.intercept_[0]
    acc = svc.score(x_test,y_test)
    return coef, intercept, acc

if __name__ == '__main__':
    coef = []
    intercept = []
    coef_ave = 0
    intercept_ave = 0
    i = 0
    while(i < 10):
        c_data, c_label = data_read(r'D:\python\complex network\test.csv')
        coef_t, intercept_t, acc = svm(c_data, c_label)
        coef.append(coef_t)
        intercept.append(intercept_t)
        i += 1
        print('第' + str(i) + '次准确率' + str(acc))
    for i in range(len(coef)):
        coef_ave = coef_ave + coef[i]
        intercept_ave = intercept_ave + intercept[i]
    coef_ave = coef_ave / i
    intercept_ave = intercept_ave / i
    print(coef_ave)
    print(intercept_ave)