from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
        im_bin = Image()
        im_bin.set_pixels(np.zeros((self.H, self.W), dtype = np.uint8))
        
        for i in range (self.H):
            for j in range (self.W):
                if self.pixels[i][j] >= S:
                    im_bin.pixels[i][j] = 255
        return im_bin

    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
        lmax = 0
        lmin = self.H
        cmax = 0
        cmin = self.W
        
        for i in range (self.H):
            for j in range (self.W):
                if self.pixels[i][j] == 0:
                    if j < cmin:
                        cmin = j
                    elif j > cmax :
                        cmax = j
                    if i < lmin:
                        lmin = i
                    elif i > lmax:
                        lmax = i
        h = lmax - lmin
        w = cmax - cmin
        
        im_red = Image()
        
        im_red.set_pixels(np.zeros((h, w), dtype = np.uint8))
        for i in range (h):
            for j in range (w):
                
                if self.pixels[lmin+i, cmin + j] == 255:
                    im_red.pixels[i][j] = 255
                elif self.pixels[lmin +i, cmin+j] == 0:
                    im_red.pixels[i][j] = 0        
        
        return im_red

    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        res_im = Image()
        new = resize(self.pixels, (new_H, new_W), 0)
        res_im.set_pixels(np.uint8(new*255))
        return res_im
        


    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        n = 0
        for i in range (self.H):
            for j in range (self.W):
                if self.pixels[i,j] == im.pixels[i,j]:
                    n = n+1
                
        return n/(self.H*self.W)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
