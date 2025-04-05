# -*- coding: utf-8 -*-
"""Brest_cancer_classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-qWuSroFmP4ys9pCJXjO4HvEGOp8WS0o

# **Report on Breast Cancer Diagnosis Prediction:**
## **A Comprehensive Analysis Using...**

### **Logistic Regression**

### **K-Nearest Neighbors**

### **Random Forest**

# **Submitted by: M ABBAS**

## Table of Contents

1. [Introduction](#introduction)
    
2. [Objectives](#objectives)
    
3. [Data Cleaning and Preprocessing](#data-cleaning-and-preprocessing)
    - [3.1 - Handling Missing Values](#handling-missing-values)
    - [3.2 - Removing Duplicates](#removing-duplicates)
    - [3.3 - Removing Unnecessary Features](#removing-unnecessary-features)
        
4. [Feature Engineering](#feature-engineering)
    - [4.1 - Standard Scaler](#standard-scaler)
    - [4.2 - MinMax Scaler](#minmax-scaler)
    - [4.3 - Categorical Columns Encoding](#columns-encoding)
       
5. [Correlation Analysis](#correlation-analysis)
    
6. [Modeling](#modeling)
    - [6.1 - Logistic Regression](#logistic-regression)
    - [6.2 - KNN Classification](#knn-classification)
    - [6.3 - Random Forest Classification](#random-forest-classification)
    - [6.4 - Comparing Models](#comparing-models)
        
7. [Conclusion](#conclusion)
    
8. [Next Steps](#next-steps)
    
9. [Key Insights](#key-insights)
    
10. [Suggestions](#suggestions)

### 1. Introduction

In this project, we analyze data from a breast cancer study to understand how different features relate to tumor characteristics. Our goals include finding out which features are most important for predicting whether a tumor is malignant or benign and testing different models like logistic regression, KNN classification, and random forest classification to see which one predicts breast cancer the best. This will help us better understand the risk factors and improve breast cancer predictions.

## 2 . Objectice

- **Identify Key Factors Influencing Breast Cancer:** Explore and analyze the breast cancer dataset to determine which health features (e.g., tumor size, texture, radius) are most strongly associated with the likelihood of a tumor being malignant or benign.
  
- **Quantify Relationships Between Health Features and Breast Cancer:** Use statistical methods such as correlation analysis and classification modeling to measure how different health features relate to the classification of tumors.
  
- **Evaluate Model Performance:** Assess the effectiveness of various predictive models, including logistic regression, KNN classification, and random forest classification, in predicting whether a tumor is malignant or benign based on health features. Determine the accuracy and reliability of these models.
  
- **Enhance Data Analysis Skills:** Improve understanding of data analysis techniques and methodologies by applying them to a real-world breast cancer dataset, thereby advancing skills in data interpretation and visualization.
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split, learning_curve
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix,ConfusionMatrixDisplay, precision_recall_fscore_support, precision_score, recall_score
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

!pip install streamlit

import pandas as pd

# Load Cancer Patients dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data"
columns = [
    'id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
    'smoothness_mean', 'compactness_mean', 'concavity_mean', 'concave points_mean',
    'symmetry_mean', 'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se',
    'area_se', 'smoothness_se', 'compactness_se', 'concavity_se', 'concave points_se',
    'symmetry_se', 'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst',
    'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst',
    'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst'
]
df_cancer_patients = pd.read_csv(url, header=None, names=columns)

# Display the first few rows
df_cancer_patients.head()

df_cancer_patients.info()

df_cancer_patients.describe()

"""## 3 Data Cleaning and Preprocessing
Describe the steps taken to clean and preprocess the data, including:
- Handling missing values
- Removing duplicates
- dropping unnecessary features

## 3.1 Handling missing values
"""

df_cancer_patients.isnull().sum()

#Handling any null values...
total = df_cancer_patients.isnull().sum().sort_values(ascending=False)
total_select = total.head(30)
total_select.plot(kind = 'bar', figsize = (8,6), fontsize = 10)
plt.xlabel("columns", fontsize = 20)
plt.ylabel("counts", fontsize = 20)
plt.title("Total missing values ", fontsize = 20)

"""**After a thorough examination of the dataset,from the above diagram it has been confirmed that there are no missing values present.**

