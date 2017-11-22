class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # message = ''
        # alphabet = string.ascii_uppercase + string.ascii_lowercase
        # for char in self.message_text:
        #   if char not in alphabet:
        #     message += ' '
        #   else:
        #     message += char
        alphabet = string.ascii_lowercase + string.ascii_uppercase
        highcount = 0
        word_list = self.valid_words
        decrypted = ()
        for shift in range(26):
          msg = ''
          shifted = self.apply_shift(shift)
          for char in shifted:
            if char not in alphabet:
              msg += ' '
            else:
              msg += char
          msgList = msg.split(' ')
          count = 0
          for word in msgList:
            if is_word(word_list, word):
              count += 1
          if count > highcount:
            highcount = count
            decrypted = (shift, shifted)
        return decrypted
