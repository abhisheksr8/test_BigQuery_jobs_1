import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.decorators import task
from airflow.models.param import Param
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from staging_abhisheks_e2etests_bigquery_automationjobs_project_bigquery_sqlairflow_mwaa_automation.tasks import (
    DBT_0,
    Script_1
)
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "staging_abhisheks_e2etests_BigQuery_AutomationJobs_Project_BigQuery_SQLAirflow_MWAA_Automation", 
    schedule_interval = "0 0 17 2 *", 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True}, 
    start_date = pendulum.today('UTC'), 
    catchup = True
) as dag:
    DBT_0_op = DBT_0()
    Script_1_op = Script_1()
    DBT_0_op >> Script_1_op
