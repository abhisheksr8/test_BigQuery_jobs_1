def DBT_0():
    from datetime import timedelta
    from airflow.operators.bash import BashOperator

    return BashOperator(
        task_id = "DBT_0",
        bash_command = "set -euxo pipefail; tmpDir=`mktemp -d`; git clone https://github.com/abhisheksr8/test_BigQuery_jobs_1.git --branch testBranchBigQueryJobs --single-branch $tmpDir; cd $tmpDir/; dbt deps --profile run_profile_bigquery; dbt seed --profile run_profile_bigquery; dbt run --profile run_profile_bigquery; ",
        env = {
          "DBT_PROFILES_DIR": "/usr/local/airflow/dags", 
          "DBT_SEND_ANONYMOUS_USAGE_STATS": "false", 
          "DBT_FULL_REFRESH": "true"
        },
        append_env = True,
        retries = 1, 
        retry_delay = timedelta(minutes = 1.0)
    )
