"""
Script chính để huấn luyện mô hình dự báo.

Cách sử dụng:
    python scripts/train.py [--config configs/config.yaml]

Mô tả:
- Load cấu hình từ file config.yaml.
- Đọc dữ liệu đã qua xử lý đặc trưng từ data/processed/.
- Khởi chạy quá trình huấn luyện mô hình (SARIMA hoặc mô hình chính).
- Thực hiện cross-validation theo chuỗi thời gian và ghi nhận kết quả đánh giá fold.
- Đăng ký các tham số, độ đo và lưu mô hình lên MLflow Server.
"""

import argparse
import sys
import os

# Thêm thư mục gốc của dự án vào PYTHONPATH để import src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models.train_model import run_training_pipeline

def main():
    parser = argparse.ArgumentParser(description="Train model pipeline for Favorita Retail Forecasting.")
    parser.add_argument("--config", type=str, default="configs/config.yaml", help="Path to config.yaml file.")
    args = parser.parse_args()
    
    print(f"Bắt đầu huấn luyện mô hình với cấu hình: {args.config}")
    run_training_pipeline(args.config)
    print("Huấn luyện mô hình hoàn tất!")

if __name__ == "__main__":
    main()