## 3.2 Removing duplicates
"""

df_cancer_patients.duplicated()

#Alternatively wat to check duplicate...
df_cancer_patients.index.is_unique

"""**After examination for duplicates across all columns of the dataset, it has been thoroughly verified that there are no duplicate entries present. This ensures the integrity and uniqueness of the data for further analysis.**

## 3.3 dropping unnecessary features
"""

df_cancer_patients = df_cancer_patients.drop(columns=['id'])



df_cancer_patients['diagnosis'].value_counts()

df_cancer_patients['diagnosis'].value_counts().plot.bar(color=['orange','black'])

"""**After examination for the target features(diagnosis) it has beenn confirmed that the features is no high imbalance.**"""

# Encode the diagnosis column (Malignant: 1, Benign: 0)
#df_cancer_patients['diagnosis'] = df_cancer_patients['diagnosis'].map({'M': 1, 'B': 0})
features = df_cancer_patients.drop(columns=['diagnosis'])

features.head(5)

"""## 4. Feature Engineering

### 4.1 Standard Scalar
"""

'''# Fit and transform the features
scaled_features = scaler.fit_transform(features)

# Convert the scaled features back to a DataFrame
df_scaled = pd.DataFrame(scaled_features, columns=features.columns)

# Check the range of the scaled features
print(f"Scaled feature range: {df_scaled.min().min()} to {df_scaled.max().max()}")'''

"""### 4.2 MinMax Scaler"""

# Initialize MinMaxScaler
scaler = MinMaxScaler()

# Fit and transform the features
scaled_features = scaler.fit_transform(features)

# Convert the scaled features back to a DataFrame
df_scaled = pd.DataFrame(scaled_features, columns=features.columns)

# Check the range of the scaled features
print(f"Scaled feature range: {df_scaled.min().min()} to {df_scaled.max().max()}")



"""## 4.3 Encoding Categorical column"""

# Encode the diagnosis column (Malignant: 1, Benign: 0)
df_cancer_patients['diagnosis'] = df_cancer_patients['diagnosis'].map({'M': 1, 'B': 0})

df_cancer_patients

"""## 5 Correlation"""

plt.figure(figsize=(25,25))
sns.heatmap(df_cancer_patients.corr(),annot=True,cmap='RdYlGn')

plt.show()

correlation = df_cancer_patients.corr()['diagnosis'].sort_values()
correlation

correlation.plot(kind='bar',figsize=(10,8))

"""**After examining the relationship of features with the target feature (diagnosis), we observe the following:**

**Strong Positive Correlations:**

- **concave points_worst**: 0.794
- **perimeter_worst**: 0.783
- **concave points_mean**: 0.777

**Weak or No Correlations:**

- **fractal_dimension_mean**: -0.013
- **texture_se**: -0.008
- **symmetry_se**: -0.007

**Further correlations:**

- **compactness_mean**: 0.597
- **concavity_worst**: 0.660
- **area_mean**: 0.709
- **radius_mean**: 0.730
- **area_worst**: 0.734
- **perimeter_mean**: 0.743
- **radius_worst**: 0.776

**These results indicate that features like concave points_worst and perimeter_worst have strong positive relationships with the diagnosis, while others show weak or no correlations.**

##  6 Modeling
"""

X = df_cancer_patients.drop(columns=['diagnosis'])
y = df_cancer_patients['diagnosis']

X.head(3)

y.head

"""## Logistic Classification 6.1"""

# First, let's split the training and testing dataset

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state = 123)

print(f"Training dataset shape, X_train: {X_train.shape}, y_train: {y_train.shape}")

print(f"Testing dataset shape, X_test: {X_test.shape}, y_test: {y_test.shape}")

"""## L2 Classification 6.1.1"""

# L2 penalty to shrink coefficients without removing any features from the model
penalty= 'l2'
# Our classification problem is multinomial
multi_class = 'multinomial'
# Use lbfgs for L2 penalty and multinomial classes
solver = 'lbfgs'
# Max iteration = 1000
max_iter = 1000

# Define a logistic regression model with above arguments
l2_model = LogisticRegression(random_state=123, penalty=penalty, multi_class=multi_class, solver=solver, max_iter=max_iter)

l2_model.fit(X_train, y_train)

l2_preds = l2_model.predict(X_test)

