import axelrod as axl

all_players = []
for s in axl.all_strategies:
    try:
        player_instance = s()
        all_players.append(player_instance)
    except Exception:
        continue 

print(f"Das große Haifischbecken wird vorbereitet mit {len(all_players)} robusten Strategien...")

# 1000 Runden, 1 Wiederholung für schnellen Cloud-Durchlauf
tournament = axl.Tournament(players=all_players, turns=1000, repetitions=1)
results = tournament.play()

print("\n" + "="*50)
print("     DAS OFFIZIELLE AXELROD HAIFISCHBECKEN (TOP 20)")
print("="*50)
for position, player in enumerate(results.ranked_names[:20], start=1):
    print(f"{position}. Platz: {player}")
print("="*50 + "\n")
