from django.shortcuts import render
# from django.http import HttpResponse

products = [
    {
        "img": "https://static.beautytocare.com/media/catalog/product/n/i/nivea-men-protect-care-deep-cleaning-face-wash-100ml_1.jpg",
        "name": "Nivea men",
        "price": "25.000 kip",
        "description":"Electric Windproof Metal Lighter Double Arc Flameless Plasma Rechargeable USB Lighter LED Power Display Touch Sensor Lighters"

    },
     {
        "img": "https://www.yankodesign.com/images/design_news/2021/08/mens-lifestyle-ds/the_top_10_mens_lifestyle_design_02.jpg",
        "name": "Razor",
        "price": "150.000 kip",
        "description":"Electric Windproof Metal Lighter Double Arc Flameless Plasma Rechargeable USB Lighter LED Power Display Touch Sensor Lighters"

    },
     {
        "img": "https://m.media-amazon.com/images/I/51gKuehPWdL._AC_UF1000,1000_QL80_.jpg",
        "name": "Notraful men",
        "price": "50.000 kip",
        "description":"Electric Windproof Metal Lighter Double Arc Flameless Plasma Rechargeable USB Lighter LED Power Display Touch Sensor Lighters"

    },
     {
        "img": "https://www.particleformen.com/wp-content/uploads/2023/12/Face-Cream-Product-300x300-11.png",
        "name": "Particle",
        "price": "100.000 kip",
        "description":"Electric Windproof Metal Lighter Double Arc Flameless Plasma Rechargeable USB Lighter LED Power Display Touch Sensor Lighters"
    },
]
# Global variable to track result (for simplicity, not recommended for production)
result = 0  # Ensure this is defined outside the view


def product(request):
    global result  # Use the global variable
    print(f"Initial result: {result}")  # Debugging: Check initial value

    if request.method == "POST":
        print(f"POST data: {request.POST}")  # Debugging: Check what is in POST data

        if "plus" in request.POST:
            result += 1
        elif "minus" in request.POST:
            result -= 1

        result = max(result, 0)  # Prevent negative values
        print(f"Updated result: {result}")  # Debugging: Check updated value

        # Redirect to prevent form resubmission
    context = {
        "products": products,
        "result": result,  # Pass the result to the template
    }
    return render(request, "product.html", context)


def index(request):
#  return HttpResponse("saichang")

 return render(request,"index.html")

def men(request):
 return render(request,"men.html")

def sale(request):
 return render(request,"sale.html")

def sport(request):
 return render(request,"sport.html")

def women(request):
 return render(request,"women.html")
def login(request):
 return render(request,"login.html")