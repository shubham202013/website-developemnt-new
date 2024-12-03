from v1.ETF.views import ETFSymbolImportResource, ETFSymbolResource
from v1.auth.views import LoginView, LogoutResource, ForgotPasswordResource, \
    ChangePasswordResource, ResetPasswordListResource, SetPasswordListResource
from v1.bhavcopy.views import StoreBhavcopyToDatabaseResource
from v1.chrome_extention_registratioin.views import ChromeExtentionRegistrationResource, VerifyChromeExtentionUserResource
from v1.contact_us.views import ContactUsListResource
from v1.etf_plantation.views import ETFPlantationSymbolImportResource, ETFPlantationSymbolResource
from v1.referral.views import ReferralDetailResource, ReferralListResource
from v1.screener_for_everest.views import MigrateScreenerForEverestResource, ScreenerForEverestResource
from v1.smart_etf_plantation.views import SmartETFPlantationSymbolImportResource, SmartETFPlantationSymbolResource
from v1.users.views import UserListResource


def api_v1_routes(api, path):
    # health check
    # api.add_resource(HealthCheckResource, f'/api/v1/healthcheck')

    # Authentication
    api.add_resource(LoginView, f'{path}/login')
    api.add_resource(LogoutResource, f'{path}/logout')
    api.add_resource(ResetPasswordListResource, f'{path}/reset-password/<string:id>')
    api.add_resource(ForgotPasswordResource, f'{path}/forgot-password')
    api.add_resource(ChangePasswordResource, f'{path}/change-password')
    # api.add_resource(RemoveDataFromRedis, f'{path}/remove-redis-data')
    api.add_resource(SetPasswordListResource, f'{path}/set-password/<string:id>')

    # User APIS
    api.add_resource(UserListResource, f'{path}/user')

    # Referral APIs
    api.add_resource(ReferralListResource, f'{path}/referral')
    api.add_resource(ReferralDetailResource, f'{path}/referral/<string:id>')

    # Bhavcopy
    api.add_resource(StoreBhavcopyToDatabaseResource, f'{path}/bhavcopy')

    #ETF
    api.add_resource(ETFSymbolImportResource, f'{path}/import-etf-symbol')
    api.add_resource(ETFSymbolResource, f'{path}/etf-symbol')

    #Screener For Everest
    api.add_resource(MigrateScreenerForEverestResource, f'{path}/migrate-screener-for-everest')
    api.add_resource(ScreenerForEverestResource, f'{path}/screener-for-everest')
    
    #ETF Plantation
    api.add_resource(ETFPlantationSymbolImportResource, f'{path}/import-etf-symbol-plantation')
    api.add_resource(ETFPlantationSymbolResource, f'{path}/etf-symbol-plantation')
    
    #ETF Plantation
    api.add_resource(SmartETFPlantationSymbolImportResource, f'{path}/import-smart-etf-symbol-plantation')
    api.add_resource(SmartETFPlantationSymbolResource, f'{path}/smart-etf-symbol-plantation')

    #Contact Us
    api.add_resource(ContactUsListResource, f'{path}/contact-us')

    # Chrome Extention Registration
    api.add_resource(ChromeExtentionRegistrationResource, f'{path}/chrome-extention-registration')
    api.add_resource(VerifyChromeExtentionUserResource, f'{path}/chrome-extention-user-verify')

