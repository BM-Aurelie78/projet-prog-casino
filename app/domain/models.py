from dataclasses import dataclass, field


@dataclass
class Player:
    name_user: str
    dotation: int = 10
    solde: int = 10
    level: int = 1


@dataclass
class LevelConfig:
    level: int
    min_number: int
    max_number: int
    max_attempts: int


@dataclass
class RoundResult:
    won: bool
    attempts_used: int
    gain: int
    new_balance: int
    next_level: int


@dataclass
class GameStats:
    total_games: int = 0
    wins: int = 0
    losses: int = 0
    highest_gain: int = 0
    total_bet: int = 0
    first_try_wins: int = 0
    max_level_reached: int = 1
    successful_attempts: list[int] = field(default_factory=list)