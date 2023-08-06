from mma_fighters_sdk.card import Card


class Battle:
    def __init__(self, user1: Card, user2: Card):

        self.user1, self.user2 = user1, user2
        self.status = []

    def start(self):
        if self.check_health():
            return self._battle_status()

        user1_power, user2_power = self.user1.kick_power(), self.user2.kick_power()
        self.status.append(self.user2.defend(user1_power))
        if self.check_health():
            return self._battle_status()

        self.status.append(self.user1.defend(user2_power))
        if self.check_health():
            return self._battle_status()

        return self.start()

    def _battle_status(self) -> list:
        self.status.append(self.user1.status())
        self.status.append(self.user2.status())

        return self.status

    def check_health(self) -> bool:
        return self.user1.health() < 0 or self.user2.health() < 0
