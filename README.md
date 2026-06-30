# Favorita Grocery Sales Forecasting

Dự án Time Series Forecasting trên bộ dữ liệu Favorita Grocery Sales (Kaggle) theo chuẩn Data Science chuyên nghiệp.

## 1. Mô tả bài toán
Dự báo doanh số bán ra (`unit_sales`) cho hàng nghìn mặt hàng tại các cửa hàng của chuỗi siêu thị Favorita (Ecuador) theo từng ngày. 
- **Mục tiêu**: Tối ưu hóa chỉ số RMSLE có trọng số (Weighted Root Mean Squared Logarithmic Error).
  - Trọng số cho các sản phẩm dễ hỏng (perishable = True) là 1.25.
  - Trọng số cho các sản phẩm thông thường (perishable = False) là 1.0.
- **Dữ liệu nguồn**: 
  - `train.csv`: Dữ liệu bán hàng theo ngày, cửa hàng, mặt hàng và thông tin khuyến mãi.
  - `stores.csv`: Thông tin metadata của cửa hàng (thành phố, bang, loại cửa hàng, cluster).
  - `items.csv`: Thông tin metadata của sản phẩm (family, class, perishable).
  - `transactions.csv`: Số lượng giao dịch của từng cửa hàng theo ngày.
  - `oil.csv`: Giá dầu hàng ngày (ảnh hưởng lớn đến kinh tế Ecuador).
  - `holidays_events.csv`: Lịch nghỉ lễ, sự kiện đặc biệt, các sự kiện chuyển giao ngày nghỉ.

## 2. Cấu trúc thư mục dự án
```text
Retail_forecasting/
├── configs/              # Cấu hình dự án (YAML)
│   └── config.yaml
├── data/                 # Thư mục chứa dữ liệu (ignored ngoại trừ .gitkeep)
│   ├── raw/              # Dữ liệu gốc từ Kaggle
│   ├── interim/          # Dữ liệu trung gian sau khi merge/clean sơ bộ
│   └── processed/        # Dữ liệu cuối cùng dùng cho training
├── notebooks/            # Jupyter Notebooks phục vụ EDA và thử nghiệm
├── src/                  # Mã nguồn chính của dự án (Production modules)
│   ├── __init__.py
│   ├── data/             # Ingestion & Validation
│   ├── features/         # Feature Engineering (Lags, Rolling, Holiday, Oil)
│   ├── models/           # Training (Baseline & MLflow) và Tuning (Optuna)
│   ├── evaluation/       # Evaluation (Metrics & Segmented Error Analysis)
│   └── visualization/    # Tạo biểu đồ báo cáo
├── models/               # Lưu trữ model artifacts (pkl, joblib, db)
├── mlruns/               # MLflow tracking logs
├── reports/              # Báo cáo kết quả
│   ├── figures/          # Hình ảnh đồ thị xuất ra
│   └── error_analysis/   # Kết quả phân tích lỗi chi tiết
├── dashboards/           # Dashboard thiết kế (Power BI, Streamlit...)
├── tests/                # Unit test
├── scripts/              # Các entry point để chạy pipeline
│   ├── train.py
│   ├── evaluate.py
│   └── tune.py
├── requirements.txt      # Thư viện phụ thuộc
├── .gitignore            # Loại trừ file rác và data lớn
└── README.md             # Tài liệu dự án
```

## 3. Hướng dẫn thiết lập môi trường
1. Tạo môi trường ảo và kích hoạt:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```
2. Cài đặt các thư viện cần thiết:
   ```bash
   pip install -r requirements.txt
   ```

## 4. Hướng dẫn chạy Pipeline
- **Hyperparameter Tuning (Optuna)**:
  ```bash
  python scripts/tune.py
  ```
- **Train Model**:
  ```bash
  python scripts/train.py
  ```
- **Evaluate Model & Phân tích lỗi**:
  ```bash
  python scripts/evaluate.py
  ```

## 5. Kết quả chính
*(Sẽ cập nhật sau khi hoàn thành chạy các mô hình)*