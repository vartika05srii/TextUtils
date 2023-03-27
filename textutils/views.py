#views takes http req and return http response
from django.http import HttpResponse
from django.shortcuts import render #for generating templates

def index(request):
    #file=open('1.txt', 'r+')
    #return HttpResponse(file.read())
    #return HttpResponse('''<h1><u>hello world</u></h1> <a href="https://www.youtube.com/">Acess Youtube</a> <br><a href="https://www.twitter.com/">Acess Twitter</a><br> <a href="https://www.facebook.com/">Acess  Facebook</a>''')
    #return HttpResponse('''<center><b><h1>Home</h1></b></center>  <a href="http://127.0.0.1:8000/removepunc"><input type=button value="Removepunc"></a> &emsp;&emsp;&emsp;<a href="http://127.0.0.1:8000/capitalisefirst"><input type=button value="capitalisefirst"></a> &emsp;&emsp; &emsp; <a href="http://127.0.0.1:8000/newlineremove"><input type=button value="newlineremove"></a> ''')        
    a={"name":"vartika", "place":"paris"}
    return render(request,'index.html',a)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

#def removepunc(request):
 #   print(request.GET.get('text','default'))
  #  return HttpResponse('''removepunc <br><br><a href="http://127.0.0.1:8000"><input type=button value="Back"></a>''' )

#def capitalisefirst(request):
   # return HttpResponse('''capitalisefirst <br><br><a href="http://127.0.0.1:8000"><input type=button value="Back"></a>''')

#def newlineremove(request):
  #  return HttpResponse('''newlineremove <br><br><a href="http://127.0.0.1:8000"><input type=button value="Back"></a>''')

#def about(request):
 #   return HttpResponse("about world")

def analyze(request):
    djtxt=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremove=request.POST.get('newlineremove','off')
    spaceremove=request.POST.get('spaceremove','off')
    charcount=request.POST.get('charcount','off')
    print(removepunc) #get text
    print(djtxt)
    if removepunc=="on":
        #return HttpResponse("remove punc") #analyze text
        #analyzed = djtxt
        punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for i in djtxt:
            if i not in punctuations:
                analyzed=analyzed+i
   
        a={'purpose':'remove punctuations', 'analyzed_text':analyzed}
        djtxt=analyzed
        #return render(request,'analyze.html',a)
    if fullcaps=="on":
        analyzed=""
        for i in djtxt:
            analyzed=analyzed+i.upper()
        a={'purpose':'change to uppercase', 'analyzed_text':analyzed}
        djtxt=analyzed
        #return render(request,'analyze.html',a)
    if newlineremove=="on":
        analyzed=""
        for i in djtxt:
            if i!="\n" and i!="\r":
                analyzed=analyzed+i
        a={'purpose':'remove new line', 'analyzed_text':analyzed}
        djtxt=analyzed
        #return render(request,'analyze.html',a)
    if spaceremove=="on":
        analyzed=""
        for i,j in enumerate(djtxt):
            if djtxt[i]==" ":
                pass
            else:
                analyzed=analyzed+j
        a={'purpose':'remove space', 'analyzed_text':analyzed}
        djtxt=analyzed
        #return render(request,'analyze.html',a)
    if charcount=="on":
        analyzed=""
        count=0
        for i in range(len(djtxt)):
            count+=1          
            analyzed=count
        a={'purpose':'charcount', 'analyzed_text':analyzed}
    if removepunc!="on" and fullcaps!="on" and newlineremove!="on" and spaceremove!="on" and charcount!="on":
        return HttpResponse("error")
        #return render(request,'analyze.html',a)
    a={'purpose':'change to desired form', 'analyzed_text':analyzed}
    return render(request, 'analyze.html', a)

def ex1(request):
    return render(request,'ex1.html')


    