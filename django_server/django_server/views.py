from django.shortcuts import render, redirect
from django.urls import reverse
from django_tables2 import RequestConfig
from .models import UserInfoModel
from .forms import UserInfoForm
from .tables import UserInfoTable
    
# The view for displaying the table data
# If it is loaded from a form submission, it will also show the last submitted row data
def test_table_session(request):
    entered_row_data = None
    # Check if the session has a last submitted primary key
    if request.session.get('last_submitted_pk'):
        entered_row_data = UserInfoModel.objects.get(pk=request.session['last_submitted_pk'])
        # Wipe out the key after the page is loaded once with it
        request.session['last_submitted_pk'] = None
    context = {
        'table': UserInfoTable(UserInfoModel.objects.all()),
        'entered_data': entered_row_data
    }
    # Configure the table with the request to handle pagination, sorting, etc.
    RequestConfig(request).configure(context['table'])
    return render(request, 'table_data.html', context)

# The home view, which is also the form/data entry page
def home(request):
    # Initialize the form to use
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            # Only save the form to the database if it is valid
            added_instance = form.save()
            # Store the last submitted primary key in the session
            request.session['last_submitted_pk'] = added_instance.pk
            # Redirect to the table data view
            return redirect('/table_data')
    else:
        form = UserInfoForm()
    return render(request, 'home.html', {'form': form})

# Use django's built-in 404 handling to redirect to home page
# This will not work if DEBUG is set to True in settings.py
def bad_request(request, exception):
    return redirect('home')
