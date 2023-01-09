import pygame


pygame.init()


class Game():
    """Класс игры"""
    __red = (254, 24, 0)
    __yellow = (255, 240, 0)
    __dark_gray = (96, 96, 96)
    __light_gray = (150, 150, 150)
    __super_light_gray = (240, 240, 240)

    def __init__(self):
        """Инициализация"""
        self.__red_sign=2
        self.__yellow_sign=3
        self.__column_count = 6
        self.__row_count = 6+1
        self.__field_list = [
            [0]*self.__column_count for i in range(self.__row_count)]
        self.__color_player = ''
        self.__query = 0
        self.__lst = [[self.__row_count]*self.__column_count]
        self.__margin = 10
        self.__size_cell = 60
        self.__bg_color = self.__dark_gray
        self.__cell_color = self.__light_gray
        self.__navigation_chip_color = self.__super_light_gray
        self.__width_field = (
            (self.__column_count*self.__size_cell) + (self.__margin*(self.__column_count+1)))
        self.__height_field = (
            (self.__row_count*self.__size_cell) + (self.__margin*(self.__row_count+1)))
        self.__size_field = (self.__width_field, self.__height_field)
        self.__screen = pygame.display.set_mode(self.__size_field)
    @property
    def get_red_sign(self):
        return self.__red_sign
    @property
    def get_yellow_sign(self):
        return self.__yellow_sign

    def column_number(self):
        return (pygame.mouse.get_pos()[0]//(self.__margin+self.__size_cell))

    def draw_game_field(self):
        """Отрисовка игрового поля"""
        for row in range(self.__row_count):
            for col in range(self.__column_count):
                x = col*self.__size_cell+(col+1)*self.__margin
                y = row*self.__size_cell+(row+1)*self.__margin
                if self.__field_list[row][col] == self.__red_sign:
                    self.__color_player = self.__red
                elif self.__field_list[row][col] == self.__yellow_sign:
                    self.__color_player = self.__yellow
                else:
                    self.__color_player = self.__light_gray
                pygame.draw.rect(self.__screen, self.__color_player,
                                 (x, y, self.__size_cell, self.__size_cell))
                self.move_navigation_chip(row, col, x, y)

    def move_navigation_chip(self, row, col, x, y):
        """Отрисовка двигающегося навигационного курсора"""
        column = self.column_number()
        if column==6:
            column=5
        self.__field_list[0][column] = 1
        if self.__field_list[row][col] == 1:
            if self.__query%2==0:
                self.__navigation_chip_color = self.__red
            else:
                self.__navigation_chip_color = self.__yellow
        else:
            self.__navigation_chip_color = self.__super_light_gray
        if row == 0:
            pygame.draw.rect(self.__screen, self.__navigation_chip_color,
                             (x, y, self.__size_cell, self.__size_cell))
        self.__field_list[0][column] = 0                                          

    def put_chip(self):
        self.column = self.column_number()
        for i in self.__lst:
            if i[self.column] != 1:
                i[self.column] -= 1
                if self.__query % 2 == 0:
                    self.__field_list[i[self.column]][self.column] = self.__red_sign
                else:
                    self.__field_list[i[self.column]][self.column] = self.__yellow_sign
                self.__query += 1

    def fill_screen(self):
        """Заливка заднего фона"""
        self.__screen.fill(self.__bg_color)

    def winning(self,sign):
        # ничья
        zeroes = 0
        for row in range(1, self.__row_count):
            zeroes += self.__field_list[row].count(0)
            if zeroes == 0:
                return True

        # победа по горизонлати
        for col in range(self.__column_count-3):
            for row in range(self.__row_count):
                if self.__field_list[row][col] == sign and self.__field_list[row][col+1] == sign and self.__field_list[row][col+2] == sign and self.__field_list[row][col+3] == sign:
                    return True

        # победа по вертикали
        for col in range(self.__column_count):
            for row in range(self.__row_count-3):
                if self.__field_list[row][col] == sign and self.__field_list[row+1][col] == sign and self.__field_list[row+2][col] == sign and self.__field_list[row+3][col] == sign:
                    return True

        # победа по главной диагонали
        for col in range(self.__column_count-3):
            for row in range(self.__row_count-3):
                if self.__field_list[row][col] == sign and self.__field_list[row+1][col+1] == sign and self.__field_list[row+2][col+2] == sign and self.__field_list[row+3][col+3] == sign:
                    return True

        # победа по побочной диагонали
        for col in range(self.__column_count-3):
            for row in range(3, self.__row_count):
                if self.__field_list[row][col] == sign and self.__field_list[row-1][col+1] == sign and self.__field_list[row-2][col+2] == sign and self.__field_list[row-3][col+3] == sign:
                    return True


game = Game()
clock = pygame.time.Clock()
FPS = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.put_chip()
    if game.winning(game.get_red_sign):
        running = False
        print('Победа красного')
    if game.winning(game.get_yellow_sign):
        running = False
        print('Победа желтого')
    game.fill_screen()
    game.draw_game_field()
    pygame.display.update()
    clock.tick(FPS)
