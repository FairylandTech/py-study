from django.db.models.expressions import result

from practice.models import UserInfoModelSimple

class UserInfoServicesimple():
    __models = UserInfoModelSimple()

    @classmethod
    def query_info(cls, data):
        page,size = data.pop("page"),data.pop("size")
        print(f"UserInfoServicesimple-query_info-data:{data}")
        user_info = cls.__models.query(page,size,data)
        print(f"UserInfoServicesimple-query_info-user_info:{user_info}")

        data = []
        print(len(user_info))
        print(type(user_info))
        if len(user_info) != 1:
            for row in user_info:
                for _id,name,account,department,status,create_at,update_at in row:
                    data.append(
                        {
                            "id":_id,
                            "name":name,
                            "account":account,
                            "department":department,
                            "status":status,
                            "create_at":create_at,
                            "update_at":update_at
                        }
                    )
        else:
            data = [
                {
                    "id":user_info.get("id"),
                    "name": user_info.get("name"),
                    "account": user_info.get("account"),
                    "department": user_info.get("department"),
                    "status": user_info.get("status"),
                    "create_at": user_info.get("create_at"),
                    "update_at": user_info.get("update_at")
                }
            ]

        print(f"UserInfoServicesimple-query_info-return-data:{data}")
        return data





    @classmethod
    def updateservice(cls,parms):
        result = cls.__models(parms)
        return result






