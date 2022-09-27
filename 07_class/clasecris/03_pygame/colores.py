import random 

class COLOR():

    WHITE = [255,255,255]
    BLACK = [0, 0, 0,]

    RED  = [255, 0, 0]
    GREEN = [0, 255, 0]
    BLUE  = [0, 0, 255]
    
    YELLOW = [0,255,255]
    
    ORANGE = [255,125,0]
    GREY = [150,150,150]
    PURPLE = [255,0,255 ]

    sYello = [100,200,200]
    sGreen = [100, 200, 100]
    sRed= [200, 100, 100]
    sPurple = [200,100,200 ]

    ColoresLista=[WHITE,
                  BLACK,
                  RED,
                  GREEN,
                  BLUE,
                  YELLOW,
                  ORANGE,
                  GREY,
                  PURPLE]

    def RandomColorVa():
        return random.choice(COLOR.ColoresLista)


    def RandomColorVb():
        return [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    
    def CreaSombra(color):
        sombracolor=[1,2,3]
        mcolor=sum(color)/len(color)
        for i in range(0,len(color)-1):
            sombracolor[i]=(2*color[i]+mcolor)/3

        return sombracolor
    
    
