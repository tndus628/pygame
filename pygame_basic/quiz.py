'''
Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오

[게임 조건]
1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
2. 똥은 화면 가장 위에서 떨어짐, x 좌표는 매번 랜덤으로 설정
3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
4. 캐릭터가 똥과 충돌하면 게임 종료
5. FPS는 30으로 고정

[게임 이미지]
1. 배경: 640 * 480 (세로, 가로) - background.png
2. 캐릭터: 70 * 70 - character.png
3. 똥: 70 * 70 - enemy.png
'''
import pygame

###################################################
#기본 초기화 (반드시 해야하는 것들)
pygame.init() #초기화(반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("avoid game")#게임 이름

#FPS
clock = pygame.time.Clock()
####################################################

#1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 등) 

#배경 이미지 불러오기
background = pygame.image.load("C:/Users/USER/Desktop/sy/coding/파이썬/pygame/pygame_basic/background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/USER/Desktop/sy/coding/파이썬/pygame/pygame_basic/character.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] #캐릭터의 가로 크기
character_height = character_size[1] #캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
character_y_pos = screen_height - character_height #화면 세로 크기 가장 아래에 해당하는 곳에 위치(세로)

#이동할 좌표
to_x = 0

#이동속도
character_speed = 0.6

#적 enemy 캐릭터
enemy = pygame.image.load("C:/Users/USER/Desktop/sy/coding/파이썬/pygame/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size #이미지의 크기를 구해옴
enemy_width = enemy_size[0] #캐릭터의 가로 크기
enemy_height = enemy_size[1] #캐릭터의 세로 크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) #화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) #화면 세로 크기 가장 아래에 해당하는 곳에 위치(세로)



#이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(30) #게임화면의 초당 프레임 수를 설정

    #print("fps: " + str(clock.get_fps()))
    
    # 2. 이벤트 처리( 키보드, 마우스 등)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            running = False #게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: #오른쪽으로
                to_x += character_speed

        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    
    #3. 게임 캐릭터 위치 정의

    character_x_pos += to_x * dt

    #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width  - character_width:
        character_x_pos = screen_width  - character_width
    
    #세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    #4. 충돌 처리

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False
    #screen.fill((0, 0, 255)) #rgb 값으로도 색깔을 나타낼 수 있음

    #5. 화면에 그리기

    screen.blit(background, (0,0)) #배경 그리기
    screen.blit(character,(character_x_pos, character_y_pos)) #캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #적 그리기

   

    pygame.display.update() #게임화면 다시 그리기!

#잠시 대기
pygame.time.delay(2000) #2초 정도 대기(ms)

#pygame 종료
pygame.quit()