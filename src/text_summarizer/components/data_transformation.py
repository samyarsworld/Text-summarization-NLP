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
        input_encodings = self.tokenizer(batch["dialogue"], truncation=True, padding=True, max_length = 1024)

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(batch["dialogue"], truncation=True, padding=True, max_length = 128)

        return {
            "input_ids": input_encodings["input_ids"],
            "attention_mask": input_encodings["attention_mask"],
            "target": target_encodings["input_ids"],
        }

    def transform(self):
        data_dict = load_from_disk(self.data_path)
        data_dict = data_dict.map(self.tokenize, batched = True)

        data_dict.save_to_disk(os.path.join(self.root_dir,"dataset"))
        
        print(data_dict)