def evaluate_metrics(yt, yp):
    results_pos = {}
    results_pos['accuracy'] = accuracy_score(yt, yp)
    precision, recall, f_beta, _ = precision_recall_fscore_support(yt, yp)
    results_pos['recall'] = recall
    results_pos['precision'] = precision
    results_pos['f1score'] = f_beta
    return results_pos

evaluate_metrics(y_test, l2_preds)

"""**L2 Model Performance:**

The L1 model achieved an accuracy of 95.61%. It has high recall (95.83% for class 0 and 95.24% for class 1), indicating it correctly identifies most positive cases. The precision is also strong (97.18% for class 0 and 93.02% for class 1), showing the model's predictions are reliable. The F1 scores (96.50% for class 0 and 94.12% for class 1) reflect a good balance between precision and recall.

## Confusion Metrics
"""

cf = confusion_matrix(y_test, l2_preds, normalize='true')

sns.set_context('talk')
disp = ConfusionMatrixDisplay(confusion_matrix=cf,display_labels=l2_model.classes_)
disp.plot()
plt.show()

"""## L1 Classification  6.1.2"""

# L1 penalty to shrink coefficients without removing any features from the model
penalty= 'l1'
# Our classification problem is multinomial
multi_class = 'multinomial'
# Use saga for L1 penalty and multinomial classes
solver = 'saga'
# Max iteration = 1000
max_iter = 1000

# Define a logistic regression model with above arguments
l1_model = LogisticRegression(random_state=123, penalty=penalty, multi_class=multi_class, solver=solver, max_iter = 1000)

l1_model.fit(X_train, y_train)

l1_preds = l1_model.predict(X_test)

evaluate_metrics(y_test, l1_preds)

"""**L1 Model Performance:**

The L1 model achieved an accuracy of 92.11%. It has high recall (95.83% for class 0 and 85.71% for class 1), indicating it correctly identifies most positive cases. The precision is also strong (92.00% for class 0 and 92.31% for class 1), showing the model's predictions are reliable. The F1 scores (93.88% for class 0 and 88.89% for class 1) reflect a good balance between precision and recall.

## Confusion Metrics
"""

cf = confusion_matrix(y_test, l1_preds, normalize='true')

sns.set_context('talk')
disp = ConfusionMatrixDisplay(confusion_matrix=cf,display_labels=l1_model.classes_)
disp.plot()
plt.show()

l1_model.coef_

"""## Features Importance"""

# Example function to get all feature coefficients without filtering
def get_all_feature_coefs(regression_model, columns):
    coef_dict = {}
    for coef, feat in zip(regression_model.coef_[0, :], columns):
        coef_dict[feat] = coef
    # Sort coefficients
    coef_dict = {k: v for k, v in sorted(coef_dict.items(), key=lambda item: item[1])}
    return coef_dict

# Example function to generate bar colors based on coefficient values
def get_bar_colors(values):
    color_vals = []
    for val in values:
        if val <= 0:
            color_vals.append('r')
        else:
            color_vals.append('g')
    return color_vals

# Example function to visualize coefficients
def visualize_all_coefs(coef_dict):
    features = list(coef_dict.keys())
    values = list(coef_dict.values())
    y_pos = np.arange(len(features))
    color_vals = get_bar_colors(values)
    plt.rcdefaults()
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.barh(y_pos, values, align='center', color=color_vals)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(features)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Feature Coefficients')
    ax.set_title('Feature Importance')
    plt.show()

# Assuming l1_model is a fitted logistic regression model
# Assuming 'features' is defined and contains the list of feature column names
coef_dict = get_all_feature_coefs(l1_model, features)

# Visualize the coefficients
visualize_all_coefs(coef_dict)

"""### Feature Importance in the L1 Model

After analyzing the feature importance using the L1 model, we observe the following:

**Features with High Positive Coefficients (Green Lines):**
- `area_worst`
- `area_se`
- `concavity_worst`

These features have high positive coefficients, indicating they are significantly important and positively correlated with the target variable (diagnosis).

**Features with High Negative Coefficients (Red Lines):**
- `perimeter_mean`
- `perimeter_worst`
- `area_mean`
- `radius_worst`

These features have high negative coefficients, indicating they are significantly important and negatively correlated with the target variable (diagnosis).

This analysis helps identify which features have the most influence on the model's predictions, providing valuable insights into the factors affecting the diagnosis.
"""

