"""
Script chính để tối ưu hóa siêu tham số mô hình với Optuna.

Cách sử dụng:
    python scripts/tune.py [--config configs/config.yaml]

Mô tả:
- Load cấu hình tuning từ file config.yaml (search space, n_trials, timeout...).
- Khởi chạy Optuna study.
- Thực hiện tìm kiếm tham số tối ưu thông qua TimeSeriesSplit cross-validation.
- Lưu trữ lịch sử study và in ra bộ tham số tối ưu nhất.
"""

import argparse
import sys
import os

# Thêm thư mục gốc của dự án vào PYTHONPATH để import src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models.tune_model import run_tuning

def main():
    parser = argparse.ArgumentParser(description="Tune model hyperparameters using Optuna.")
    parser.add_argument("--config", type=str, default="configs/config.yaml", help="Path to config.yaml file.")
    args = parser.parse_args()
    
    print(f"Bắt đầu quá trình tối ưu hóa siêu tham số với cấu hình: {args.config}")
    run_tuning(args.config)
    print("Quá trình tối ưu hóa siêu tham số hoàn tất!")

if __name__ == "__main__":
    main()
