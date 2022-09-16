#https://petersimpson.dev/blog/trying-out-django-ninja/
from msilib.schema import Media
from typing import List
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from ninja import File, Form, NinjaAPI, Schema, Router
from ninja.files import UploadedFile


from .models import ConjuntoModel

api = NinjaAPI()
router = Router()

class ConjumtoIn(Schema):
    name: str
    email: str
    telephone: str
    #logo: str image: Optional[UploadedFile] = None
    #imagen: str image: Optional[UploadedFile] = None
    adress: str
    about: str
    eslogan: str
    is_active: bool

class ConjuntoUpdate(Schema):
    name: str
    email: str
    telephone: str
    logo: str
    imagen: str
    adress: str
    about: str
    eslogan: str
    is_active: bool

class ConjuntoPartialUpdate(Schema):
    name: str
    email: str
    telephone: str
    logo: str
    imagen: str
    adress: str
    about: str
    eslogan: str
    is_active: bool

class ConjuntoOut(Schema):
    name: str
    email: str
    telephone: str
    logo: str
    imagen: str
    adress: str
    about: str
    eslogan: str
    is_active: bool

@router.get("/listar", response=List[ConjuntoOut], tags=["conjunto"], summary="Listar conjunto", description="API para listar todos los conjuntos")
def list_conjunto(request):
    qs = ConjuntoModel.objects.all()
    return qs

@router.get("/listar/{conjunto_id}", response=ConjuntoOut, tags=["conjunto"], summary="Listar conjunto por id", description="API para listar un unico conjunto por id")
def get_conjunto(request,conjunto_id:int):
    conjuntodata = get_object_or_404(ConjuntoModel,id=conjunto_id)
    return conjuntodata

@router.post("/crear", tags=["conjunto"], summary="Crear conjunto", description="API para crear conjunto")
def create_conjunto(request,payload:ConjumtoIn, Logoimg: UploadedFile = File(...), Img: UploadedFile = File(...)):
    conjuntodata = ConjuntoModel.objects.create(**payload.dict(), logo =Logoimg, imagen=Img)
    return {
        "message": f"Conjunto creado con id: {conjuntodata.id}"
    }

@router.put("/uploadlogo/{conjunto_id}", tags=["conjunto"], summary="Agregar o actualizar logo conjunto", description="API para agregar o actualizar logo conjunto")
def update_logo(request, logoimg: UploadedFile = File(...)):
    data = logoimg.read().decode()
    return {
        'name': logoimg.name, 
        'len': len(data)
    }
    #conjuntodata = get_object_or_404(ConjuntoModel, id=conjunto_id)
    #media = Media.objects.create(conjunto_logo=conjuntodata, logo=logoimg)
    #return {"message": f"Logo agregado o actualizado id: {media.id}"}

@router.api_operation(["PUT", "PATCH"], "/actaulizar/{conjunto_id}", tags=["conjunto"], summary="Actualizar conjunto", description="API para actualizar conjunto")
def update_conjunto(request, conjunto_id: int, payload: ConjuntoPartialUpdate):
    conjuntodata = get_object_or_404(ConjuntoModel, id=conjunto_id)
    for attr, value in payload.dict().items():
        if value:
            setattr(conjuntodata, attr, value)
    conjuntodata.save()
    return {"message": f"Conjunto actualizado con id: {conjuntodata.id}"}

@router.delete("/eliminar/{conjunto_id}", tags=["conjunto"], summary="Eliminar conjunto", description="API para eliminar conjunto")
def delete_conjunto(request, conjunto_id: int):
    conjuntodata = get_object_or_404(ConjuntoModel, id=conjunto_id)
    conjuntodata.delete()
    return {"message": f"Conjunto borrado con id: {conjuntodata.id}"}

"""
======
@router.put("/actualizar/{conjunto_id}", tags=["conjunto"])
def full_update_conjunto(request,conjunto_id:int,payload: ConjuntoUpdate):
    conjuntodata = get_object_or_404(ConjuntoModel, id=conjunto_id)
    for attr,value in payload.dict().items():
        setattr(conjuntodata,attr,value)
    conjuntodata.save()
    return {"message": f"Conjunto actualizado con id: {conjuntodata.id}"}

@router.patch("/patch/{conjunto_id}", tags=["conjunto"])
def partial_update_conjunto(request,conjunto_id:int,payload: ConjuntoUpdate):
    conjuntodata = get_object_or_404(ConjuntoModel, id=conjunto_id)
    for attr,value in payload.dict().items():
        setattr(conjuntodata,attr,value)
    conjuntodata.save()
    return {"message": f"Conjunto updated project id: {conjuntodata.id}"}

@router.post("/crear", tags=["conjunto"], summary="Crear conjunto", description="API para crear conjunto")
def create_conjunto(request,payload:ConjumtoIn,logo: UploadedFile = File(...)):
    conjuntodata = ConjuntoModel.objects.create(**payload.dict())
    return {"message": f"Conjunto creado con id: {conjuntodata.id}"}
======
"""