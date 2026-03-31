# Liste, um alle Ergebnisse zu speichern
results = []

# Conv Layer 1
macs = (32 * 32 * 32) * (3 * 3 * 3)
weights = (3 * 3 * 3) * 32 + 32
results.append({"layer": "Conv1", "MACs": macs, "Weights": weights})

# Conv Layer 2
macs = (32 * 32 * 32) * (3 * 3 * 32)
weights = (3 * 3 * 32) * 32 + 32
results.append({"layer": "Conv2", "MACs": macs, "Weights": weights})

# Conv Layer 3
macs = (16 * 16 * 64) * (3 * 3 * 32)
weights = (3 * 3 * 32) * 64 + 64
results.append({"layer": "Conv3", "MACs": macs, "Weights": weights})

# Conv Layer 4
macs = (16 * 16 * 64) * (3 * 3 * 64)
weights = (3 * 3 * 64) * 64 + 64
results.append({"layer": "Conv4", "MACs": macs, "Weights": weights})

# Conv Layer 5
macs = (8 * 8 * 128) * (3 * 3 * 64)
weights = (3 * 3 * 64) * 128 + 128
results.append({"layer": "Conv5", "MACs": macs, "Weights": weights})

# Conv Layer 6
macs = (8 * 8 * 128) * (3 * 3 * 128)
weights = (3 * 3 * 128) * 128 + 128
results.append({"layer": "Conv6", "MACs": macs, "Weights": weights})

# FC Layer 1
macs = 2048 * 128
weights = 2048 * 128 + 128
results.append({"layer": "FC1", "MACs": macs, "Weights": weights})

# FC Layer 2
macs = 128 * 310
weights = 128 * 310 + 310
results.append({"layer": "FC2", "MACs": macs, "Weights": weights})

# FC Layer 3
macs = 310 * 10
weights = 310 * 10 + 10
results.append({"layer": "FC3", "MACs": macs, "Weights": weights})

# Ausgabe der Ergebnisse
for r in results:
    print(f"{r['layer']}: MACs = {r['MACs']}, Weights = {r['Weights']}")

# Optional: Gesamtsummen berechnen
total_macs = sum(r["MACs"] for r in results)
total_weights = sum(r["Weights"] for r in results)
print(f"\nTotal MACs = {total_macs}")
print(f"Total Weights = {total_weights}")