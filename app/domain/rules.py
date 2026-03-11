from random import randrange
from .models import LevelConfig, RoundResult

def get_level_config(level):
    configs = {
        1: LevelConfig(level=1, min_number=1, max_number=10, max_attempts=3),
        2: LevelConfig(level=2, min_number=1, max_number=20, max_attempts=5),
        3: LevelConfig(level=3, min_number=1, max_number=30, max_attempts=7),
    }
    return configs[level]

def generate_secret_number(min_number, max_number):
    return randrange(min_number, max_number + 1)

def compare_numbers(nb_user, nb_python):
    if nb_user > nb_python:
        return "too_high"
    if nb_user < nb_python:
        return "too_low"
    return "correct"

def calculate_gain(mise, attempt_number):
    if attempt_number == 1:
        return mise * 2
    if attempt_number == 2:
        return mise
    if attempt_number == 3:
        return mise // 2
    return 0

def update_balance_after_round(solde, mise, gain, won):
    if won:
        return solde + gain
    return solde - mise

def get_next_level(current_level, won):
    if won and current_level < 3:
        return current_level + 1
    if not won and current_level > 1:
        return current_level - 1
    return current_level
        