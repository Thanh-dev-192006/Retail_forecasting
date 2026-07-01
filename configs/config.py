from pathlib import Path
import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent

_cfg_path = Path(__file__).resolve().parent / "config.yaml"
with open(_cfg_path) as _f:
    _cfg = yaml.safe_load(_f)

def _p(rel: str) -> Path:
    return PROJECT_ROOT / rel

# Directory paths
_paths = _cfg["paths"]
RAW_DIR          = _p(_paths["raw_data_dir"])
INTERIM_DIR      = _p(_paths["interim_data_dir"])
PROCESSED_DIR    = _p(_paths["processed_data_dir"])
SPLITS_DIR       = _p(_paths["splits_dir"])
CLEANED_DIR      = _p(_paths["cleaned_dir"])
MODELS_DIR       = _p(_paths["model_dir"])
REPORTS_DIR      = _p(_paths["reports_dir"])
FIGURES_DIR      = _p(_paths["figures_dir"])
ERROR_ANALYSIS_DIR = _p(_paths["error_analysis_dir"])

# File paths (all raw data files live in RAW_DIR)
_files = _cfg["data_files"]
TRAIN_PATH             = RAW_DIR / _files["train"]
TEST_PATH              = RAW_DIR / _files["test"]
OIL_PATH               = RAW_DIR / _files["oil"]
STORES_PATH            = RAW_DIR / _files["stores"]
HOLIDAYS_PATH          = RAW_DIR / _files["holidays"]
TRANSACTIONS_PATH      = RAW_DIR / _files["transactions"]
SAMPLE_SUBMISSION_PATH = RAW_DIR / _files["sample_submission"]
