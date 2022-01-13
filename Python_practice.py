voting_data = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in voting_data.items():
    print(f"{county} county has {voters:,} registered voters.")