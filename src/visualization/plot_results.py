"""
Module visualization: Vẽ đồ thị và trực quan hóa kết quả dự báo, sai số.

Mục đích:
- Vẽ biểu đồ thực tế vs dự báo theo chuỗi thời gian cho một vài store/item tiêu biểu.
- Trực quan hóa mức độ quan trọng của đặc trưng (feature importance) nếu sử dụng mô hình dạng cây.
- Trực quan hóa sai số phân khúc (ví dụ: bar chart sai số theo store, heatmap sai số theo family vs store).
- Lưu các đồ thị dưới dạng hình ảnh vào reports/figures/ để nhúng vào báo cáo.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def plot_actual_vs_predicted(df_plot: pd.DataFrame, store_nbr: int, item_nbr: int, save_path: str):
    """
    Vẽ biểu đồ so sánh doanh số thực tế và doanh số dự báo của một mặt hàng cụ thể tại một cửa hàng.
    
    Args:
        df_plot (pd.DataFrame): DataFrame chứa chuỗi thời gian thực tế và dự báo
        store_nbr (int): Mã cửa hàng
        item_nbr (int): Mã sản phẩm
        save_path (str): Đường dẫn lưu hình ảnh
    """
    pass

def plot_error_distribution(y_true: pd.Series, y_pred: pd.Series, save_path: str):
    """
    Vẽ phân phối sai số dự báo (residuals distribution).
    
    Args:
        y_true (pd.Series): Doanh số thực tế
        y_pred (pd.Series): Doanh số dự báo
        save_path (str): Đường dẫn lưu hình ảnh
    """
    pass

def plot_segment_errors(store_errors: pd.DataFrame, family_errors: pd.DataFrame, save_dir: str):
    """
    Vẽ các biểu đồ cột biểu diễn sai số theo cửa hàng và theo nhóm sản phẩm.
    
    Args:
        store_errors (pd.DataFrame): Bảng sai số theo cửa hàng
        family_errors (pd.DataFrame): Bảng sai số theo nhóm sản phẩm
        save_dir (str): Thư mục lưu các biểu đồ
    """
    pass
