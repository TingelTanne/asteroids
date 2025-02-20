import pygame
from constants import *
from player import *
from asteroid import *
from asteroidsfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    updateble = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updateble, drawable)
    Asteroid.containers = (asteroids, updateble, drawable)
    AsteroidField.containers = (updateble, )
    Shot.containers = (shots, updateble, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for thing_to_update in updateble:
            thing_to_update.update(dt)
        
        for asteroid in asteroids:
            if asteroid.check_colliding(player):
                exit("Game over!")
        
        for thing_to_draw in drawable:
            thing_to_draw.draw(screen)
        
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()