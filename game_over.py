import pygame.ftfont

class Game_over:
	def __init__(self,screen,stats):
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.width, self.height = self.screen_rect.width, self.screen_rect.height
		self.go_color = (0,0,0)
		self.text_color = (255, 255, 255)
		self.font_size = int(self.screen_rect.height/15)
		self.font = pygame.font.SysFont(None, self.font_size)
		self.rect = pygame.Rect(0, 0, self.width, self.height)

		# msg 1 (Game Over msg)
		self.msg0_image = self.font.render("Game Over", True, self.text_color, self.go_color)
		self.msg0_image_rect = self.msg0_image.get_rect()
		self.msg0_image_rect.center = (self.rect.centerx,self.rect.centery - self.font_size*2)

		# msg 2 (score)
		self.msg1_image = self.font.render("Score : {:,}".format(stats.score), True, self.text_color, self.go_color)
		self.msg1_image_rect = self.msg1_image.get_rect()
		self.msg1_image_rect.center = (self.rect.centerx,self.rect.centery - self.font_size)

		# msg 3 (high score)
		self.msg2_image = self.font.render("High Score : {:,}".format(stats.high_score), True, self.text_color, self.go_color)
		self.msg2_image_rect = self.msg2_image.get_rect()
		self.msg2_image_rect.center = (self.rect.centerx,self.rect.centery)

		# msg 4 (level)
		self.msg3_image = self.font.render("Level : {:,}".format(stats.level), True, self.text_color, self.go_color)
		self.msg3_image_rect = self.msg3_image.get_rect()
		self.msg3_image_rect.center = (self.rect.centerx,self.rect.centery + self.font_size)

		# msg 5 (Click to continue)
		self.msg4_image = self.font.render("Click to Continue", True, self.text_color, self.go_color)
		self.msg4_image_rect = self.msg4_image.get_rect()
		self.msg4_image_rect.center = (self.rect.centerx,self.rect.centery + self.font_size*2)

	def draw_button(self):
		self.screen.fill(self.go_color)
		self.screen.blit(self.msg0_image, self.msg0_image_rect)
		self.screen.blit(self.msg1_image, self.msg1_image_rect)
		self.screen.blit(self.msg2_image, self.msg2_image_rect)
		self.screen.blit(self.msg3_image, self.msg3_image_rect)
		self.screen.blit(self.msg4_image, self.msg4_image_rect)