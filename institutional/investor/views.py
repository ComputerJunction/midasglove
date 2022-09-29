import os
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.template import Context

# Create your views here.
from collections import defaultdict
from json import dumps

this_folder = os.getcwd()

def clean_text(line):
    
    for val in [b'\\',b'%',b'#',b'&', b'/', b'?', b'*', b'(', b')', b'!', b'.']:
        
        line = line.replace(val, b'')
        
    for val in [b'3m co']:
        
        line = line.replace(val,b'three m')
    
    return line.decode().strip()


def split_strip(line=[], splitter=',', maxsplit=1):
    
    line = line.split(sep=splitter, maxsplit=maxsplit)
    
    line = [i.strip() for i in line]
    
    return line

def landing(request):

    return render(request, 'landing.html')


def index(request):
    
    return render(request, './html/index.html')


def sic(request):
    
    sics = defaultdict(list)
    
    count = {}
    
    with open(r'.\investor\templates\data\sic.txt', 'rb') as r:
        
        for line in r:
            
            line = clean_text(line)
            
            line = split_strip(line=line, maxsplit=2)
            
            tag = line[1]
            
            name = line[2]
            
            header = line[0]
            #will want an inner count
            subheaders = f"{tag}-{name} Count of companies - Link 1"
            
            sics[header].append(subheaders)
            
    for ind, arr in sics.items():
        header_with_count = f"{ind} - SubTotal - {len(arr)}"
        count[header_with_count] = arr
            
    context = {"sics":count}
    
    return render(request, 'html/sic_base.html', context )

def inv(request):
    
    count = []
    
    headers = ['Name', 'State']
    
    with open(r'.\investor\templates\data\inv.txt', 'rb') as r:
        
        for line in r:
                    
            line = clean_text(line)
            
            line = split_strip(line=line)
            
            name = line[0]
            
            count.append([name, line[1]])
            
    
    context = {'sics':dumps(count), 'headers': headers}
    
    return render(request, 'html/inv_base.html', {"context":context} )


def sec(request):
    
    count = []
    
    headers = ['Index', 'Name', 'Class', 'Cusip', 'Total Records']
    
    with open(r'.\investor\templates\data\sec.txt', 'rb') as r:
        
        j = 1
        for line in r:
        #for j in range(0, 2000):
           
            
            line = clean_text(line)
            
            line = split_strip(line=line)
            
            try:
                #name, class, cusip
                name, class_, cusip = split_strip(line=line[0], splitter="-", maxsplit=2)
                #count

                num_of = split_strip(line=line[1], splitter="-")
                num_of = num_of[1]


                count.append([j,name, class_, cusip, num_of])

                j = j + 1

            except ValueError:
                
                continue
                
    context = {'sics':dumps(count), 'headers':headers}

    
    return render(request, 'html/sec_base.html', {"context":context} )

def graph(request):
    
    #r = r".\investor\templates\data\simple_numbers.txt"
    
    count = [
        {
         "2010":6190,
        "2019":2609,
            "State":"verition",
        },

        {"2010":37254523,"2019":39512223,"State":"California"},
                {"State":"sanders",
        "2019":3131,
        "2010":1866},
        {"State":"Jones",
        "2019":500,
        "2010":600},
        
        {"columns":["State", "2019", "2010"]}
        
        
    ]


    context = dumps(count)
    return render(request, 'html/graph_base.html', {"context":context} )    
    
