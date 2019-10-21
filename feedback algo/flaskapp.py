from flask import Flask, render_template, \
 url_for, redirect, request, flash, session

import os
import PyPDF2 
  
# creating a pdf file object 


app = Flask(__name__)

@app.route('/')
def home():

    cmd  = 'python cvparseV2.py'
		
    print(cmd)
    os.system(cmd)
    
    pdfFileObj = open('results.pdf', 'rb') 
  
# creating a pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
   
# creating a page object 
    pageObj = pdfReader.getPage(0) 
  
# extracting text from page 
    output = pageObj.extractText()
  
# closing the pdf file object 
    pdfFileObj.close() 
    
    ss=output.split('\n')
    final_str=[ss[0]]
    for i in range(1,len(ss)-1,2):
        #print(i)
    
        st=[]
        st.append(ss[i])
        st.append(ss[i+1])
        final_str.append(' '.join(st))
    string = '\n'.join(final_str)
    
    return ("{}".format(string))

	
		

        



if __name__ == '__main__':
	app.run(debug=True)
