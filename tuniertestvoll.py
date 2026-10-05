import axelrod as axl

# 1. Das ist die magische Zeile: Sie liest ALLE im Framework existierenden Strategien ein!
# Über 200 Stück, inklusive KIs, Klassikern und deiner neuen Strategie.
all_players = [s() for s in axl.all_strategies]

print(f"Turnier wird vorbereitet mit {len(all_players)} Strategien...")

# 2. Das riesige Turnier konfigurieren (1000 Runden)
# Wir nutzen 2 Wiederholungen (repetitions=2), damit die GitHub-Server nicht zu lange rechnen
tournament = axl.Tournament(players=all_players, turns=1000, repetitions=2)

# 3. Das Turnier starten
results = tournament.play()

# 4. Die Top 20 im Terminal ausgeben
print("\n" + "="*50)
print("     DAS OFFIZIELLE AXELROD HAIFISCHBECKEN (TOP 20)")
print("="*50)
for position, player in enumerate(results.ranked_names[:20], start=1):
    print(f"{position}. Platz: {player}")
print("="*50 + "\n")
