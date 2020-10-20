import pygame
##########################################################################
#기본 초기화 (반드시 해야 하는 것들)
pygame.init() #초기화 (반드시 필요)

#화면크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

#fps
clock = pygame.time.Clock()
##############################################################################

#1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등)
#배경 만들기
backgraound = pygame.image.load("C:\\Users\\김대기\\Desktop\\python git\\practice\\pygame_basic\\background.png")

#캐릭터 만들기
character = pygame.image.load("C:\\Users\\김대기\\Desktop\\python git\\practice\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동 위치
to_x = 0
character_speed = 10

# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임 수를 설정

#캐릭터가 1초동안 100만큼 이동을 해야함
#10 fps : 1초동안 10번 동작 -> 1번에 몇만큰 이동? 10만큼! 10 * 10 = 100
#20 fps : 1초동안 20번 동작 -> 1번에 몇만큰 이동? 5만큼! 5 * 20 = 100

    # 2. 이벤트 처리 ( 키보드, 마우스 )
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
        
    #3.게임 캐릭터 위치 정의    
    

    #4. 충돌 처리

    
    #5. 화면의 기르기
    screen.blit(backgraound, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos)

    # pygame.display.update() #게임화면을 다시 그리기!


# pygame 종료

#깃 연습
pygame.quit()