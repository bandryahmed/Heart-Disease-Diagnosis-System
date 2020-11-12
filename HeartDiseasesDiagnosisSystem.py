
import pandas as pd
import numpy as np
import warnings
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from tkinter import *
warnings.filterwarnings("ignore")

def mod():
    def heart_disease(new_input):
        df=pd.read_csv(r"dataset.csv")
        df.count().isnull()
        df.describe()
        x= df.drop('target',axis=1)
        y=df['target']
        model= ExtraTreesClassifier()
        model.fit(x,y)
        feat_importances = pd.Series(model.feature_importances_, index=x.columns)
        randomforest_classifier= RandomForestClassifier(n_estimators=100)
        score=cross_val_score(randomforest_classifier,x,y,cv=15)
        acc=score.mean()
        op=model.predict(new_input)
        com=[op,acc]
        return com

    window = Tk()
    window.title("Heart Diseases Diagnosis System")
    window.geometry('550x450')
    window.configure(bg='#fab1a0')

    lbl = Label(window, text="Enter your Health Diagnostic Information:",background="#fab1a0", foreground="#2d3436")
    lbl.grid(column=1, row=0)
    lbl.config(font=("Times",12))

    lbl = Label(window, text=" AGE",background="#ff7675", foreground="#ecf0f1")
    lbl.grid(column=1, row=1)
    lbl.config(font=("Times",10 ))
    age = Entry(window,width=20)
    age.grid(column=3, row=1)
    age.focus()

    lbl = Label(window, text=" SEX (m=1,f=0)",background="#b2bec3", foreground="#ecf0f1")
    lbl.grid(column=1, row=2)
    lbl.config(font=("Times", 11))
    sex = Entry(window,width=20)
    sex.grid(column=3, row=2)
    sex.focus()

    lbl = Label(window, text=" Chest Pain Level (0-3)",background="#ff7675", foreground="#ecf0f1")
    lbl.grid(column=1, row=3)
    lbl.config(font=("Times", 12))
    cp = Entry(window,width=20)
    cp.grid(column=3, row=3)
    cp.focus()

    lbl = Label(window, text=" Resting Blood Pressure (in mm Hg )",background="#b2bec3", foreground="#ecf0f1")
    lbl.grid(column=1, row=4)
    lbl.config(font=("Times", 11))
    bps = Entry(window,width=20)
    bps.grid(column=3, row=4)
    bps.focus()

    lbl = Label(window, text="Cholestoral (in mg/dl)",background="#ff7675", foreground="#ecf0f1")
    lbl.grid(column=1, row=5)
    lbl.config(font=("Times", 11))
    chol = Entry(window,width=20)
    chol.grid(column=3, row=5)
    chol.focus()

    lbl = Label(window, text="Fasting Blood Sugar > 120 (mg/dl) (1=true; 0=false)",background="#b2bec3", foreground="#ecf0f1")
    lbl.grid(column=1, row=6)
    lbl.config(font=("Times", 11))
    fbs = Entry(window,width=20)
    fbs.grid(column=3, row=6)
    fbs.focus()

    lbl = Label(window, text="Resting Electrocardiographic Results",background="#ff7675", foreground="#ecf0f1")
    lbl.grid(column=1, row=7)
    lbl.config(font=("Times", 11))
    ecg = Entry(window,width=20)
    ecg.grid(column=3, row=7)
    ecg.focus()

    lbl = Label(window, text="Maximum Heart Rate Achieved",background="#b2bec3", foreground="#ecf0f1")
    lbl.grid(column=1, row=8)
    lbl.config(font=("Times", 11))
    mhr = Entry(window,width=20)
    mhr.grid(column=3, row=8)
    mhr.focus()

    lbl = Label(window, text="Exercise Induced Angina (1 = yes; 0 = no)",background="#ff7675", foreground="#ecf0f1")
    lbl.grid(column=1, row=9)
    lbl.config(font=("Times", 11))
    eia = Entry(window,width=20)
    eia.grid(column=3, row=9)
    eia.focus()

    lbl = Label(window, text="ST Depression Induced by Exercise Relative to Rest",background="#b2bec3", foreground="#ecf0f1")
    lbl.grid(column=1, row=10)
    lbl.config(font=("Times", 11))
    st = Entry(window,width=20)
    st.grid(column=3, row=10)
    st.focus()

    lbl = Label(window, text="The Slope of the Peak Exercise ST Segment",background="#ff7675", foreground="#ecf0f1")
    lbl.grid(column=1, row=11)
    lbl.config(font=("Times", 11))
    slope = Entry(window,width=20)
    slope.grid(column=3, row=11)
    slope.focus()

    lbl = Label(window, text="Number of Major Vessels (0-3) Colored by flourosopy",background="#b2bec3", foreground="#ecf0f1")
    lbl.grid(column=1, row=12)
    lbl.config(font=("Times", 11))
    ca = Entry(window,width=20)
    ca.grid(column=3, row=12)
    ca.focus()

    lbl = Label(window, text="A blood Disorder Called thalassemia \n (3=Normal; 6=Fixed Defect; 7=Reversable Defect)",background="#ff7675", foreground="#ecf0f1")
    lbl.grid(column=1, row=13)
    lbl.config(font=("Times", 11))
    thal = Entry(window,width=20)
    thal.grid(column=3, row=13)
    thal.focus()

    def clicked():
        new_input=[age.get(),sex.get(),cp.get(),bps.get(),chol.get(),fbs.get(),ecg.get(),mhr.get(),eia.get(),st.get(),slope.get(),ca.get(),thal.get()]
        new_input= np.reshape(new_input,(1,-1))
        d=heart_disease(new_input)
        ans=d[0]
       #score=cross_val_score(randomforest_classifier,x,y,cv=15)
        sc=str(d[1]*100)

        if(ans==1):
            s='You have a Heart Disease'
        else:
            s="You are in Perfect Health"
        ot.configure(text="Result: " + s + "\n(Accuracy= "+ sc +"% )" )
    btn = Button(window, text="submit",command=clicked, bg='#ff7675', fg='white')
    btn.grid(column=3, row=15)

    ot = Label(window, text="",font=("Arial Bold", 10))
    ot.grid(column=1, row=17)
    window.mainloop()
mod()