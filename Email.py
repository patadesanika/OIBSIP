import pandas as pd
import seaborn as sns
def Email_Spam_Detector():
    data=pd.read_csv("spam.csv")
    print(data.head())
    print("__________________________________________________________________________")
def main():
    print("Spam Email Detector!")
    ret=Email_Spam_Detector()
if __name__=="__main__":
    main()