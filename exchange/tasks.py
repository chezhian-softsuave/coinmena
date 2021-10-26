from celery import shared_task

from exchange.api import exchange_api, insert_data


@shared_task
def exchange_data():
    """
    Celery task to fetch the data for every hour
    and store it in the database.
    :return: None
    """
    response, status_code = exchange_api()
    if status_code == 200:
        """
        Inserting data if response status is 200
        """
        insert_data(response)
    elif status_code == 400:
        print("Server API is getting bad request")
    elif status_code == 500:
        print("Problem with connecting API of alphavantage")
    else:
        print("Connection Error")
