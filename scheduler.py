from apscheduler.schedulers.background import BackgroundScheduler

from monitor.api_checker import check_all_apis


scheduler = BackgroundScheduler()


def start_scheduler():
    """
    Starts background monitoring.
    """

    scheduler.add_job(
        func=check_all_apis,
        trigger="interval",
        seconds=30,
        id="api_monitor_job",
        replace_existing=True
    )

    scheduler.start()

    print("Background Scheduler Started")