from rest_framework import views
from rest_framework.response import Response


class DebugAPI(views.APIView):
    permission_classes = []

    def get(self, request, format=None):
        import boto3
        import botocore
        from botocore.client import Config

        # s3 = boto3.client('s3')
        # with open('events.csv', 'wb') as f:
        #     s3.download_fileobj('work-sample-mk', '2021/04/events.csv', f)
        #     print(f)

        BUCKET_NAME = "work-sample-mk"  # replace with your bucket name
        KEY = "2021/04/events.csv"  # replace with your object key

        s3 = boto3.resource("s3", config=Config(signature_version=botocore.UNSIGNED))

        try:
            s3.Bucket(BUCKET_NAME).download_file(KEY, "truc")
        except botocore.exceptions.ClientError as e:
            if e.response["Error"]["Code"] == "404":
                print("The object does not exist.")
            else:
                raise

        response = {
            "test": "chips",
        }
        return Response(response)
