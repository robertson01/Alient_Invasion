file_record = 'record.txt'
class GameStats:
    """Отслеживание статистики  для игры Alien Invasion"""

    def __init__(self, ai_game):
        """Инициализирует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()
        # Игра Alien Invasion запускается в неактивном состоянии.
        self.game_active = False
        # Рекорд не должен сбрасываться.
        self.high_score = self.read_high_score()

    def write_high_score(self):
        """Запись рекорда в файл после выхода игры"""
        with open(file_record, 'w') as file:
            file.write(str(self.high_score))

    def read_high_score(self):
        with open(file_record, 'r') as file:
            self.high_score = file.read()
        return int(self.high_score)

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1