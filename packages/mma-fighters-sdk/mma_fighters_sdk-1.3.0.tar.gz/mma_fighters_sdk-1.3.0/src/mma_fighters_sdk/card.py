import random
from mma_fighters_sdk.card_param import CardParam
from mma_fighters_sdk import const


class Card:

    def __init__(self, param: CardParam = None):
        if not param:
            raise ValueError("Card param did not set!")

        self.param = param

    def kick_power(self) -> dict:
        power = self.param.power
        percent_double_power = random.randint(0, 100)

        # Technique logic
        if self.param.techniques:
            # Get random number 0-100 and compare if any are equal
            techniques_random_values = {random.randint(0, 100) for _ in range(0, 25)}
            techniques_random_to_compare_chance = {random.randint(0, 100) for _ in range(0, 25)}
            if techniques_random_values & techniques_random_to_compare_chance:
                # Get technique and compare random chance
                tech = random.choice(self.param.techniques)
                percent_technique = random.randint(0, 100)
                if percent_technique <= tech.max_number_randomize:
                    return {
                        const.KICK_TYPE: const.KICK_TYPE_TECHNIQUE,
                        const.POWER: tech.power,
                        const.TECHNIQUE_NAME: tech.name,
                        const.NAME: self.param.name
                        }

        # Double power
        if percent_double_power <= self.param.max_percent_double_power:
            return {const.KICK_TYPE: const.KICK_TYPE_DOUBLE_POWER, const.POWER: power * 2, const.NAME: self.param.name}

        random_power = power * (random.randint(0, self.param.max_percent_randomize) / 100)

        # Random increase or decrease of power
        if random.randint(0, 1):
            power += random_power
        else:
            power -= random_power

        # Default kick
        return {
            const.POWER: power,
            const.KICK_TYPE: const.KICK_TYPE_KICK,
            const.NAME: self.param.name
        }

    def defend(self, power: dict) -> dict:
        block = random.randint(0, 100)
        miss = random.randint(0, 100)
        status_message = {
            const.BATTLE_STATUS: {
                const.DEFEND_USER: self.param.name,
                const.ATTACK_USER: power[const.NAME]
            }
        }

        if block <= self.param.max_percent_block:
            status_message[const.KICK_TYPE] = const.DEFEND_TYPE_BLOCK_KICK
            status_message[const.GET_DAMAGE_FROM_ENEMY] = 0
            return status_message

        if miss <= self.param.max_percent_miss:
            status_message[const.KICK_TYPE] = const.DEFEND_TYPE_MISS_KICK
            status_message[const.GET_DAMAGE_FROM_ENEMY] = 0
            return status_message

        # Parse kick enemy
        self.param.health -= power[const.POWER]
        status_message[const.HEALTH] = self.health()
        status_message[const.GET_DAMAGE_FROM_ENEMY] = power[const.POWER]
        status_message[const.KICK_TYPE] = power[const.KICK_TYPE]

        return status_message

    def health(self) -> float:
        return round(self.param.health, 2)

    def status(self) -> dict:
        return {const.NAME: self.param.name, const.HEALTH: self.param.health, const.LOSE: self.param.health <= 0}