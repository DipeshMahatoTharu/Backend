"""
Practice Project: Cricket Player Management
===========================================
Requirements:
1. Create a `Player` class:
   - Attributes: `name` (str), `role` (str, e.g., "Batsman", "Bowler", "All-rounder"), `matches` (int), `runs` (int), `wickets` (int).
   - Methods:
     - `get_batting_average()`: Returns (runs / matches) or 0 if matches = 0.
     - `get_bowling_average()`: Returns (runs_conceded / wickets) or 0 if wickets = 0. (For simplicity, we can assume a concession or just use a fixed ratio, or just runs/wickets). Let's use `runs / wickets` or just a mock `runs_conceded` parameter in the method. Let's make it simpler: `get_bowling_strike_rate()` which is `matches * 6 / wickets` if wickets > 0 else 0, or just calculate a standard average. Let's use standard runs scored divided by matches for batting average.
2. Create a `CricketTeam` class:
   - Attributes: `team_name` (str), `players` (list of Player objects).
   - Methods:
     - `add_player(player)`: Adds a Player object to the team (max 11 players).
     - `get_total_runs()`: Returns the sum of runs scored by all players.
     - `get_total_wickets()`: Returns the sum of wickets taken by all players.
     - `get_team_stats()`: Displays a summary of all players, their roles, runs, wickets, and averages.

Write your code below and test it by running this file.
"""

class Player:
    def __init__(self, name: str, role: str, matches: int = 0, runs: int = 0, wickets: int = 0):
        # TODO: Initialize player attributes
        pass

    def get_batting_average(self) -> float:
        # TODO: Calculate batting average (runs / matches)
        return 0.0


class CricketTeam:
    def __init__(self, team_name: str):
        # TODO: Initialize team attributes
        pass

    def add_player(self, player: Player) -> bool:
        # TODO: Add player to team (ensure maximum limit of 11 players)
        pass

    def get_total_runs(self) -> int:
        # TODO: Calculate total runs scored by the team
        return 0

    def get_total_wickets(self) -> int:
        # TODO: Calculate total wickets taken by the team
        return 0

    def get_team_stats(self):
        # TODO: Display team statistics summary
        pass


# =====================================================================
# TEST SUITE (Run this file to verify your implementation)
# =====================================================================
if __name__ == "__main__":
    print("Testing Cricket Player Management Class...")
    
    # Try testing your code here:
    # team = CricketTeam("Nepal Rhinos")
    # p1 = Player("Sandeep Lamichhane", "Bowler", 50, 150, 120)
    # team.add_player(p1)
    # ...
    
    print("\nComplete the class implementation to pass the test cases!")
