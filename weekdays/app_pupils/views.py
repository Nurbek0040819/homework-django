from django.shortcuts import render

# Create your views here.
pupils = ['Nurbek Doniyorov', 'Azimov Murodjon', 'Yusufjon Muhammadov', 'Obidjon Yoqubov', 'Sanjarbek Rasulov']
baholar = [25, 33, 35, 34, 38]
def pupils_view(request):
    return render(request, 'pupils/pupil.html', context={'pupils': pupils, 'baholar': baholar})
for pupil in pupils:
    def pupil_view(request):
        return render(request, 'pupils/oquvchi natijasi.html', context={'pupil': pupil})

for baho in baholar:
    def pupil_view(request):
        return render(request, 'pupils/oquvchi natijasi.html', context={'baho': baho})