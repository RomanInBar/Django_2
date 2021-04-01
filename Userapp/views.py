from django.conf import settings
from django.contrib import auth
from django.shortcuts import HttpResponseRedirect, render, HttpResponse
from django.urls import reverse
from django.core.mail import send_mail

from Userapp.forms import ShopUserEditForm, ShopUserLoginForm, ShopUserRegisterForm

from Userapp.models import ShopUser


def send_verify_mail(user):
    verify_link = reverse("user:verify", args=[user.email, user.activation_key])
    title = f"Подтверждение учетной записи {user.username}"
    message = f"Для подтверждения учетной записи {user.username} на портале \
    {settings.DOMAIN_NAME} перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}"

    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = ShopUser.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request, "Userapp/verification.html")
        print(f"error activation user: {user}")
        return render(request, "Userapp/verification.html")
    except Exception as e:
        print(f"error activation user: {e.args}")
        return HttpResponseRedirect(reverse("main"))


def login(request):
    title = "вход"

    login_form = ShopUserLoginForm(data=request.POST or None)
    next_page = request.GET["next"] if "next" in request.GET.keys() else ""

    if request.method == "POST" and login_form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if "next_page" in request.POST.keys():
                return HttpResponseRedirect(request.POST["next_page"])
            return HttpResponseRedirect(reverse("main"))

    content = {"title": title, "login_form": login_form, "next_page": next_page}
    return render(request, "Userapp/login.html", content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("main"))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("main"))


def register(request):
    title = "регистрация"
    error = ''
    if request.method == "POST":
        register_form = ShopUserRegisterForm(request.POST, request.FILES)      
        if register_form.is_valid():
            user = register_form.save()
            if send_verify_mail(user):
                print("сообщение подтверждения отправлено")
                return HttpResponseRedirect(reverse("user:login"))
            else:
                print("ошибка отправки сообщения")
                return HttpResponseRedirect(reverse("user:login"))
        else:
            error = 'Error, not valid form'   
    register_form = ShopUserRegisterForm()
    content = {"title": title, "register_form": register_form, 'error': error}
    return render(request, "Userapp/register.html", content)


def edit(request):
    title = "редактировать"

    if request.method == "POST":
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("user:edit"))

    edit_form = ShopUserEditForm(instance=request.user)
    content = {"title": title, "edit_form": edit_form, "media_url": settings.MEDIA_URL}
    return render(request, "Userapp/edit.html", content)
