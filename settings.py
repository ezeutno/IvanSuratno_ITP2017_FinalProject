class Settings():
    def __init__(self):
        #Screen Settings
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.caption = 'Matching Cards'

        # speed factor for dynamic changes to the Lv
        self.time_scale = 1.2
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        # point setting
        self.card_points = 5
        # timer setting
        self.min_fr_time = 0.00005

    def increase_data(self):
        self.card_points = int(self.card_points*self.score_scale)
        self.min_fr_time = self.min_fr_time*self.time_scale

