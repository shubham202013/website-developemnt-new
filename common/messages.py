api_message = {
    'old_password_wrong': 'Please enter valid old password.',
    'user_not_found': 'User not found.',
    'phone_number_existed': 'Phone Number already existed!!',
    'email_existed': 'Email already existed!!',
    'invalid_credentials': 'Please enter Valid Credentials.',
    'success_logout': 'Successfully Logout',
    'token_required': 'Token required',
    'invalid_token': 'Invalid token',
    'token_expired': 'Token Expired',
    'api_required': 'apikey required',
    'not_authorized': 'You are not authorized',
    'email_forgot_password': 'Check your email to reset password.',
    'password_updated': 'Password successfully changed.',
    'company_name': 'Company already existed!!',
    'inactive_login': 'User is not active',
    "wrong_credentials": "You have entered wrong credentials",
    "login_success": "Successfully Logged in",
    'no_data_fount': 'No data found',
    'update_data': 'Updated successfully',

    'title_already_exist': 'Title Already Exist !',
    'employee_exist_with_this_doc': 'Employee already exist with this document group',

    # Module config
    'name_already_exist': 'Name Already Exist !',
    'key_already_exist': 'Key Already Exist !',
}
response_text: dict = dict()
response_text[200]: str = "Success" # type: ignore
response_text[400]: str = "Bad Request"
response_text[401]: str = "Unauthorized"
response_text[403]: str = "Forbidden"
response_text[404]: str = "Not Found"
response_text[500]: str = "Internal Server Error"
response_text[601]: str = "Data Duplication"
response_text[602]: str = "Could Not Save" # type: ignore
response_text[603]: str = "No data found" # type: ignore
