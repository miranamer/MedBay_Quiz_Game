# .\env\Scripts\activate
# python3 -m pip install lib_name
# D:\Stuff\melon_honey

from copyreg import dispatch_table
from tkinter.tix import Tree
from matplotlib.pyplot import draw
import pygame as pg
import os
from pygame import mixer
import pandas as pd

pg.init()

WIDTH, HEIGHT = 800, 600

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("New_Game - V1")

FPS = 60


class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pg.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw_bttn(self, surface):
		action = False
		#get mouse position
		pos = pg.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pg.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		WIN.blit(self.image, (self.rect.x, self.rect.y))

		return action

start_bttn_img = pg.image.load('Assets/bttn_1_new-removebg-preview.png').convert_alpha()
stop_bttn_img = pg.image.load('Assets/bttn_2-removebg-preview.png').convert_alpha()
yes_bttn_img = pg.image.load('Assets/yes_bttn_img.PNG').convert_alpha()
no_bttn_img = pg.image.load('Assets/no_bttn_img.PNG').convert_alpha()

start_bttn = Button(130, 420, start_bttn_img, 0.7)
stop_bttn = Button(540, 420, stop_bttn_img, 0.7)


yes_bttn = Button(240, 440, yes_bttn_img, 0.2)
no_bttn = Button(440, 440, no_bttn_img, 0.2)


fontObj = pg.font.Font("C:/Users/ayaan/Downloads/vcr_osd_mono/VCR_OSD_MONO_1.001.ttf", 30) # ADD THIS FONT TO ALL TEXT

