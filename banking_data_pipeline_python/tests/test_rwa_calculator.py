import pandas as pd
import pytest
from banking_data_pipeline.rwa_calculator import CreditRiskETL


@pytest.fixture
def etl_instance():
    return CreditRiskETL(db_name="test_risk.db")


def test_rwa_calculation_logic(etl_instance: CreditRiskETL):
    """
    Test the core math: EAD * PD * LGD * 12.5
    EAD: 100, PD: 0.1, LGD: 0.5 -> RWA should be 62.5
    """
    mock_data = pd.DataFrame(
        {
            "loan_id": ["T001"],
            "customer_name": ["Test Corp"],
            "exposure_at_default": [100.0],
            "probability_of_default": [0.1],
            "loss_given_default": [0.5],
        }
    )

    transformed_df = etl_instance.transform(mock_data)
    expected_rwa = 100.0 * 0.1 * 0.5 * 12.5

    assert transformed_df.iloc[0]["rwa"] == expected_rwa
    assert len(transformed_df) == 1


def test_negative_exposure_filtering(etl_instance: CreditRiskETL):
    """
    Ensures the 'Senior' logic of filtering out bad data works.
    One valid row, one negative EAD row. Only one should remain.
    """
    mock_data = pd.DataFrame(
        {
            "loan_id": ["T001", "T002"],
            "customer_name": ["Good Co", "Bad Co"],
            "exposure_at_default": [500.0, -100.0],  # Negative should be dropped
            "probability_of_default": [0.05, 0.05],
            "loss_given_default": [0.4, 0.4],
        }
    )

    transformed_df = etl_instance.transform(mock_data)

    # Check that only 'Good Co' remains
    assert len(transformed_df) == 1
    assert transformed_df.iloc[0]["loan_id"] == "T001"


def test_missing_file_error(etl_instance: CreditRiskETL):
    """Verifies the Support-friendly error handling."""
    with pytest.raises(FileNotFoundError):
        etl_instance.extract("non_existent_file.csv")
