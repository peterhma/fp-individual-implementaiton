from django.shortcuts import render
from coloring.models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def get_author_by_name(authorname): 
  author = None
  
  # check if an Author with name 'authorname' already exists
  if Author.objects.filter(name = authorname).exists():
    # if so, fetch that object from the database
    author = Author.objects.get(name=authorname)
    
  else: 
    # otherwise, create a new Author with the name authorname
    author = Author(name = authorname)
    # save the created object
    author.save()

  return author



@csrf_exempt
def index(request, authorname="DefaultAuthor"):

  print("The authorname is:", authorname)
  author = get_author_by_name(authorname)
  
  if request.POST: 
    # POST request received
    
    # demonstrating printing out the POST request & data
    print("Received POST request with data:")
    data = json.loads(request.body.decode('UTF-8'))
    print(data)

    try:
      Drawing.objects.get(author=data.author, title=data.title).update(points=data.points)
      
    except:
        drawing = Drawing(title=data.title, author=data.data, points=data.points)
        drawing.save()
    

    # find out if a Drawing with the Author and Title already exists?
    # if it doesn't exist, you may create a new Drawing object
    # if it does exist, you may update an existing Drawing object
    
    # make sure to save your object after creating or updating 
    # for more information, see get_author_by_name() and reference below
    # https://docs.djangoproject.com/en/4.0/ref/models/instances/#saving-objects
    
    return HttpResponse(True)

  else: 
    # GET request received

    # if a drawing by the author already exists,
    # send the drawing conent and title with the data below
    data= json.loads(request.body.decode('UTF-8'))
    try: 
       drawing = Drawing.objects.get(author=data.author, title=data.title)
    except:
      print("No such title or author") 
    data = {
      "title": data.title,
      "author": author,
      'drawing': drawing.points,
    }
    
    return render(request, 'coloring/index.html', data)