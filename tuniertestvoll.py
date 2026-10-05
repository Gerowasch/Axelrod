import axelrod as axl

# 1. Sicherheitsfilter: Lädt nur die KIs und Strategien, die fehlerfrei starten
all_players = []
for s in axl.all_strategies:
    try:
        player_instance = s()
        all_players.append(player_instance)
    except Exception:
        continue  # Überspringt fehlerhafte oder unvollständige Fremdstrategien

print(f"Das große Haifischbecken wird vorbereitet mit {len(all_players)} Strategien...")

# 2. Rundenanzahl bleibt bei 1000, aber Wiederholungen (repetitions) auf 1 oder 2 setzen!
# Das spart den Servern Stunden an Rechenzeit, liefert aber ein klares Ergebnis.
tournament = axl.Tournament(players=all_players, turns=1000, repetitions=1)

# 3. Turnier starten
results = tournament.play()

# 4. Die Top 20 sauber ausgeben
print("\n" + "="*50)
print("     DAS OFFIZIELLE AXELROD HAIFISCHBECKEN (TOP 20)")
print("="*50)
for position, player in enumerate(results.ranked_names[:20], start=1):
    print(f"{position}. Platz: {player}")
print("="*50 + "\n")
