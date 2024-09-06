import datetime

import pandas as pd

import great_expectations as gx
import great_expectations.jupyter_ux
from great_expectations.core.batch import BatchRequest
from great_expectations.checkpoint import SimpleCheckpoint
from great_expectations.exceptions import DataContextError

context = gx.get_context()

batch_request = {'datasource_name': 'Datasource', 'data_connector_name': 'default_inferred_data_connector_name', 'data_asset_name': 'vaccine_data.data_us', 'limit': 1000}

expectation_suite_name = "cov_suite"

validator = context.get_validator(
    batch_request=BatchRequest(**batch_request),
    expectation_suite_name=expectation_suite_name
)
column_names = [f'"{column_name}"' for column_name in validator.columns()]
print(f"Columns: {', '.join(column_names)}.")
print(validator.head(n_rows=5, fetch_all=False))