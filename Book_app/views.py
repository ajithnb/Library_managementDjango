from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View

# Create your views here.

class GoodMorningView(View):
    def get(self,request):
        data= {
             "Message": "Good Morning..!"
            }

        return JsonResponse(data)

class LibraryView(View):
    def get(self,request):
        data={
            "Library": "Central Library",
            "contact":"987654321",
            "owner":"Renjith",
            "Location": "Idukki",
            "Status": "Open"

        }

        return JsonResponse(data)
    
class BookView(View):
    def get(self,request):
        data={
            "Book_Name": "Django for Beginners",
            "Author": "William S. Vincent",
            "Price": 650,
            "Description":"",
            "published_year":2000

        }
        return JsonResponse(data)
    
class StudentView(View):
    def get(self,request):
        data={
             "Name": "Anu",
            "Course": "Python Django",
            "Batch": "June 2026",
            "Institution":"Luminar Technolab",
            "joining_year":2026,
            "joining_month":"May",
            "Location":"Kochi",
            "Mobile":8976543210,
            "DOB":"20/08/2000"

        }

        return JsonResponse(data)
    
class BooksView(View):
    def get(self,request):
        data={
            "Books": ["Python","Django","Java","React","MySQL"]
        }
        return JsonResponse(data)
    
class EmployeeView(View):
    def get(self,request):
        data={
        "id":"1",
        "name":"ajith",
        "place":"alattil",
        "designation":"python devolper",
        "contact":"9876543456",
        "experience":"10 years",
        "qualification":" degree"

        }
        return JsonResponse(data)

    