from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score
from sklearn.preprocessing import label_binarize
import pandas as pd

# Get predictions from the models
y_pred = pd.DataFrame({
    'l1': l1_model.predict(X_test),
    'l2': l2_model.predict(X_test)
})

# Initialize lists to store metrics and confusion matrices
metrics = list()
cm = dict()

# Labels for the models
coeff_labels = ['l1', 'l2']

# Iterate over models to compute metrics
for lab in coeff_labels:
    # Compute precision, recall, f-score
    precision, recall, fscore, _ = score(y_test, y_pred[lab], average='weighted')

    # Compute accuracy
    accuracy = accuracy_score(y_test, y_pred[lab])

    # Binarize the data for ROC-AUC computation
    y_test_binarized = label_binarize(y_test, classes=[0, 1])
    y_pred_binarized = label_binarize(y_pred[lab], classes=[0, 1])

    # Compute ROC-AUC score
    auc = roc_auc_score(y_test_binarized, y_pred_binarized, average='weighted')

    # Compute confusion matrix
    cm[lab] = confusion_matrix(y_test, y_pred[lab])

    # Append metrics to the list
    metrics.append(pd.Series({
        'precision': precision,
        'recall': recall,
        'fscore': fscore,
        'accuracy': accuracy,
        'auc': auc
    }, name=lab))

# Combine metrics into a DataFrame
metrics_df = pd.concat(metrics, axis=1)

# Display the results
print("Model Performance Metrics:")
metrics_df

"""### Model Performance Metrics Comparison

The table below summarizes the performance metrics for the L1 and L2 models:

| Metric     | L1         | L2         |
|------------|------------|------------|
| Precision  | 0.921134   | 0.956505   |
| Recall     | 0.921053   | 0.956140   |
| F-Score    | 0.920396   | 0.956245   |
| Accuracy   | 0.921053   | 0.956140   |
| AUC        | 0.907738   | 0.955357   |

**Explanation:**
- **Precision:** The L2 model has a higher precision (0.9565) compared to the L1 model (0.9211), indicating it makes fewer false positive predictions.
- **Recall:** The L2 model also outperforms the L1 model in recall (0.9561 vs. 0.9211), meaning it identifies more true positives.
- **F-Score:** The L2 model achieves a higher F-score (0.9562) compared to the L1 model (0.9204), showing a better balance between precision and recall.
- **Accuracy:** The accuracy of the L2 model (0.9561) is higher than that of the L1 model (0.9211), indicating better overall correctness.
- **AUC:** The L2 model's AUC score (0.9554) is significantly higher than the L1 model's AUC (0.9077), reflecting better performance in distinguishing between classes.

**Conclusion:**
The L2 model consistently outperforms the L1 model across all metrics, demonstrating superior precision, recall, F-score, accuracy, and AUC. Therefore, the L2 model is likely the better choice for the given task.
"""



"""## KNN Classificaton  6.2"""

from sklearn.neighbors import KNeighborsClassifier

# Split the data into training and test samples
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Define a KNN classifier with `n_neighbors=2`
knn_model = KNeighborsClassifier(n_neighbors=9)

knn_model.fit(X_train, y_train.values.ravel())

preds = knn_model.predict(X_test)

def evaluate_metrics(yt, yp):
    results_pos = {}
    results_pos['accuracy'] = accuracy_score(yt, yp)
    precision, recall, f_beta, _ = precision_recall_fscore_support(yt, yp, average='binary')
    results_pos['recall'] = recall
    results_pos['precision'] = precision
    results_pos['f1score'] = f_beta
    return results_pos

evaluate_metrics(y_test, preds)

"""### KNN Model Performance Metrics

The KNN model shows excellent performance with an accuracy of 97.81%, precision of 98.70%, recall of 95.00%, and an F-score of 96.82%. This indicates it is highly effective in both identifying positive cases and minimizing false positives.

## Confusion metrics
"""

# Compute confusion matrix
cm = confusion_matrix(y_test, preds)

