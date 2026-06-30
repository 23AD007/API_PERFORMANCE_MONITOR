import time
import requests
from datetime import datetime, timedelta
from database.db import db
from database.models import API, Metric
from logger import logger

REQUEST_TIMEOUT = 10  # seconds


def check_api(api):
    """
    Check a single API and store its performance metrics.
    """

    start_time = time.perf_counter()
    logger.info(f"Checking API: {api.name} ({api.url})")
    try:
        response = requests.request(
            method=api.method,
            url=api.url,
            timeout=REQUEST_TIMEOUT
        )

        response_time = round(
            (time.perf_counter() - start_time) * 1000,
            2
        )

        metric = Metric(
            api_id=api.id,
            status_code=response.status_code,
            response_time=response_time,
            success=response.ok,
            error_message=None
        )
        logger.info(
           f"{api.name} | Status: {response.status_code} | Response Time: {response_time} ms"
       )
    except requests.exceptions.Timeout:
        logger.error(f"{api.name} | Request Timeout")

        metric = Metric(
            api_id=api.id,
            status_code=0,
            response_time=None,
            success=False,
            error_message="Request Timeout"
        )

    except requests.exceptions.ConnectionError:
        logger.error(f"{api.name} | Connection Error")

        metric = Metric(
            api_id=api.id,
            status_code=0,
            response_time=None,
            success=False,
            error_message="Connection Error"
        )

    except requests.exceptions.SSLError:
        logger.error(f"{api.name} | SSL Error")

        metric = Metric(
            api_id=api.id,
            status_code=0,
            response_time=None,
            success=False,
            error_message="SSL Error"
        )

    except Exception as e:
        logger.exception(f"{api.name} | Unexpected Error")

        metric = Metric(
            api_id=api.id,
            status_code=0,
            response_time=None,
            success=False,
            error_message=str(e)
        )

    db.session.add(metric)
    db.session.commit()

    return metric


def check_all_apis():

    apis = API.query.all()

    for api in apis:

        now = datetime.utcnow()

        if api.last_checked:

            elapsed = now - api.last_checked

            if elapsed < timedelta(seconds=api.interval):
                continue

        check_api(api)

        api.last_checked = now

        db.session.commit()