# Nuclear Cross-Section Prediction

This project implements a **polynomial regression model** in Python to predict nuclear cross-section data based on incident energy.  
The dataset used is experimental data from Hermann et al. (1999), which contains energy and corresponding renormalized cross-section values.

---

## 📊 Project Overview

- **Goal:** Predict nuclear cross-sections based on user-provided energy values.
- **Model Used:** Polynomial Regression (degree 4)
- **Tools:** Python, Pandas, Scikit-Learn, Matplotlib

---

## 📁 Dataset

- **File:** `hermanne1999.csv`
- **Features:**
  - `EN(MeV)` – Incident Energy in MeV
  - `Renormalized CS(mB)` – Renormalized Cross-Section in millibarns

---

## ⚙️ How to Run

1. Make sure you have the required Python packages:
   ```bash
   pip install pandas scikit-learn matplotlib numpy
2. Run the Python script
3. The program will ask you to enter an energy value in MeV.
4. The program will display the predicted cross-section.