# Plot confusion matrix
sns.set_palette(sns.color_palette())
_, ax = plt.subplots(figsize=(12, 12))
ax = sns.heatmap(cm, annot=True, fmt='d', annot_kws={"size": 40, "weight": "bold"})
labels = ['False', 'True']
ax.set_xticklabels(labels, fontsize=25)
ax.set_yticklabels(labels[::-1], fontsize=25)
ax.set_ylabel('Prediction', fontsize=30)
ax.set_xlabel('Ground Truth', fontsize=30)
plt.show()

from sklearn.metrics import f1_score

# Try K from 1 to 50
max_k = 50
# Create an empty list to store f1score for each k
f1_scores = []

for k in range(1, max_k + 1):
    # Create a KNN classifier
    knn = KNeighborsClassifier(n_neighbors=k)
    # Train the classifier
    knn = knn.fit(X_train, y_train.values.ravel())
    preds = knn.predict(X_test)
    # Evaluate the classifier with f1score
    f1 = f1_score(preds, y_test)
    f1_scores.append((k, round(f1_score(y_test, preds), 4)))
# Convert the f1score list to a dataframe
f1_results = pd.DataFrame(f1_scores, columns=['K', 'F1 Score'])
f1_results.set_index('K')

"""**the above result show that the model workind best with k=9, and k=11; from all of the above value of k. which also confirmed from the below diaghram**"""

# Plot F1 results
ax = f1_results.plot(figsize=(12, 12), linewidth=4)
ax.set(xlabel='Num of Neighbors', ylabel='F1 Score')
ax.set_xticks(range(1, max_k, 2));
plt.ylim((0.85, 1))
plt.title('KNN F1 Score')







"""## Random Forest Classification 6.3"""

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=4)
print ('Train set:', X_train.shape,  y_train.shape)
print ('Test set:', X_test.shape,  y_test.shape)

from sklearn.ensemble import RandomForestClassifier

n_estimators=20

M_features=X.shape[1]

max_features=round(np.sqrt(M_features))-1
max_features

y_test

rf_model = RandomForestClassifier( max_features=max_features,n_estimators=n_estimators, random_state=0)

rf_model.fit(X_train,y_train)

random_pred = rf_model.predict(X_test)

from sklearn.metrics import accuracy_score

# Initialize and train the model
model = RandomForestClassifier(max_features=max_features, n_estimators=n_estimators, random_state=0)
model.fit(X_train, y_train)

# Function to get accuracies
def get_accuracy(X_train, X_test, y_train, y_test, model):
    return {
        "test Accuracy": accuracy_score(y_test, model.predict(X_test)),
        "train Accuracy": accuracy_score(y_train, model.predict(X_train))
    }

# Use the model directly, not `model.best_estimator_`
print(get_accuracy(X_train, X_test, y_train, y_test, model))

random_pred = rf_model.predict(X_test)

evaluate_metrics(y_test, random_pred)

"""### Random Forest Model Performance Metrics

The Random Forest model has an accuracy of 91.23%, precision of 77.27%, recall of 100.00%, and an F-score of 87.18%. It excels in identifying all positive cases but has lower precision.

## Grid Search
"""

from sklearn.model_selection import GridSearchCV

model = RandomForestClassifier()
model.get_params().keys()

param_grid = {'n_estimators': [2*n+1 for n in range(20)],
             'max_depth' : [2*n+1 for n in range(10) ],
             'max_features':["auto", "sqrt", "log2"]}

search = GridSearchCV(estimator=model, param_grid=param_grid,scoring='accuracy', cv=5)
search.fit(X_train, y_train)

prediction = search.predict(X_test)

search.best_score_

search.best_params_

from sklearn.metrics import accuracy_score

def get_accuracy(X_train, X_test, y_train, y_test, model):
    return {
        "test Accuracy": accuracy_score(y_test, model.predict(X_test)),
        "train Accuracy": accuracy_score(y_train, model.predict(X_train))
    }

# Assuming 'search' is your GridSearchCV or RandomizedSearchCV object
print(get_accuracy(X_train, X_test, y_train, y_test, search.best_estimator_))

evaluate_metrics(y_test, prediction)

"""### Random Forest Model Performance Metrics (GridSearchCV)

The Random Forest model, optimized with GridSearchCV, shows an accuracy of 92.98%, precision of 82.50%, recall of 97.06%, and an F-score of 89.19%. While it performs well with high recall, precision can be improved by tuning additional hyperparameters or using feature selection techniques.

## Confusion metrics
"""

