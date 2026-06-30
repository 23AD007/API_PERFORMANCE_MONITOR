import time
import requests

from database.db import db
from database.models import API, Metric


REQUEST_TIMEOUT = 10  # seconds


def check_api(api):
    """
    Check a single API and store its performance metrics.
    """

    start_time = time.perf_counter()

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

    except requests.exceptions.Timeout:

        metric = Metric(
            api_id=api.id,
            status_code=0,
            response_time=None,
            success=False,
            error_message="Request Timeout"
        )

    except requests.exceptions.ConnectionError:

        metric = Metric(
            api_id=api.id,
            status_code=0,
            response_time=None,
            success=False,
            error_message="Connection Error"
        )

    except requests.exceptions.SSLError:

        metric = Metric(
            api_id=api.id,
            status_code=0,
            response_time=None,
            success=False,
            error_message="SSL Error"
        )

    except Exception as e:

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
    """
    Monitor every registered API.
    """

    apis = API.query.all()

    results = []

    for api in apis:
        result = check_api(api)
        results.append(result)

    return results