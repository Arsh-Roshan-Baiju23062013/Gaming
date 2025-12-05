import pgzrun
WIDTH = 700
HEIGHT = 500

title=Rect(5, 10, 680, 50)
question=Rect(5, 65, 500, 70)
timer=Rect(510, 65, 90, 70)
score=Rect(605, 65, 90, 70)
question1=Rect(5, 200, 680, 50)
question2=Rect(5, 260, 680, 50)
question3=Rect(5, 320, 680, 50)
question4=Rect(5, 380, 680, 50)
restart=Rect(100, 450, 150, 50)
quit=Rect(400, 450, 150, 50)
total_time=20
game=True
lose=Rect(0, 0, 700, 700)
happy=Rect(0, 0, 700, 700)
scores=0
question_index=0
questions=[]
current_questions=[]
Quit=Rect(0, 0, 700, 700)

def emit():
    global total_time
    total_time=total_time-1
    
def text_read():
    r=open("Questions.txt", "r")
    for i in r:
        questions.append(i)
    print(questions)
    
def read_current_question():  
    global questions, current_questions
    global question_index
    global game
    if question_index>4:
        game="win"
    else:
        current_questions=questions.pop(0).strip().split("|")
        question_index=question_index+1
text_read()
    
read_current_question()
print(current_questions)    
clock.schedule_interval(emit, 1)
answer_boxes=[question1, question2, question3, question4]

def draw():
    global total_time
    global game
    screen.fill("black")
    if game==True:
        screen.blit("question_marks", (0, 0))
        screen.draw.filled_rect(title, ("light blue")) 
        screen.draw.textbox("QUIZZERIN'", title, color="Black")
        screen.draw.filled_rect(question, ("dark blue"))
        screen.draw.textbox(current_questions[0].strip(), question, color="White")
        screen.draw.filled_rect(timer, ("turquoise"))
        screen.draw.textbox(str(total_time), timer, color="black")
        screen.draw.filled_rect(score, ("pink"))
        screen.draw.textbox(str(scores), score, color="black")
        screen.draw.filled_rect(question1, ("forest green"))
        screen.draw.textbox(current_questions[1], question1, color="Black")
        screen.draw.filled_rect(question2, ("red"))
        screen.draw.textbox(current_questions[2], question2, color="Black")
        screen.draw.filled_rect(question3, ("orange"))
        screen.draw.textbox(current_questions[3], question3, color="Black")
        screen.draw.filled_rect(question4, ("brown"))
        screen.draw.textbox(current_questions[4], question4, color="Black")
        screen.draw.filled_rect(restart, ("grey"))
        screen.draw.textbox("Restart", restart, color="black")
        screen.draw.filled_rect(quit, ("black"))
        screen.draw.textbox("Quit", quit, color="white")
    else:
        screen.draw.filled_rect(lose, ("red"))   
        screen.draw.text("Wrong Answer", (280, 250), color="black")
        screen.draw.text("Press 'r' to restart", (260, 280), color="black")
        screen.draw.text(f"Your Score is: {scores}",(260, 310), color="black")   
    if total_time<=0:
        game=False
        screen.draw.filled_rect(lose, ("red"))   
        screen.draw.text("You Lost by Time", (260, 250), color="black")
        screen.draw.text("Press 'r' to restart", (260, 280), color="black")
        screen.draw.text(f"Your Score is: {scores}",(260, 310), color="black")    
    if game=="win":
        screen.draw.filled_rect(happy, ("Gold"))
        screen.draw.text("You Won", (280, 250), color="black")
        screen.draw.text("Press 'r' to restart", (260, 280), color="black")
        screen.draw.text(f"Your Score is: {scores}",(260, 310), color="black")  
    if game=="quit":
        screen.draw.filled_rect(Quit, ("black"))   
        screen.draw.text("You Quitted, don't quit, be fit", (250, 250), color="white")
        screen.draw.text("Press 'r' to restart", (270, 280), color="white")
        screen.draw.text(f"Your Score is: {scores}",(260, 310), color="white")          
def update():
    global current_questions
    global questions
    global scores
    global total_time
    global game
    global question_index
    title.x=title.x-3
    if title.right<0:
        title.left=680
    if keyboard.r:
        scores=0
        question_index=0
        total_time=20
        current_questions=[]
        questions=[]
        text_read()
        read_current_question() 
        game=True   
def on_mouse_down(pos):
    global current_questions
    global questions
    global scores
    global total_time
    global game
    global question_index
    index=1
    for i in answer_boxes:
        if i.collidepoint(pos):
            if index==int(current_questions[5]):
                scores=scores+1
                print(scores)
                read_current_question()
                total_time=20
            else: 
                game=False      
        index=index+1 
    if restart.collidepoint(pos):
        scores=0
        question_index=0
        total_time=20
        current_questions=[]
        questions=[]
        text_read()
        read_current_question()
    if quit.collidepoint(pos):
       game="quit" 
        
        
pgzrun.go()
  