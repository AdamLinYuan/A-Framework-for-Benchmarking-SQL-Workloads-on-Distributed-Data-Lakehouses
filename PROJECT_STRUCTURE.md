# Dissertation Project Structure

```
/Users/adamyuan/Documents/UofG/Yr 4/Dissertation/Code/
├── docker-compose.yml          # Main Docker configuration
├── requirements.txt            # Python dependencies
├── .venv/                     # Python virtual environment
├── .python-version           # Python version (3.11)
├── README.md                 # Project plan and documentation
│
├── trino/                    # Trino configuration
│   └── conf/
│       └── catalog/
│           ├── tpch.properties      # TPC-H connector
│           ├── iceberg.properties   # Iceberg connector
│           └── memory.properties    # Memory connector
│
├── data/                     # Data storage
│   └── warehouse/           # Iceberg warehouse data
│
├── scripts/                  # Python scripts
│   ├── test_setup.py        # Main setup test
│   └── week1_analysis.py    # Week 1 analysis scripts
│
├── notebooks/               # Jupyter notebooks
│   └── week1_exploration.ipynb
│
└── Python/                  # Legacy scripts (to be migrated)
    └── test_trino.py
```

## Quick Start

1. **Start Trino:**
   ```bash
   docker-compose up -d
   ```

2. **Install dependencies:**
   ```bash
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Test setup:**
   ```bash
   python scripts/test_setup.py
   ```

## Week 1 Goals Checklist

- [x] Trino installed locally using Docker
- [x] Connect via Python client and run simple queries
- [x] ~1GB benchmark dataset (TPC-H SF1)
- [x] Load data into Iceberg tables
- [x] Basic performance testing setup

## Data Available

- **TPC-H tiny**: Small test dataset
- **TPC-H SF1**: 1GB dataset with ~6M rows total
- **Iceberg**: Lakehouse format for advanced features
