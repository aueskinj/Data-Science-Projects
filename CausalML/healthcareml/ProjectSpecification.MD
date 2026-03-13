# Data Science Project Specification: Causal Analysis of Diabetes Readmission Rates

## 1. Project Title
Evaluating observational causal effects of inpatient diabetes treatment intensity on 30-day readmission risk.

## 2. Current Scope Covered in Notebook
This specification reflects what is implemented and executed in the notebook.

Primary implementation file:
- healthcarecausalml.ipynb

Current notebook coverage:
- Structural leakage removal for impossible-readmission encounters.
- Outcome definition aligned to true 30-day readmission.
- Clinical feature engineering for diagnosis and specialty grouping.
- Primary treatment analysis: medication change during encounter.
- Secondary treatment analysis: diabetes medication prescribed.
- Doubly robust effect estimation using AIPW.
- Positivity diagnostics and trimming (0.05 to 0.95).
- Subgroup effect summaries for Circulatory and Diabetes diagnosis groups.

## 3. Data Source
- Dataset: Diabetes 130-US hospitals for years 1999-2008 (UCI / Health Facts extract in project zip).
- Effective cohort after leakage filtering: 99,340 encounters.

## 4. Implemented Causal Design
### 4.1 Outcome
- `readmit_30 = 1` if `readmitted == "<30"`, else `0`.

### 4.2 Leakage Handling
- Excluded `discharge_disposition_id` in `{11, 13, 14, 19, 20, 21}` to remove encounters structurally ineligible for 30-day readmission.

### 4.3 Treatment Definitions
- Primary treatment: `medication_change = 1` when `change == "Ch"`.
- Secondary treatment: `diabetes_med_prescribed = 1` when `diabetesMed == "Yes"`.

### 4.4 Adjustment Set (Pre-treatment Confounders)
- age, race, gender
- admission_type_id, admission_source_id, payer_code
- number_inpatient, number_emergency, number_outpatient
- number_diagnoses, time_in_hospital
- medical_specialty_group, diag1_group

### 4.5 Estimation Workflow
- Propensity model: LogisticRegression with balanced class weights.
- Outcome nuisance models: separate GradientBoostingClassifier models for treated and control.
- Estimator: Augmented Inverse Probability Weighting (AIPW).
- Diagnostics:
  - Propensity overlap histogram.
  - Trimming to overlap region: propensity in [0.05, 0.95].

## 5. Results Covered
### 5.1 Primary Treatment: Medication Change
- Treatment prevalence: 0.4643.
- Observed readmission rates:
  - No medication change: 0.1084
  - Medication change: 0.1202
- Observed risk difference: 0.0118.
- AIPW ATE: 0.0074, 95% CI [0.0034, 0.0115].
- AIPW ATE (trimmed): 0.0075, 95% CI [0.0035, 0.0115].

Subgroup effects (trimmed):
- Circulatory: 0.0101, 95% CI [0.0028, 0.0175].
- Diabetes: -0.0082, 95% CI [-0.0234, 0.0069].

### 5.2 Secondary Treatment: Diabetes Medication Prescribed
- Treatment prevalence: 0.7723.
- Observed readmission rates:
  - No diabetes medication prescribed: 0.0987
  - Diabetes medication prescribed: 0.1184
- Observed risk difference: 0.0197.
- AIPW ATE: 0.0151, 95% CI [0.0111, 0.0190].
- AIPW ATE (trimmed): 0.0151, 95% CI [0.0112, 0.0191].

Subgroup effects (trimmed):
- Circulatory: 0.0242, 95% CI [0.0170, 0.0314].
- Diabetes: -0.0046, 95% CI [-0.0171, 0.0079].

## 6. Interpretation Implemented
- Both treatment definitions are associated with higher adjusted 30-day readmission risk.
- Adjusted effects are smaller than naive observed differences, consistent with confounding adjustment reducing bias magnitude.
- Trimmed and full-sample AIPW estimates are very close, indicating acceptable overlap for the implemented treatment definitions.
- Effect heterogeneity is present, with stronger positive effects in circulatory primary diagnoses and weaker/uncertain effects in diabetes primary diagnoses.

## 7. Current Deliverables in Repository
- Executable notebook with full causal workflow and outputs.
- Visual overlap diagnostics for each treatment.
- Table outputs for naive vs adjusted effects and subgroup effects.
- Final conclusions section in notebook summarizing report-ready findings.

## 8. Limitations Explicitly Acknowledged
- Observational assumptions remain required, especially no important unmeasured confounding.
- Estimates are conditional on current variable encoding, adjustment set, and model class choices.
- This notebook does not yet include bootstrap confidence intervals or sensitivity analysis for hidden bias.

## 9. Recommended Next Extensions
- Add bootstrap confidence intervals for AIPW estimates.
- Add insulin-specific escalation treatment definitions.
- Add formal sensitivity analyses for unmeasured confounding and model robustness.

