# Russian Shadow Tankers Analysis (OFAC SDN)

A Python-based data analysis project examining sanctioned maritime vessels using the U.S. Treasury OFAC SDN dataset.

The objective is to identify Russian-linked vessels within officially sanctioned entities and compare the results to broader public estimates of the Russian “shadow fleet”.

---

## 📌 Project Goal

Public reports estimate that Russia operates approximately 600–900 shadow tankers.  
This project investigates:

- How many vessels are officially sanctioned?
- How many of those appear Russian-linked?
- Which sanction programs dominate?
- Why official data differs from media estimates?

---

## 📊 Data Source

**U.S. Department of the Treasury – OFAC SDN List (CSV)**

- ~18,000 sanctioned entities
- 1,428 vessels identified
- Data format: government CSV (no headers, inconsistent metadata)

Important:
The SDN list contains only officially sanctioned entities.
It does NOT represent the full global shadow fleet.

---

## ⚙️ Methodology

1. Load raw OFAC SDN CSV (headerless format).
2. Assign column names manually.
3. Filter entities where `sdn_type = vessel`.
4. Perform heuristic country attribution using keyword matching in:
   - Sanction remarks
   - Vessel ownership information
5. Export structured datasets for analysis.

### Russian Attribution Keywords

Examples used for detection:

Russia, Russian Federation, Rosneft, Sovcomflot, Gazprom, Moscow, SCF, PAO

Attribution is heuristic and not a legal classification.

---

## 📈 Key Results

- Total sanctioned vessels: **1,428**
- Russian-linked sanctioned vessels: **215**
- Major sanction programs include:
  - RUSSIA-EO14024
  - IRAN-EO13902
  - UKRAINE-related regimes
  - GLOMAG

The identified 215 vessels represent a conservative subset of the broader
Russian shadow fleet often cited in media reports (600–900 vessels).

---

## 🛠 Tech Stack

- Python 3
- pandas
- pathlib

No external APIs required.  
Fully reproducible from raw OFAC SDN data.

---

## 🗂 Project Structure

Tankers/
├── data/
│ └── ofac_sdn.csv
├── output/
│ ├── shadow_tankers.csv
│ └── russian_shadow_tankers.csv
├── process.py
├── analysis.py
└── README.md

## ▶️ How to Run

1. Place `ofac_sdn.csv` inside the `data/` folder.
2. Run:

python download.py
python process.py
python analysis.py


3. Results will be generated in the `output/` directory.

---

## ⚠️ Limitations

- OFAC SDN does not provide complete vessel metadata.
- Flag and vessel type fields are often incomplete.
- Country attribution is heuristic.
- This project analyzes only officially sanctioned vessels.

---

## 📚 Educational Purpose

This project demonstrates:

- Working with messy government datasets
- Cleaning and structuring CSV data
- Heuristic entity classification
- Building a reproducible Python data pipeline
- Interpreting results with methodological limitations

---

## 🔎 Why Numbers Differ From Media Estimates

Media estimates of 600–900 Russian shadow tankers include:

- Non-sanctioned vessels
- Reflagged vessels
- Indirect ownership structures
- AIS-manipulated tankers

This project analyzes only vessels formally listed in the OFAC SDN database,  
which explains the lower figure (215 Russian-linked vessels).

