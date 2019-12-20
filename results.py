import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import f1_score
from inspect import signature

import datetime

def ExtractionFromExcel(path):
    xcl = pd.read_excel(path)
    
    return xcl[1].values

def GetClasses(frames, ratios, frames_number, threshold):
    classes = np.zeros(frames_number)
    for i, ratio in enumerate(ratios):
        if ratio < threshold:
            classes[frames[i] - 1] = 1
            
    return classes

def PrecisionRecall(y_test, y_pred, title):
    print(title)
    average_precision = average_precision_score(y_test, y_pred)
    print('Average precision-recall score: {0:0.2f}'.format(average_precision))
    
    precision, recall, _ = precision_recall_curve(y_test, y_pred)

    step_kwargs = ({'step': 'post'} if 'step' in signature(plt.fill_between).parameters else {})
    plt.step(recall, precision, color='b', alpha=0.2, where='post')

    plt.fill_between(recall, precision, alpha=0.2, color='b')

    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.ylim([0.0, 1.05])
    plt.xlim([0.0, 1.0])
    plt.title('Precision-Recall curve: AP={0:0.2f}'.format(average_precision))
    
    print("F1 score:", f1_score(y_test, y_pred))

def PredictionToTimecodes(prediction):
    timecodes = []
    for index, label in enumerate(prediction):
        if label == 1:
            seconds = index * 10
            timecode = str(datetime.timedelta(seconds=seconds))
            timecodes.append(timecode)
    return timecodes
