from practice.models import UserInfoModelSimple

class UserInfoServicesimple():
    __models = UserInfoModelSimple()

    @classmethod
    def query_info(cls, data):
        page,size = data.pop("page"),data.pop("size")
        print(data)
        user_info = cls.__models.query(page,size,data)
        print(user_info)

        data = []
        if len(user_info) != 1:
            for row in user_info:
                for _id,name,account,department,status,created_at,update_at in row:
                    data.append(
                        {
                            "id":_id,
                            "name":name,
                            "account":account,
                            "department":department,
                            "status":status,
                            "created_at":created_at,
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
                    "created_at": user_info.get("status"),
                    "update_at": user_info.get("update_at")
                }
            ]

        return data