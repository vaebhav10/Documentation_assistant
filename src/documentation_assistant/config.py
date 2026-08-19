from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "Data"

MODELS_DIR = PROJECT_ROOT / "models"
GOLDEN_DATASET = PROJECT_ROOT/'evaluation/golden_data'