from app.domain.models import Player
from app.domain.rules import (
    get_level_config,
    generate_secret_number,
    compare_numbers,
    calculate_gain,
    update_balance_after_round,
    get_next_level,
)
from app.domain.stats_service import (
    create_empty_stats,
    register_round,
    stats_to_dict,
    dict_to_stats,
)
from app.infrastructure.stats_repository import save_stats, load_stats
from app.interface.console_ui import (
    afficher_message_accueil,
    demander_pseudo,
    afficher_message_bienvenue,
    demander_voir_regles,
    afficher_regles,
    demander_mise,
    demander_nombre,
    afficher_nombre_trop_grand,
    afficher_nombre_trop_petit,
    afficher_victoire,
    afficher_defaite,
    demander_continuer_jeu,
    afficher_passage_niveau,
    afficher_fin_partie,
)


def run_game():
    afficher_message_accueil()

    pseudo = demander_pseudo()
    player = Player(name_user=pseudo)

    afficher_message_bienvenue(player.name_user, player.dotation)

    if demander_voir_regles():
        afficher_regles()

    saved_stats = load_stats(player.name_user)
    stats = dict_to_stats(saved_stats) if saved_stats else create_empty_stats()

    continue_game = True

    while continue_game and player.solde > 0:
        round_result = play_round(player, stats)

        player.solde = round_result.new_balance
        player.level = round_result.next_level

        save_stats(player.name_user, stats_to_dict(stats))

        if player.solde <= 0:
            afficher_fin_partie(player.solde)
            break

        continue_game = demander_continuer_jeu()
        if continue_game:
            afficher_passage_niveau(player.level)
        else:
            afficher_fin_partie(player.solde)


def play_round(player, stats):
    config = get_level_config(player.level)
    mise = demander_mise(1, player.solde)
    nb_python = generate_secret_number(config.min_number, config.max_number)

    won = False
    gain = 0
    attempts_used = 0

    for attempt in range(1, config.max_attempts + 1):
        nb_user = demander_nombre(config.min_number, config.max_number)
        attempts_used = attempt

        result = compare_numbers(nb_user, nb_python)

        if result == "correct":
            won = True
            gain = calculate_gain(mise, attempt)
            afficher_victoire(attempt)
            break
        elif result == "too_high":
            afficher_nombre_trop_grand()
        else:
            afficher_nombre_trop_petit()

    if not won:
        afficher_defaite(nb_python)

    new_balance = update_balance_after_round(player.solde, mise, gain, won)
    next_level = get_next_level(player.level, won)

    register_round(stats, player.level, mise, won, gain, attempts_used)

    from app.domain.models import RoundResult
    return RoundResult(
        won=won,
        attempts_used=attempts_used,
        gain=gain,
        new_balance=new_balance,
        next_level=next_level,
    )