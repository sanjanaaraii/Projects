import random
import time
import winsound
class morsecode:
    morsecode_dict={
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
        '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', 
        "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', 
        ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', 
        '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', 
        '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
    }

    def __init__(self):
        self.run=True

    def choice(self,option):
        if(option==1):
            message=input("enter your message :")
            result=self.morsecodeTOalphabets(message)
            print(result)
        elif option == 2:
            message = input("Enter your text message: ")
            result = self.alphabetsTOmorsecode(message)
            print( result)
        elif option == 3:
            self.practisemode()
        elif(option==4):
            choose=int(input("1 to enter alphabets in message \n2 to enter morse code in message\n"))
            if(choose==1):
                message=input("enter the message : ")
                r=self.alphabetsTOmorsecode(message)
                self.audio(r)
            elif(choose==2):
                message=input("enter the message in morse code")
                self.audio(message)
            else:
                print("INVALID")
        elif(option==5):
            print("Exiting")
            self.exit()
        else:
            print("invalid option")
        

    def morsecodeTOalphabets(self,message):
        words = message.split(' / ')  # Words are separated by "/"
        decipher = ''
        for word in words:
            for morse_letter in word.split():
                if morse_letter in self.morsecode_dict.values():
                    decipher += list(self.morsecode_dict.keys())[list(self.morsecode_dict.values()).index(morse_letter)]
                else:
                    decipher += 'invalid morse code'
            decipher += ' '  
        return decipher.strip()
 

    def alphabetsTOmorsecode(self,message):
        message = message.upper()
        encoded = ''
        for char in message:
            if char in self.morsecode_dict:
                encoded += self.morsecode_dict[char] + ' '
            else:
                return "Invalid character in message"
        return encoded.strip()


    def practisemode(self):
        print("Practice Mode: Guess the translation!")
        score = 0
        for _ in range(5):
            mode = random.choice(["to_morse", "to_text"])
            if mode == "to_morse":
                word = random.choice([k for k in self.morsecode_dict.keys() if len(k) == 1])  
                print(f"Translate this character to Morse code: {word}")
                user_input = input("Your answer: ").strip()
                correct_answer = self.alphabetsTOmorsecode(word)
                if user_input == correct_answer:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! The correct answer was: {correct_answer}")
            else:
                morse_word = random.choice(list(self.morsecode_dict.values()))
                print(f"Translate this Morse code to text: {morse_word}")
                user_input = input("Your answer: ").strip().upper()
                correct_answer = self.morsecodeTOalphabets(morse_word)
                if user_input == correct_answer:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! The correct answer was: {correct_answer}")
        print(f"Your final score: {score}/5")


    def audio(self,message):
        dot_duration = 300  
        dash_duration = 600  
        pause_duration = 200  
        
        for symbol in message:
            if symbol == '.':
                winsound.Beep(1000, dot_duration)  
            elif symbol == '-':
                winsound.Beep(1000, dash_duration) 
            elif symbol == ' ':
                time.sleep(pause_duration / 1000)  
            elif symbol == '/':
                time.sleep(3 * pause_duration / 1000)  


    def exit(self):
        self.run=False

    def start(self):
        while(self.run==True):
            print(" 1. Morse Code to Alphabets \n 2. Alphabets To Morse Code \n 3. Practise morse code \n 4. Audio output of morse code :) \n 5. Exit")
            option=int(input("Enter Your Choice : "))
            self.choice(option)
tool=morsecode()
tool.start()

    

