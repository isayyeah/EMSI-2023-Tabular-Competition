import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from xgboost import XGBClassifier

# Read the test and train data
test = pd.read_csv('test.csv')
train = pd.read_csv('train.csv')

# Select the features for training and testing
fe_sel = ['age', 'height(cm)', 'weight(kg)', 'waist(cm)', 'eyesight(left)',
          'eyesight(right)', 'hearing(left)', 'hearing(right)', 'systolic',
          'relaxation', 'fasting blood sugar', 'Cholesterol', 'triglyceride',
          'hemoglobin', 'Urine protein', 'serum creatinine', 'dental caries', 'HDL',
          'LDL', 'AST', 'ALT', 'Gtp']

train_fe_sel = train[fe_sel]
test_fe_sel = test[fe_sel]

# Split the data into training and testing sets
X = train[fe_sel]
y = train['smoking']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# Create and train the XGBoost model use
model = XGBClassifier(learning_rate=0.04, n_estimators=2000)

#Train the model 
model.fit(X_train, y_train)

# Make predictions on the test set
pred = model.predict(X_test)

# Calculate AUC
auc = roc_auc_score(y_test, pred)
print("AUC:", auc)

# Make final predictions on the test data
final_pred = model.predict(test_fe_sel)

# Create a DataFrame with the predictions and save it to a CSV file
df = pd.DataFrame({'id': test.id, 'smoking': final_pred})
df.to_csv('submission2.csv', index=False)
