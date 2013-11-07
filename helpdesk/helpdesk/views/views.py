from django.shortcuts import render

def helloworld(request):
	context = {"data":["hello world", "hello mars"], "moredata":"goodbye world"}
	return render(request, 'helloworld.html', context)