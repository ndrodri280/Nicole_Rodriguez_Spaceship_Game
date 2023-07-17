from game.components.enemies.enemy import Enemy, Enemy2
from random import randint, choice
class EnemyManager:
    def __init__(self):
        self.enemies =[]


    def update(self):
        self.add_enemy()
        
        for enemy  in self.enemies:
            enemy.update(self.enemies)
        for enemy2 in self.enemies:
            enemy2.update(self.enemies)
    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)
        for enemy2 in self.enemies:
            enemy2.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 1:
            enemy_type = choice([Enemy, Enemy2])  
            enemy = enemy_type()  
            self.enemies.append(enemy)
        

   