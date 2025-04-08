from dj_rest_auth.views import UserDetailsView as BaseUserDetailsView
from djangorestframework_camel_case.parser import CamelCaseMultiPartParser

class UserDetailsView(BaseUserDetailsView):
    parser_classes = [CamelCaseMultiPartParser]
