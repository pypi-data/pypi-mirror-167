from fastapi import APIRouter, Depends, HTTPException, status
from starlette.responses import FileResponse
from system.config import db
from api.show import show_exception
from api.models import ImmMake, ImmCheck, ImmPdfform, ImmWebform, ImmWord, ImmRun
import os
from api import oauth2
from basemodels.user import User

case = db.case

router = APIRouter(
    prefix="/case", tags=["Cases"], responses={404: {"description": "Nof found"}}
)


def permission_check(command: str, user: User):
    user_permissions = user.get("permission")
    if not command in user_permissions and not "all" in user_permissions:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You have no permission for make command.",
        )


@router.post("/make")
async def make(data: ImmMake, current_user: User = Depends(oauth2.get_current_user)):
    permission_check("make", current_user)
    try:
        filename = data.make()
        return FileResponse(filename)
    except Exception as e:
        show_exception(e)


@router.post("/check")
async def check(data: ImmCheck, current_user: User = Depends(oauth2.get_current_user)):
    permission_check("check", current_user)
    try:
        return data.check()
    except Exception as e:
        show_exception(e)


@router.post("/word")
async def word(data: ImmWord, current_user: User = Depends(oauth2.get_current_user)):
    permission_check("word", current_user)
    try:
        filename = data.word()
        return FileResponse(filename)
    except Exception as e:
        show_exception(e)


@router.post("/webform")
async def webform(
    data: ImmWebform, current_user: User = Depends(oauth2.get_current_user)
):
    permission_check("webform", current_user)
    try:
        filename = data.webform()
        return FileResponse(filename)
    except Exception as e:
        show_exception(e)


@router.post("/pdfform")
async def pdfform(
    data: ImmPdfform, current_user: User = Depends(oauth2.get_current_user)
):
    permission_check("pdfform", current_user)
    try:
        filename = data.pdfform()
        return FileResponse(filename)
    except Exception as e:
        show_exception(e)


@router.post("/run")
async def run(data: ImmRun, current_user: User = Depends(oauth2.get_current_user)):
    permission_check("run", current_user)
    try:
        return data.run()
    except Exception as e:
        show_exception(e)
