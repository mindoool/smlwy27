import random
#-*-coding: utf-8-*-
#Game Start!
import os

print "야구게임에 오신 것을 환영합니다. 지금부터 야구 게임을 시작하겠습니다."


player_list=[]
play_check =[]

def baseball_game(player_list, play_log):
	com_list = random.sample(range(0,10),4)
	play_log=play_log+"\n\n"	
	play_log=play_log+"컴퓨터의 값:" + str(com_list[0])+str(com_list[1])+str(com_list[2])+str(com_list[3])+"\n\n"
	answer=""
	save_answer=""
	number=1
	count=0
	strike=0
	ball=0
	while strike<4:
		strike = 0
		ball = 0
		guess = str(raw_input("겹치지 않는 숫자 네 개를 입력하세요:"))
		if guess.isdigit()==False:
			print "0~9범위에서 골라주세요."
		else: 
			play_log = play_log+"당신의 "+str(count+1)+"번째 추측:"+guess+"\n"
			player_list = [int(x) for x in str(guess)]
			while len(player_list)!=4:
				print player_list
				print "숫자 4자리를 입력하셔야 합니다. 다시 입력하세요"
				break
			else:
				print player_list
				if player_list[0] != player_list[1] and player_list[0] != player_list[2] and player_list[0]!= player_list[3] and player_list[1] != player_list[2] and player_list[1] !=player_list[3] and player_list[2] != player_list[3]:
					for i in range(4):
						if player_list[i] == com_list[i]:
							strike +=1
						elif player_list[i] in com_list:
							ball +=1
					count +=1
					print "strike %d" %strike
					print "ball %d" %ball
					play_log = play_log+"strike:"+str(strike)+" "
					play_log = play_log+"ball:"+str(ball)+"\n\n"
				else:
					print "겹치지 않게 입력해주세요."
	print com_list
	print "당신은 %d 회 만에 맞추셨습니다!" %count
	play_log = play_log+"축하합니다! 당신은 "+str(count)+"회 만에 맞추셨습니다!"+"\n\n"
	while (answer!="yes") and (answer!="no"):
		print "한 판 더? (yes/no)"
		answer = str(raw_input("Answer:"))
		if answer == "no":
			print "Game Over! 게임 데이터를 저장하시겠습니까?"
			play_log=play_log+"게임 종료!"
			while (save_answer!="yes") and (save_answer!="no"):
				save_answer = str(raw_input("Answer:"))
				if save_answer== "no":
					print "bye"
					play_check.append("1")
					break
				elif save_answer =="yes":
					if os.path.isdir(".\game_log")==False:
						os.mkdir("game_log")
					title = str(raw_input("원하시는 파일명을 입력하세요:"))
					title = title+".txt"
					file = open("game_log/"+title,"w")
					file.write(play_log)
					file.close()
					print "로그파일이 성공적으로 저장되었습니다."
				else:
					print "You have to choose yes or no!!!"
			break
		elif answer == "yes":
			number +=1
			baseball_game(player_list, play_log)
		else:
			print "You have to answer yes or no!!!"
	answer="1"


print baseball_game(player_list, "게임 시작!")