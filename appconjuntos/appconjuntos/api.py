from ninja import NinjaAPI
from apps.users.api import router as users_router
from apps.conjunto.api import router as conjunto_router

#api = NinjaAPI()

api = NinjaAPI(
    version='1.0.0',
    title="Conjunto API",
    description="API que controla la aplicación para la APP conjunto",
    urls_namespace="conjunto",
)

api.add_router("/users/", users_router)
api.add_router("/conjunto/", conjunto_router)