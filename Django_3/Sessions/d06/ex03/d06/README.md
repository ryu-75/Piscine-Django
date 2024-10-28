# Handle permissions

1. python manage.py shell

2. user = User.objects.get(username='username')

3. permission = Permission.objects.get(codename='can_delete_tip')

4. user.user_permissions.add(permission)