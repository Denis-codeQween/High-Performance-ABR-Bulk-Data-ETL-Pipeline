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
Пример работы пайплайна в консоли (обработка более 1 млн записей за 26 секунд):

![Pipeline Execution Output](terminal_output.png)

```text
============================================================
☑ ABR DATA FILTERING & ETL PIPELINE
============================================================

[INFO] Parsing and filtering: 20261014_Public01.xml
[DEBUG] [20261014_Public01.xml] Processed:   100,000 | Matched: 1,487
[DEBUG] [20261014_Public01.xml] Processed:   200,000 | Matched: 2,702
[DEBUG] [20261014_Public01.xml] Processed:   300,000 | Matched: 4,141
[DEBUG] [20261014_Public01.xml] Processed:   400,000 | Matched: 5,385
[DEBUG] [20261014_Public01.xml] Processed:   500,000 | Matched: 6,784
[DEBUG] [20261014_Public01.xml] Processed:   600,000 | Matched: 8,004
[DEBUG] [20261014_Public01.xml] Processed:   700,000 | Matched: 9,311
[DEBUG] [20261014_Public01.xml] Processed:   800,000 | Matched: 10,649
[DEBUG] [20261014_Public01.xml] Processed:   900,000 | Matched: 11,838
[DEBUG] [20261014_Public01.xml] Processed: 1,000,000 | Matched: 13,199
[SUCCESS] Finished 20261014_Public01.xml. Total processed: 1,030,200, Filtered & Matched: 13,567

[INFO] Exporting clean filtered TSV file to: abr_filtered_output.tsv
[SUCCESS] Export complete. Total filtered rows in spreadsheet: 13,567
============================================================
☑ Finished in 26.07 seconds.
============================================================