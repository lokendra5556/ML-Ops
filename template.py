import logging
import os
from pathlib import Path
# import pdb; pdb.set_trace()

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    #data ingestion, EDA, Feature engineering all this stages are called components of the pipeline
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_training.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py"
    "test/unit/__init__.py",
    "test/unit/unit.py",
    "test/integration/__init__.py",
    "test/integration/integration.py",
    "init_setup.sh",
    "requirements.txt",
    "setup.py",
    "setup.config",
    "pyproject.toml",
    "tox.ini",
    "experiments/experiment.ipynb"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    folder, file = os.path.split(file_path)
    if folder != "":
        # exist_ok = True, pass if already exist
        os.makedirs(folder, exist_ok=True)
        # logging.info(f"Creating directory: {folder} for file: {file}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass # create an empty file