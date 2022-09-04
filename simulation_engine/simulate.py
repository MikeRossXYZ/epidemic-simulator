import random

import table
import config as config
from entity import Entity
from relation import Relation

from constants import HealthStatus


def update_health_status(entity):
    if (entity.health_status == HealthStatus.Infected):
        if (entity.days_at_health_status > 10):
            entity.health_status = HealthStatus.Resolved
            entity.days_at_health_status = 0

    entity.days_at_health_status += 1
    return entity.health_status


def relation_expose(ctx, relation, entity1, entity2):
    infection_prob_tbl = ctx.tables["infection_probability"]

    if (entity1.health_status == HealthStatus.Infected
            and entity2.health_status == HealthStatus.Susceptible):
        prob_infect = table.tbl_lookup_value(infection_prob_tbl, {
            "connection_type": relation.name,
            "behaviour_infected": entity1.behaviour,
            "behaviour_susceptible": entity2.behaviour
        })

        if (random.random() < prob_infect):
            entity2.health_status = HealthStatus.Infected
            entity2.days_at_health_status = 0

    if (entity2.health_status == HealthStatus.Infected
            and entity1.health_status == HealthStatus.Susceptible):
        prob_infect = table.tbl_lookup_value(infection_prob_tbl, {
            "connection_type": relation.name,
            "behaviour_infected": entity2.behaviour,
            "behaviour_susceptible": entity1.behaviour
        })

        if (random.random() < prob_infect):
            entity1.health_status = HealthStatus.Infected
            entity1.days_at_health_status = 0


def create_group(name, entity_lst):
    edges = []
    for a in entity_lst:
        for b in entity_lst:
            if a != b:
                edge = Relation(name, a, b)
                a.relations[b.name] = edge
                b.relations[a.name] = edge
                edges.append(edge)
    return edges


def create_population(ctx):
    population = []
    for i in range(10000):
        population.append(Entity(str(i)))
    return population


def create_relations(ctx, population):
    relations_all = []

    # Construct the social groups in the model
    for group in config.SOCIAL_GROUPS:
        n_sample = int(len(population) * group["pct_population_in_a_group"])
        sample = random.sample(population, n_sample)

        group_sizes = []
        group_probs = []
        for size, prob in group["prob_group_size"].items():
            group_sizes.append(size)
            group_probs.append(prob)

        n_to_add = 0
        cur_group = []
        while len(sample) > 0:
            if n_to_add == 0 or len(sample) == 0:
                if len(cur_group) > 0:
                    relations = create_group(group["name"], cur_group)
                    cur_group.clear()
                    relations_all.extend(relations)

                n_to_add = random.choices(group_sizes, group_probs, k=1)[0]
            else:
                # Add individual from our sample into this specific group
                # Remove them from the sample so they are not selected again
                cur_group.append(sample.pop())
                n_to_add -= 1

    return relations_all


def run_simulation(ctx):
    PROB_INFECTING_RANDOM = 0.10

    # Create the list of entities (people) in the simulation
    population = create_population(ctx)

    # Create the list of all relationships
    relations_all = create_relations(ctx, population)

    # Initial infected
    for infected in random.sample(population, 5):
        infected.health_status = HealthStatus.Infected

    # Simulation loop
    ctx.output("Susceptible,Infected,Resolved")
    for day in range(60):
        # Loop through each relationship to see if they infect the person
        for relation in relations_all:
            relation_expose(ctx, relation, relation.p1, relation.p2)

        counts = {
            HealthStatus.Susceptible: 0,
            HealthStatus.Infected: 0,
            HealthStatus.Resolved: 0
        }
        for person in population:
            # Will we randomly infect a stranger?
            stranger = random.choice(population)
            if stranger != person:
                if person.health_status == HealthStatus.Infected and stranger.health_status == HealthStatus.Susceptible:
                    if random.random() < PROB_INFECTING_RANDOM:
                        stranger.health_status = HealthStatus.Infected

            # Handle resolving infections
            update_health_status(person)
            counts[person.health_status] += 1

        ctx.output(f"{counts[HealthStatus.Susceptible]},{counts[HealthStatus.Infected]},{counts[HealthStatus.Resolved]}")

    # Close the output process
    ctx.output(None)
