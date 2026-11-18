# 🚀 ABR Bulk Data Streaming ETL Pipeline

## 📌 Overview
A high-performance, memory-efficient ETL (Extract, Transform, Load) pipeline built in Python to process massive Australian Business Register (ABR) bulk XML datasets. The pipeline streams multi-gigabyte XML files, filters target legal entity types, and exports clean, structured datasets ready for business analysis and Excel reporting.

---

## 🛠️ Tech Stack & Libraries
- **Language:** Python 3.x
- **Parsing:** `lxml` (`etree.iterparse`) — for high-speed, memory-efficient streaming XML processing.
- **Data Management:** `pandas`, built-in `csv` module.
- **Output Format:** TSV (Tab-Separated Values) with `UTF-8-SIG` encoding for seamless Excel integration.

---

## ⚙️ Key Architectural Features
1. **Zero OOM (Out-of-Memory) Risk:** Utilizes iterative event-driven parsing (`iterparse`) combined with DOM node clearing (`elem.clear()`) to process arbitrarily large XML files with a constant, minimal memory footprint.
2. **Robust Delimiter Management:** Switches from standard CSV to TSV formatting to completely eliminate data corruption caused by commas within corporate organization names.
3. **Strict Business Logic Filtering:** Automated filtering tailored to extract specific legal structures: **Public Company Limited by Guarantee** (`PUB`) and **Other Incorporated Entity** (`OIE`).

---

## 💻 Execution Output & Performance
Console benchmark demonstrating streaming extraction of **1,000,000+ XML records in 26 seconds**:

![Pipeline Execution Output](terminal_output.png)

---

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Denis-codeQween/High-Performance-ABR-Bulk-Data-ETL-Pipeline.git
   cd High-Performance-ABR-Bulk-Data-ETL-Pipeline
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the streaming ETL pipeline:**
   ```bash
   python main.py
   ```
