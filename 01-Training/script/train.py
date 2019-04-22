
import argparse
import os
import numpy as np
import pandas as pd

from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_validate

from azureml.core.run import Run

# Retrieve command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--data-folder', type=str,  help='data folder mounting point')
parser.add_argument('--filename', type=str,  help='training file name')
parser.add_argument('--C', type=float , help='regularization')
args = parser.parse_args()

# Configure a path to training data
data_folder = os.path.join(args.data_folder, 'datasets')
print('Loading data from: ', data_folder)
data_csv_path = os.path.join(data_folder, args.filename)

# Load the dataset
df = pd.read_csv(data_csv_path)

# Preprocess the data
feature_columns = [
                   # Demographic
                   'age', 
                   'job', 
                   'education', 
                   'marital',  
                   'housing', 
                   'loan', 
                   # Previous campaigns
                   'month',
                   'campaign',
                   'poutcome',
                   # Economic indicators
                   'emp_var_rate',
                   'cons_price_idx',
                   'cons_conf_idx',
                   'euribor3m',
                   'nr_employed']

df = df[feature_columns + ['y']]
df_train = pd.get_dummies(df, drop_first=True).astype(dtype='float')

# Create logistic regression estimater
lr = LogisticRegression(solver='lbfgs', C=args.C, max_iter=300, class_weight='balanced')

# Logistic regression requires feature scaling
scaler = StandardScaler()

# Create a training pipeline
pipeline = Pipeline(steps=[('scaler', scaler),
                           ('lr', lr)])


# Train and evaluate the model using cross validation
X = df_train.drop('y', axis=1)
y = df_train.y

# Evaluate mterics(s) by cross-validation
print("Starting training ...")
scoring = ['accuracy', 'recall']
scores = cross_validate(pipeline, X, y, 
                        cv=10, 
                        return_train_score=False,
                        scoring=scoring)

cv_accuracy = np.mean(scores['test_accuracy'])
cv_recall = np.mean(scores['test_recall'])

print("CV accuracy: ", cv_accuracy)
print("CV recall: ", cv_recall)

# Persist the metrics in Azure ML Experiment
# Acquire the current run and log run parameters and performance measures
run = Run.get_context()
run.log("C", args.C)
run.log("CV Accuracy", cv_accuracy)
run.log("CV Recall", cv_recall)


# Train the model on a full dataset
trained_pipeline = pipeline.fit(X, y)

# Serialize the model to ./outputs directory so that it can be automatically copied to Azure ML Experiment
print("Saving the model to outputs ...")
joblib.dump(value=trained_pipeline, filename='outputs/model.pkl')
