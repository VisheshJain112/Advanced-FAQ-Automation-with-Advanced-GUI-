import os






stre=r"""



if __name__ == '__main__':
    from tkinter import *
    from tkinter.ttk import *
    import tkinter as tk
    from tkinter import ttk
    from tkinter import *
    import time
    import numpy as np
    from tkinter.filedialog import askopenfilename
    from csv import writer

    import tkinter as tk
    from PIL import Image, ImageTk
    from itertools import count

        # Initialize the recognizer
        # r = sr.Recognizer()

        # def SpeakText(command):
        # Initialize the engine
        # engine = pyttsx3.init()
        # engine.say(command)
        # engine.runAndWait()

    import tkinter as tk
    from PIL import Image, ImageTk
    from itertools import count

    class ImageLabel(tk.Label):

        def load(self, im):
            if isinstance(im, str):
                im = Image.open(im)
            self.loc = 0
            self.frames = []

            try:
                for i in count(1):
                    self.frames.append(ImageTk.PhotoImage(im.copy()))
                    im.seek(i)
            except EOFError:
                pass

            try:
                self.delay = im.info['duration']
            except:
                self.delay = 100

            if len(self.frames) == 1:
                self.config(image=self.frames[0])
            else:
                self.next_frame()

        def unload(self):
            self.config(image="")
            self.frames = None

        def next_frame(self):
            if self.frames:
                self.loc += 1
                self.loc %= len(self.frames)
                self.config(image=self.frames[self.loc])
                self.after(self.delay, self.next_frame)

    root = tk.Tk()
    root.title('Cuemath- Loading...')

    root.iconbitmap(r'logo.ico')
    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('whoa.gif')

    # Destroy the widget after 30 seconds
    root.after(5000, lambda: root.destroy())
    root.mainloop()
    root = Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    img = PhotoImage(file="logo.png")
    canvas.create_image(0, 0, anchor=NW, image=img)
    # Destroy the widget after 30 seconds
    root.after(1500, lambda: root.destroy())
    root.mainloop()

    import warnings

    warnings.filterwarnings("ignore")
    import tkinter as tk
    from tkinter import simpledialog
    from tkinter import messagebox

    application_window = tk.Tk()

    root = tk.Tk()
    root.title('Cuemath')
    # p1 = PhotoImage(file='logo.ico')

    root.iconbitmap(r'logo.ico')
    application_window.withdraw()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    T = tk.Text(root, height=height, width=width)

    T.pack()

    import os
    import re
    
    import nltk
    import numpy as np
    import random
    import string  # to process standard python strings

    import os
    import re
    import tkinter as tk
    import pandas as pd

    from nltk.corpus import stopwords

    import requests

    req = requests.get("https://www.cuemath.com/live-online-classes/")

    from bs4 import BeautifulSoup

    soup_blom = BeautifulSoup(req.text, 'html5lib')
    summaries_blom_q = soup_blom.find_all(
        "div", class_="sc-bxivhb faqs__TitleTextWrapper-sc-16cai2p-3 hpdWaM")
    summaries_blom_a = soup_blom.find_all("div",
                                          class_="sc-bxivhb faqs__TextDescriptionWrapper-sc-16cai2p-4 bmKhWc")
    question = []
    answere = []
    for summary_blom in summaries_blom_q:
        title_question = (summary_blom.get_text().strip())

        question.append(title_question)

    for summary_blom in summaries_blom_a:
        title_answere = (summary_blom.get_text().strip())

        answere.append(title_answere)

    total = answere

    sent_total = total

    counter = 0
    for tweet in sent_total:
        sent_total[counter] = tweet.lower()
        counter += 1

    raw = '\n'.join(sent_total)

    f = open('demo.txt', 'r', errors='ignore')
    f = f.read()
    f = f.replace('?', ' \n')
    import re
    f_1 = open('demo_1.txt', 'r', errors='ignore')
    f_1 = f_1.read()

    # f_1=f_1.translate(str.maketrans(' ', ' ', string.punctuation))
    f_1 = re.sub(r"[\?]+", "", f_1)
    f_1 = re.sub(r'[\n]+', '', f_1)

    f_2 = open('demo_2.txt', 'r', errors='ignore')
    f_2 = f_2.read()
    # f_2=f_2.translate(str.maketrans(' ', ' ', string.punctuation))
    f_2 = re.sub(r"[\?]+", " ", f_2)
    f_2 = re.sub(r'[\n]+', ' ', f_2)

    f_3 = open('demo_3.txt', 'r', errors='ignore')
    f_3 = f_3.read()
    # f_2=f_2.translate(str.maketrans(' ', ' ', string.punctuation))
    f_3 = re.sub(r"[\?]+", " ", f_3)
    f_3 = re.sub(r'\n+', ' ', f_3)

    f_4 = open('demo_4.txt', 'r', errors='ignore')
    f_4 = f_4.read()
    # f_2=f_2.translate(str.maketrans(' ', ' ', string.punctuation))
    f_4 = re.sub(r"[\?]+", " ", f_4)
    f_4 = re.sub(r'[\n]+', ' ', f_4)

    f_5 = open('demo_5.txt', 'r', errors='ignore')
    f_5 = f_5.read()
    # f_2=f_2.translate(str.maketrans(' ', ' ', string.punctuation))
    f_5 = re.sub(r"[\?]+", " ", f_5)
    f_5 = re.sub(r'[\n]+', ' ', f_5)

    file = open(r"my_usage.txt", "r", errors='ignore')
    raw = raw + f_1 + f_2 + f_3 + f_4 + f_5

    def runner(raw):
        raw = raw.lower()

        sent_tokens = nltk.sent_tokenize(raw)
        for i in range(len(sent_tokens) - 3):
            str = 'why'
            if (len(sent_tokens[i]) > 2 and (str not in sent_tokens[i])):
                sent_tokens[i] = sent_tokens[i] + sent_tokens[i +
                    1] + sent_tokens[i + 2] + sent_tokens[i + 3]
            else:
                sent_tokens[i] = ''

        lemmer = nltk.stem.WordNetLemmatizer()

        # WordNet is a semantically-oriented dictionary of English included in NLTK.
        def LemTokens(tokens):
            return [lemmer.lemmatize(token) for token in tokens]

        remove_punct_dict = dict((ord(punct), None)
                                 for punct in string.punctuation)

        def LemNormalize(text):
            return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

        GREETING_INPUTS = ("hello", "hi", "greetings",
                           "sup", "what's up", "hey",)
        GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there",
            "hello", "I am glad! You are talking to me"]

        def greeting(sentence):

            for word in sentence.split():
                if word.lower() in GREETING_INPUTS:
                    return random.choice(GREETING_RESPONSES)

        from sklearn.feature_extraction.text import TfidfVectorizer

        from sklearn.metrics.pairwise import cosine_similarity

        def response(user_response, i):
            robo_response = ''
            sent_tokens.append(user_response)
            TfidfVec = TfidfVectorizer(
                tokenizer=LemNormalize, stop_words='english')
            tfidf = TfidfVec.fit_transform(sent_tokens)
            vals = cosine_similarity(tfidf[-1], tfidf)
            idx = vals.argsort()[0][-2 - i]
            flat = vals.flatten()
            flat.sort()
            req_tfidf = flat[-2]
            i = 0
            if (req_tfidf == 0):
                robo_response = robo_response + "I am sorry! I don't understand you"
                return robo_response
            else:
                robo_response = robo_response + sent_tokens[idx]
                return robo_response

        from tkinter import colorchooser

        flag = True

        cnt = 0
        T.insert(tk.END, "Welcome to the Cuemath. If you want to exit, type Bye!")
        while (flag == True):
            user_response = simpledialog.askstring("Cuemath", "You : ", parent = application_window)
            T.delete(1.0, tk.END)

            T.insert(tk.END,"Welcome to the Cuemath. If you want to exit, type Bye!\n\n")
            user_response = user_response.lower()


            if (user_response == 'adminpass'):
                Tk().withdraw()
                # we don't want a full GUI, so keep the root window from appearing
                filename = askopenfilename(title="Cuemath: Select")
                f_3 = open('{}'.format(filename), 'r', errors='ignore')
                f_3 = f_3.read()
                # f_2=f_2.translate(str.maketrans(' ', ' ', string.punctuation))
                f_3 = re.sub(r"[\?]+", "", f_3)
                # f_3 = re.sub(r'\n\s*\n', '.', f_3)
                raw = raw + f_3
                file1 = open("my_usage.txt", "a")  # append mode
                file1.write(f_3)
                file1.close()

                runner(raw)

            if (user_response == 'next'):
                if (cnt == 0):

                    i += 1

                    T.insert(tk.END, "CUEMATH: \n")

                    T.insert(tk.END, response(prev_response, i))
                    # SpeakText(response(prev_response,i))

                    cnt += 1
                else:
                    i += 2

                    T.insert(tk.END, "CUEMATH: \n")

                    T.insert(tk.END, response(prev_response, i))
                    # SpeakText(response(prev_response, i))
                    cnt = 0
            if (user_response == 'note'):

                def save():
                    e_p_name_t = e_p_name.get()
                    e_s_name_t = e_s_name.get()
                    e_number_t = e_number.get()
                    e_issue_t = e_issue.get()
                    e_remark_t = e_remark.get()
                    data_list = np.array([e_p_name_t, e_s_name_t, e_number_t, e_issue_t, e_remark_t])
                    SpeakText("YOUR DATA IS SAVED")

                    with open('my_data.csv', 'a+', newline='') as write_obj:
                        csv_writer = writer(write_obj)

                        csv_writer.writerow(data_list)

                    top.destroy()

                    T.insert(tk.END, "CUEMATH: \n")
                    runner(raw)

                top = tk.Tk()

                top.title('Cuemath')
                # p1 = PhotoImage(file='logo.ico')

                top.iconbitmap(r'logo.ico')

                top.geometry("800x450")
                entry_field_variable_1 = tk.StringVar()
                entry_field_variable_2 = tk.StringVar()
                entry_field_variable_3 = tk.StringVar()
                entry_field_variable_4 = tk.StringVar()
                entry_field_variable_5 = tk.StringVar()

                p_name = tk.Label(top, text="Parent Name :")
                p_name.place(x=30, y=50)

                s_name = tk.Label(top, text="Student name :")
                s_name.place(x=30, y=90)

                number = tk.Label(top, text="Number :")
                number.place(x=30, y=130)

                issue = tk.Label(top, text="Issue :")
                issue.place(x=30, y=170)

                remark = tk.Label(top, text="Remark :")
                remark.place(x=30, y=210)

                e_p_name = tk.Entry(top, textvariable=entry_field_variable_1, width=80)
                e_p_name.place(x=120, y=50)

                e_s_name = tk.Entry(top, textvariable=entry_field_variable_2, width=80)
                e_s_name.place(x=120, y=90)
                e_number = tk.Entry(top, textvariable=entry_field_variable_3, width=80)
                e_number.place(x=120, y=130)

                e_issue = tk.Entry(top, textvariable=entry_field_variable_4, width=80)
                e_issue.place(x=120, y=170)

                e_remark = tk.Entry(top, textvariable=entry_field_variable_5, width=80)
                e_remark.place(x=120, y=210)

                sbmitbtn = tk.Button(top, text="Note It!", activebackground="pink", activeforeground="blue",
                                     command=save)
                sbmitbtn.place(x=260, y=250)








            elif (user_response != 'bye'):
                if (user_response == 'thanks' or user_response == 'thank you'):
                    flag = False
                    stuart = tk.END
                    T.insert(tk.END, "CUEMATH: You are welcome..")



                else:
                    if (greeting(user_response) != None):
                        stuart = tk.END
                        T.insert(tk.END, "CUEMATH: " + greeting(user_response))
                        # SpeakText(greeting(user_response))



                    else:

                        T.insert(tk.END, "CUEMATH: \n")
                        stuart = tk.END
                        cnt = 0
                        prev_response = user_response
                        T.insert(tk.END, response(user_response, i))
                        # SpeakText(response(user_response,i))
                        i = 0

                        sent_tokens.remove(user_response)

            else:
                flag = False
                T.insert(tk.END, "Thanks for Using Cuemath agent, Bye Take care..")
                # SpeakText("Bye Take care")
                import time
                time.sleep(1)
                root.destroy()
                root.mainloop()
                exit()
                file.close()

    runner(raw)
"""


















f= open("faq_test.py","w+")
f.write(stre)
f.close()

os.system('cmd /c "python faq_test.py"')
import os
os.remove("faq_test.py")
#for i in tqdm(ls_r):
   #os.system('cmd /c "python faq.py"')









