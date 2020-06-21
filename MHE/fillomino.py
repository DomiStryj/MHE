def eksport(y):
    with open("v1.txt", 'r') as file:
        for ex in file:
            if ex.split():
                ex = [x for x in ex.split()]
                y.append(ex)


def save(y, time, countEmptyStart, countEmptyEnd):
    with open("my_solution.txt", "a") as f:
        st = ""
        for i in range(len(y)):
            for j in range(len(y)):
                st += y[i][j] + "  "
            st += "\n"
        st += "\n"
        f.write(st + "\n")
        f.write("pomiar czasu " + str(time) + "\n")
        f.write("puste pola na poczatku " + str(countEmptyStart) + "\n")
        f.write("puste pola na koncu " + str(countEmptyEnd) + "\n")


def type_format(y, x):
    if x == 1:
        for i in range(len(y)):
            for j in range(len(y)):
                if y[i][j] != 'o':
                    n = int(y[i][j])
                    y[i][j] = n
    if x == 0:
        for i in range(len(y)):
            for j in range(len(y)):
                if type(y[i][j]) == int:
                    n = str(y[i][j])
                    y[i][j] = n


def view(y):
    for i in range(len(y)):
        for j in range(len(y)):
            print(y[i][j], end='  ')
        print()


def empty_field(y):
    count = 0
    for i in range(len(y)):
        for j in range(len(y)):
            if y[i][j] == 'o':
                count += 1
    return count


def check_down_c(i, j, y, forleftcorners, forrightcorners):
    if forleftcorners:
        checkdown = y[i + 1][j] == 'o' and y[i][j + 1] != 'o'
    if forrightcorners:
        checkdown = y[i + 1][j] == 'o' and y[i][j - 1] != 'o'
    return checkdown


def check_right_c(i, j, y, forleftupcorners, forleftdowncorners):
    if forleftupcorners:
        checkright = y[i][j + 1] == 'o' and y[i + 1][j] != 'o'
    if forleftdowncorners:
        checkright = y[i][j + 1] == 'o' and y[i - 1][j] != 'o'
    return checkright


def check_up_c(i, j, y, forlefdowntcorners, forrightdowncorners):
    if forlefdowntcorners:
        checkup = y[i - 1][j] == 'o' and y[i][j + 1] != 'o'
    if forrightdowncorners:
        checkup = y[i - 1][j] == 'o' and y[i][j - 1] != 'o'
    return checkup


def check_left_c(i, j, y, forrightupcorners, forrightdowncorners):
    if forrightupcorners:
        checkleft = y[i][j - 1] == 'o' and y[i + 1][j] != 'o'
    if forrightdowncorners:
        checkleft = y[i][j - 1] == 'o' and y[i - 1][j] != 'o'
    return checkleft


def find_way_c(y):
    count = 1
    for i in range(0, len(y), 1):
        for j in range(0, len(y), 1):
            if i == 0 and j == 0:  # lewy górny róg
                if type(y[i][j]) == int and y[i][j] != 1:
                    temp = y[i][j]
                    if check_right_c(i, j, y, forleftupcorners=True, forleftdowncorners=False):
                        y[i][j + 1] = temp
                    if check_down_c(i, j, y, forleftcorners=True, forrightcorners=False):
                        y[i + 1][j] = temp
            if i == 0 and j == len(y) - 1:  # prawy górny róg
                if type(y[i][j]) == int and y[i][j] != 1:
                    temp = y[i][j]
                    if check_left_c(i, j, y, forrightupcorners=True, forrightdowncorners=False):
                        y[i][j - 1] = temp
                    if check_down_c(i, j, y, forrightcorners=True, forleftcorners=False):
                        y[i + 1][j] = temp
            if i == len(y) - 1 and j == 0:  # lewy dolny róg
                if type(y[i][j]) == int and y[i][j] != 1:
                    temp = y[i][j]
                    if check_right_c(i, j, y, forleftdowncorners=True, forleftupcorners=False):
                        y[i][j + 1] = temp
                    if check_up_c(i, j, y, forlefdowntcorners=True, forrightdowncorners=False):
                        y[i - 1][j] = temp
            if i == len(y) - 1 and j == len(y) - 1:  # prawy dolny róg
                if type(y[i][j]) == int and y[i][j] != 1:
                    temp = y[i][j]
                    if check_left_c(i, j, y, forrightupcorners=False, forrightdowncorners=True):
                        y[i][j - 1] = temp
                    if check_up_c(i, j, y, count, forlefdowntcorners=False, forrightdowncorners=True):
                        y[i - 1][j] = temp


def check_left_e(i, j, y, forupedges):
    if forupedges:
        checkleft = y[i][j - 1] == 'o' and y[i][j + 1] != 'o' and y[i + 1][j] != 'o'

    return checkleft


def check_right_e(i, j, y, forupedges):
    if forupedges:
        checkright = y[i][j + 1] == 'o' and y[i][j - 1] != 'o' and y[i + 1][j] != 'o'

    return checkright


def check_down_e(i, j, y, forupedges):
    if forupedges:
        checkdown = y[i + 1][j] == 'o' and y[i][j - 1] != 'o' and y[i][j + 1] != 'o'

    return checkdown


def find_way_e(y):
    count = 1
    for i in range(0, len(y), 1):
        for j in range(0, len(y) - 1, 1):
            if i == 0:  # górna krawedz w lewo
                if type(y[i][j]) == int and y[i][j] != 1:
                    if check_left_e(i, j, y, forupedges=True):
                        temp = y[i][j]
                        while temp > count:
                            if check_left_e(i, j, y, forupedges=True):
                                y[i][j - 1] = temp
                                count += 1
                                j -= 1

#                    if check_right_e(i, j, y, forupedges=True):  # górna krawedz w prawo
 #                       temp = y[i][j]
  #                      while temp > count:
   #                         if check_right_e(i, j, y, forupedges=True):
    #                            y[i][j + 1] = temp
     #                           count += 1
      #                          j += 1


                    if check_down_e(i, j, y, forupedges=True):  # górna krawedz w dół
                        temp = y[i][j]
                        while temp > count:
                            if check_down_e(i, j, y, forupedges=True):
                                y[i + 1][j] = temp
                                count += 1
                                i += 1


#   count = 1
#
#   for i in range(0,len(y)-1,1):
#      for j in range(0,len(y)-1,1):


#    if type(y[0][0]) == int and y[0][1] == 'o' and y[1][0] != 'o': #lewy górny róg
#       temp = y[0][0]
#      y[0][1] = temp
# if type(y[0][len(y)-1]) == int and y[0][len(y)-2] == 'o' and y[1][len(y)-1] != 'o': #prawy górny róg
#    temp = y[0][len(y)-1]
#   y[0][len(y)-2] = temp
# if type(y[len(y)-1][len(y)-1]) == int and y[len(y)-1][1] == 'o' and y[1][0] != 'o': #prawy dolny róg


#        while True:
#              temp = y[0][0]
#            y[0][1] = temp
#
#           count += 1
#          if count == temp:
#             count == 1
#            return False


x = []
eksport(x)

type_format(x, 1)
countEmptyStart = empty_field(x)

from timeit import default_timer as timer

timestart = timer()

find_way_c(x)
find_way_e(x)

timestop = timer()
score = timestop - timestart
view(x)
countEmptyEnd = empty_field(x)
type_format(x, 0)
save(x, score, countEmptyStart, countEmptyEnd)
