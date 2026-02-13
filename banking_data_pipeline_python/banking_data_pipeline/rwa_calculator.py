import logging
import os
import sqlite3
from pathlib import Path

import pandas as pd
from pandas import DataFrame

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class CreditRiskETL:
    def __init__(self, db_name: str = "banking_risk.db"):
        self.db_name = db_name

    def extract(self, file_path: str) -> DataFrame:
        logging.info(f"Extracting data from {file_path}")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Source file {file_path} missing.")
        return pd.read_csv(file_path)

    def transform(self, df: DataFrame) -> DataFrame:
        logging.info("Starting transformation: Calculating RWA")

        # 1. Data Cleaning: Remove invalid exposure
        valid_df = df[df["exposure_at_default"] > 0].copy()
        dropped = len(df) - len(valid_df)
        if dropped > 0:
            logging.warning(f"Dropped {dropped} rows with invalid exposure values.")

        # 2. RWA Calculation: RWA = EAD * PD * LGD * 12.5
        # Using 12.5 as the standard Basel multiplier for demo purposes
        valid_df["rwa"] = (
            valid_df["exposure_at_default"]
            * valid_df["probability_of_default"]
            * valid_df["loss_given_default"]
            * 12.5
        )

        return valid_df

    def load(self, df: DataFrame) -> None:
        logging.info(f"Loading {len(df)} records to database {self.db_name}")
        conn = sqlite3.connect(self.db_name)

        # Mapping DataFrame columns to SQL table
        df.to_sql("risk_reports", conn, if_exists="append", index=False)
        conn.close()
        logging.info("Load complete.")


if __name__ == "__main__":
    PACKAGE_ROOT = Path(__file__).resolve().parent
    DATA_FILE = PACKAGE_ROOT / "data" / "mock_loans.csv"

    etl = CreditRiskETL()
    try:
        raw_data = etl.extract(str(DATA_FILE))
        processed_data = etl.transform(raw_data)
        etl.load(processed_data)
    except Exception as e:
        logging.error(f"Pipeline Failed: {e}")
