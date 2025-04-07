from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .form import question_paper_form
from app.models import Subject_data
import pandas as pd

def index(request):
    return render(request, "index.html")

def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Log In Successful...!")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid User...!")
            return redirect("log_in")

    return render(request, "log_in.html")


def register(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username:
            messages.error(request, "Username must be set")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists...!")
            return redirect("register")
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request, "Registration Successful...!")
            return redirect("log_in")

    return render(request, "register.html")


@login_required(login_url="log_in")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
    context = {
        'fname': request.user.first_name,
        'form': question_paper_form(),
    }

    if request.method == "POST":
        form = question_paper_form(request.POST, request.FILES)
        if form.is_valid():
            scheme = form.cleaned_data['scheme']
            selected_test = form.cleaned_data['test']
            college_name = form.cleaned_data['college_name']
            branch_name = form.cleaned_data['branch_name']
            semester = form.cleaned_data['semester']
            subject_name = form.cleaned_data['subject_name']
            year = form.cleaned_data['year']
            faculty = form.cleaned_data['faculty']
            date = form.cleaned_data['date']
            qb = form.cleaned_data['qb']

            reader = pd.read_csv(qb)

            required_columns = {'question', 'marks', 'blooms_level'}
            if not required_columns.issubset(reader.columns):
                messages.error(request, "Uploaded file must contain 'question', 'marks', and 'blooms_level' columns.")
                return redirect("dashboard")

            reader = reader[reader['marks'].isin([2, 4, 6])]
            counts = reader['marks'].value_counts()
            print("Counts per marks category:", counts)

            try:
                if scheme == "I-scheme":
                    selected_data_6 = reader[reader['marks'] == 6].sample(n=min(4, counts.get(6, 0)), random_state=24)
                    selected_data_4 = reader[reader['marks'] == 4].sample(n=min(4, counts.get(4, 0)), random_state=24)
                    selected_data_2 = reader[reader['marks'] == 2].sample(n=min(4, counts.get(2, 0)), random_state=24)
                else:
                    selected_data_6 = reader[reader['marks'] == 6].sample(n=min(5, counts.get(6, 0)), random_state=24)
                    selected_data_4 = reader[reader['marks'] == 4].sample(n=min(4, counts.get(4, 0)), random_state=24)
                    selected_data_2 = reader[reader['marks'] == 2].sample(n=min(3, counts.get(2, 0)), random_state=24)

                selected_data = pd.concat([selected_data_6, selected_data_4, selected_data_2], axis=0)

                # Ensure at least 16 questions are available
                selected_data = ensure_16_questions(selected_data)

                selected_list = selected_data[['question', 'marks']].values.tolist()
                blooms_levels = selected_data['blooms_level'].tolist()

                qus = []
                [qus.extend([str(q), str(m)]) for q, m in selected_list]

                # Ensure exactly 16 questions are present
                while len(qus) < 32:
                    qus.append('N/A')
                    qus.append('0')

                while len(blooms_levels) < 16:
                    blooms_levels.append('N/A')

                # Replace empty strings with appropriate values
                for i in range(0, len(qus), 2):
                    if qus[i] == '':
                        qus[i] = 'N/A'
                for i in range(1, len(qus), 2):
                    if qus[i] == '':
                        qus[i] = '0'
                blooms_levels = [bl if bl else 'N/A' for bl in blooms_levels]

                # Debugging
                print(f"Final Questions List (16 expected): {qus}")
                print(f"Final Blooms Levels List (16 expected): {blooms_levels}")
                print(f"q15: {qus[28]}, m15: {qus[29]}, bl15: {blooms_levels[14]}")
                print(f"q16: {qus[30]}, m16: {qus[31]}, bl16: {blooms_levels[15]}")

                subject_data = Subject_data(
                    scheme=scheme,
                    college_name=college_name,
                    branch_name=branch_name,
                    semester=semester,
                    subject_name=subject_name,
                    year=year,
                    faculty=faculty,
                    qb=qb,
                    q1=qus[0], q2=qus[2], q3=qus[4], q4=qus[6], q5=qus[8],
                    q6=qus[10], q7=qus[12], q8=qus[14], q9=qus[16], q10=qus[18],
                    q11=qus[20], q12=qus[22], q13=qus[24], q14=qus[26],
                    q15=qus[28], q16=qus[30],
                    m1=qus[1], m2=qus[3], m3=qus[5], m4=qus[7], m5=qus[9],
                    m6=qus[11], m7=qus[13], m8=qus[15], m9=qus[17], m10=qus[19],
                    m11=qus[21], m12=qus[23], m13=qus[25], m14=qus[27],
                    m15=qus[29], m16=qus[31],
                    bl1=blooms_levels[0], bl2=blooms_levels[1], bl3=blooms_levels[2], bl4=blooms_levels[3],
                    bl5=blooms_levels[4], bl6=blooms_levels[5], bl7=blooms_levels[6], bl8=blooms_levels[7],
                    bl9=blooms_levels[8], bl10=blooms_levels[9], bl11=blooms_levels[10], bl12=blooms_levels[11],
                    bl13=blooms_levels[12], bl14=blooms_levels[13],
                    bl15=blooms_levels[14], bl16=blooms_levels[15],
                    test=selected_test,  # Add this line to save the selected test
                    date=date
                )
                subject_data.save()

                return redirect("result")
            except ValueError as e:
                messages.error(request, f"Error selecting questions: {e}")
                return redirect("dashboard")

    return render(request, "dashboard.html", context)

def ensure_16_questions(selected_data):
    while len(selected_data) < 16:
        additional_data = selected_data.sample(n=(16 - len(selected_data)), replace=True, random_state=24)
        selected_data = pd.concat([selected_data, additional_data], ignore_index=True)
    return selected_data

@login_required(login_url="log_in")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def result(request):
    subject_data = Subject_data.objects.last()
    template_name = "ischeme_paper.html" if subject_data.scheme == "I-scheme" else "kscheme_paper.html"

    context = {
        'fname': request.user.first_name,
        'subject_data': subject_data,
        'selected_test': subject_data.test,  # Pass the selected test to the template
        'selected_scheme': subject_data.scheme
    }
    
    return render(request, template_name, context)

def log_out(request):
    logout(request)
    messages.success(request, "Logged out successfully...!")
    return redirect("log_in")
