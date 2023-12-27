import turtle
import pandas
from name_generation import Text
screen=turtle.Screen()
screen.title("States Guessing Game")
img="blank_states_img.gif"
turtle.addshape(img)
turtle.shape(img)

#An example to demonstrate how to get the coordinates of respective state and save to csv file

# states_and_coordinates={
#     "states" : ["Florida","Arizona","Texas","New Mexico","California"],
#     "x" : [],
#     "y" : []
# }

# def getStateCoordinates(x,y):
#     states_and_coordinates["x"].append(x)
#     states_and_coordinates["y"].append(y)
#     if len(states_and_coordinates["x"])>=5:
#         turtle.onscreenclick(None)

# screen.onscreenclick(getStateCoordinates)
# screen.mainloop()
# coordinates_data=pandas.DataFrame(states_and_coordinates)
# print(coordinates_data)
# coordinates_data.to_csv("../newSelfFetchedStatesCoordinates.csv")

#In this way we fetched 5 states coordinates and saved to a new csv file newSelfFetchedStateCoordinates.csv
current_count=1
total_count=50
data=pandas.read_csv("50_states.csv")

#additional variable i had to add in case i wanted to tell about missing states
guessed_states=[]
#########

textObj=Text()
while current_count<=total_count:
    answer_state=screen.textinput(f"Guess the state {current_count}/{total_count}","Enter a state's name").title()
    # if answer_state==str(data[data.state==answer_state].state.iloc[0]):
    #     print(current_count)
    #     current_count+=1
    temp=data[data.state==answer_state]
    if answer_state=="Exit":
        #######
        textObj.clear()
        missing_states=[]
        all_states=data.state.to_list()
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        for state in missing_states:
            new_temp=data[data.state==state]
            name=str(new_temp.state.iloc[0])
            x=new_temp.x.iloc[0]
            y=new_temp.y.iloc[0]
            textObj.goto(x,y)
            textObj.write(name,False,"left",("Arial",8,"normal"))
        ########
        break
    if not temp.empty and answer_state not in guessed_states:
        x=temp.x.iloc[0]
        y=temp.y.iloc[0]
        text_val=str(temp.state.iloc[0])
        #########
        guessed_states.append(answer_state)
        ########
        textObj.goto(x,y)
        textObj.write(text_val,False,"left",("Arial",8,"normal"))
        current_count+=1
    
    
screen.exitonclick()
