from text_summarizer.components.model_training import ModelTraining


class ModelTrainingPipeline:
    def __init__(self, config):
        self.config = config

    def run(self):
        model_training_config = self.config.get_model_training_config()
        model_training= ModelTraining(model_training_config)

        return model_training.train()