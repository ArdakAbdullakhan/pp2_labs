import pygame,sys, math

pygame.init()
#frames per second
fps = 144
clock = pygame.time.Clock()
#screen size
width = 800
height = 600
active_brush = -100#no size
active_color = 'white'#transparent

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Paint program')
painting = []#drawn paintings

def draw_menu(size, color):
    pygame.draw.rect(screen, 'gray', [0,0,width, 90])#drawing menu
    pygame.draw.line(screen, 'black', (0,90), (width, 90), 2)
    big_brush = pygame.draw.rect(screen, 'black', [20,20,50,50])#brush sizes
    pygame.draw.circle(screen, 'white', (45,45),20)
    medium_brush = pygame.draw.rect(screen, 'black', [80,20,50,50])
    pygame.draw.circle(screen, 'white', (105,45),15)
    small_brush = pygame.draw.rect(screen, 'black', [140,20,50,50])
    pygame.draw.circle(screen, 'white', (165,45),10)
    rect_brush = pygame.draw.rect(screen, 'black', [200,20,50,50])#rectangle brush
    pygame.draw.rect(screen, 'white', [210,35,30,20])
    square_brush = pygame.draw.rect(screen, 'black', [260,20,50,50])#rectangle brush
    pygame.draw.rect(screen, 'white', [270,30,30,30])
    triangle_brush = pygame.draw.rect(screen, 'black', [320,20,50,50])#rectangle brush
    pygame.draw.polygon(screen, 'white', [(330,30),(360,30), (360,60)])
    eq_triangle_brush = pygame.draw.rect(screen, 'black', [380,20,50,50])
    vertices = [(405,30), (390,60), (420, 60)]
    pygame.draw.polygon(screen, 'white', vertices)
    rhombus_brush = pygame.draw.rect(screen, 'black', [440,20,50,50])
    pygame.draw.polygon(screen, 'white', [(465,30),(450,45),(465,60),(480,45)])
    brush_list = [big_brush, medium_brush, small_brush, rect_brush, square_brush, triangle_brush, eq_triangle_brush, rhombus_brush]
    if size == 20:#showing which brush is chosen
        pygame.draw.rect(screen, 'green', [20,20,50,50], 3)
    if size == 15:
        pygame.draw.rect(screen, 'green', [80,20,50,50], 3)
    if size == 10:
        pygame.draw.rect(screen, 'green', [140,20,50,50], 3)
    if size == 5:
        pygame.draw.rect(screen, 'green', [200,20,50,50], 3)
    if size == 0:
        pygame.draw.rect(screen, 'green', [260,20,50,50], 3)
    if size == -5:
        pygame.draw.rect(screen, 'green', [320,20,50,50], 3)
    if size == -10:
        pygame.draw.rect(screen, 'green', [380,20,50,50], 3)
    if size == -15:
        pygame.draw.rect(screen, 'green', [440,20,50,50], 3)
    #showing which color is chosen
    pygame.draw.circle(screen, color, (600,45),30)
    pygame.draw.circle(screen, 'darkgray', (600,45),30, 3)
    #colors list
    blue = pygame.draw.rect(screen, (0,0,255), [width-45,20,25,25])
    red = pygame.draw.rect(screen, (255,0,0), [width-45,45,25,25])
    green = pygame.draw.rect(screen, (0,255,0), [width-70,20,25,25])
    yellow = pygame.draw.rect(screen, (255,255,0), [width-70,45,25,25])
    l_blue = pygame.draw.rect(screen, (0,255,255), [width-95,20,25,25])
    black = pygame.draw.rect(screen, (0,0,0), [width-95,45,25,25])
    eraser = pygame.draw.rect(screen, (255,255,255), [width-130,20,25,25])
    color_rect = [blue,red,green,yellow,l_blue,black,eraser]
    rgb_list = [(0,0,255),(255,0,0),(0,255,0), (255,255,0),
                (0,255,255), (0,0,0), (255,255,255) ]

    return brush_list, color_rect, rgb_list
