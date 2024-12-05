from NNclassifier import NNClassifier
import numpy as np
class Validator:
    def __init__(self,classifier);
        self.classifier = classifier
    #passing in feature data, correct label, and feature subsets
    def evaluate(self, data, labels, featureSubset):
        correctPredictions = 0
        numInstances = len(data)

        for i in range(numInstances):
            #i gets the index of the instance and feature subset give
            testInstance = []
            for j in featureSubset:
                testInstance.append(data[i][j])
            testLabel = labels[i]
            trainData = []
            trainLabels = []
            for j in range(len(data)):
                if j != i:  
                    trainData.append([data[j][k] for k in featureSubset])
                    trainLabels.append(labels[j])
            trainData = np.array(trainData)
            trainLabels = np.array(trainLabels)
            self.classifier.train(trainData, trainLabels)
            predictedLabel = self.classifier.test(testInstance)

            if(predictedLabel == testLabel):
                correctPredictions+=1
            
        accuracy = correctPredictions / numInstances
        return accuracy
