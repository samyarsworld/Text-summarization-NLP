from transformers import AutoTokenizer
from transformers import pipeline

class TargetPredictionPipeline:
    def __init__(self, config):
        self.config = config.get_target_prediction_config()

    def run(self, text):        
        tokenizer = AutoTokenizer.from_pretrained(self.config["tokenizer_path"])
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

        model_pipeline = pipeline("summarization", model=self.config["model_path"],tokenizer=tokenizer)

        # print("Dialogue:")
        # print(text)

        output = model_pipeline(text, **gen_kwargs)[0]["summary_text"]
        output = output.replace("<n>", "\n")
        output = output.replace(" .", ".")

        # print("\nModel Summary:")
        # print(output)

        return output