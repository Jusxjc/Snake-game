import pygame
import random
import csv
class Apple:
    def __init__(self):
        self.apple_surface = pygame.Surface((15,15))
        self.apple_surface.fill("Red")
        x = (random.randint(0,39))*15
        y= (random.randint(0,39))*15
        self.apple_rect= self.apple_surface.get_rect(topleft=(x,y))
    def draw(self, screen):
        screen.blit(self.apple_surface,self.apple_rect)

class tile:
    def __init__(self,x_coord,y_coord, tile_color,):
        self.x_coord= x_coord
        self.y_coord=y_coord
        self.tile_color=tile_color
        self.tile_surface = pygame.surface.Surface((15,15))
        self.tile_surface.fill(self.tile_color)
        self.tile_rect= self.tile_surface.get_rect(topleft=(self.x_coord,self.y_coord))
    
    def draw(self,screen):
        screen.blit(self.tile_surface,self.tile_rect)

def move_snake(direct):
    head_body=snake_body[0]
    newPos= (0,0)
    if direct== "left":
        newPos=(head_body[0]-15, head_body[1])
    elif direct== "right":
        newPos=(head_body[0]+15, head_body[1])
    elif direct== "up":
        newPos=(head_body[0], head_body[1]-15)
    elif direct== "down":
        newPos=(head_body[0], head_body[1]+15)
    snake_body.insert(0,(newPos))
snake_body=[(300,300)]
#Retrieves tilemap from file
tilemap= []
with open("tilemap40x40.csv") as file:
    reader = csv.reader(file)
    for line in file:
        row=  line.rstrip().split(",")
        tilemap.append(row)

#iterates the tile map to create tile objects
row_count=-1
col_count=-1
list_of_tiles=[]
for row in tilemap:
    row_count+=1
    for num in row:
        col_count+=1
         #print(num, " is ", "[" ,col_count, row_count,"]")
        if tilemap[row_count][col_count]=="1":
            tile_col= "darkgrey"
        elif tilemap[row_count][col_count]=="0":
            tile_col = "Brown"
        else:
            tile_col = "Red"
        current_tile= tile(col_count*15,row_count*15,tile_col)
        list_of_tiles.append(current_tile)
    #Resets column count (x)
    col_count=-1

#creation of the screen
pygame.init()
screen= pygame.display.set_mode((600,600))
pygame.display.set_caption("")
clock = pygame.time.Clock()
score=0
score_font= pygame.font.Font(None,30)
score_surface= score_font.render(str(score),True,"black")

#Ext
tick_counter=0
snake_apple= Apple()
direction= "up"
running =True
#Main game
while running:
    milli_counter= clock.tick(60)
    tick_counter += 1
    pygame.display.update()
    for event in pygame.event.get():
        #Terminate the screen
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                direction="left"
            elif event.key== pygame.K_l:
                direction="right"
            elif event.key== pygame.K_i:
                direction="up"
            elif event.key== pygame.K_k:
                direction= "down"
    if snake_apple.apple_rect.collidepoint(snake_body[0]):
        snake_apple= Apple()
        score +=1
        score_surface= score_font.render(str(score),True,"black")
        move_snake(direction)

    if tick_counter%30==0:
        move_snake(direction)
        snake_body.pop()
    
    if snake_body[0] in snake_body[1:]:
        running=False
    #put blitt for tiles
    for tiles in list_of_tiles:
        tiles.draw(screen)
    for body in snake_body:
        temp_surface = pygame.Surface((15, 15))
        temp_surface.fill("springgreen")
        temp_rect = temp_surface.get_rect(topleft=body)
        screen.blit(temp_surface, temp_rect)
    snake_apple.draw(screen)
    screen.blit(score_surface,(300,300))
        