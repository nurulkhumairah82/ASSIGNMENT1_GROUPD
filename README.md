# Assignment 1 - Household Income and Poverty Analysis

## Group Information

Group ID: A1-GROUPD

## Members

| Name | Matric Number | Role | Focus State |
|--------|--------|--------|--------|
| Member 1 | 311279 | Role  -  | W.P. Putrajaya |
| Member 2 | 311294 | Role  -  | W.P. Labuan |
| Nurul Khumairah Bt Sawlihim | 311397 | Role 5 - Intergration and Test Lead | Pahang |
| Member 4 | 312114 | Role  -  | Kelantan |
| Member 5 | 313429 | Role  -  | Perak 

---

## Dataset Information

Data Source:
1. DOSM Household Income State Dataset
2. DOSM Household Poverty State Dataset

Download Date:
- 20 October 2026

Data Location:
```text
data/raw/hh_income_state.json
data/raw/hh_poverty_state.json
```

---

## Setup Instructions

### Requirements

- Python 3.11 or newer
-NumPy

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Run Instructions

Open Jupyter Notebook and run:
```bash
jupyter notebook
```

Open:
```text
assignment1.ipynb
```

Run all cells from top to bottom.

Alternatively:
```bash
jupyter nbconvert --execute assignment1.ipynb
```

## Data Files 

Fallback Files Used:
- No

If the API is unavailable, use the fallback files provided on LMS and place them in:
```text
data/raw/
```

---

## Project Structure 

```text
A1_<group-id>/
├── README.md
├── CONTRIBUTIONS.md
├── solution.py
├── assignment1.ipynb
├── requirements.txt
└── data
    └── raw
        ├── hh_income_state.json
        └── hh_poverty_state.json
```

---


## Completion Checklist

- [x] Task 1 – Record Validation and Inspection
- [x] Task 2 – Indexing and Matrix Construction
- [x] Task 3 – Focus-State Vector Analysis
- [x] Task 4 – Matrix Analysis
- [x] Task 5.1 – State Profile Function
- [x] Task 5.2 – Tests and Assertions
- [x] Task 5.3 – Comparison and Interpretation
- [x] Task 5.4 – Reproducibility Check

---

## References

Department of Statistics Malaysia (DOSM).

- Household Income and Expenditure Survey (HIES)
- Household Income State Dataset
- Household Poverty State Dataset

Licensed under CC BY 4.0
