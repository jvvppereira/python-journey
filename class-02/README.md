# 📊 Python Insights – Customer Cancellation Analysis

This project demonstrates a simple **data analysis workflow** using **Python** to investigate customer cancellations and identify possible actions to reduce churn.

The analysis is performed in a **Jupyter Notebook** using **Pandas** for data manipulation and **Plotly** for interactive visualizations.

---

# 📁 Project Structure

```
.
├── analysis.ipynb      # Jupyter notebook containing the data analysis
├── cancelations.csv    # Dataset used in the analysis
└── README.md
```

---

# 🎯 Project Objective

A company with more than **800,000 customers** noticed that a large portion of its customers had **already canceled their services**.

The goal of this project is to:

* analyze the dataset
* identify patterns related to cancellations
* understand the main causes of churn
* propose actions to reduce customer cancellations

---

# 📦 Dataset

The dataset contains customer information such as:

| Column                 | Description                                    |
| ---------------------- | ---------------------------------------------- |
| CustomerID             | Unique identifier for each customer            |
| idade                  | Customer age                                   |
| sexo                   | Gender                                         |
| tempo_como_cliente     | Time as a customer                             |
| frequencia_uso         | Service usage frequency                        |
| ligacoes_callcenter    | Number of calls to support                     |
| dias_atraso            | Payment delay in days                          |
| assinatura             | Subscription type                              |
| duracao_contrato       | Contract duration                              |
| total_gasto            | Total amount spent                             |
| meses_ultima_interacao | Months since last interaction                  |
| cancelou               | Cancellation status (1 = canceled, 0 = active) |

---

# ⚙️ Requirements

Before running this project, you must install **Python**.

Download it from the official website:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

---

# 📚 Install Required Libraries

This project uses the following libraries:

* **Pandas** → data processing
* **Plotly** → charts and visual analysis

Install them with:

```bash
pip install pandas plotly
```

If you plan to run the notebook locally, you should also install **ipykernel** and **Jupyter Notebook**:

```bash
pip install notebook ipykernel
```

---

# ▶️ Running the Analysis

1. Clone or download the repository
2. Install the required dependencies
3. Open the notebook

```bash
jupyter notebook
```

4. Open:

```
analysis.ipynb
```

5. Run the cells sequentially to reproduce the analysis.

---

# 🔎 Analysis Steps

The notebook follows a simple data analysis workflow:

### 1. Import the dataset

Load the CSV file using **Pandas**.

### 2. Explore the data

Inspect the dataset and remove unnecessary columns.

### 3. Clean the data

Handle missing values and verify data types.

### 4. Analyze cancellation rates

Calculate the number and percentage of cancellations.

### 5. Visualize patterns

Use **Plotly** histograms to understand how each variable influences cancellations.

---

# 📈 Key Insights

The analysis revealed several patterns related to cancellations:

**1️⃣ Monthly contracts have a very high cancellation rate**

Recommendation:

* Encourage customers to switch to **annual or quarterly plans**
* Offer discounts or incentives for longer contracts

---

**2️⃣ Customers who call support more than 4 times tend to cancel**

Recommendation:

* Improve the **customer support workflow**
* Ensure issues are solved in **3 calls or fewer**

---

**3️⃣ Customers with payment delays greater than 20 days tend to cancel**

Recommendation:

* Implement early **payment reminders**
* Offer solutions before reaching **15 days of delay**

---

# 📊 Impact Simulation

After applying filters based on these recommendations, the notebook simulates the potential reduction in cancellations.

The comparison shows:

* cancellation rate **before actions**
* cancellation rate **after applying improvements**

This helps estimate the impact of operational changes.

---

# 🎓 Educational Purpose

This project demonstrates a simple **end-to-end data analysis workflow**, including:

* data cleaning
* exploratory analysis
* visualization
* business insights generation

It is intended for **learning data analysis with Python**.

---

# 📜 License

This project is intended for **educational and demonstration purposes**.

---

⭐ If this project helped you learn **Python data analysis**, consider starring the repository.
