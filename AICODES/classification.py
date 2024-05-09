import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

data = pd.read_csv('candidate_data2.csv')
data.columns = data.columns.str.strip()
features = ['graduation_percentage','Experience (years)', 'Written Score', 'Interview Score']
target = "Selection"
x = data[features]
y = data[target]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
mymodel =GaussianNB()
mymodel.fit(x_train, y_train)
prediction=mymodel.predict(x_test)
accuracy_test=accuracy_score(y_test,prediction)
precision_test=precision_score(y_test,prediction)
recall_test=recall_score(y_test,prediction)
print('accuracy is {}%'.format(int(accuracy_test*100)))
print('precision is {}%'.format(int(precision_test*100)))
print('recall is {}%'.format(int(recall_test*100)))
person_a = [90,5,8,10]
person_b = [75,8,7,6]
Selection_a = mymodel.predict([person_a])[0]
Selection_b = mymodel.predict([person_b])[0]
print("Selection of prson A is : {}".format(Selection_a))
print("Selection of person B is : {}".format(Selection_b))