import tkinter as tk
from tkinter import filedialog, Text
import p_00_auto_main
import os

window = tk.Tk()
window.title("Corpus Vectorizer")
dataFiles = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempDataFiles = f.read()
        tempDataFiles = tempDataFiles.split(',') #creates array
        dataFiles = [x for x in tempDataFiles if x.strip()] #remove empty spaces

def openFile():
    for widget in filesFrame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                        filetypes=(("dat files", "*.dat"), ("all files", "*.*")))
    
    if filename != "":
        dataFiles.append(filename)
    
    for dataFile in dataFiles:
        label = tk.Label(filesFrame, text=dataFile, bg="gray")
        label.pack()

def clearDataFileList():
    for widget in filesFrame.winfo_children():
        widget.destroy()

    del dataFiles[:] #empty list of files

    # clear content in save file
    with open('save.txt', 'r+') as f:
        f.truncate(0)
        f.close()

def processVectorization():
    filesToProcess = [x for x in dataFiles if x.strip()] #remove empty spaces just in case
    for filename in filesToProcess:
        p_00_auto_main.main(filename)

def addTextToOutput(words):
    text = tk.LabelFrame(outputFrame, text=words)
    text.pack()

#### GUI APP ####

# canvas = tk.Canvas(window, height=700, width=700, bg="#263D42")
# canvas.pack()

actionsFrame = tk.Frame(window, bg="#add8e6")
actionsFrame.grid(row=0, column=0, sticky="ns")

filesFrame = tk.LabelFrame(window, bg="white", text="Input")
filesFrame.grid(row=0, column=1, sticky="nsew")

outputFrame = tk.LabelFrame(window, bg="white", text="Output")
outputFrame.grid(row=1, column=1, sticky="nsew")

openFileBtn = tk.Button(actionsFrame, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=openFile)
openFileBtn.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

clearFilesBtn = tk.Button(actionsFrame, text="Clear File List", padx=10, pady=5, fg="white", bg="#263D42", command=clearDataFileList)
clearFilesBtn.grid(row=1, column=0, sticky="ew", padx=5)

processFilesBtn = tk.Button(window, text="Run Vectorization On Selected Files", padx=10, pady=10, highlightbackground="green", fg="white", bg="#263D42", command=processVectorization)
processFilesBtn.grid(row=2, column=1, stick="ew", padx=5)

for dataFile in dataFiles:
    label = tk.Label(filesFrame, text=dataFile)
    label.pack()

window.mainloop() #runs gui app

with open('save.txt', 'w') as f:
    for dataFile in dataFiles:
        f.write(dataFile + ',')