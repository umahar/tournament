def tally(rows):
    table = [
        "Team                           | MP |  W |  D |  L |  P",
    ]
    teams = {}

    # Initialize teams with default values
    for row in rows:
        teams_l = row.partition(";")[0]
        temp_t = row.partition(";")[2]
        teams_r = temp_t.partition(";")[0]
        if teams_l not in teams:
            teams[teams_l] = [0, 0, 0, 0, 0]  # MP, W, D, L, P
        if teams_r not in teams:
            teams[teams_r] = [0, 0, 0, 0, 0]  # MP, W, D, L, P

    # Process match results
    for row in rows:
        teams_l = row.partition(";")[0]
        temp_t = row.partition(";")[2]
        teams_r = temp_t.partition(";")[0]
        result = temp_t.partition(";")[2]

        # Update the match count for both teams
        teams[teams_l][0] += 1
        teams[teams_r][0] += 1

        if result == "win":
            # Left team wins, right team loses
            teams[teams_l][1] += 1  # Win for left team
            teams[teams_l][4] += 3  # Points for left team
            teams[teams_r][3] += 1  # Loss for right team
        elif result == "loss":
            # Right team wins, left team loses
            teams[teams_r][1] += 1  # Win for right team
            teams[teams_r][4] += 3  # Points for right team
            teams[teams_l][3] += 1  # Loss for left team
        elif result == "draw":
            # Both teams draw
            teams[teams_l][2] += 1  # Draw for left team
            teams[teams_r][2] += 1  # Draw for right team
            teams[teams_l][4] += 1  # Points for left team
            teams[teams_r][4] += 1  # Points for right team

    # Format the table
    for team, score_board in sorted(teams.items(), key=lambda x: (-x[1][4], x[0])):
        t_name = team
        MP, W, D, L, P = score_board
        row = f"{t_name:30} |  {MP} |  {W} |  {D} |  {L} | {P:>2}"
        table.append(row)

    for i in table:
        print(i)

    return table


# Test the function with match results
results = [
    "Devastating Donkeys;Blithering Badgers;win",
    "Devastating Donkeys;Blithering Badgers;win",
    "Devastating Donkeys;Blithering Badgers;win",
    "Devastating Donkeys;Blithering Badgers;win",
    "Blithering Badgers;Devastating Donkeys;win",
]
print(tally(results))
