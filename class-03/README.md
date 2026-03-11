# Python AI Project – Customer Credit Score Prediction

## 📌 Project Overview

This project demonstrates a simple **Artificial Intelligence / Machine Learning workflow in Python** to predict a customer's **credit score** based on their financial and behavioral information.

The model analyzes customer data and classifies the credit score into three categories:

* **Poor**
* **Fair**
* **Good**

The goal is to simulate a real-world banking scenario where a bank needs an automated system to evaluate customer creditworthiness.

---

## 🧠 Business Case

You were hired by a bank to build a system capable of **automatically determining the credit score of customers**.

Using historical customer data, a machine learning model is trained to recognize patterns and predict the credit score of new customers.

---

## 📂 Dataset

The dataset contains several attributes related to customers such as:

* Profession (`profissao`)
* Credit mix (`mix_credito`)
* Payment behavior (`comportamento_pagamento`)
* Other financial information

Dataset files:
https://drive.google.com/drive/folders/1FbDqVq4XLvU85VBlVIMJ73p9oOu6u2-J?usp=drive_link

Main files used:

* `customers.csv` – training dataset
* `new-customers.csv` – dataset used for predictions

---

## ⚙️ Technologies Used

* Python
* Pandas
* Scikit-learn

Main libraries:

```
pandas
scikit-learn
```

Install dependencies:

```bash
pip install pandas scikit-learn
```

---

## 🚀 Project Workflow

### Step 1 – Import the Dataset

The project starts by loading the customer dataset using **Pandas**.

```python
import pandas as pd

table = pd.read_csv("customers.csv")
```

---

### Step 2 – Data Preprocessing

Some dataset columns contain **categorical text values**, which must be converted into numbers for machine learning models.

Example columns:

* profession
* credit mix
* payment behavior

This conversion is done using **LabelEncoder**.

```python
from sklearn.preprocessing import LabelEncoder
```

---

### Step 3 – Train Machine Learning Models

Two machine learning models are used:

* **Random Forest Classifier**
* **K-Nearest Neighbors (KNN)**

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
```

The dataset is divided into:

* **Training data (70%)**
* **Testing data (30%)**

Using:

```python
from sklearn.model_selection import train_test_split
```

---

### Step 4 – Model Evaluation

Both models generate predictions, which are evaluated using **accuracy score**.

```python
from sklearn.metrics import accuracy_score
```

The model with the best performance is selected.

---

### Step 5 – Predict New Customer Scores

After selecting the best model (Random Forest), the system predicts credit scores for **new customers**.

```python
predict = decision_tree_model.predict(new_customers_table)
```

The prediction is added as a new column:

```
previsao
```

---

## 📊 Example Output

| Customer   | Predicted Credit Score |
| ---------- | ---------------------- |
| Customer A | Good                   |
| Customer B | Fair                   |
| Customer C | Poor                   |

---

## 📈 Possible Improvements

The model could be improved by:

* Using **GridSearch for hyperparameter tuning**
* Training with **larger datasets**
* Testing **additional machine learning algorithms**
* Performing **feature engineering**

---

## 🎯 Learning Objectives

This project demonstrates fundamental concepts of:

* Data preprocessing
* Machine learning model training
* Model evaluation
* Credit risk prediction
* Using Scikit-learn in real-world scenarios

---

## 📜 License

This project is for **educational purposes**.
