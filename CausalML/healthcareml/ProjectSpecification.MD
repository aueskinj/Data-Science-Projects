# Data Science Project Charter: Causal Analysis of Diabetes Readmission Rates

## 1. Project Title
**Evaluating the Causal Impact of HbA1c Measurement on Hospital Readmission Rates for Diabetic Patients**

## 2. Project Goal
To **quantify the causal effect** of HbA1c measurement on hospital readmission rates for diabetic patients, and to demonstrate how causal inference methods can enhance the predictive power and explainability of machine learning (ML) models. This project aims to go beyond simple correlation analysis and establish true causal relationships that can inform healthcare policy and practice.

## 3. Objectives

* Develop a **causal model** representing the relationships between patient characteristics, HbA1c measurement, and readmission rates.
* **Identify and control for potential confounding variables** that may bias the observed relationships.
* **Estimate the causal effect** of HbA1c measurement on readmission rates using appropriate causal inference techniques.
* Compare the performance of **causal ML models** with standard non-causal ML models in terms of prediction accuracy and explainability.
* **Interpret the findings** to provide actionable insights for healthcare providers and policymakers.
* Evaluate the **direct and indirect effects** of different variables using the mediation formula.
* **Test the validity of causal assumptions** using graphical and statistical methods.
* Explore the **potential for counterfactual analysis** to evaluate different intervention scenarios.

## 4. Data Source
The primary data source will be the **"Diabetes 130-US hospitals for years 1999-2008" dataset from the UCI Machine Learning Repository**. This dataset includes over 70,000 clinical database patient records and contains a variety of patient-related attributes, including demographics, medical history, lab results, medication information, and readmission status.

### Specific Data Points to be Used:
* **HbA1c test results**: The primary treatment variable crucial for examining its causal effect.
* **Readmission Status**: Indicates if the patient was readmitted and is the primary outcome variable.
* **Patient Demographics**: Age, gender, race.
* **Medical History**: Diagnoses, previous admissions, and other medical conditions.
* **Medication Information**: Details of prescriptions during the stay.
* **Other Lab Results**: Relevant variables to address potential confounding.

## 5. Causal Inference Methods

* **Causal Diagrams**: Construct causal diagrams to visualize the hypothesized relationships between variables, clarify assumptions, and guide method selection.
* **Intervention Analysis**: Use intervention analysis to estimate how manipulating specific factors, such as HbA1c testing, affects readmission rates, employing methods like the *do(x)* operator.
* **Confounding Control**: Control potential confounders using techniques such as the **back-door criterion**.
* **Structural Equation Modelling (SEM)**: Utilize SEM to model causal pathways and graphically understand variable relationships.
* **EconML Library**:
  * Estimate **Heterogeneous Treatment Effects** using methods like **Double Machine Learning (DML)** and **Doubly Robust (DR)** estimators.
  * Explore **Instrumental Variables (IV)** methods if appropriate IVs can be identified.
  * Apply **Meta Learners** such as T-Learner, S-Learner, and X-Learner.
  * Investigate the effects of **policy changes** on readmission rates.
  * Interpret models using tools like **Tree Interpreter and SHAP**.
* **Counterfactual Analysis**: Explore hypothetical scenarios, such as "What would the readmission rate be if a specific patient did not have a HbA1c test?" to assess intervention impacts.

## 6. Machine Learning Models

* **Causal ML Models**: Create and evaluate causal models using the methods outlined.
* **Non-Causal ML Models**: Train and test standard ML models (e.g., regression, classification, decision trees) for comparison.
* **Performance Metrics**: Evaluate models using accuracy, precision, recall, F1-score, and AUC, with a focus on explainability and predictive accuracy.

## 7. Expected Outcomes

* Quantified causal effect of HbA1c measurement on hospital readmission rates.
* Identification of key confounding factors affecting readmission rates.
* Demonstration of how causal inference improves ML model predictive power and explainability compared to purely statistical models.
* Actionable insights for healthcare providers and policymakers regarding the optimal use of HbA1c testing.
* A validated causal model for future research and policy analysis.

## 8. Project Timeline

* **Phase 1 (4 weeks)**: Data exploration, pre-processing, and development of the causal diagram.
* **Phase 2 (6 weeks)**: Implementation of causal inference methods and model development using EconML.
* **Phase 3 (4 weeks)**: Comparison of causal and non-causal ML models, and interpretation of results.
* **Phase 4 (2 weeks)**: Documentation, report writing, and presentation.

## 9. Project Team

* Data Scientists
* Machine Learning Engineers
* Domain Expert (Healthcare)

## 10. Deliverables

* Comprehensive report on methodology and findings.
* Documented, reproducible code base.
* Presentation summarizing results.
* Visualized causal model diagram.
* Comparison of causal and non-causal ML models.

## 11. Project Success Criteria

* Successful implementation of planned causal inference methods.
* Quantifiable evidence of causal effects of HbA1c measurement.
* Demonstrated improvement in model explainability.
* Identification of key confounding variables and causal pathways, including direct and indirect effects.
* Actionable insights for healthcare improvement.

This charter provides a clear framework for conducting causal analysis. By using the diabetes dataset and applying rigorous causal inference techniques, this project will demonstrate how causality improves ML models and deepens understanding of factors influencing hospital readmission rates.

