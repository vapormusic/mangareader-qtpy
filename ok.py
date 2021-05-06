if __name__ == "__main__":
   alphabet = list('qwertyuioplkjhgfdsazxcvbnm')
   for char in alphabet:
       print "self.key_" + char + ".clicked.connect( lambda:self.kbinput('"+char+"'))"