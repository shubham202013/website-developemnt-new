# from threading import Thread

# from common.constants import MODULE_ACTION_ARRAY, APP_MODULE, CLIENT_PERMS_MODULES
# from v1.users.constants import USER_ROLE_CHOICES


# class MyThread(Thread):

#     def create_role(self, company_id):
#         for action in MODULE_ACTION_ARRAY:
#             for module in APP_MODULE:
#                 for role in dict(USER_ROLE_CHOICES):
#                     if module in ["report", "dashboard"] and action != "list":
#                         print("report and dashboard module")
#                     else:
#                         obj = {
#                             "company_id": company_id,
#                             "user": role,
#                             "action": action,
#                             "module": module
#                         }

#                         if role == 3:
#                             obj.update({"permission": True})
#                         elif role == 4 and action == "list" and module in CLIENT_PERMS_MODULES:
#                             obj.update({"permission": True})
#                         else:
#                             obj.update({"permission": False})
#                         # obj.save()
#         print("Role created")


# def create_role(company_id):
#     t1 = MyThread()
#     t1.create_role(company_id)
#     t1.start()
