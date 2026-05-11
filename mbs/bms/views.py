from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
@login_required(login_url='login/')
def books(request):
    if request.method == "POST":
        book_name = request.POST.get('book_name')
        book_description = request.POST.get('book_description')
        book_image = request.FILES.get('book_image')

        Book.objects.create(
            book_name=book_name,
            book_description=book_description,
            book_image=book_image
        )
        return redirect('/')

    queryset = Book.objects.all()
    context = {'books': queryset}
    return render(request, 'books.html', context)


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('/')


def update_book(request, id):
    queryset = Book.objects.get(id=id)

    if request.method == "POST":
        book_name = request.POST.get('book_name')
        book_description = request.POST.get('book_description')
        book_image = request.FILES.get('book_image')

        queryset.book_name = book_name
        queryset.book_description = book_description

        if book_image:
            queryset.book_image = book_image
        queryset.save()
        return redirect('books')
    context = {'book': queryset}
    return render(request, 'updatebooks.html', context)


def login_page(request):

    return render(request, 'login.html')


def logout_page(request):
    return render(request,'login.html')

def register_page(request):
    if request.method == "POST":
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        un = request.POST.get('username')
        em = request.POST.get('email')
        pw = request.POST.get('password')

        # if not fn or not ln or un or not em or not pw:
        #     messages.error(request,"Fill all field")
        #     return redirect('/register/')
        if User.objects.filter(username =un).exists():
            messages.error(request,"Username already exits")
            return redirect('/register/')
        user = User.objects.create_user(username= un,first_name = fn, last_name = ln,email = em,password=pw)
        messages.success(request,"User account is sucessfully created")
        text_content = f'Hi {fn}, Thank you for registering at BksManager.'
        
        html_content = f"""
               <html>
         <body style="margin:0; padding:0; background-color:#f4f6f9; font-family:Arial, Helvetica, sans-serif;">
       
           <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#f4f6f9; padding:30px 0;">
             <tr>
               <td align="center">
       
                 <table width="600" cellpadding="0" cellspacing="0" border="0"
                        style="background:#ffffff; border-radius:12px; overflow:hidden; box-shadow:0 4px 12px rgba(0,0,0,0.08);">
       
                   <!-- Header -->
                   <tr>
                     <td align="center" style="background:linear-gradient(135deg, #3498db, #2ecc71); padding:35px 20px;">
                       <h1 style="margin:0; color:white; font-size:28px;">
                         Welcome to BksManager 🎉
                       </h1>
                       <p style="margin-top:10px; color:#ecf0f1; font-size:15px;">
                         Your account is ready to go
                       </p>
                     </td>
                   </tr>
       
                   <!-- Content -->
                   <tr>
                     <td style="padding:35px 40px; color:#333333; line-height:1.7; font-size:16px;">
       
                       <p style="margin-top:0;">Hi <strong>{fn}</strong>,</p>
       
                       <p>
                         Thank you for registering at <strong>BksManager</strong>.
                         Your account has been created successfully, and you can now log in to access your dashboard and start managing your services.
                       </p>
       
                       <div style="text-align:center; margin:35px 0;">
                         <a href="http://127.0.0.1:8000/login/"
                            style="background-color:#3498db;
                                   color:#ffffff;
                                   text-decoration:none;
                                   padding:14px 28px;
                                   border-radius:8px;
                                   font-size:16px;
                                   font-weight:bold;
                                   display:inline-block;">
                           Login Now
                         </a>
                       </div>
       
                       <p style="font-size:14px; color:#7f8c8d;">
                         If you did not create this account, please ignore this email.
                       </p>
       
                     </td>
                   </tr>
       
                   <!-- Footer -->
                   <tr>
                     <td align="center"
                         style="background:#fafafa; padding:20px; font-size:13px; color:#95a5a6; border-top:1px solid #eeeeee;">
                       © 2026 BksManager. All rights reserved.
                     </td>
                   </tr>
       
                 </table>
       
               </td>
             </tr>
           </table>
       
         </body>
       </html>
               """
        return redirect('/login')
    return render(request,'register.html')