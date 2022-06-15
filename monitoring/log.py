# import google.cloud.logging
from google.cloud import logging

# # set up the Google Cloud Logging python client library
# client = google.cloud.logging.Client()
# client.setup_logging()


"""write logs to GCP"""
# # The data to log
# text = "Hello, world!"
#
# # Emits the data using the standard logging module
# logging.warning(text)
#
# print("Logged: {}".format(text))


def write_entry(logger_name):
    """Writes log entries to the given logger."""
    logging_client = logging.Client()

    # This log can be found in the Cloud Logging console under 'Custom Logs'.
    logger = logging_client.logger(logger_name)

    # Simple text log with severity.
    logger.log_text("write log from jm han", severity="INFO")

    # Struct log. The struct can be any JSON-serializable dictionary.
    # logger.log_struct(
    #     {
    #         "name": "King Arthur",
    #         "quest": "Find the Holy Grail",
    #         "favorite_color": "Blue",
    #     },
    #     severity="INFO"
    # )
    print("Wrote logs to {}.".format(logger.name))


"""read log from log name"""
def list_entries(logger_name):
    """Lists the most recent entries for a given logger."""
    logging_client = logging.Client()
    logger = logging_client.logger(logger_name)

    print("Listing entries for logger {}:".format(logger.name))

    for entry in logger.list_entries():
        timestamp = entry.timestamp.isoformat()
        print("* {}: {}".format(timestamp, entry.payload))


# write_entry("log-from-jm-han")
# list_entries("compute.googleapis.com%2Fhealthchecks")

list_entries("log-from-jm-han")
# list_entries("cloudaudit.googleapis.com%2Factivity")







"""
https://cloud.google.com/logging/docs/samples/logging-write-log-entry
https://medium.com/google-cloud/introducing-google-cloud-logging-python-v3-0-0-4c548663bab4
https://levelup.gitconnected.com/how-to-write-logs-to-google-cloud-logging-in-python-46e7b514c60b
"""