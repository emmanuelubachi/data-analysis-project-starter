# 📁 Data Directory Structure

This folder contains all datasets used throughout the data analysis project, organized according to their processing stage.  
Each subfolder serves a specific purpose — ensuring clarity, reproducibility, and efficient data handling.

---

## **Folder Overview**

### **`source/`**

Stores original and reference data inputs.

- **`raw/`** — Unmodified datasets directly collected from sources (e.g., CSVs, databases, APIs, web scrapes).  
  _➡ Do not edit these files manually._

- **`external/`** — Third-party or external datasets (e.g., open data, partner data, public APIs).  
  _➡ Keep original structure and include citation/source info._

- **`lookup/`** — Reference and mapping tables (e.g., country codes, category mappings, metadata files).  
  _➡ Use for joins, standardization, or enrichment._

---

### **`staging/`**

Intermediate data storage for preprocessed or merged datasets.  
Used for testing transformations, schema alignment, or temporary joins before full cleaning.

---

### **`EDA/`**

Data used during **Exploratory Data Analysis (EDA)** — cleaned and profiled versions of source data.

- **`cleaned/`** — Clean, filtered, and lightly transformed datasets ready for exploration and visualization.
- **`interim/`** — Temporary analysis outputs, summary tables, or feature exploration data.

---

### **`processed/`**

Fully cleaned and transformed datasets ready for formal analysis, modeling, or feature engineering.  
_➡ These files represent the most stable and reusable data assets._

---

### **`final/`**

Final, production-ready datasets used for visualization, dashboards, or reporting.  
_➡ Serve as the ultimate output of your data pipeline._

---

### **`validation/`**

Validation and quality control outputs.

- Schema or integrity check results
- Data profiling reports
- Duplicates or missing value logs

---

## **Folder Structure**

```bash
├── data/
│   ├── validation/                # Temporary data validation or manual checks
│   ├── EDA/
│   │   ├── cleaned/               # Cleaned datasets used in exploration
│   │   ├── interim/               # Intermediate processed data
│   │   ├── final/                 # Final datasets for reporting or visualization
│   │   └── processed/             # Processed datasets ready for analysis
│   ├── source/
│   │   ├── external/              # External data sources (APIs, public datasets)
│   │   ├── lookup/                # Reference tables, keys, mappings
│   │   └── raw/                   # Raw input data (untouched)
│   └── staging/                   # Temporary workspace for loading or transformations

```

---

## **Best Practices**

1. **Do not overwrite raw data.** Always create new versions in `staging` or `processed`.
2. **Document all transformations** (e.g., via scripts or notebooks).
3. **Use consistent naming conventions** (e.g., `snake_case`, include date/version if needed).
4. **Keep large files out of version control** (use `.gitignore` for raw or interim data).
5. **Add metadata or data dictionaries** in each folder when applicable.

---

## **Example Data Flow**