#drawing itself
def draw_painting(paints):
    for paint in paints:
        if paint[2] == 5: #if rectangular shape
            pygame.draw.rect(screen, paint[0], (paint[1][0]-paint[2]//2, paint[1][1]-paint[2]//2, 30, 20))
        elif paint[2] == 0:
            pygame.draw.rect(screen, paint[0], (paint[1][0]-paint[2]//2, paint[1][1]-paint[2]//2, 30, 30))
        elif paint[2] == -5:
            pygame.draw.polygon(screen, paint[0], [(paint[1][0]-paint[2]//2, paint[1][1]-paint[2]//2),(paint[1][0]-paint[2]//2+30, paint[1][1]-paint[2]//2),(paint[1][0]-paint[2]//2+30, paint[1][1]-paint[2]//2+30) ])
        elif paint[2] == -10:
            pygame.draw.polygon(screen, paint[0], [(paint[1][0]-paint[2]//2+15, paint[1][1]-paint[2]//2),(paint[1][0]-paint[2]//2, paint[1][1]-paint[2]//2+30), (paint[1][0]-paint[2]//2+30, paint[1][1]-paint[2]//2+30) ])
        elif paint[2] == -15:
            vertices = [(paint[1][0]-paint[2]//2+15, paint[1][1]-paint[2]//2),(paint[1][0]-paint[2]//2, paint[1][1]-paint[2]//2+15), (paint[1][0]-paint[2]//2+15, paint[1][1]-paint[2]//2+30), (paint[1][0]-paint[2]//2+30, paint[1][1]-paint[2]//2+15)]
            pygame.draw.polygon(screen, paint[0], vertices)
        else: #circular
            pygame.draw.circle(screen, paint[0], paint[1], paint[2]) 

    


running = True
while running:
    clock.tick(fps)#fps
    screen.fill('white')
    mouse = pygame.mouse.get_pos()#mouse position
    left_click = pygame.mouse.get_pressed()[0]#click for drawing
    #add new shape to painting list on mouse click
    if left_click and mouse[1] > 90:
        painting.append((active_color, mouse, active_brush))
    if mouse[1] > 90:#draw shapes, like showing it 
        if active_brush == 5:  
            pygame.draw.rect(screen, active_color, (mouse[0]-active_brush//2, mouse[1]-active_brush//2, 30, 20))
        elif active_brush == 0:
            pygame.draw.rect(screen, active_color, (mouse[0]-active_brush//2, mouse[1]-active_brush//2, 30, 30))
        elif active_brush == -5:
            tri_vert = [(mouse[0]-active_brush//2, mouse[1]-active_brush//2),(mouse[0]-active_brush//2+30, mouse[1]-active_brush//2), (mouse[0]-active_brush//2+30, mouse[1]-active_brush//2+30) ]
            pygame.draw.polygon(screen, active_color,tri_vert )
        elif active_brush == -10:
            eq_tri = [(mouse[0]-active_brush//2+15, mouse[1]-active_brush//2),(mouse[0]-active_brush//2, mouse[1]-active_brush//2+30), (mouse[0]-active_brush//2+30, mouse[1]-active_brush//2+30) ]
            pygame.draw.polygon(screen, active_color, eq_tri)
        elif active_brush == -15:
            rhomb_vert = [(mouse[0]-active_brush//2+15, mouse[1]-active_brush//2),(mouse[0]-active_brush//2, mouse[1]-active_brush//2+15), (mouse[0]-active_brush//2+15, mouse[1]-active_brush//2+30), (mouse[0]-active_brush//2+30, mouse[1]-active_brush//2+15)]
            pygame.draw.polygon(screen, active_color, rhomb_vert)
        else:  
            pygame.draw.circle(screen, active_color, mouse, active_brush)
    
    draw_painting(painting)

    brushes, colors, rgb = draw_menu(active_brush, active_color) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:#for closing game
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN: #erasing all paintings
            if event.key == pygame.K_SPACE:
                painting = []

        if event.type == pygame.MOUSEBUTTONDOWN:#changing shape, size and color
            for brush in range(len(brushes)):
                if brushes[brush].collidepoint(event.pos):
                    active_brush = 20 - (brush*5)
            
            for color in range(len(colors)):
                if colors[color].collidepoint(event.pos):
                    active_color =  rgb[color]
            
    

    pygame.display.flip()


