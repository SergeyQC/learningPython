# a = int(input()) - прочитать строку с клавы и пребразовать в число

##############################################

# minutes = int(input())
# time_hour = int(minutes/60)
# time_min = minutes - time_hour*60
# print(time_hour)
# print(time_min)

##############################################

X = int(input())
H = int(input())
M = int(input())
time = H * 60 + M + X
H1 = int(time/60)
M1 = time - H1*60
print(H1)
print(M1)
