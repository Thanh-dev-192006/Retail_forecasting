"""
Module data_ingestion: Đọc, kiểm tra (validate) và làm sạch dữ liệu ban đầu.

Mục đích:
- Đọc các file dữ liệu gốc (.csv) từ thư mục data/raw/.
- Thực hiện kiểm tra định dạng dữ liệu (data types, missing values, date ranges).
- Xử lý các giá trị thiếu cơ bản (ví dụ: interpolation cho giá dầu thiếu vào cuối tuần).
- Ghi dữ liệu đã làm sạch vào data/interim/ để sẵn sàng cho bước tạo feature.
"""

import pandas as pd
import logging

logger = logging.getLogger(__name__)

def load_raw_data(data_path: str) -> dict:
    """
    Đọc tất cả các file CSV gốc từ thư mục dữ liệu thô.
    
    Args:
        data_path (str): Đường dẫn đến thư mục data/raw/
        
    Returns:
        dict: Dictionary chứa các DataFrame tương ứng với các file dữ liệu.
    """
    pass

def validate_data(dfs: dict) -> bool:
    """
    Thực hiện kiểm tra tính toàn vẹn của dữ liệu (data types, columns, missing values).
    
    Args:
        dfs (dict): Dictionary các DataFrame
        
    Returns:
        bool: True nếu dữ liệu hợp lệ, ngược lại False.
    """
    pass

def preprocess_raw_data(dfs: dict) -> dict:
    """
    Xử lý sơ bộ dữ liệu thô (ví dụ: điền giá trị thiếu của giá dầu, chuẩn hóa định dạng ngày tháng).
    
    Args:
        dfs (dict): Dictionary các DataFrame thô
        
    Returns:
        dict: Dictionary các DataFrame đã được làm sạch sơ bộ.
    """
    pass

def save_interim_data(dfs: dict, output_path: str):
    """
    Lưu các DataFrame đã làm sạch sơ bộ vào thư mục interim.
    
    Args:
        dfs (dict): Dictionary các DataFrame đã xử lý
        output_path (str): Đường dẫn đến data/interim/
    """
    pass
