"""
Module tune_model: Tìm kiếm siêu tham số tối ưu sử dụng Optuna.

Mục đích:
- Định nghĩa hàm mục tiêu (objective function) cho Optuna.
- Xác định không gian tìm kiếm (search space) cho SARIMA hoặc các mô hình khác.
- Tích hợp cross-validation trong quá trình tune để đánh giá khách quan điểm số.
- Lưu lại lịch sử tuning (study) và export tham số tốt nhất ra file config hoặc log lên MLflow.
"""

import optuna
import logging

logger = logging.getLogger(__name__)

def objective(trial: optuna.Trial, train_df: pd.DataFrame, cv_params: dict) -> float:
    """
    Hàm mục tiêu cho Optuna đánh giá độ lỗi (Weighted RMSLE) dựa trên hyperparameters được gợi ý.
    
    Args:
        trial (optuna.Trial): Đối tượng thử nghiệm của Optuna
        train_df (pd.DataFrame): Dữ liệu huấn luyện
        cv_params (dict): Tham số cấu hình cross-validation
        
    Returns:
        float: Điểm lỗi trung bình trên các fold validation
    """
    pass

def run_tuning(config_path: str):
    """
    Khởi tạo và chạy Optuna study để tìm bộ tham số tối ưu.
    
    Args:
        config_path (str): Đường dẫn đến file config.yaml
    """
    pass
