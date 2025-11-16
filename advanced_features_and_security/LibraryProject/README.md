<!-- @format -->

LibraryProject

This project uses custom permissions and user groups to control access to specific actions. Each permission (such as viewing, creating, editing, or deleting) is defined in the CustomUser model and assigned to groups like Viewers, Editors, and Admins. Groups determine what each type of user can do within the system—for example, Viewers can only access basic information, while Editors can modify data, and Admins have full control. These permissions are enforced in the views using Django’s @permission_required decorator, ensuring that only authorized users can access protected features.
