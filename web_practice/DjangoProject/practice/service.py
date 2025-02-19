

class UserInfoService():

    def query_info(self, query):
        user_name = query.get('user_name')
        usser_account = query.get('usser_account')
        if user_name and usser_account:
            user_sql = 'select * from user_info where user_name = %s and usser_account = %s'.format(user_name, usser_account)
            user_info =

            user_name = user_info.get('user_name')
            user_account = user_info.get('user_info')
            department = user_info.get('department')
            enabled_staus = user_info.get('enabled_status')
            register_time = user_info.get('register_time')
            update_time = user_info.get('update_time')

            responses = {
                'user_name': user_name,
                'user_account': user_account,
                'department': department,
                'enabled_status': enabled_staus,
                'register_time': register_time,
                'update_time': update_time
            }

        return query