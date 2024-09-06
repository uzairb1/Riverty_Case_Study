DataHub with Great Expectations
Overview
This project integrates DataHub with Great Expectations to provide data quality checks and data cataloging for your data pipelines. DataHub is a metadata platform that helps you manage and understand your data assets, while Great Expectations provides a framework for defining and validating data expectations.

Features
Data Quality Checks: Define and validate data expectations using Great Expectations.
Data Cataloging: Manage and discover data assets using DataHub.
Integration with Snowflake: Use Snowflake as the datasource for both Great Expectations and DataHub.

Prerequisites
Python 3.7 or higher
DataHub
Great Expectations
Docker 

Ingest data to snowflake first of all, or a data source of your choosing, the script ingest.py is configured for snowflake ingestions 
put in the required credentials within the code and then run the following command
python3 ingest.py
Or if you want to setup another data source then make sure that the following datahub and great expectations datasources are also the source that 
you defined

Setting Up DataHub on Local Machine

Install Dependencies:
pip install -r requirements.txt

Setting up DataHub
python3 -m datahub docker quickstart #to run the images locally

Setting Up Great Expectations
Create and Activate a Virtual Environment:

bash
Copy code
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate.bat`
Install Great Expectations:

bash
Copy code
pip install 'acryl-datahub-gx-plugin'

Initialize Great Expectations in Your Project:

bash
Copy code
great_expectations init
Configuration
Connecting Great Expectations to DataHub

Set Up Great Expectations Data Context:

Update your Great Expectations configuration to include DataHub integration. You may need to adjust your great_expectations.yml file or use a custom connector.

Configure DataHub Metadata Ingestion:

Follow the DataHub ingestion documentation to set up metadata ingestion for your data sources.

Define Expectations in Great Expectations:

Create or update your expectations suite to include data quality checks relevant to your dataset.


bash
Copy code
great_expectations datasource new  #follow the on screen commands
great_expectations suite new  #follow the on screen commands
create new cells under Table Expectations and add the following checks

validator.expect_table_row_count_to_be_between(max_value=878, min_value=878)

validator.expect_table_columns_to_match_set(column_set=['vaccine', 'date', 'people_vaccinated', 'people_fully_vaccinated', 'source_url', 'total_vaccinations', 'total_boosters'])

validator.expect_table_row_count_to_equal(value=878)

validator.expect_column_values_to_not_be_null(column='date')

validator.expect_column_values_to_match_regex(column='date', regex='\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}')

validator.expect_column_values_to_not_be_null(column='vaccine')

validator.expect_column_values_to_be_of_type(column='vaccine', type_='VARCHAR')

validator.expect_column_values_to_be_between(column='total_vaccinations', min_value=0)

validator.expect_column_values_to_be_between(column='people_vaccinated', min_value=0)

validator.expect_column_values_to_be_between(column='people_fully_vaccinated', min_value=0)

validator.expect_column_values_to_be_of_type(column='people_fully_vaccinated', type_='_CUSTOM_DECIMAL')

validator.expect_column_values_to_be_between(column='total_boosters', min_value=0)

validator.expect_column_values_to_be_of_type(column='total_boosters', type_='_CUSTOM_DECIMAL')

validator.expect_column_values_to_not_be_null(column='source_url')

validator.expect_column_values_to_match_regex(column='source_url', regex='https:\/\/data\.cdc\.gov\/Vaccinations\/COVID-19-Vaccination-Trends-in-the-United-States-N\/rh2h-3yt2')

validator.expect_column_values_to_be_of_type(column='source_url', type_='VARCHAR')

Review and Save the expectations by running the code at the last cell
great_expectations suite edit <suite_name> #to edit your expectations
great_expectations checkpoint run <checkpoint_name>
Access DataHub:

Navigate to the DataHub UI to explore and manage your data assets.
http://localhost:9002.
to view the data quality checks as a report, run the following command
great_expectations docs build


Contact
For any questions or support, please contact me at bhatti.uzair08@gmail.com.

Acknowledgements
DataHub: DataHub Project
Great Expectations: Great Expectations