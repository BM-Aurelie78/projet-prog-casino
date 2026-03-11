from .models import GameStats


def create_empty_stats():
    return GameStats()


def register_round(stats, level, mise, won, gain, attempts_used):
    stats.total_games += 1
    stats.total_bet += mise
    stats.max_level_reached = max(stats.max_level_reached, level)

    if won:
        stats.wins += 1
        stats.highest_gain = max(stats.highest_gain, gain)
        stats.successful_attempts.append(attempts_used)
        if attempts_used == 1:
            stats.first_try_wins += 1
    else:
        stats.losses += 1

    return stats


def compute_average_bet(stats):
    if stats.total_games == 0:
        return 0
    return stats.total_bet / stats.total_games


def compute_success_rate(stats):
    if stats.total_games == 0:
        return 0
    return (stats.wins / stats.total_games) * 100


def compute_average_attempts_on_success(stats):
    if not stats.successful_attempts:
        return 0
    return sum(stats.successful_attempts) / len(stats.successful_attempts)


def stats_to_dict(stats):
    return {
        "total_games": stats.total_games,
        "wins": stats.wins,
        "losses": stats.losses,
        "highest_gain": stats.highest_gain,
        "total_bet": stats.total_bet,
        "first_try_wins": stats.first_try_wins,
        "max_level_reached": stats.max_level_reached,
        "successful_attempts": stats.successful_attempts,
    }


def dict_to_stats(data):
    stats = GameStats()
    stats.total_games = data.get("total_games", 0)
    stats.wins = data.get("wins", 0)
    stats.losses = data.get("losses", 0)
    stats.highest_gain = data.get("highest_gain", 0)
    stats.total_bet = data.get("total_bet", 0)
    stats.first_try_wins = data.get("first_try_wins", 0)
    stats.max_level_reached = data.get("max_level_reached", 1)
    stats.successful_attempts = data.get("successful_attempts", [])
    return stats