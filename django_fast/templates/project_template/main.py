from myframework import app, route
from django_orm_setup import setup_django
setup_django()

@route("/")
async def index(request):
    return {"message": "Welcome to your new app!"}
