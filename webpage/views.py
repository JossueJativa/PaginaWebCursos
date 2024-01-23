from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from monolito.models import User, Cursos

# Create your views here.
def index(request):
    return render(request, "intro/index.html", {
        "cursos": Cursos.objects.all()
    })

def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        # Check if username and password are correct\
        user = User.objects.filter(email=email).first()
        if user:
            user = authenticate(request, username=user.username, password=password)
        else:
            return render(request, "intro/login.html", {
                "message": "Invalid credentials."
            })

        # If user object is not None
        if user:
            login(request, user)
            return redirect("webpage:index")
        else:
            return render(request, "intro/login.html", {
                "message": "Invalid credentials."
            })
    else:
        return render(request, "intro/login.html")
    
def logout_view(request):
    logout(request)
    return render(request, "intro/login.html", {
        "message": "Logged out."
    })

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        email = request.POST["email"]

        print(username, password, password2, email)

        # Check if passwords match
        if password != password2:
            return render(request, "intro/register.html", {
                "error_message": "Passwords must match."
            })
        
        # Check if username is taken
        if User.objects.filter(username=username).exists():
            return render(request, "intro/register.html", {
                "error_message": "Username already taken."
            })
        
        # Check if email is taken
        if User.objects.filter(email=email).exists():
            return render(request, "intro/register.html", {
                "error_message": "Email already taken."
            })
        
        # Create new user
        user = User.objects.create_user(username, email, password)
        user.save()

        if user is None:
            return render(request, "intro/register.html", {
                "error_message": "Something went wrong."
            })

        return render(request, "intro/login.html", {
            "message": "Registered successfully."
        })
    return render(request, "intro/register.html")

def curso(request, curso_id):
    curso = Cursos.objects.get(pk=curso_id)
    user = User.objects.get(pk=request.user.id)
    # Obtener el curso del usuario
    try:
        curso_user = user.cursos.filter(pk=curso_id).first()
        print(curso_user)
    except:
        curso_user = None
    return render(request, "intro/curso.html", {
        "curso": curso,
        "curso_done": curso_user
    })

def cursos_personales(request):
    if not request.user.is_authenticated:
        return redirect("webpage:login")
    return render(request, "intro/curso_personal.html", {
        "user": User.objects.get(pk=request.user.id)
    })