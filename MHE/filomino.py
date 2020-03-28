def window(a):
    for i in range(len(a)):
        for j in range (len(a[i])):
            print (a[i][j],end='   ')
        print()

diagram=[['',5,'','',2],
        [5,' ',3,' ',' '],
        ['',2,' ',' ',1],
        [' ',1,' ',1,' '],
        [1,' ',' ',3,2]]

window(diagram)