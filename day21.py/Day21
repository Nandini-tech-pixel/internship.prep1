#Machine Learning

from sklearn.datasets import load_diabetes
diabetes = load_diabetes()
print(diabetes.data.shape)

#ANS1 
from sklearn.datasets import load_iris 
data = load_iris()
print("Features:", data.feature_names)
print("Targets:", data.target_names)
print("Data:", data.data[:5])       
print("Target values:", data.target[:5])

from sklearn.linear_model import LinearRegression 
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
diabetes = load_diabetes()
X = diabetes.data      
y = diabetes.target      
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)  
y_pred = model.predict(X_test)  

#ANS2
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
diabetes = load_diabetes()
X = diabetes.data    
y = diabetes.target  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
print("Model Coefficients:", model.coef_)
print("Model Intercept:", model.intercept_)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
def adjusted_r2(y_true, y_pred, n_features):
  n = len(y_true)
r2_val = r2_score(y_test, y_pred) 
def adjusted_r2(y_true, y_pred, n_features):
        n = len(y_true)
        r2_val = r2_score(y_true, y_pred)
        return 1 - ((1 - r2_val) * (n - 1)) / (n - n_features - 1)
adj_r2 = adjusted_r2(y_test, y_pred, X_test.shape[1])
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R:", r2)
print("Adjusted R:", adj_r2) 

#ANS3
import numpy as np
X_train = np.hstack((X_train, np.random.rand(X_train.shape[0], 1)))
X_test = np.hstack((X_test, np.random.rand(X_test.shape[0], 1)))

#ANS4 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
X_train = np.hstack((X_train, np.random.rand(X_train.shape[0], 1)))
X_test = np.hstack((X_test, np.random.rand(X_test.shape[0], 1)))
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
def adjusted_r2(y_true, y_pred, n_features):
    n = len(y_true)
    r2_val = r2_score(y_true, y_pred)
    return 1 - ((1 - r2_val) * (n - 1)) / (n - n_features - 1)

adj_r2 = adjusted_r2(y_test, y_pred, X_test.shape[1])
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R²:", r2)
print("Adjusted R²:", adj_r2)

import matplotlib.pyplot as plt
plt.scatter(y_test, y_pred)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.show()

#ANS5 
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', edgecolors='k')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted Target Values')
plt.grid(True)
plt.show()

#MINI PROJECT
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error (MSE):", mse)
print("R² Score:", r2)

plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', edgecolors='k')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted Values (Diabetes Dataset)')
plt.grid(True)
plt.show()


