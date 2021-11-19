# Project_4_Backend

#Uploading Images

-pip install Pillow
*this allows us to use media uploads

-Add Media URL(file path) to setting.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

*This says when it gets in image it will be stored in a folder called 'media'

-Add Media URL to Django URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('main.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 DEBUG must be set to True

import os (if needed)
from django.conf import settings (if needed)
from django.conf.urls.static import static (if needed)

**TODO: CREATE FORMS THAT TAKE IMAGE UPLOAD
----------------------------------------------------------------------
##User Auth
This article was the guide to create the front end portion of User Auth.
https://www.freecodecamp.org/news/how-to-persist-a-logged-in-user-in-react/

-When a user logs in, check credentials against DB
-If login is successful, set 'online' property of that User to True.
-store logged-in user to local storage. This will be used to conditionally render the current user's page.
