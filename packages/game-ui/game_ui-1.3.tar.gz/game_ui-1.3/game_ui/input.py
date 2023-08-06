import pygame

pygame.init()

class Input:
    def __init__(self, surface,  **args):
        inputs.append(self)

        self.x = 0; self.y = 0
        self.width = 200; self.height = 50
        self.noText = 'Text'
        self.text = ''
        self.textColor = (255, 255, 255)
        self.color = (150, 150, 150)
        self.pressedColor = (100, 100, 100)
        self.fontSize = 30

        self.maxChars = 16

        self.font = pygame.font.Font(None, self.fontSize)

        self.mode = 0
        self.render = True
        self.surface = surface

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        for arg in args:

            if arg == 'x':
                self.x = args[arg]
            if arg == 'y':
                self.y = args[arg]
            
            if arg == 'width':
                self.width = args[arg]
            if arg == 'height':
                self.height = args[arg]
            
            if arg == 'noText':
                self.noText = args[arg]
            
            if arg == 'textColor':
                self.textColor = args[arg]
            if arg == 'color':
                self.color = args[arg]
            if arg == 'pressedColor':
                self.pressedColor = args[arg]
            
            if arg == 'fontSize':
                self.fontSize = args[arg]
            
            if arg == 'maxChars':
                self.maxChars = args[arg]
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.font = pygame.font.Font(None, self.fontSize)
    
    def setRender(self, value):
        if value:
            self.render = True
        elif not value:
            self.render = False

    def Press(self, key):
        keys = pygame.key.get_pressed()

        if not keys[pygame.K_BACKSPACE] and self.mode == 1 and len(self.text) < self.maxChars:
            self.text += key
        elif keys[pygame.K_BACKSPACE] and self.mode == 1 and self.text != '':
            self.text = self.text[:-1]

    def update(self):
        b1, b2, b3 = pygame.mouse.get_pressed()
        mx, my = pygame.mouse.get_pos()

        if b1 and self.rect.collidepoint(mx, my):
            self.mode = 1
        elif b1 and not self.rect.collidepoint(mx, my):
            self.mode = 0
        
        self.draw()


    def draw(self):
        if self.render:

            if self.mode == 0:
                pygame.draw.rect(self.surface, self.color, self.rect)
            elif self.mode == 1:
                pygame.draw.rect(self.surface, self.pressedColor, self.rect)

            if self.text == '':
                noText = self.font.render(self.noText, 1, self.textColor)
                textWin = noText.get_rect(center=((self.rect.x + noText.get_width() // 2) + 5, self.rect.y + self.height // 2))

                self.surface.blit(noText, textWin)
            else:
                Text = self.font.render(self.text, 1, self.textColor)
                textWin = Text.get_rect(center=((self.rect.x + Text.get_width() // 2) + 5, self.rect.y + self.height // 2))

                self.surface.blit(Text, textWin)

inputs = []