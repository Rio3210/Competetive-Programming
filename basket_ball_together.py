n, d = map(int, input().split())
player_powers = sorted(list(map(int, input().split())), reverse=True)
 
num_wins = 0
right_idx = n - 1
 
for left_idx in range(n):
    team_power = player_powers[left_idx]
    while right_idx > left_idx and team_power <= d:
        team_power += player_powers[left_idx]
        right_idx -= 1
    if team_power>d:
        num_wins += 1
print(num_wins)
