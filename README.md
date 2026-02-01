# CSV Data Explorer 📊

A simple **Streamlit app** to upload, explore, and visualize CSV data.  
Easily preview your dataset, generate charts, and download visualizations.  

---

## Features

- Upload any CSV file for analysis.  
- Preview the dataset and its first rows.  
- Dataset summary:
  - Total rows and columns  
  - Numeric vs non-numeric columns  
  - Missing values per column  
  - Descriptive statistics for numeric columns  
- Interactive visualization:
  - Choose X-axis and multiple Y-axis columns  
  - Multiple chart types: Line, Bar, Scatter, Area, Histogram, Box Plot  
  - Pick chart color, width, and height  
  - Download chart as PNG  
---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/0samaHaider/streamlit-csv-data-explorer.git
cd csv-data-explorer
````

2. Create a virtual environment (optional but recommended):

```bash
python -m venv .venv
```

3. Activate the virtual environment:

* **Windows**:

```bash
.venv\Scripts\activate
```

* **Mac/Linux**:

```bash
source .venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

* The app will open in your browser at `http://localhost:8501`.
* Upload a CSV file and navigate through **Data Preview**, **Visualization**, and **Summary & Report** using the sidebar.

---

## Dependencies

* Python 3.8+
* [Streamlit](https://streamlit.io/)
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)

You can also install all dependencies at once:

```bash
pip install streamlit pandas matplotlib seaborn
```

---
