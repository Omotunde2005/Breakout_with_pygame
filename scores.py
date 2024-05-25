import pygame as pg


class ScoreBoard:
    def __init__(self, x, color, screen):
        self.screen = screen
        self.color = color
        self.x = x
        self.score = 0
        self.high_score = 0
        self.trials = 5
        self.font = pg.font.SysFont("calibri", 20)

    def show_scores(self):
        score_text = self.font.render(f"Score: {self.score}", True, self.color)
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, self.color)
        trials_text = self.font.render(f"Trials: X{self.trials}", True, self.color)

        score_text_rect = score_text.get_rect(topleft=(self.x, 10))
        high_score_text_rect = high_score_text.get_rect(topleft=(self.x, 26))
        trials_text_rect = trials_text.get_rect(topleft=(self.x, 42))

        self.screen.blit(score_text, (self.x, 10))
        self.screen.blit(high_score_text, (self.x, 26))
        self.screen.blit(trials_text, (self.x, 42))

    def is_game_over(self):
        if self.trials == 0:
            return True
        return False

    def game_over(self):
        game_over_color = 'red'
        game_over_font = pg.font.SysFont("calibri", 30)
        game_over_text = game_over_font.render(f"Game Over! Click '0' to restart.", True, game_over_color)
        game_over_rect = game_over_text.get_rect(topright=(50, 300))
        self.screen.blit(game_over_text, (50, 300))
        self.record_high_score()

    def success(self):
        game_success_color = 'green'
        game_success_font = pg.font.SysFont("calibri", 30)
        game_success_text = game_success_font.render(f"You won! Click '0' to restart.", True, game_success_color)
        game_success_rect = game_success_text.get_rect(topleft=(50, 300))
        self.screen.blit(game_success_text, (50, 300))
        self.record_high_score()

    def set_high_score(self):
        try:
            with open("records.txt", mode="r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            with open("records.txt", mode="w") as data:
                data.write("0")
                score = 0
        else:
            score = lines[0]

        self.high_score = int(score)

    def record_high_score(self):
        if self.score > self.high_score:
            with open("records.txt", mode="w") as file:
                file.write(f"{self.score}")
