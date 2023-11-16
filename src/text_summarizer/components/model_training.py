import os

class ModelTraining:
    def __init__(self, config):
        self.root_dir = config["root_dir"]
        self.data_path = config["data_path"]
        self.model_ckpt = config["model_ckpt"]

    def train(self):
        pass
