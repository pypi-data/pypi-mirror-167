from abc import ABC, abstractmethod
from datetime import datetime
import logging

logger = logging.getLogger()

@abstractmethod
def monitor():
    raise NotImplementedException()

class PyMonitoring:
    """
    Class for auxiliary method for monitor
    """
    @staticmethod
    def send_slack_monitoring_massage(message, channel="monitor", attachments=""):
        """
        Send message to the slack channel
        :param message: the message to send
        :param channel: the slack channel
        :param attachments:
        :return:
        """
        logger.info("implement with you slack")

    @staticmethod
    def check_table_in_sf(start_ts: int, end_ts:int, table:str, sf_client,
                               send_slack_if_no_data: bool = True, time_field_name: str= "start_ts") -> bool:
        """
        Check if there is data in the specified table between the start ts and end ts in the given time_field_name
        if there is data return True else can send slack notification and return False
        :param start_ts: the timestamp to start from
        :param end_ts: the end timestamp
        :param table: the snowflake table to look into
        :param sf_client: the snoflake client to use
        :param send_slack_if_no_data: default is True. send slack message if there is no data
        :param time_field_name: the field to check start_ts and end_ts in
        :return: True if there is Data False otherwise
        """
        query = f"select * from {table} where {time_field_name} between {start_ts} and {end_ts}"
        result = PyMonitoring.check_query_in_sf(query, sf_client, False)
        if not result and send_slack_if_no_data:
            message = f"No result for table {table} between {datetime.fromtimestamp(start_ts)} and " \
                        f"{datetime.fromtimestamp(end_ts)}" \
                        f"\nQuery is {query}" \
                        f"\nResult is {result}"
            PyMonitoring.send_slack_monitoring_massage(message)
            return False
        return True

    @staticmethod
    def check_query_in_sf(query:str, sf_client,
                          send_slack_if_no_data: bool=True)->list:
        """
        Send query to snowflake and return the query result.
        send slack message if there is no data
        :param query: the query to send the snowflake client
        :param sf_client: the snowflake client
        :param send_slack_if_no_data: default is True. send slack message if there is no data
        :return: The query result
        """
        logger.info(f"Going to run query:\n{query}")
        result = []
        #should be:
        #result = sf_client.query(query)

        if not result:
            if send_slack_if_no_data:
                message = f"No result for query {query}" \
                          f"\nResult is {result}"

                PyMonitoring.send_slack_monitoring_massage(message)
        return result

