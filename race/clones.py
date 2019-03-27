import random

racers = (('<:DoggoHorde:560208530724880477>', 'fast'), ('<:SpinningSaw:560208592200925184>', 'fast'), ('<:FlyingDoggos:560208528728653836>', 'fast'), ('<:FireBirds:560208529621909515>', 'fast'),
          ('<:Doggos:560208530389467146>', 'fast'), ('<:BombSpider:560208347677327392>', 'fast'), ('<:Balloon:560208343864573982>', 'fast'), ('<:BouncyBomb:560208346498727988>', 'fast'),
          ('<:StrikerBoy:560208590405894174>', 'steady'), ('<:Spiky:560208588795019269>', 'steady'), ('<:Rogue:560208589348667392>', 'steady'),
          ('<:Lumberjackie:560208530833932289>', 'steady'), ('<:Bombfly:560208346204995615>', 'steady'), ('<:BlastRocket:560208346536476672>', 'abberant'),
          ('<:Icicle:560208530716491776>', 'abberant'), ('<:BombBirds:560208344573411370>', 'abberant'), ('<:BlastFish:560208346045480981>', 'abberant'),
          ('<:BlastBot:560208345219203082>', 'abberant'), ('<:Fireball:560208531266076693>', 'abberant'), ('<:Magnet:560208529391091714>', 'abberant'),
          ('<:Snatcher:560208588006752277>', 'predator'), ('<:ClusterBomb:560208527877079043>', 'predator'), ('<:CoreBomber:560208529718509588>', 'special'), ('<:AntiGravity:560208344002986120>', 'special'), 
          ('<:BombFrog:560208347132067897>', 'special'), ('<:PufferBug:560208588253954108>', 'slow'), ('<:FlyingBarrel:560208530049859614>', 'slow'), ('<:BombGolem:560208347769471016>', 'slow'),
          ('<:BombDrone:560208346452590592>', 'slow'), ('<:BigSmith:560208349430284303>', 'slow'), ('<:FloatingBomb:560208528761946131>', 'slow'), ('<:Arrows:560208346213253121>', 'slow'),
          ('<:StickyBomb:560208588891750410>', 'slow'), ('<:PlainBomb:560208528590241853>', 'slow'), ('<:MiniBomb:560208528053108761>', 'slow'))


class Clone:
    def __init__(self, emoji, _type):
        self.emoji = emoji
        self._type = _type
        self.track = '•   ' * 20
        self.position = 80
        self.turn = 0
        self.current = self.track + self.emoji

    def move(self):
        self._update_postion()
        self.turn += 1
        return self.current

    def _update_postion(self):
        distance = self._calculate_movement()
        self.current = ''.join((self.track[:max(0, self.position - distance)], self.emoji,
                                self.track[max(0, self.position - distance):]))
        self.position = self._get_position()

    def _get_position(self):
        return self.current.find(self.emoji)

    def _calculate_movement(self):
        if self._type == 'slow':
            return random.randint(1, 3) * 3
        elif self._type == 'fast':
            return random.randint(0, 4) * 3

        elif self._type == 'steady':
            return 2 * 3

        elif self._type == 'abberant':
            if random.randint(1, 100) >= 90:
                return 5 * 3
            else:
                return random.randint(0, 2) * 3

        elif self._type == 'predator':
            if self.turn % 2 == 0:
                return 0
            else:
                return random.randint(2, 5) * 3

        elif self._type == 'special':
            if self.turn % 3:
                return random.choice([len('blue'), len('red'), len('green')]) * 3
            else:
                return 0
        else:
            if self.turn == 1:
                return 14 * 3
            elif self.turn == 2:
                return 0
            else:
                return random.randint(0, 2) * 3
