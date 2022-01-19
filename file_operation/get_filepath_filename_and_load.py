from tkinter import filedialog as fd
from tkinter import messagebox
import tkinter as tk
import pandas as pd
import os


def select_files(filetype):
        #enables multifile selection and returns list of [filename,filepath]
        filename = None
        filepath = None
        file_list = []
        root = tk.Tk()
        root.update()
        if filetype == ".csv" :
            
            filetypes = (('csv files', '*.csv'),('All files','*.*'))
            
            

            try:
                root.update()
                files = fd.askopenfilenames(parent= root, title='Open a file',  filetypes= filetypes)
                filelist = root.tk.splitlist(files)
        
                for i in filelist:

                    filename = os.path.splitext(os.path.basename(i))[0] + '.csv'
                    filepath = i[:-len(filename)]
                    
                    file_list.append([filename, filepath])
            
                
                    print("------------------------------------------------")
                    print('Selected file: ', filename)
                    print("------------------------------------------------")
                
                    print("------------------------------------------------")
                    print('Filepath: ', filepath)
                    print("------------------------------------------------")
        
                messagebox.showinfo(title='Selected File',message= "Files selected")
                print("------------------------------------------------")
                print(file_list)
                print("------------------------------------------------")
        
            except:
                print("------------------------------------------------")
                print("Error select_file", filename, filepath)
                print("------------------------------------------------")
                
        else:
                print("------------------------------------------------")
                print("Filetype invalid")
                print("------------------------------------------------")
        
        root.destroy()
        
        return file_list



def load_file(file):
        
        
        filename = file[0]
        filepath = file[1]
        
        os.chdir(filepath)
        
        print("------------------------------------------------")
        print("Current working directory: {0}".format(os.getcwd()))
        print("------------------------------------------------")
        
        df = pd.read_csv(filename, sep = '\t', decimal = ',')
        if object in df.dtypes.to_list():
            df = pd.read_csv(filename, sep = '\t', decimal = '.')
        

        print("------------------------------------------------")
        print('File loaded: ', filename)
        print("------------------------------------------------")
        
        #show loaded dataframe
        pd.set_option('display.max_columns', 19)
        df.head(10)
        
        print("------------------------------------------------")
        print (df)
        print("------------------------------------------------")
        
        return filename,df

