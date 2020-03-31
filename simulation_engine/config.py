SOCIAL_GROUPS = [
    {
        "name": "Family",
        # What is the probability that an individual is in N groups?
        # E.g. member of only one family, but two sports teams
        # Key: number of groups, Value: probability
        "pct_population_in_a_group": 1,
        # What is the size of the group?
        # Key: members in group, Value: probability
        "prob_group_size": {
            1: 0.25,
            2: 0.50,
            3: 0.05,
            4: 0.20
        },
        # Should groups be created with replacement?
        # i.e., Can a member belong to more than one of these groups
        "with_replacement": False
    },
    {
        "name": "Workplace",
        "pct_population_in_a_group": 0.5,
        "prob_group_size": {
            2: 0.10,
            3: 0.10,
            4: 0.10,
            5: 0.30,
            6: 0.30,
            7: 0.05,
            8: 0.05
        },
        "with_replacement": False
    }
]

INFECTION_TRANSMISSION_RECORDS = [
    ({"connection_type": "Family", "behaviour_infected": "Normal", "behaviour_susceptible": "Normal"}, 0.25),
    ({"connection_type": "Workplace", "behaviour_infected": "Normal", "behaviour_susceptible": "Normal"}, 0.05)
]
