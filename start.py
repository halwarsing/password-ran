import random
from threading import Thread
import time
import sys

class thr(Thread):
        def __init__(self):
                self.tim = time.time()
                Thread.__init__(self)
                self.chars = "!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
                self.ai = 0
                self.le = 8
                self.ac = 100
                with open("password/passwords0.txt", "r") as f:
                        text = f.read()
                        self.sl = text.split(",")

                f.close()
                
        def run(self):
                self.pas()

        def pas(self):
                while(self.ai <= self.ac):
                        pa = ""

                        for i in range(self.le):
                                pa += random.choice(self.chars)

                        if pa not in self.sl:
                                with open("password/passwords0.txt","r") as f:
                                        te = f.read()
                                        self.sl = te.split(",")
                                        f.close()
                                        
                                self.sl.append(pa)
                                self.ai += 1
                                print(pa)
                                with open("password/passwords0.txt","a") as f:
                                        f.write(pa+",")
                                        f.close()

                print("The end len list = "+str(len(self.sl)))
                

                f.close()
                sys.exit()

def run():
        thrd = thr()
        thrd.start()
