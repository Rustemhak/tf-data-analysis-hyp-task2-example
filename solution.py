import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu

chat_id = 326525586 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    _, p_value = mannwhitneyu(x, y, alternative="two-sided")
    alpha = 0.07
    return p_value < alpha # Ваш ответ, True или False
