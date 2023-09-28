from flask import Blueprint

from ident.lib.validation import validate

from . import models, service

applications_router = Blueprint('applications', __name__, url_prefix='/applications')


@applications_router.post("")
@validate(body=models.CreateApplication)
def create_application(application: models.CreateApplication):
    pass