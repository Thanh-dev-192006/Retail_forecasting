"""
Module features: Xây dựng các đặc trưng (features) cho mô hình dự báo Time Series.

Mục đích:
- Tạo các đặc trưng trễ (lag features) và đặc trưng cuộn (rolling window statistics) cho unit_sales.
- Xử lý thông tin khuyến mãi (promotion status, rolling promotions).
- Xử lý các sự kiện nghỉ lễ (holidays_events) và phân loại ngày (weekday, weekend, holiday type).
- Tích hợp giá dầu (oil price) với các lag features của giá dầu.
- Mã hóa các biến phân loại (store type, cluster, item family).
- Tạo tập dữ liệu hoàn chỉnh để đưa vào mô hình và lưu tại data/processed/.
"""

import pandas as pd
import logging

logger = logging.getLogger(__name__)

def build_time_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Tạo các đặc trưng liên quan đến thời gian (day of week, month, year, day of year, is_weekend).
    
    Args:
        df (pd.DataFrame): DataFrame chứa cột ngày tháng
        
    Returns:
        pd.DataFrame: DataFrame kèm các đặc trưng thời gian.
    """
    pass

def build_lag_features(df: pd.DataFrame, target_col: str, lags: list) -> pd.DataFrame:
    """
    Tạo các đặc trưng trễ (lags) cho cột mục tiêu.
    
    Args:
        df (pd.DataFrame): DataFrame đầu vào
        target_col (str): Tên cột mục tiêu (ví dụ: unit_sales)
        lags (list): Danh sách các khoảng trễ (ví dụ: [1, 7, 14, 28])
        
    Returns:
        pd.DataFrame: DataFrame kèm các đặc trưng trễ.
    """
    pass

def build_rolling_features(df: pd.DataFrame, target_col: str, windows: list) -> pd.DataFrame:
    """
    Tạo các đặc trưng thống kê cuộn (rolling mean, rolling std) trên các cửa sổ thời gian.
    
    Args:
        df (pd.DataFrame): DataFrame đầu vào
        target_col (str): Tên cột mục tiêu
        windows (list): Danh sách các kích thước cửa sổ (ví dụ: [3, 7, 14, 30])
        
    Returns:
        pd.DataFrame: DataFrame kèm các đặc trưng cuộn.
    """
    pass

def merge_external_features(train_df: pd.DataFrame, stores_df: pd.DataFrame, 
                            items_df: pd.DataFrame, oil_df: pd.DataFrame, 
                            holidays_df: pd.DataFrame) -> pd.DataFrame:
    """
    Gộp dữ liệu bán hàng với các thông tin ngoại cảnh (stores, items, oil price, holidays).
    
    Args:
        train_df (pd.DataFrame): Dữ liệu bán hàng chính
        stores_df (pd.DataFrame): Thông tin cửa hàng
        items_df (pd.DataFrame): Thông tin sản phẩm
        oil_df (pd.DataFrame): Giá dầu
        holidays_df (pd.DataFrame): Lịch nghỉ lễ
        
    Returns:
        pd.DataFrame: DataFrame tích hợp đầy đủ.
    """
    pass

def generate_features_pipeline(input_dir: str, output_dir: str):
    """
    Pipeline chính để thực hiện feature engineering từ dữ liệu interim và lưu vào processed.
    
    Args:
        input_dir (str): Đường dẫn đến data/interim/
        output_dir (str): Đường dẫn đến data/processed/
    """
    pass
