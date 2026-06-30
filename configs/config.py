from pathlib import Path

# Path resolution: __file__ is inside configs/, so parent.parent points to the project root
PROJECT_ROOT  = Path(__file__).resolve().parent.parent
DATA_DIR      = PROJECT_ROOT / 'data'
RAW_DIR       = DATA_DIR / 'raw'
PROCESSED_DIR = DATA_DIR / 'processed'
MODELS_DIR    = PROJECT_ROOT / 'models'
NOTEBOOKS_DIR = PROJECT_ROOT / 'notebooks'
SPLITS_DIR    = PROCESSED_DIR / 'splits'
CLEANED_DIR   = PROCESSED_DIR / 'cleaned'