def display_score():
    curr_time = int(pg.time.get_ticks() / 1000) - start_time
    score_surf = fontObj.render(f'Time: {curr_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (720, 580))
    WIN.blit(score_surf, score_rect)
    #print(curr_time, start_time) <--- For testing time


def display_q_num(q_num):
    q_surf = fontObj.render(f'Q: {q_num}', False, (64,64,64))
    q_rect = q_surf.get_rect(center = (40, 580))
    WIN.blit(q_surf, q_rect)


def display_user_score(user_score):
    us_surf = fontObj.render(f'Your Score: {user_score}', False, (64,64,64))
    us_rect = us_surf.get_rect(center = (380, 580))
    WIN.blit(us_surf, us_rect)


def display_user_score_2(user_score): # <----------- Add some stuff like accuracy (score / total * 100) or add a quote like 'very good' if good score
    

    end_surf = fontObj.render('Game Over', False, 'Red')
    end_rect = end_surf.get_rect(center = (390, 100))



    us_surf = fontObj.render(f'Final Score: {user_score} / 4', False, (64,64,64))
    us_rect = us_surf.get_rect(center = (380, 270))
    WIN.blit(us_surf, us_rect)
    WIN.blit(end_surf, end_rect)


    

start_time = 0

brain_img = pg.image.load('Assets/brain_img.png') # left brain img
brain_img = pg.transform.scale(brain_img, (80, 90))

brain_img2 = pg.image.load('Assets/brain_img.png')
brain_img2 = pg.transform.scale(brain_img, (80, 90))
brain_img2 = pg.transform.flip(brain_img2, True, False)

brain_img_3 = pg.image.load('Assets/mri.jpg')
brain_img3 = pg.transform.scale(brain_img_3, (80, 90))

brain_img_4 = pg.image.load('Assets/mri.jpg')
brain_img4 = pg.transform.scale(brain_img_4, (80, 90))

brain_img_5 = pg.image.load('Assets/mri.jpg')
brain_img5 = pg.transform.scale(brain_img_4, (80, 90))




text_surf = fontObj.render('Troublesome', False, (255, 0, 0)) # Troublesome
text_surf2 = fontObj.render('Tumours', False, (0, 0, 245)) # Tumours

brain_scan =pg.image.load('Assets/mri.jpg') # Brain Scan img
brain_scan = pg.transform.scale(brain_scan, (200, 220))


intro_surf = fontObj.render('Welcome To Troublesome Tumours!', False, (255,0,0))
intro_rect = intro_surf.get_rect(center = (400, 200))

intro_surf_2 = fontObj.render('Created By MedBay (2022)', False, (0, 0, 254))
intro_rect_2 = intro_surf.get_rect(center = (455, 300))

game_logo = pg.image.load('Assets/game_logo.png')
game_logo = pg.transform.scale(game_logo, (WIDTH, HEIGHT))
game_logo_rect = game_logo.get_rect(topleft = (0, 0))

fontObj2 = pg.font.Font("C:/Users/ayaan/Downloads/vcr_osd_mono/VCR_OSD_MONO_1.001.ttf", 20)

game_q_title = fontObj2.render('Is There A Tumour?', False, (0,0,0))
game_q_rect = intro_surf.get_rect(center = (565, 155))

perf_score = fontObj2.render('Perfect :)', False, 'Green')
perf_score_rect = intro_surf.get_rect(center = (610, 380))

zero_score = fontObj2.render('Horrendous :(', False, 'Red')
zero_score_rect = intro_surf.get_rect(center = (590, 380))



def draw_intro(intro_surf, intro_rect, Q, game_active): # intro screen
    WIN.blit(game_logo, game_logo_rect)
    #WIN.fill((255, 255, 255))
    #WIN.blit(intro_surf, intro_rect)
    #WIN.blit(intro_surf_2, intro_rect_2)
    
    if start_bttn.draw_bttn(WIN) and game_active == False:
      button_sound_effect = mixer.Sound('Assets/laser.wav')
      button_sound_effect.play()
      game_active = True
      Q += 1
    
    elif stop_bttn.draw_bttn(WIN) and game_active == False:
      pg.quit()
    
    pg.display.update()
    

def draw_window(Q, user_score): # Q1
    WIN.fill((255, 255, 255)) # white bg
    WIN.blit(brain_img, (200,35))
    WIN.blit(brain_img2, (500, 35))
    WIN.blit(game_q_title, game_q_rect)
    WIN.blit(text_surf, (300, 45))
    WIN.blit(text_surf2, (330, 80))
    WIN.blit(brain_scan, (290, 180))
    display_score()
    display_q_num(Q)
    display_user_score(user_score)
    
    pg.display.update()

def draw_window_2(Q, user_score): # Q2
    WIN.fill((232, 239, 21)) # yellow bg <--------------- 
    WIN.blit(brain_img, (200,35))
    WIN.blit(brain_img2, (500, 35))
    WIN.blit(game_q_title, game_q_rect)
    WIN.blit(text_surf, (300, 45))
    WIN.blit(text_surf2, (330, 80))
    WIN.blit(brain_scan, (290, 180))
    display_score()
    display_q_num(Q)
    display_user_score(user_score)
    
    pg.display.update()

def draw_window_3(Q, user_score): # Q3
    WIN.fill((51, 255, 153)) # green bg
    WIN.blit(brain_img, (200,35))
    WIN.blit(brain_img2, (500, 35))
    WIN.blit(game_q_title, game_q_rect)
    WIN.blit(text_surf, (300, 45))
    WIN.blit(text_surf2, (330, 80))
    WIN.blit(brain_scan, (290, 180))
    display_score()
    display_q_num(Q)
    display_user_score(user_score)
    
    pg.display.update()

def draw_window_4(Q, user_score):
    WIN.fill((255, 204, 255)) # green bg
    WIN.blit(brain_img, (200,35))
    WIN.blit(brain_img2, (500, 35))
    WIN.blit(game_q_title, game_q_rect)
    WIN.blit(text_surf, (300, 45))
    WIN.blit(text_surf2, (330, 80))
    WIN.blit(brain_scan, (290, 180))
    display_score()
    display_q_num(Q)
    display_user_score(user_score)
    
    pg.display.update()


def draw_end_game(user_score, written): # end game screen
    WIN.fill((255, 255, 255))
    display_user_score_2(user_score)
    if user_score == 4:
        WIN.blit(perf_score, perf_score_rect)
    elif user_score == 0:
        WIN.blit(zero_score, zero_score_rect)

    
    pg.display.update()

#if not game_active:
                #if event.type == pg.KEYDOWN and event.type == pg.K_SPACE:
                    #game_active = True

            #if game_active:
                #draw_window()
            #else:
                #WIN.fill(0, 0, 0)


def main():  # CLICK SPACE AFTER EVERY Y OR N TO REGISTER IT <----------------------------------------------------- IMPORTANT!!

    game_active = False
    clock = pg.time.Clock()
    run = True
    Q = 0 # q number
    user_ans = []
    ans = ['Y', 'Y', 'N', 'Y']
    user_score = 0
    written = False
    end_scores = []

    while run:

        keys=pg.key.get_pressed()

        for event in pg.event.get():
            clock.tick(FPS)
            if event.type == pg.QUIT:
                run = False

            ##if event.type == pg.KEYDOWN and game_active == False:
                #print('KD')
                #game_active = True
                #start_time = pg.time.get_ticks()  # <------- THIS DOES NOT WORK. I DONT KNOW WHY?. I WANT TIME TO RESET TO 0 AFTER GAME BEGINS.
                #Q += 1
            if start_bttn.draw_bttn(WIN) and game_active == False:
              game_active = True
              Q += 1
              

            if game_active and Q == 1:
                draw_window(Q, user_score)
                if yes_bttn.draw_bttn(WIN):  # <---------------- ITS GETTING APPENDED BUT Q IS NOT CHANGING
                    user_ans.append('Y')
                    if user_ans[0] == ans[0]:
                        user_score += 1
                    Q += 1
                elif no_bttn.draw_bttn(WIN):
                    user_ans.append('N')
                    if user_ans[0] == ans[0]:
                        user_score += 1
                    Q += 1
                
                pg.display.update()
               
            
            elif game_active and Q == 2:
                draw_window_2(Q, user_score)
                if yes_bttn.draw_bttn(WIN):  # <---------------- ITS GETTING APPENDED BUT Q IS NOT CHANGING
                    user_ans.append('Y')
                    if user_ans[1] == ans[1]:
                        user_score += 1
                    Q += 1
                elif no_bttn.draw_bttn(WIN):
                    user_ans.append('N')
                    if user_ans[1] == ans[1]:
                        user_score += 1
                    Q += 1

                pg.display.update()
            
            elif game_active and Q == 3:
                draw_window_3(Q, user_score)
                if yes_bttn.draw_bttn(WIN):  # <---------------- ITS GETTING APPENDED BUT Q IS NOT CHANGING
                    user_ans.append('Y')
                    if user_ans[2] == ans[2]:
                        user_score += 1
                    Q += 1
                elif no_bttn.draw_bttn(WIN):
                    user_ans.append('N')
                    if user_ans[2] == ans[2]:
                        user_score += 1
                    Q += 1

                pg.display.update()
            
            elif game_active and Q == 4:
                draw_window_4(Q, user_score)
                if yes_bttn.draw_bttn(WIN):  # <---------------- ITS GETTING APPENDED BUT Q IS NOT CHANGING
                    user_ans.append('Y')
                    if user_ans[3] == ans[3]:
                        user_score += 1
                    Q += 1
                elif no_bttn.draw_bttn(WIN):
                    user_ans.append('N')
                    if user_ans[3] == ans[3]:
                        user_score += 1
                    Q += 1

                pg.display.update()

            #for index, value in enumerate(user_ans):
                #if value == ans[index]:
                    #user_score += 1
                #else:
                    #continue

            if len(user_ans) == len(ans):
                draw_end_game(user_score, written)
                if written == False:
                    f = open("Assets/scores.txt", "a")
                    f.write(str(user_score) + '\n')
                    f.close()
                    written = True

                    #with open('Assets/scores.txt') as q:
                        #lines = q.readlines()
                        #end_scores.append(lines)
                        #print(lines)
                

                
            if not game_active:
                draw_intro(intro_surf, intro_rect, Q, game_active) # <---- INTRO SCREEN GUI
            
    
    
    
    pg.quit()



# create intro screen
# ans = ['Y', 'Y', 'N'] => q ans'
# user_ans = [] => ans that user inputs
# Q = 0
# User_Score = 0 => users score

# if user_input == pg.K_Y:
    # user_ans.append('Y')
# elif user_input == pg.K_N:
    # user_ans.append('N')

# draw_window() => for q 1
# def draw_window_2() => for q 2
# def draw_window_3() => for q 3
# if Q == 4:
    # for i, v in enumerate(user_ans):
        # if v == ans[i]:
            # User_Score += 1
    # def end_screen() # => end of game screen showing score




#Y_bttn = Button()
#N_bttn = Button()    
    






  


if __name__ == "__main__":
    main()