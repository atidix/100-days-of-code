#import turtle
import pandas

# screen = turtle.Screen()
# screen.screensize(800, 1000)

# coor = []

# image = "day-25/India-States-Game/state_map.gif"
# screen.addshape(image)

# turtle.shape(image)
# tim = turtle.Turtle()


# def get_mouse(x, y):
#     print(x,y)
#     global coor
#     coor.append((x,y))
#     screen.title(f"{len(coor)}/36")
#     print(coor)

list_coor = [(-146.0, 337.0), (-163.0, 291.0), (-121.0, 255.0), (-76.0, 207.0), (-154.0, 235.0), (-158.0, 216.0), (-135.0, 184.0), (-116.0, 164.0), (-69.0, 145.0), (49.0, 112.0), (103.0, 44.0), (123.0, 148.0), (187.0, 124.0), (192.0, 104.0), (237.0, 177.0), (256.0, 122.0), (247.0, 94.0), (225.0, 55.0), (195.0, 60.0), (43.0, 52.0), (-221.0, 130.0), (-238.0, 47.0), (-213.0, -28.0), (-186.0, -54.0), (-87.0, 41.0), (-24.0, -9.0), (31.0, -23.0), (-91.0, -150.0), (-82.0, -86.0), (-171.0, -159.0), (-118.0, -177.0), (-191.0, -149.0), (-140.0, -266.0), (-101.0, -255.0), (-250.0, -238.0), (247.0, -211.0)]
states = ['Ladakh', 'Jammu and Kashmir', 'Himachal Pradesh', 'Uttarakhand', 'Chandigarh', 'Punjab', 'Haryana', 'New Delhi', 'Uttar Pradesh', 'Bihar', 'West Bengal', 'Sikkim', 'Assam', 'Meghalaya', 'Arunachal Pradesh', 'Nagaland', 'Manipur', 'Mizoram', 'Tripura', 'Jharkhand', 'Rajasthan', 'Gujarat', 'Daman and Diu and Dadra and Nagar Haveli', 'Maharashtra', 'Madhya Pradesh', 'Chattisgarh', 'Odisha', 'Andhra Pradesh', 'Telangana', 'Karnataka', 'Pondicherry', 'Goa', 'Kerala', 'Tamil Nadu', 'Lakshadweep', 'Andaman and Nicobar']

x_coor_list = [-146.0, -163.0, -121.0, -76.0, -154.0, -158.0, -135.0, -116.0, -69.0, 49.0, 103.0, 123.0, 187.0, 192.0, 237.0, 256.0, 247.0, 225.0, 195.0, 43.0, -221.0, -238.0, -213.0, -186.0, -87.0, -24.0, 31.0, -91.0, -82.0, -171.0, -101.0, -191.0, -140.0, -101.0, -250.0, 247.0]
y_coor_list = [337.0, 291.0, 255.0, 207.0, 235.0, 216.0, 184.0, 164.0, 145.0, 112.0, 44.0, 148.0, 124.0, 104.0, 177.0, 122.0, 94.0, 55.0, 60.0, 52.0, 130.0, 47.0, -28.0, -54.0, 41.0, -9.0, -23.0, -150.0, -86.0, -159.0, -285.0, -149.0, -266.0, -255.0, -238.0, -211.0]

# for (x, y) in list_coor:
#     x_coor_list.append(x)
#     y_coor_list.append(y)

# print(len(states))
# print(len(x_coor_list))
# print(len(y_coor_list))

d1 = {'state': states, "x": x_coor_list, "y": y_coor_list}
dF = pandas.DataFrame(d1)
# dF.to_csv('day-25/India-States-Game/36.csv')


# for i in range(0,36):
#     tim.goto(list_coor[i])
#     state_input = screen.textinput("State","Input State")
#     states.append(state_input)
#     print(states)

#turtle.onscreenclick(get_mouse)
#turtle.mainloop()
