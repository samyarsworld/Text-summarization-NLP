from text_summarizer.components.model_trainer import ModelTrainer


class ModelTrainingPipeline:
    def __init__(self, config):
        self.config = config

    def run(self):
        model_trainer_config = self.config.get_model_trainer_config()
        model_trainer= ModelTrainer(model_trainer_config)
        model_trainer.train()