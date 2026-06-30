"""
Module train_model: Đào tạo mô hình dự báo và tích hợp MLflow để theo dõi thực nghiệm.

Mục đích:
- Thiết lập baseline model (SARIMA) và các model chính (LightGBM/XGBoost nếu mở rộng).
- Sử dụng TimeSeriesSplit để thực hiện cross-validation phù hợp với dữ liệu thời gian.
- Tính toán RMSLE (hoặc Weighted RMSLE) cho từng fold.
- Log các thông số (hyperparameters), độ đo (metrics), và lưu file model artifacts (.pkl, .joblib) lên MLflow tracking.
"""

import pandas as pd
import logging
import mlflow

logger = logging.getLogger(__name__)

def get_cv_splits(df: pd.DataFrame, n_splits: int, test_size: int):
    """
    Tạo các fold chia dữ liệu theo thời gian (TimeSeriesSplit hoặc Custom Time Split).
    
    Args:
        df (pd.DataFrame): DataFrame chứa dữ liệu chuỗi thời gian đã sắp xếp
        n_splits (int): Số lượng fold
        test_size (int): Kích thước tập test (số ngày hoặc dòng)
        
    Yields:
        tuple: (train_index, val_index) cho mỗi fold
    """
    pass

def train_sarima(train_data: pd.DataFrame, order: tuple, seasonal_order: tuple) -> object:
    """
    Huấn luyện mô hình SARIMA trên dữ liệu được cung cấp.
    
    Args:
        train_data (pd.DataFrame): Dữ liệu huấn luyện
        order (tuple): Tham số (p, d, q) của SARIMA
        seasonal_order (tuple): Tham số (P, D, Q, s) của SARIMA
        
    Returns:
        object: Model đã được fit
    """
    pass

def run_training_pipeline(config_path: str):
    """
    Chạy toàn bộ quy trình train model: đọc data processed, split CV, train model,
    đánh giá, và log thông tin lên MLflow.
    
    Args:
        config_path (str): Đường dẫn đến file config.yaml
    """
    pass
