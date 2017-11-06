import pygame

class Timer:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width = self.screen_rect.width
        self.height = self.screen_rect.height/100
        self.timer_color = (0,0,0)

    #minus the
    def update_time(self,min_fr_time):
        if self.width >= 0:
            self.width -= self.screen_rect.width*min_fr_time

    def get_time_left(self):
        return self.width

    def reset_time(self):
        self.width = self.screen_rect.width

    def draw_timer(self):
        self.rect = pygame.Rect(0,0,self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.top = self.screen_rect.top
        self.screen.fill(self.timer_color,self.rect)
