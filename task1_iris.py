from  sklearn.datasets import load_iris
from sklearn import tree
import numpy as np
def iris():
    #load the dataset
    iris=load_iris()

    print(iris.feature_names)
    print("______________________________________________________________________")
    print(iris.target_names)
    print("______________________________________________________________________")

    test_index=[1,51,101]

    Train_Data=np.delete(iris.data,test_index,axis=0)
    Train_Target=np.delete(iris.target,test_index)

    test_data=iris.data[test_index]
    test_target=iris.target[test_index]

    classifire=tree.DecisionTreeClassifier()

    classifire.fit(Train_Data,Train_Target)
    print("value that we are give for testing")
    print(test_target)
    print("______________________prediction result________________________________________________")
    print("value of Our Prediction")
    print(classifire.predict(test_data))

if __name__=="__main__":
    iris()