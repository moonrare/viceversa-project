from django.shortcuts import render

def home(request):
	return render(request,'home.html')
def reverse(request):
	get_user_text = request.GET['usertext']
	count_words = len(get_user_text.split())
	reversed_text = get_user_text[::-1]
	return render(request,'reverse.html',{'usertext':get_user_text,'reversedtext':reversed_text,'countwords':count_words})