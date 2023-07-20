#------------------------------------------------------------------
# created by iliya faramrzi (telegram:iliyawww | gmail:iliyafaramarzi1384@gmail.com | linkedin:iliyafaramrzi | github: iliyafaramarzi)
# some notes that help you to know code better:
# 0 means way
# 1 mean don't way(wall)
# 2 start point
# 3 finish point
# '_' means this way is checked befor
#------------------------------------------------------------------
import  numpy as np
from PIL import Image



# print list 10 * 10
def printli(li):
    count = 0
    for i in li:
        if count == 9:
            print(i)
            count = 0
        else:
            print(i, end=' ')
            count += 1
#find start point(2)
def find_start(li):
    return li.index(2)
#find the finish point(3)
def find_finish(li):
    return li.index(3)
# return up point of the location 
def up(pos):
    return pos - 10
# return down point of the location 
def down(pos):
    return pos + 10
# return right point of the location 
def right(pos):
    return pos + 1
# return left point of the location 
def left(pos):
    return pos - 1
#reset list with a source list(keep '_')
def reset(change, source):
    for i in change:
        index = change.index(i)
        if not i == '_':
            change[index] = source[index]

    return change
#reset all the numbers in a list with a source list
def reset_all(change, source):
    for i in change:
        index = change.index(i)
        change[index] = source[index]

    return change

#list that work on it
li =   [1,2,1,1,3,1,0,0,0,0,
        1,0,1,1,0,1,0,0,0,0,
        1,0,1,1,0,1,1,1,1,1,
        1,0,0,0,0,0,0,0,0,1,
        1,1,1,1,1,1,0,1,1,1,
        0,0,0,0,0,1,0,1,0,0,
        0,0,0,0,0,1,0,1,0,0,
        0,0,0,0,0,1,0,1,0,0,
        0,0,0,0,0,1,0,1,0,0,
        0,0,0,0,0,1,1,1,0,0]
#source list and don't change it at program
LI =   [1,2,1,1,3,1,0,0,0,0,
        1,0,1,1,0,1,0,0,0,0,
        1,0,1,1,0,1,1,1,1,1,
        1,0,0,0,0,0,0,0,0,1,
        1,1,1,1,1,1,0,1,1,1,
        0,0,0,0,0,1,0,1,0,0,
        0,0,0,0,0,1,0,1,0,0,
        0,0,0,0,0,1,0,1,0,0,
        0,0,0,0,0,1,0,1,0,0,
        0,0,0,0,0,1,1,1,0,0]

loc = find_start(li)
intersection = False
path = []


while 3 in li:
    if find_finish(li) < loc:

        if up(loc) == 0 and left(loc) == 0: # if we have more one way it is change the 'intersection' to True
            intersection = True

        if li[up(loc)] == 0 or li[up(loc)] == 3 and not li[up(loc)] == '_':  # if te up point is 0 or 3 and it is not _ it work
            loc = up(loc) # change location
            li[loc] = 9 # change pointer
            if not li[loc + 10] == '_': # check if don't gone this way befor do codes
                li[loc + 10] = '*'
                path.append(loc + 10)
            
            if intersection == True:    # check if 'intersection' is True make a sign that if this way is not true don't test it again
                li[loc] == '_'
                intersection = False
                path.append(loc)

        elif li[left(loc)] == 0 or li[left(loc)] == 3 and not li[left(loc)] == '_':
            loc = left(loc)
            li[loc] = 9
            if not li[loc + 1] == '_':
                li[loc + 1] = '*'
                path.append(loc + 1)
            

            if intersection == True:
                li[loc] == '_'
                intersection = False
                path.append(loc)
            #----------------------------------------
        elif li[down(loc)] == 0 or li[down(loc)] == 3 and not li[down(loc)] == '_':
            loc = down(loc)
            li[loc] = 9
            if not li[loc -10] == '_':
                li[loc - 10] = '*'
                path.append(loc - 10)

            if intersection == True:
                li[loc] = '_'
                intersection = False
                path.append(loc)

        elif li[right(loc)] == 0 or li[right(loc)] == 3 and not li[right(loc)] == '_':
            loc = right(loc)
            li[loc] = 9
            if not li[loc -1] == '_':
                li[loc - 1] = '*'
                path.append(loc - 1)
            

            if intersection == True:
                li[loc] == '_'
                intersection = False
                path.append(loc)
            #----------------------------------------

        else:
            li = reset(li, LI)
            loc = find_start(li)
            path.clear()

    elif find_finish(li) > loc:
        if li[down(loc)] == 0 and li[right(loc)] == 0:
            intersection = True

        if li[down(loc)] == 0 or li[down(loc)] == 3 and not li[down(loc)] == '_':
            loc = down(loc)
            li[loc] = 9
            if not li[loc -10] == '_':
                li[loc - 10] = '*'
                path.append(loc - 10)

            if intersection == True:
                li[loc] = '_'
                intersection = False
                path.append(loc)

        elif li[right(loc)] == 0 or li[right(loc)] == 3 and not li[right(loc)] == '_':
            loc = right(loc)
            li[loc] = 9
            if not li[loc -1] == '_':
                li[loc - 1] = '*'
                path.append(loc - 1)
            

            if intersection == True:
                li[loc] == '_'
                intersection = False
                path.append(loc)
                #-----------------------------------------
        elif li[up(loc)] == 0 or li[up(loc)] == 3 and not li[up(loc)] == '_':
            loc = up(loc)
            li[loc] = 9
            if not li[loc + 10] == '_':
                li[loc + 10] = '*'
                path.append(loc + 10)
            
            if intersection == True:
                li[loc] == '_'
                intersection = False
                path.append(loc)

        elif li[left(loc)] == 0 or li[left(loc)] == 3 and not li[left(loc)] == '_':
            loc = left(loc)
            li[loc] = 9
            if not li[loc + 1] == '_':
                li[loc + 1] = '*'
                path.append(loc + 1)
            

            if intersection == True:
                li[loc] == '_'
                intersection = False
                path.append(loc)
                #-----------------------------------------
        else:
            li = reset(li, LI)
            loc = find_start(li)
            path.clear()

#reset list for show the path  
li = reset_all(li, LI)

for i in path:
    li[i] = '*'

# Change the values to the RGB colors
b = []
for i in li:
    if i == 1:
        b.append(tuple((255,255,255)))
    elif i == 0:
        b.append(tuple((0,0,0)))
    elif i == 3:
        b.append(tuple((249,0,25)))
    elif i == 2:
        b.append(tuple((252,243,32)))
    elif i == '*':
        b.append(tuple((213,237,237)))

# change the 'b' list to the something that can be Visualize with pillow 
finall = []
counter = 0
for j in range(1, 11):
    counter += 1
    finall.insert(j-1, b[(j-1) * 10: j * 10])

x = np.asarray(finall, dtype=np.uint8)
image = Image.fromarray(x) #Change list to the image
image.show() #Show Image 

printli(li)
