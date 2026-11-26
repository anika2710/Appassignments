import numpy as np
import pandas as pd

runs = np.array([3500, 6200, 8500, 4200, 10500])

print("Average Runs:", np.mean(runs))
print("Highest Runs:", np.max(runs))
print("Lowest Runs:", np.min(runs))

players = pd.DataFrame({
    'Player': ['Player 1', 'Player 2', 'Player 3', 'Player 4', 'Player 5'],
    'Runs': runs
})

print("\nCricket Statistics:")
print(players)

print("\nPlayers scoring more than 5000 runs:")
print(players[players['Runs'] > 5000])
