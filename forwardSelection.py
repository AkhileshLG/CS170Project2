import random
import itertools
from loaddata import load_dataset
from NNclassifier import NNClassifier
from validator import Validator

def forwardsSelection(datasetpath):
    features, labels = load_dataset(datasetpath)
    NN = NNClassifier()
    callValidator = Validator(NN)

    randomVal = str(round(random.uniform(50, 100), 1))
    print("Using no features and \"random\" evaluation, I get an accuracy of " + randomVal + "%\n")
    
    overallMaxAccuracy = str(0)
    maxValue = str(0)
    maxIndex = str(0)
    featureLst = []
    resultLst = []
    bestLst = []
    numOfFeatures = len(features[0])
    
    for i in range(0, numOfFeatures):
        featureLst.append(i + 1)
    
    print("Beginning Search.\n")
    resultLst.clear()
    for i in range(0, numOfFeatures):
        maxAccuracy = str(0)
        for k in range(0, len(featureLst)):
            tempLst = resultLst
            tempLst.append(featureLst[k])
            if len(resultLst) == 0:
                tempAccuracy = str(callValidator.evaluate(features, labels, tempLst))
                print("     Using feature(s) {" + str(featureLst[k]) + "} arruracy is " + tempAccuracy + "%\n")
            elif len(resultLst) != 0:
                tempAccuracy = str(callValidator.evaluate(features, labels, tempLst))
                print("     Using feature(s) {" + ','.join(str(tempLst)) + "} arruracy is " + tempAccuracy + "%\n")

            if maxAccuracy <= tempAccuracy:
                maxAccuracy = tempAccuracy
                maxValue = featureLst[k]
                maxIndex = k

        resultLst.append(maxValue)
        featureLst.pop(maxIndex)

        if overallMaxAccuracy <= maxAccuracy:
            bestLst = resultLst.copy()
            overallMaxAccuracy = str(maxAccuracy)
        
        if len(featureLst) != 0:
            print("Feature set {" + ','.join(str(resultLst)) + "} was best, accuracy is " + maxAccuracy + "%\n")
        elif len(featureLst) == 0:
            if overallMaxAccuracy <= maxAccuracy:
                print("Feature set {" + ','.join(str(resultLst)) + "} was best, accuracy is " + maxAccuracy + "%\n")
            elif overallMaxAccuracy > maxAccuracy:
                print("Warning, Accuracy has decreased!)")
                print("Feature set {" + ','.join(str(bestLst)) + "} was best, accuracy is " + overallMaxAccuracy + "%\n")