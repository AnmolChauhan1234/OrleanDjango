from django.shortcuts import render

def healthcare_dashboard(request):
    submitted_data = None
    # Pass a list of ages from 1 to 100 to the template
    age_range = list(range(1, 101))

    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        file = request.FILES.get('file')

        # Assuming you process the file and data here
        submitted_data = {
            'name': name,
            'age': age,
            'file': file
        }

    return render(request, 'dashboard/index.html', {'submitted_data': submitted_data, 'age_range': age_range})
