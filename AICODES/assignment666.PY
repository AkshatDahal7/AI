import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split


data = pd.read_csv('candidate_data.csv')
data.columns = data.columns.str.strip()
features = ['Experience (years)', 'Written Score', 'Interview Score', 'Criteria']
target = "Salary"
x = data[features]
y = data[target]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
mymodel = KNeighborsRegressor(n_neighbors=3)
mymodel.fit(x_train, y_train)
person_a = [5, 80, 90, 37.9]
person_b = [8, 70, 60, 41.6]
salary_a = mymodel.predict([person_a])[0]
salary_b = mymodel.predict([person_b])[0]
print("Salary of person A is : {}".format(salary_a))
print("Salary of person B is : {}".format(salary_b))
