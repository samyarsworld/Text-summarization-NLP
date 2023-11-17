import os
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk

class DataTransformation:
    def __init__(self, config):
        self.root_dir = config["root_dir"]
        self.data_path = config["data_path"]

        # Use a pretrained tokenizer model
        self.tokenizer = AutoTokenizer.from_pretrained(config["tokenizer"])

    def tokenize(self, batch):
        input_encodings = self.tokenizer(batch["dialogue"], truncation=True, max_length = 1024)

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(batch["summary"], truncation=True, max_length = 128)

        
        return {
            "input_ids": input_encodings["input_ids"],
            "attention_mask": input_encodings["attention_mask"],
            "labels": target_encodings["input_ids"],
        }

    def transform(self):
        # Load dataset splits (train, test, validation)
        dataset = load_dataset(self.data_path)

        dataset = dataset.map(self.tokenize, batched = True)
        dataset.save_to_disk(os.path.join(self.root_dir,"dataset"))
        