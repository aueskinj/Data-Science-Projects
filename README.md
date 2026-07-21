# Data Science Projects

A collection of notebooks covering exploratory data analysis, causal inference, supervised learning, and NLP fine-tuning across economic, healthcare, and business datasets.

## Contents

1. [Student Performance Indicator](#1-student-performance-indicator)
2. [Government Social Programs and Poverty in Kenya](#2-government-social-programs-and-poverty-in-kenya)
3. [Petroleum Price Changes and Demand in Kenya](#3-petroleum-price-changes-and-demand-in-kenya)
4. [Taxation and SME Performance](#4-taxation-and-sme-performance)
5. [Fine-Tuning an English-Swahili Translation Model](#5-fine-tuning-an-english-swahili-translation-model)
6. [Lyrics Finder](#6-lyrics-finder)
7. [English-Kiswahili Translation Notebook](#7-english-kiswahili-translation-notebook)
8. [PandemAI](#8-pandemai)
9. [Supervised Learning with SVM](#9-supervised-learning-with-svm)
10. [Supervised Learning with Random Forests](#10-supervised-learning-with-random-forests)
11. [Customer Churn Prediction](#11-customer-churn-prediction)
12. [Causal Inference with Bayesian Networks](#12-causal-inference-with-bayesian-networks)

---

## 1. Student Performance Indicator

[Notebook](https://colab.research.google.com/github/aueskinj/Data-Science-Projects/blob/main/EDA_STUDENT_PERFORMANCE_.ipynb)

End-to-end EDA on student performance data: problem definition, data checks, preprocessing, model training, and model selection.

## 2. Government Social Programs and Poverty in Kenya

[Notebook](https://colab.research.google.com/github/aueskinj/Data-Science-Projects/blob/main/Effect_of_government_social_programs_on_poverty_in_Kenya.ipynb)

Descriptive and correlation analysis of how government social programs relate to poverty levels in Kenya.

## 3. Petroleum Price Changes and Demand in Kenya

[Notebook](https://colab.research.google.com/github/aueskinj/Data-Science-Projects/blob/main/Effect_of_petroleum_prices_changes_on_the_demand_for_petroleum_in_Kenya.ipynb)

Correlation and descriptive analysis of petroleum price changes against demand trends in the Kenyan market.

## 4. Taxation and SME Performance

[Notebook](https://colab.research.google.com/github/aueskinj/Data-Science-Projects/blob/main/Effect_of_taxation_on_sme_performance.ipynb)

Frequency and descriptive analysis of how taxation affects the performance of small and medium enterprises.

## 5. Fine-Tuning an English-Swahili Translation Model

[Notebook](https://colab.research.google.com/github/aueskinj/Data-Science-Projects/blob/main/FineTuningEngSwaModel.ipynb)

Fine-tunes a translation model using TensorFlow and Keras, with preprocessing, training, and evaluation steps.

## 6. Lyrics Finder

[Notebook](https://colab.research.google.com/github/aueskinj/Data-Science-Projects/blob/main/LyricsFinder.ipynb)

Scrapes Genius.com for an artist's song URLs, then fetches and parses lyrics with BeautifulSoup.

## 7. English-Kiswahili Translation Notebook

[Notebook](https://colab.research.google.com/github/aueskinj/Data-Science-Projects/blob/main/eng_kisw_traslation_notebook.ipynb)

Fine-tunes an English-Kiswahili translation model on GPU runtime.

## 8. PandemAI

[Notebook](https://colab.research.google.com/github/aueskinj/Data-Science-Projects/blob/main/pandemai.ipynb)

Data cleaning and formatting pipeline supporting the broader PandemAI project.

## 9. Supervised Learning with SVM

[Notebook](https://colab.research.google.com/github/aueskinj/Data-Science-Projects/blob/main/supervised_learning(SVM).ipynb)

Trains and evaluates a Support Vector Machine classifier on a supervised learning task.

## 10. Supervised Learning with Random Forests

[Notebook](https://colab.research.google.com/github/aueskinj/Data-Science-Projects/blob/main/supervised_learning(randomForests).ipynb)

Attribute selection, model training, and evaluation (confusion matrix, classification report) for a Random Forest classifier.

## 11. Customer Churn Prediction

[Notebook](https://github.com/aueskinj/Data-Science-Projects/blob/main/Customer_Churn_Prediction.ipynb)

Predicts customer churn on retail customer data using Random Forest, AdaBoost, SVC, and XGBoost, compared by accuracy and confusion matrix.

**Dependencies:** pandas 1.5.3, numpy 1.24.3, matplotlib 3.8.0, seaborn 0.14.0, scikit-learn 1.3.0, xgboost 2.1.0

**Data:** [Online Retail Customer Churn Dataset](https://www.kaggle.com/datasets/)

## 12. Causal Inference with Bayesian Networks

[Notebook](https://github.com/aueskinj/Data-Science-Projects/blob/main/CausalML/healthcareml/healthcarecausalml.ipynb)

Estimates the causal effect of treatment decisions on 30-day hospital readmission using the Diabetes 130-US Hospitals (1999-2008) dataset, after removing encounters that cannot structurally be readmitted within 30 days.

**Cohort:** 99,340 encounters, after excluding discharge dispositions `{11, 13, 14, 19, 20, 21}`.

**Treatments analyzed:**
- Medication change during encounter (primary)
- Diabetes medication prescribed (secondary)

**Method:** Logistic regression propensity model, gradient boosting outcome models, AIPW (doubly robust) estimation, with positivity checks and trimming at propensity [0.05, 0.95].

**Results:**

| Treatment | Prevalence | AIPW ATE (trimmed) | 95% CI |
|---|---|---|---|
| Medication change | 0.464 | 0.0075 | 0.0035 to 0.0115 |
| Diabetes medication prescribed | 0.772 | 0.0151 | 0.0112 to 0.0191 |

Both treatments show a positive adjusted association with readmission risk, smaller than the naive difference, consistent with confounding adjustment. Effects are stronger in circulatory-diagnosis encounters and weaker or uncertain in diabetes-diagnosis encounters.

**Limitations:** Estimates rely on no-unmeasured-confounding assumptions and current feature definitions. No bootstrap intervals or formal sensitivity analysis yet.

**Next steps:** Bootstrap intervals for AIPW estimates, insulin-specific treatment definitions, sensitivity analysis for hidden confounding.

---

## Getting Started

**Requirements:** Python 3.x, Jupyter, and the libraries listed per notebook (TensorFlow, Keras, scikit-learn, pandas, BeautifulSoup, etc.)

```bash
git clone https://github.com/aueskinj/Data-Science-Projects.git
cd Data-Science-Projects
```

Open any notebook in Jupyter or via the Colab links above.

### Author

Kimuhu Njuguna
