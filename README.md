# Network Intrusion Detection

Binary classification model detecting network attacks 
using the NSL-KDD dataset and scikit-learn.

## Status
🚧 In progress — Sprint 1/4

## Stack
- Python, scikit-learn, pandas, matplotlib, seaborn

## Dataset
NSL-KDD — 125,973 training samples, 22,544 test samples,
41 network connection features, binary classification (normal/attack)

## Results so far
| Model | Precision (attack) | Recall (attack) | F1 |
|---|---|---|---|
| Logistic Regression (baseline) | 0.92 | 0.64 | 0.75 |

## Project structure
    notebooks/   — EDA and modeling
    src/         — reusable modules
    data/        — raw data (not tracked)
    docs/        — theory notes
