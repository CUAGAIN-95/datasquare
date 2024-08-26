'''데이터베이스 페이지 관리 라우터 모듈'''


from datetime import datetime

from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.crud.noti import get_notification_count
from app.schemas.user_schema import User
from app.utils.get_current_user import get_current_user


router = APIRouter()
templates = Jinja2Templates(directory='app/templates')


@router.get('/databases', name='databases')
async def databases(
    request: Request,
    current_user: User = Depends(get_current_user)
):
    '''데이터베이스 페이지 함수'''

    return templates.TemplateResponse('pages/success.html', {
        'request': request,
        'company_name': 'Your Company',
        'current_year': datetime.now().year,
        'notification_count': get_notification_count(current_user.profile_id)
    })
