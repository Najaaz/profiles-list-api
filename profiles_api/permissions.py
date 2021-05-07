from rest_framework import permissions



class UpdateOwnProfile(permissions.BasePermission):
    # Allow users to edit their own profile

    def has_object_permission(self, request, view, obj):
        # Check if the user is trying to edit his own profile
        if request.method in permissions.SAFE_METHODS: # If the method (eg:HTTP) is requested then it is stored in the SAFE_METHODS and is allowed
            return True
        
        return obj.id == request.user.id