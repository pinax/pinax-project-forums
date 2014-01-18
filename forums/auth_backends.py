class PermissionBackend(object):

    supports_object_permissions = True
    supports_anonymous_user = True

    def authenticate(self, **kwargs):
        # always return a None user
        return None

    def has_perm(self, user, perm, obj=None):
        if user.is_anonymous():
            return False
        if perm in ["agora.add_forumthread", "agora.add_forumreply"]:
            return True
