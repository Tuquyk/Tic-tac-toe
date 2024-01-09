import pygame

pygame.init()
screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("tictactoe") 
screen.fill((0,0,0))

#check
rows, cols = 3, 3
matrix = [[-1 for _ in range(cols)] for _ in range(rows)]
player=[pygame.image.load('pygame/project3/resource/a.png') , pygame.image.load('pygame/project3/resource/b.png') ]
turn=True
move=9
run=True
quit=False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False
            quit=True
    px,py= pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0] == 1:
        if move%2==1:
            if matrix[int(px/200)][int(py/200)]==-1:
                matrix[int(px/200)][int(py/200)]=1
                screen.blit(player[0], (int(px/200)*220,int(py/200)*220))
                move=move-1
        elif move%2==0:
            if matrix[int(px/200)][int(py/200)]==-1:
                matrix[int(px/200)][int(py/200)]=0
                screen.blit(player[1], (int(px/200)*220,int(py/200)*220))
                move=move-1
        for i in range(3):
            if matrix[i][0]==matrix[i][1]==matrix[i][2]!=-1:
                winner=matrix[i][0]
                run=False
        for i in range(3):
            if matrix[0][i]==matrix[1][i]==matrix[2][i]!=-1:
                winner=matrix[0][i]
                run=False
            
            
            
    
    
    #4 lines
    pygame.draw.rect(screen, (255,255,255), (200,0,20,640))
    pygame.draw.rect(screen, (255,255,255), (420,0,20,640))
    pygame.draw.rect(screen, (255,255,255), (0,200,640,20))
    pygame.draw.rect(screen, (255,255,255), (0,420,640,20))
    pygame.display.update()

screen.fill((0,0,0))
if quit==False:
    if(winner==1):
        winner="PLAYER 1 IS THE WINNER"
    if(winner==0):
        winner="PLAYER 2 IS THE WINNER"
    end_font=pygame.font.Font(None,50)
    end=True
    while end==True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False
        Truewinner = end_font.render(winner, True , (125,125,125))
        screen.blit((Truewinner),(screen_width/2-200, screen_height/2))
        pygame.display.update()
pygame.quit()