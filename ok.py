if __name__ == "__main__":
   alphabet = list('qwertyuioplkjhgfdsazxcvbnm')
   for char in alphabet:
      # print "        self.key_" + char + ".clicked.connect( lambda:self.kbinput(str(self.key_" + char + ".text())))"
      print "self.key_" + char + ".setText('"+char.lower()+"')"