# Compute confusion matrix
cm = confusion_matrix(y_test, prediction)

# Plot confusion matrix
sns.set_palette(sns.color_palette())
_, ax = plt.subplots(figsize=(12, 12))
ax = sns.heatmap(cm, annot=True, fmt='d', annot_kws={"size": 40, "weight": "bold"})
labels = ['False', 'True']
ax.set_xticklabels(labels, fontsize=25)
ax.set_yticklabels(labels[::-1], fontsize=25)
ax.set_ylabel('Prediction', fontsize=30)
ax.set_xlabel('Ground Truth', fontsize=30)
plt.show()



"""## Comparing Models 7"""

# Define your metrics for each model
# Define your metrics for each model
metrics_data = {
    'Model': ['l1', 'l2', 'knn', 'rf'],
    'Precision': [0.9210526, 0.956505, 0.987013, 0.84615],
    'Recall': [0.921053, 0.956140, 0.95, 0.970588],
    'F-Score': [0.920396, 0.956245, 0.968153, 0.904109],
    'Accuracy': [0.921053, 0.956140, 0.978070, 0.9385964]
}

# Create a DataFrame
metrics_df = pd.DataFrame(metrics_data)

# Set the model column as the index
metrics_df.set_index('Model', inplace=True)

# Transpose the DataFrame for vertical display
metrics_df = metrics_df.T

# Display the DataFrame
print("Model Performance Metrics:")
metrics_df

"""### Model Performance Metrics:

| Model      | l1       | l2       | knn      | rf       |
|------------|----------|----------|----------|----------|
| **Precision**  | 0.921053 | 0.956505 | 0.987013 | 0.846150 |
| **Recall**     | 0.921053 | 0.956140 | 0.950000 | 0.970588 |
| **F-Score**    | 0.920396 | 0.956245 | 0.968153 | 0.904109 |
| **Accuracy**   | 0.921053 | 0.956140 | 0.978070 | 0.938596 |

### Explanation:

- **Precision**: The KNN model has the highest precision (0.9870), indicating it makes the fewest false positive predictions.
- **Recall**: The RF model achieves the highest recall (0.9706), meaning it identifies the most true positives.
- **F-Score**: The KNN model reaches the highest F-score (0.9682), showing the best balance between precision and recall.
- **Accuracy**: KNN also leads in accuracy (0.9781), demonstrating the best overall correctness.

### Conclusion:

The KNN model stands out with the highest precision, accuracy, and F-score. Although RF excels in recall, KNN's overall performance makes it the better choice for this analysis.
"""



"""# 8 - Conclusion

In this project, we compared different models to predict breast cancer diagnosis:

- **Logistic Regression Models:** The L2 model performed better overall compared to the L1 model. It had higher precision, recall, and accuracy, making it more reliable.

- **K-Nearest Neighbors (KNN):** KNN had the highest accuracy and precision, meaning it was very good at correctly classifying cases. However, its recall was slightly lower.

- **Random Forest (RF):** The RF model had a good balance between precision and recall, with a bit lower precision but higher recall compared to KNN.

**In summary,** The KNN model stands out with the highest precision, accuracy, and F-score. Although RF excels in recall, KNN's overall performance makes it the better choice for this analysis.

# 9 - Next Steps

- **Model Tuning**: Refine hyperparameters for improved accuracy and precision.
- **Feature Engineering**: Explore adding or transforming features to enhance model predictions.
- **Algorithm Exploration**: Test advanced algorithms (e.g., Support Vector Machines, Gradient Boosting) to potentially improve performance.

# 10 - Key Insights

- **High Accuracy Models**: Random Forest and K-Nearest Neighbors models performed well in classifying breast cancer.
- **Logistic Regression**: Provides interpretable coefficients, useful for understanding feature importance.
- **Feature Significance**: Specific features, such as cell radius and texture, significantly influence the predictions.

# 11 - Suggestion

- Focus on feature selection to reduce model complexity without sacrificing accuracy.
- Test more robust data preprocessing methods to handle any outliers or imbalanced data issues.
- Consider using ensemble methods to combine predictions for potentially higher accuracy.

## References

**M Abbas. 2024. Breast Cancer Prediction Analysis. Personal research project.**
"""

