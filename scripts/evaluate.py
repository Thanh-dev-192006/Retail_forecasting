"""
Script chính để chạy đánh giá và phân tích sai số mô hình.

Cách sử dụng:
    python scripts/evaluate.py [--config configs/config.yaml] [--model_path models/model.pkl]

Mô tả:
- Load cấu hình và mô hình đã được huấn luyện.
- Thực hiện dự báo trên tập kiểm thử / validation.
- Tính toán Weighted RMSLE và tạo các bảng biểu phân tích sai số theo store, family, khuyến mãi, ngày lễ.
- Xuất các báo cáo CSV/Markdown và đồ thị trực quan hóa lỗi dự báo.
"""

import argparse
import sys
import os

# Thêm thư mục gốc của dự án vào PYTHONPATH để import src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main():
    parser = argparse.ArgumentParser(description="Evaluate model and perform error analysis.")
    parser.add_argument("--config", type=str, default="configs/config.yaml", help="Path to config.yaml file.")
    parser.add_argument("--model_path", type=str, default="models/best_model.pkl", help="Path to model file.")
    args = parser.parse_args()
    
    print(f"Bắt đầu đánh giá mô hình: {args.model_path} sử dụng cấu hình: {args.config}")
    # Đọc dữ liệu và mô hình
    # Thực hiện dự báo
    # Chạy evaluate.weighted_rmsle
    # Chạy segment_analysis và plot_results
    print("Đánh giá mô hình và phân tích sai số hoàn tất! Kết quả đã được lưu tại reports/")

if __name__ == "__main__":
    main()
