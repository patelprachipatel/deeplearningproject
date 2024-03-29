import os
import sys
from Xray.exception import XRayException

class S3Operaation:

    def sink_folder_to_S3(self, folder: str, bucket_name: str, bucket_folder_name: str) ->None:
        try:
            command: str=(
                f" aws s3 sync {folder} s3://{bucket_name}/{bucket_folder_name}"
            )

            os.system(command)
        except Exception as e:
            raise Exception(e, sys)

    def sink_folder_from_S3(self, folder: str, bucket_name: str, bucket_folder_name: str) ->None:
        try:
            command: str=(
                f" aws s3 sync s3://{bucket_name}/{bucket_folder_name}/{folder} "
            )

            os.system(command)
        except Exception as e:
            raise Exception(e, sys) 