# import google.cloud.logging
from google.cloud import logging
import util.dict_to_list as dl
import settings as st

"""auth GCP"""
# # set up the Google Cloud Logging python client library
# client = google.cloud.logging.Client()
# client.setup_logging()

# Alternatively, but not recommended. It's helpful when you can't set an environment variable.
logging_client = logging.Client.from_service_account_json(st.SERVICE_KEY_PATH_JISUN)


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
    # logging_client = logging.Client()

    # This log can be found in the Cloud Logging console under 'Custom Logs'.
    logger = logging_client.logger(logger_name)

    """write simple text log with severity."""
    # logger.log_text("write log from jm han", severity="INFO")

    """write struct log. The struct can be any JSON-serializable dictionary."""
    logger.log_struct(
        {
                "healthCheckProbeResult": {
                    "detailedHealthState": "TIMEOUT",
                    "healthCheckProtocol": "TCP",
                    "healthState": "UNHEALTHY",
                    "ipAddress": "10.0.0.19",
                    "previousDetailedHealthState": "HEALTHY",
                    "previousHealthState": "HEALTHY",
                    "probeCompletionTimestamp": "2022-06-07T05:13:12.470178139Z",
                    "probeResultText": "Connection timed out",
                    "probeSourceIp": "209.85.204.100",
                    "responseLatency": "5.001336s",
                    "targetIp": "34.64.111.245",
                    "targetPort": 80,
                }
        },
        severity="INFO"
    )
    print("Wrote logs to {}.".format(logger.name))


"""read log from log name"""
def list_entries(logger_name):
    """Lists the most recent entries for a given logger."""
    # logging_client = logging.Client()
    logger = logging_client.logger(logger_name)

    print("Listing entries for logger {}:".format(logger.name))

    for entry in logger.list_entries():
        timestamp = entry.timestamp.isoformat()
        # print(entry.payload)
        print("* {}: {}".format(timestamp, entry.payload))
        log = entry.payload
        print(log)
        print(type(entry))
        # print(type(log))
        # print(log.values())
        # print(type(log.values()))

        # dl.dict_to_list(log)
        # print(type(dl.dict_to_list(log)))
        # if log.find("'healthState': 'UNHEALTHY'") != -1:
        #     print("LB DOWN")
        # for item in entry.payload:
        #     print(item)


# write_entry("log-from-jm-han-1")

# list_entries("compute.googleapis.com%2Fhealthchecks")
# list_entries("cloudaudit.googleapis.com%2Factivity")
# list_entries("log-from-jm-han-1")
list_entries("cloudaudit.googleapis.com%2Factivity")







"""
https://cloud.google.com/logging/docs/samples/logging-write-log-entry
https://medium.com/google-cloud/introducing-google-cloud-logging-python-v3-0-0-4c548663bab4
https://levelup.gitconnected.com/how-to-write-logs-to-google-cloud-logging-in-python-46e7b514c60b
"""