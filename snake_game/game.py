import pygame

class Game:
    def __init__(self):
        pygame.init()

        self._clock = pygame.Clock()

        self._running = True

    def run(self):
        while self.running:
            self._poll_events()

            self.update()
            self.render()

            self._clock.tick(60)

    def quit(self):
        pygame.quit()
    
    def poll_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
    
    def update(self):
        pass

    def render(self):
        pass