# CausalML Healthcare Readmission Analysis

This folder contains a causal analysis of 30-day hospital readmission risk in diabetic inpatient encounters using the Diabetes 130-US Hospitals dataset.

## What Is Implemented

Main notebook:
- healthcarecausalml.ipynb

Implemented workflow:
- Structural leakage removal for encounters that cannot be readmitted within 30 days.
- Outcome definition aligned to true 30-day readmission (`readmitted == "<30"`).
- Clinical feature engineering:
  - Primary diagnosis grouping from ICD-9 (`diag1_group`).
  - Medical specialty consolidation (`medical_specialty_group`).
- Two treatment analyses:
  - Primary: medication change during encounter (`change == "Ch"`).
  - Secondary: diabetes medication prescribed (`diabetesMed == "Yes"`).
- Confounding adjustment via a pre-treatment covariate set.
- Doubly robust effect estimation with AIPW.
- Positivity checks using propensity-score overlap plots.
- Trimming analysis using propensity in [0.05, 0.95].
- Subgroup effects for Circulatory and Diabetes diagnosis groups.

## Data and Cohort

- Source: Diabetes 130-US Hospitals 1999-2008 dataset.
- Leakage exclusions: `discharge_disposition_id` in `{11, 13, 14, 19, 20, 21}`.
- Final analysis cohort: 99,340 encounters.

## Causal Setup

### Outcome
- `readmit_30 = 1` if readmitted within 30 days, else `0`.

### Treatments
- `medication_change = 1` if medication changed during encounter.
- `diabetes_med_prescribed = 1` if diabetes medication prescribed.

### Adjustment Set
- age, race, gender
- admission_type_id, admission_source_id, payer_code
- number_inpatient, number_emergency, number_outpatient
- number_diagnoses, time_in_hospital
- medical_specialty_group, diag1_group

### Estimation
- Propensity model: logistic regression.
- Outcome nuisance models: gradient boosting for treated and control arms.
- Estimator: AIPW (Augmented Inverse Probability Weighting).

## Key Results

### Primary Treatment: Medication Change
- Treatment prevalence: 0.4643
- Observed risk difference: 0.0118
- AIPW ATE: 0.0074 (95% CI: 0.0034 to 0.0115)
- AIPW ATE (trimmed): 0.0075 (95% CI: 0.0035 to 0.0115)

Subgroups (trimmed):
- Circulatory: 0.0101 (95% CI: 0.0028 to 0.0175)
- Diabetes: -0.0082 (95% CI: -0.0234 to 0.0069)

### Secondary Treatment: Diabetes Medication Prescribed
- Treatment prevalence: 0.7723
- Observed risk difference: 0.0197
- AIPW ATE: 0.0151 (95% CI: 0.0111 to 0.0190)
- AIPW ATE (trimmed): 0.0151 (95% CI: 0.0112 to 0.0191)

Subgroups (trimmed):
- Circulatory: 0.0242 (95% CI: 0.0170 to 0.0314)
- Diabetes: -0.0046 (95% CI: -0.0171 to 0.0079)

## Interpretation

- Both treatment definitions show a positive adjusted association with 30-day readmission.
- Adjusted effects are smaller than naive differences, consistent with confounding adjustment.
- Full and trimmed estimates are close, suggesting adequate overlap.
- Effects are stronger in circulatory-primary-diagnosis encounters and weaker/uncertain in diabetes-primary-diagnosis encounters.

## Limitations

- Results remain observational and rely on no-unmeasured-confounding assumptions.
- Estimates depend on current feature definitions, adjustment set, and model choices.
- No bootstrap confidence intervals or formal sensitivity analysis yet.

## Recommended Next Steps

- Add bootstrap intervals for AIPW estimates.
- Add insulin-specific escalation treatment definitions.
- Add sensitivity analysis for hidden confounding and model robustness.