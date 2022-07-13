from google.cloud import monitoring_v3
import time
import os
import settings as st

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= st.SERVICE_KEY_P_2



client = monitoring_v3.MetricServiceClient()
project = st.P_1  # TODO: Update to your project ID.
# project = st.P_2  # TODO: Update to your project ID.
project_name = f"projects/{project}"


"""
모니터링 리소스 나열 > 모니터링할 수 있는 클라우드 항목"""
resource_descriptors = client.list_monitored_resource_descriptors(name=project_name)
for descriptor in resource_descriptors:
    print(descriptor.type)


"""
클라우드 항목 중 세부 metric 유형 나열"""
for descriptor in client.list_metric_descriptors(name=project_name):
    print(descriptor.type)


"""
모니터링 리소스 세부정보 가져오기"""
# resource_path = (
#     f"projects/{project}/monitoredResourceDescriptors/gce_instance"
# )
# print(client.get_monitored_resource_descriptor(name=resource_path))


"""
사용 가능한 시계열 나열"""
# now = time.time()
# seconds = int(now)
# nanos = int((now - seconds) * 10 ** 9)
# interval = monitoring_v3.TimeInterval(
#     {
#         "end_time": {"seconds": seconds, "nanos": nanos},
#         "start_time": {"seconds": (seconds - 1200), "nanos": nanos},
#     }
# )
# results = client.list_time_series(
#     request={
#         "name": project_name,
#         "filter": 'metric.type = "compute.googleapis.com/instance/cpu/utilization"',
#         "interval": interval,
#         "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.HEADERS,
#     }
# )
# for result in results:
#     print(result)


"""
Metric값 가져오기
https://cloud.google.com/monitoring/custom-metrics/reading-metrics?hl=ko#monitoring_read_timeseries_fields-python
"""
# interval = monitoring_v3.TimeInterval()
#
# now = time.time()
# seconds = int(now)
# nanos = int((now - seconds) * 10 ** 9)
# interval = monitoring_v3.TimeInterval(
#     {
#         "end_time": {"seconds": seconds, "nanos": nanos},
#         "start_time": {"seconds": (seconds - 1200), "nanos": nanos},
#     }
# )
#
# results = client.list_time_series(
#     request={
#         "name": project_name,
#         "filter": 'metric.type = "compute.googleapis.com/instance/cpu/utilization"',
#         "interval": interval,
#         "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL,
#     }
# )
# for result in results:
#     print(result)