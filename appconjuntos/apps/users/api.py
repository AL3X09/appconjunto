#https://petersimpson.dev/blog/trying-out-django-ninja/
from typing import List
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from ninja import File, Form, NinjaAPI, Schema, Router
from ninja.files import UploadedFile

from .models import User

api = NinjaAPI()
router = Router()

class UserIn(Schema):
    username: str
    is_active: bool
    is_staff: bool

class UserUpdate(Schema):
    username: str
    is_active: bool
    is_staff: bool
    is_superuser: bool

class UserPartialUpdate(Schema):
    username: str
    is_active: bool
    is_staff: bool
    is_superuser: bool

class UserOut(Schema):
    id: int
    username: str
    is_active: bool
    is_staff: bool
    is_superuser: bool

@router.get("/user", response=List[UserOut], tags=["usuarios"])
def list_user(request):
    qs = User.objects.all()
    return qs

@router.get("/user/{user_id}",response=UserOut, tags=["usuarios"])
def get_user(request,user_id:int):
    userdata = get_object_or_404(User,id=user_id)
    return userdata

@router.post("/user", tags=["usuarios"])
def create_user(request,payload:UserIn):
    userdata = User.objects.create(**payload.dict())
    return {"message": f"successfully created user id: {userdata.id}"}

@router.put("/user/{user_id}", tags=["usuarios"])
def full_update_user(request,user_id:int,payload: UserUpdate):
    userdata = get_object_or_404(User, id=user_id)
    for attr,value in payload.dict().items():
        setattr(userdata,attr,value)
    userdata.save()
    return {"message": f"successfully updated project id: {userdata.id}"}

@router.patch("/user/{user_id}", tags=["usuarios"])
def partial_update_user(request,user_id:int,payload: UserUpdate):
    userdata = get_object_or_404(User, id=user_id)
    for attr,value in payload.dict().items():
        setattr(userdata,attr,value)
    userdata.save()
    return {"message": f"successfully updated project id: {userdata.id}"}

@router.api_operation(["PUT", "PATCH"], "/user/{user_id}", tags=["usuarios"])
def update_user(request, user_id: int, payload: UserPartialUpdate):
    userdata = get_object_or_404(User, id=user_id)
    for attr, value in payload.dict().items():
        if value:
            setattr(userdata, attr, value)
    userdata.save()
    return {"message": f"successfully updated project id: {userdata.id}"}

@router.delete("/user/{user_id}", tags=["usuarios"])
def delete_user(request, user_id: int):
    userdata = get_object_or_404(User, id=user_id)
    userdata.delete()
    return {"message": f"successfully deleted project id: {userdata.id}"}