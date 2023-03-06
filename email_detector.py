import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
def email_detector():
    #load the dataset
    data=pd.read_csv("spam.csv", encoding = "ISO-8859-1")
    print(data.head())
    print("_____________________________________________________________________________")
    print(data.shape)
    print(data.isnull().sum())
    x=data.v2
    y=data.v1
    y.replace(to_replace='ham',value=1,inplace=True)
    y.replace(to_replace='spam',value=0,inplace=True)
    print(y)
    print("_____________________________________________________________________________")
    print(y.value_counts())
    sns.histplot(y)
    plt.show()
    x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.9,random_state=25)
    gok= pd.concat([x_train, y_train], axis=1)

    print(gok)
    spam = gok[gok.v1==0]
    print("______________Spam mail from datsets are:-______________")
    print(spam)
    ham = gok[gok.v1==1]
    print("______________Not a Spam Mails are:- ______________")
    print(ham)
def main():
    print("Spam Email Detector!")
    email_detector()
if __name__=="__main__":
    main()