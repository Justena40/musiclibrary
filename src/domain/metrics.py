import boto3 from cloudwatch

class Metrics:
    def __init__(self, cloudwatch):
        self.cloudwatch = cloudwatch

    def put_metrics(self, namespace, operation, is_exception=True):
        self.cloudwatch.put_metrics_data(
            Namespace = namespace
            MetricData=[
                {
                    "MetricName": f"{operation}"
                    if not is_exception
                    else f"{operation}-exception",
                    "Values": [
                        1,
                    ],
                    "Unit": "None",
                },
            ],
        )