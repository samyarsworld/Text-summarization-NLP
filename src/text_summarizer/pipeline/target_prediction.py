from transformers import AutoTokenizer
from transformers import pipeline


class TargetPredictionPipeline:
    def __init__(self, config):
        self.config = config

    def run(self,text):
        target_prediction_config = self.config.get_target_prediction_config()
        
        tokenizer = AutoTokenizer.from_pretrained(target_prediction_config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

        model_pipeline = pipeline("summarization", model=target_prediction_config.model_path,tokenizer=tokenizer)

        print("Dialogue:")
        print(text)

        output = model_pipeline(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)

        return output