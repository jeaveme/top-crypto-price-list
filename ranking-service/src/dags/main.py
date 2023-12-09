import datetime
import logging

from airflow import DAG
from airflow.operators.python import task, get_current_context
from services import RankingService

logger = logging.getLogger(__name__)

ranking_service = RankingService()

with DAG(
    dag_id="fetch-crypto-ranking",
    start_date=datetime.datetime(2023, 12, 9),
    schedule="@hourly",
):

    @task(task_id="retrieve_ranking")
    async def retrieve_ranking():
        ds = get_current_context()["ds"]

        ranking = await ranking_service.getToplistBy24hVolume()
        logger.info(", ".join(ranking))
