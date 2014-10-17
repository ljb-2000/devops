#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import stat


class KeyStorage(FileSystemStorage):
    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL, file_permissions_mode=stat.S_IREAD):
        super(KeyStorage, self).__init__(location, base_url, file_permissions_mode)

    def _save(self, name, content):
        # os.chmod(name, stat.S_IREAD)
        return super(KeyStorage, self)._save(name, content)
