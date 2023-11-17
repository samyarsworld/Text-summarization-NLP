from text_summarizer.components.model_evaluation import ModelEvaluation



class ModelEvaluationPipeline:
    def __init__(self, config):
        self.config = config
    

    def run(self):
        model_evaluation_config = self.config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.evaluate()