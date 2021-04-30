from config import * 
from snake import *
from apple import * 
import pygame, sys

class Game():
    def __init__(self):
        pygame.init()
        self.screen= pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.BASICFONT= pygame.font.Font('freesansbold.ttf',18)
        pygame.display.set_caption('Snake Game')
        self.apple= apple()
        self.snake= snake()

    def resetGame(self):
        del self.snake
        del self.apple
        self.snake = snake()
        self.apple = apple()
        return True

    def isgameover(self):
        if(self.snake.snakeCoords[self.snake.HEAD]['x'] == -1 or self.snake.snakeCoords[self.snake.HEAD]['x'] == config.CELLWIDTH or self.snake.snakeCoords[self.snake.HEAD]['y'] == -1 or self.snake.snakeCoords[self.snake.HEAD]['y'] == config.CELLHEIGHT):
            return self.resetGame()
        
        for snakebody in self.snake.snakeCoords[1:]:
            if snakebody['x'] == self.snake.snakeCoords[self.snake.HEAD]['x'] and snakebody['y'] == self.snake.snakeCoords[self.snake.HEAD]['y']:
                return self.resetGame()


    def draw(self):
        self.screen.fill(config.BG_COLOR)
        self.drawGrid()
        self.drawApple()
        self.drawSnake()
        pygame.display.update()
        self.drawScore(len(self.snake.snakeCoords) - 3)
        self.clock.tick(config.FPS)

    def drawGrid(self):
        for x in range(0,config.WINDOW_WIDTH,config.CELLSIZE):
            pygame.draw.line(self.screen,config.DARKGRAY,(x,0), (x,config.WINDOW_HEIGHT))
        for y in range(0,config.WINDOW_HEIGHT,config.CELLSIZE):
            pygame.draw.line(self.screen,config.DARKGRAY,(0,y), (config.WINDOW_WIDTH,y))
    
    def drawSnake(self):
        for coord in self.snake.snakeCoords:
            x= coord['x'] * config.CELLSIZE
            y= coord['y'] * config.CELLSIZE
            snakeSegmentRect = pygame.Rect(x, y, config.CELLSIZE,config.CELLSIZE)
            pygame.draw.rect(self.screen, config.DARKGREEN, snakeSegmentRect)

            snakeInnerSegmentRect = pygame.Rect(x+4, y+4 , config.CELLSIZE-8, config.CELLSIZE-8)
            pygame.draw.rect(self.screen, config.GREEN, snakeInnerSegmentRect)

    def drawApple(self):
        x= self.apple.x * config.CELLSIZE
        y= self.apple.y * config.CELLSIZE
        appleRect = pygame.Rect(x,y,config.CELLSIZE, config.CELLSIZE)
        pygame.draw.rect(self.screen, config.RED, appleRect)
    
    
    def drawScore(self, score):
        scoreSurf = self.BASICFONT.render('Score: %s' % (score), True, config.WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (config.WINDOW_WIDTH - 120, 10)
        self.screen.blit(scoreSurf, scoreRect)

    def gameLoop(self):
        while True:
            for event in pygame.event.get(): 
                if event.type== pygame.QUIT:
                    pygame.quit()
                    
                elif event.type == pygame.KEYDOWN:
                    self.handleKeyEvents(event)
            self.snake.update(self.apple)  
            self.draw()
            if self.isgameover():
                break
            
    def run(self):
        while True:
            self.gameLoop()
            self.displayGameOver()



    def checkForKeyPress(self):
        if len(pygame.event.get(pygame.QUIT)) > 0:
            pygame.quit()

        keyUpEvents = pygame.event.get(pygame.KEYUP)

        if len(keyUpEvents) == 0:
            return None

        if keyUpEvents[0].key == pygame.K_ESCAPE:
            pygame.quit()
            quit()

        return keyUpEvents[0].key

    def drawPressKeyMsg(self):
        pressKeySurf = self.BASICFONT.render(
            'Press a key to play.', True, config.DARKGRAY)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (config.WINDOW_WIDTH - 200,
                                config.WINDOW_HEIGHT - 30)
        self.screen.blit(pressKeySurf, pressKeyRect)

    def displayGameOver(self):
        gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
        gameSurf = gameOverFont.render('Game', True, config.WHITE)
        overSurf = gameOverFont.render('Over', True, config.WHITE)
        gameRect = gameSurf.get_rect()
        overRect = overSurf.get_rect()
        gameRect.midtop = (config.WINDOW_WIDTH / 2, 10)
        overRect.midtop = (config.WINDOW_WIDTH / 2, gameRect.height + 10 + 25)
        self.screen.blit(gameSurf, gameRect)
        self.screen.blit(overSurf, overRect)    
        self.drawPressKeyMsg()
        pygame.display.update()
        pygame.time.wait(500)   
        self.checkForKeyPress()
        while True:
            if self.checkForKeyPress():
                pygame.event.get()  # clear event queue
                return

    def handleKeyEvents(self, event):
        if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.snake.direction != self.snake.RIGHT:
            self.snake.direction = self.snake.LEFT
        elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.snake.direction != self.snake.LEFT:
            self.snake.direction = self.snake.RIGHT
        elif (event.key == pygame.K_UP or event.key == pygame.K_w) and self.snake.direction != self.snake.DOWN:
            self.snake.direction = self.snake.UP
        elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.snake.direction != self.snake.UP:
            self.snake.direction = self.snake.DOWN
        elif event.key == pygame.K_ESCAPE:
            pygame.quit()


'''    def run(self):
        while True:
            for event in pygame.event.get(): 
                if event.type== pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

        self.screen.fill((255,255,255))
        pygame.display.update()
        self.clock.tick(60)

'''