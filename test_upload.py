# import boto3

# s3_client = boto3.client("s3")
# s3_resource = boto3.resource("s3")

# from_filename = 'yolov7/best.pt'
# bucket_name = 'object-1'
# to_filename = 'best.pt'

# print('testing bucket')

# s3_resource.meta.client.upload_file(
#                 from_filename, bucket_name, to_filename
#             )

# print('uploading done')
from isd.entity.config_entity import ModelPredictorConfig
from isd.exception import isdException
from isd.configuration.s3_operations import S3Operation
import sys

class test:
    def __init__(self, config:ModelPredictorConfig=ModelPredictorConfig()):
        self.loaded_model=None
        
        try:
            # self.schema_config = read_yaml_file(SCHEMA_FILE_PATH)
            self.config = config 
            self.s3_operations = S3Operation()

        except Exception as e:
            raise isdException(e, sys)
    
    def predict(self):
        """
        :param dataframe:
        :return:
        """
        try:
            print(1)
            if self.loaded_model is None:
                print(2)
                self.loaded_model = self.s3_operations.load_model(self.config.model_file_path, 
                                               self.config.model_bucket_name)
                return self.loaded_model
                print('model loaded successfully')
            
        except Exception as e:
            raise isdException(e, sys)
        
# obj = test()
# obj.predict()