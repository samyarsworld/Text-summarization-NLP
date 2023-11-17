import os
import torch
from datasets import load_from_disk

from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class ModelTrainer:
    def __init__(self, config):
        self.root_dir = config["root_dir"]
        self.data_path = config["data_path"]
        self.model_ckpt = config["model_ckpt"]
        self.algorithm_name = config["algorithm_name"]

        self.h_params = config["h_params"]


    def train(self):
        # Device agnostic training
        DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

        # Initialize pretrained training functions
        tokenizer = AutoTokenizer.from_pretrained(self.model_ckpt)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.model_ckpt).to(DEVICE)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

        # Load data to a data dictionary (train, validation, test)
        data_dict = load_from_disk(self.data_path)

        output_dir = os.path.join(self.root_dir, self.algorithm_name)
        
        trainer_args = TrainingArguments(
            output_dir=output_dir,
            num_train_epochs=self.h_params["epochs"],
            warmup_steps=self.h_params["warmup_steps"],
            per_device_train_batch_size=self.h_params["train_batch_size"],
            per_device_eval_batch_size=self.h_params["eval_batch_size"],
            weight_decay=self.h_params["weight_decay"],
            logging_steps=self.h_params["logging_steps"],
            evaluation_strategy=self.h_params["evaluation_strategy"],
            eval_steps=self.h_params["eval_steps"],
            save_steps=self.h_params["save_steps"],
            gradient_accumulation_steps=self.h_params["gradient_accumulation_steps"]
        ) 

        trainer = Trainer(
            model=model,
            args=trainer_args,
            tokenizer=tokenizer,
            data_collator=seq2seq_data_collator,
            train_dataset=data_dict["train"], 
            eval_dataset=data_dict["validation"]
        )

        trainer.train()

        # ## Save model
        # model.save_pretrained(os.path.join(output_dir, self.algorithm_name))
        # ## Save tokenizer
        # tokenizer.save_pretrained(os.path.join(output_dir, "tokenizer"))
