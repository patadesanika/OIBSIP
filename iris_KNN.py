from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
def iris():
    dataset=load_iris()
    data_iris=dataset.data
    target_iris=dataset.target

    data_train,data_test,target_train,target_test=train_test_split(data_iris,target_iris,test_size=0.5)
    #lets apply algo
    classifire=KNeighborsClassifier()
    #train the model
    classifire.fit(data_train,target_train)
    #prediction
    prediction=classifire.predict(data_test)
    #accuracy
    Accuracy=accuracy_score(prediction,target_test)
    return Accuracy
def main():
    ret=iris()
    print("Accuracy score is:-",ret*100)
if __name__=="__main__":
    main()
