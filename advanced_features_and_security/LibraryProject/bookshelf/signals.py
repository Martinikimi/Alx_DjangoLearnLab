from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.apps import apps


@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    if sender.name == "bookshelf":
        Book = apps.get_model("bookshelf", "Book")

        # Fetch permissions
        perms = Permission.objects.filter(content_type__app_label="bookshelf", content_type__model="book")

        # Create groups
        editors, _ = Group.objects.get_or_create(name="Editors")
        viewers, _ = Group.objects.get_or_create(name="Viewers")
        admins, _ = Group.objects.get_or_create(name="Admins")

        for perm in perms:
            if perm.codename in ["can_edit", "can_create"]:
                editors.permissions.add(perm)
            if perm.codename == "can_view":
                viewers.permissions.add(perm)
            if perm.codename in ["can_edit", "can_create", "can_delete", "can_view"]:
                admins.permissions.add(perm)
