from text_summarizer.components.data_transformation import DataTransformation


class DataTransformationPipeline:
    def __init__(self, config):
        self.config = config

    
    def run(self):
        data_transformation_config = self.config.get_data_transformation_config()
        data_transformation = DataTransformation(data_transformation_config)

        transformed_batch = data_transformation.transform()

        return transformed_batch