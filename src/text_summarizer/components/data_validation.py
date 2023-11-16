import os

class DataValidation:
    def __init__(self, config):
        self.root_dir = config["root_dir"]
        self.required_files = config["required_files"]
        self.status_path = config["status_path"]


    def validate(self) -> bool:
        all_files = os.listdir(os.path.join("artifacts","data_ingestion", "dataset"))
        status = True
        validation_status = "Success" if status else "Failure"
        with open(self.status_path, 'w') as f:
            f.write(f"Validation status: {validation_status}")

        return validation_status

