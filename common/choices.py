USER_TYPE_SUPER_ADMIN = 0
USER_TYPE_COMPANY_ADMIN = 1
USER_TYPE_TEAM = 2
USER_TYPE_CLIENT = 3
USER_TYPE_EMPLOYEE = 4
USER_TYPE_CHOICES = (
    (USER_TYPE_SUPER_ADMIN, "Super Admin"),
    (USER_TYPE_COMPANY_ADMIN, "Company Admin"),
    (USER_TYPE_TEAM, "Team"),
    (USER_TYPE_CLIENT, "Client"),
    (USER_TYPE_EMPLOYEE, "Employee"),
)

PROJECT_TYPE_FIXED = 1
PROJECT_TYPE_DEDICATED = 2
PROJECT_TYPE_HOURLY = 3

PROJECT_TYPE = ((PROJECT_TYPE_FIXED, "Fixed"), (PROJECT_TYPE_DEDICATED, "Dedicated"), (PROJECT_TYPE_HOURLY, "Hourly"))

PROJECT_MANAGE_YES = 1
PROJECT_MANAGE_NO = 2
PROJECT_MANAGE = (
    (PROJECT_MANAGE_YES, "Yes"),
    (PROJECT_MANAGE_NO, "No"),
)

# PROJECT_STATUS
PROJECT_STATUS_ACTIVE = 1
PROJECT_STATUS_ON_HOLD = 2
PROJECT_STATUS_COMPLETED = 3
PROJECT_STATUS = (
    (PROJECT_STATUS_ACTIVE, "Active"),
    (PROJECT_STATUS_ON_HOLD, "On Hold"),
    (PROJECT_STATUS_COMPLETED, "Completed"),
)

# PROJECT_CONTRACT_STATUS
PROJECT_CONTRACT_STATUS_ACTIVE = 1
PROJECT_CONTRACT_STATUS_INACTIVE = 2
PROJECT_CONTRACT_STATUS__COMPLETED = 3
PROJECT_CONTRACT_STATUS = (
    (PROJECT_CONTRACT_STATUS_ACTIVE, "Active"),
    (PROJECT_CONTRACT_STATUS_INACTIVE, "Inactive"),
    (PROJECT_CONTRACT_STATUS__COMPLETED, "Completed"),
)

# PROJECT_CONTRACT_STATUS_NEW
PROJECT_CONTRACT_STATUS_ACTIVE = 1
PROJECT_CONTRACT_STATUS_HOLD = 2
PROJECT_CONTRACT_STATUS__COMPLETED = 3
PROJECT_CONTRACT_STATUS__Cancelled = 4
PROJECT_CONTRACT_STATUS_NEW = (
    (PROJECT_CONTRACT_STATUS_ACTIVE, "Active"),
    (PROJECT_CONTRACT_STATUS_HOLD, "Hold"),
    (PROJECT_CONTRACT_STATUS__COMPLETED, "Completed"),
    (PROJECT_CONTRACT_STATUS__Cancelled, "Cancelled"),
)

# RELEASE_STATUS
RELEASE_STATUS_IN_PROGRESS = "2"
RELEASE_STATUS_OPEN = "1"
RELEASE_STATUS_COMPLETED = "3"
RELEASE_STATUS = (
    (RELEASE_STATUS_IN_PROGRESS, "UnReleased"),
    (RELEASE_STATUS_OPEN, "Released"),
    (RELEASE_STATUS_COMPLETED, "Archived"),
)
# TASK LIST STATUS
TASK_LIST_STATUS_PENDING = "1"
TASK_LIST_STATUS_OPEN = "2"
TASK_LIST_STATUS_COMPLETED = "3"
TASK_LIST_STATUS = (
    (TASK_LIST_STATUS_PENDING, "Pending"),
    (TASK_LIST_STATUS_OPEN, "Start"),
    (TASK_LIST_STATUS_COMPLETED, "Complete"),
)

# TASK_STATUS
TASK_STATUS_OPEN = 1
TASK_STATUS_IN_PROGRESS = 2
TASK_STATUS_COMPLETED = 3
TASK_STATUS_HOLD = 4
TASK_STATUS = (
    (TASK_STATUS_OPEN, "Open"),
    (TASK_STATUS_IN_PROGRESS, "In Progress"),
    (TASK_STATUS_COMPLETED, "Completed"),
    (TASK_STATUS_HOLD, "Hold"),
)
# TASK_TYPES
TASK_TYPES_BACKLOGS = 1
TASK_TYPES_TASKS = 2
TASK_TYPES_BUGS = 3
TASK_TYPES_BACKLOGS_BUGS = 4
TASK_TYPES = (
    (TASK_TYPES_BACKLOGS, "Backlogs"),
    (TASK_TYPES_TASKS, "Tasks"),
    (TASK_TYPES_BUGS, "BUGS"),
    (TASK_TYPES_BACKLOGS_BUGS, "Backlogs BUGS"),
)

LANGUAGE_CHOICES = (("en", "English"),)

DATE_FORMAT_CHOICES = (
    (1, "dd/MM/yyyy"),
    (2, "dd-MM-yyyy"),
)

TIME_FORMAT_CHOICES = (
    (1, "h:i A"),
    (2, "H:M:S"),
)

WORKING_DAYS = [
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
    (6, "Saturday"),
    (7, "Sunday"),
]

CURRENCY_CHOICES = (
    ("INR", "&#8377;"),
    ("USD", "&#36;")
)

TIMEZONE_CHOICES = (
    ("Africa/Cairo", "(GMT+02:00) Cairo"),
    ("Africa/Casablanca", "(GMT) Casablanca"),
    ("Africa/Harare", "(GMT+02:00) Harare"),
    ("Africa/Monrovia", "(GMT) Monrovia"),
    ("Africa/Nairobi", "(GMT+03:00) Nairobi"),
    ("America/Bogota", "(GMT-05:00) Bogota"),
    ("America/Buenos_Aires", "(GMT-03:00) Buenos Aires"),
    ("America/Caracas", "(GMT-04:30) Caracas"),
    ("America/Chihuahua", "(GMT-07:00) Chihuahua"),
    ("America/La_Paz", "(GMT-04:00) La Paz"),
    ("America/Lima", "(GMT-05:00) Lima"),
    ("America/Mazatlan", "(GMT-07:00) Mazatlan"),
    ("America/Mexico_City", "(GMT-06:00) Mexico City"),
    ("America/Monterrey", "(GMT-06:00) Monterrey"),
    ("America/Santiago", "(GMT-04:00) Santiago"),
    ("America/Tijuana", "(GMT-08:00) Tijuana"),
    ("Asia/Almaty", "(GMT+06:00) Almaty"),
    ("Asia/Baghdad", "(GMT+03:00) Baghdad"),
    ("Asia/Baku", "(GMT+04:00) Baku"),
    ("Asia/Bangkok", "(GMT+07:00) Bangkok"),
    ("Asia/Chongqing", "(GMT+08:00) Chongqing"),
    ("Asia/Dhaka", "(GMT+06:00) Dhaka"),
    ("Asia/Hong_Kong", "(GMT+08:00) Hong Kong"),
    ("Asia/Irkutsk", "(GMT+09:00) Irkutsk"),
    ("Asia/Jakarta", "(GMT+07:00) Jakarta"),
    ("Asia/Jerusalem", "(GMT+02:00) Jerusalem"),
    ("Asia/Kabul", "(GMT+04:30) Kabul"),
    ("Asia/Karachi", "(GMT+05:00) Karachi"),
    ("Asia/Kathmandu", "(GMT+05:45) Kathmandu"),
    ("Asia/Kolkata", "(GMT+05:30) Kolkata"),
    ("Asia/Krasnoyarsk", "(GMT+08:00) Krasnoyarsk"),
    ("Asia/Kuala_Lumpur", "(GMT+08:00) Kuala Lumpur"),
    ("Asia/Kuwait", "(GMT+03:00) Kuwait"),
    ("Asia/Magadan", "(GMT+12:00) Magadan"),
    ("Asia/Muscat", "(GMT+04:00) Muscat"),
    ("Asia/Novosibirsk", "(GMT+07:00) Novosibirsk"),
    ("Asia/Riyadh", "(GMT+03:00) Riyadh"),
    ("Asia/Seoul", "(GMT+09:00) Seoul"),
    ("Asia/Singapore", "(GMT+08:00) Singapore"),
    ("Asia/Taipei", "(GMT+08:00) Taipei"),
    ("Asia/Tashkent", "(GMT+05:00) Tashkent"),
    ("Asia/Tbilisi", "(GMT+04:00) Tbilisi"),
    ("Asia/Tehran", "(GMT+03:30) Tehran"),
    ("Asia/Tokyo", "(GMT+09:00) Tokyo"),
    ("Asia/Ulaanbaatar", "(GMT+08:00) Ulaan Bataar"),
    ("Asia/Urumqi", "(GMT+08:00) Urumqi"),
    ("Asia/Vladivostok", "(GMT+11:00) Vladivostok"),
    ("Asia/Yakutsk", "(GMT+10:00) Yakutsk"),
    ("Asia/Yekaterinburg", "(GMT+06:00) Ekaterinburg"),
    ("Asia/Yerevan", "(GMT+04:00) Yerevan"),
    ("Atlantic/Azores", "(GMT-01:00) Azores"),
    ("Atlantic/Cape_Verde", "(GMT-01:00) Cape Verde Is."),
    ("Atlantic/Stanley", "(GMT-02:00) Stanley"),
    ("Australia/Adelaide", "(GMT+09:30) Adelaide"),
    ("Australia/Brisbane", "(GMT+10:00) Brisbane"),
    ("Australia/Canberra", "(GMT+10:00) Canberra"),
    ("Australia/Darwin", "(GMT+09:30) Darwin"),
    ("Australia/Hobart", "(GMT+10:00) Hobart"),
    ("Australia/Melbourne", "(GMT+10:00) Melbourne"),
    ("Australia/Perth", "(GMT+08:00) Perth"),
    ("Australia/Sydney", "(GMT+10:00) Sydney"),
    ("Canada/Atlantic", "(GMT-04:00) Atlantic Time (Canada)"),
    ("Canada/Newfoundland", "(GMT-03:30) Newfoundland"),
    ("Canada/Saskatchewan", "(GMT-06:00) Saskatchewan"),
    ("Europe/Amsterdam", "(GMT+01:00) Amsterdam"),
    ("Europe/Athens", "(GMT+02:00) Athens"),
    ("Europe/Belgrade", "(GMT+01:00) Belgrade"),
    ("Europe/Berlin", "(GMT+01:00) Berlin"),
    ("Europe/Bratislava", "(GMT+01:00) Bratislava"),
    ("Europe/Brussels", "(GMT+01:00) Brussels"),
    ("Europe/Bucharest", "(GMT+02:00) Bucharest"),
    ("Europe/Budapest", "(GMT+01:00) Budapest"),
    ("Europe/Copenhagen", "(GMT+01:00) Copenhagen"),
    ("Europe/Dublin", "(GMT) Dublin"),
    ("Europe/Helsinki", "(GMT+02:00) Helsinki"),
    ("Europe/Istanbul", "(GMT+02:00) Istanbul"),
    ("Europe/Kiev", "(GMT+02:00) Kyiv"),
    ("Europe/Lisbon", "(GMT) Lisbon"),
    ("Europe/Ljubljana", "(GMT+01:00) Ljubljana"),
    ("Europe/London", "(GMT) London"),
    ("Europe/Madrid", "(GMT+01:00) Madrid"),
    ("Europe/Minsk", "(GMT+02:00) Minsk"),
    ("Europe/Moscow", "(GMT+03:00) Moscow"),
    ("Europe/Paris", "(GMT+01:00) Paris"),
    ("Europe/Prague", "(GMT+01:00) Prague"),
    ("Europe/Riga", "(GMT+02:00) Riga"),
    ("Europe/Rome", "(GMT+01:00) Rome"),
    ("Europe/Sarajevo", "(GMT+01:00) Sarajevo"),
    ("Europe/Skopje", "(GMT+01:00) Skopje"),
    ("Europe/Sofia", "(GMT+02:00) Sofia"),
    ("Europe/Stockholm", "(GMT+01:00) Stockholm"),
    ("Europe/Tallinn", "(GMT+02:00) Tallinn"),
    ("Europe/Vienna", "(GMT+01:00) Vienna"),
    ("Europe/Vilnius", "(GMT+02:00) Vilnius"),
    ("Europe/Volgograd", "(GMT+04:00) Volgograd"),
    ("Europe/Warsaw", "(GMT+01:00) Warsaw"),
    ("Europe/Zagreb", "(GMT+01:00) Zagreb"),
    ("Greenland", "(GMT-03:00) Greenland"),
    ("Pacific/Auckland", "(GMT+12:00) Auckland"),
    ("Pacific/Fiji", "(GMT+12:00) Fiji"),
    ("Pacific/Guam", "(GMT+10:00) Guam"),
    ("Pacific/Midway", "(GMT-11:00) Midway Island"),
    ("Pacific/Port_Moresby", "(GMT+10:00) Port Moresby"),
    ("US/Alaska", "(GMT-09:00) Alaska"),
    ("US/Arizona", "(GMT-07:00) Arizona"),
    ("US/Central", "(GMT-06:00) Central Time (US &amp; Canada)"),
    ("US/East-Indiana", "(GMT-05:00) Indiana (East)"),
    ("US/Eastern", "(GMT-05:00) Eastern Time (US &amp; Canada)"),
    ("US/Hawaii", "(GMT-10:00) Hawaii"),
    ("US/Mountain", "(GMT-07:00) Mountain Time (US &amp; Canada)"),
    ("US/Pacific", "(GMT-08:00) Pacific Time (US &amp; Canada)"),
    ("US/Samoa", "(GMT-11:00) Samoa"),
)

TIME_INTERVAL = (
    ("W", "Week"),
    ("M", "Month"),
    ("Y", "Year"),
)

IS_BILLABLE = (
    (1, "Yes"),
    (2, "No"),
)

# USER_ROLE_CHOICES
ROLE_EMPLOYEE = 1
ROLE_MANAGER = 2
ROLE_ADMIN = 3
ROLE_CLIENT = 4
USER_ROLE_CHOICES = (
    (ROLE_EMPLOYEE, "Employee"),
    (ROLE_MANAGER, "Manager"),
    (ROLE_ADMIN, "Company Admin"),
    (ROLE_CLIENT, "Client"),
)

# PEOPLE_SELECT_CHOICES
PEOPLE_ADD = 1
PEOPLE_REMOVE = 2
PEOPLE_SELECT_CHOICES = (
    (PEOPLE_ADD, 1),
    (PEOPLE_REMOVE, 2),
)

DOCUMENT_TYPE_CHOICES = (
    (1, "Release"),
    (2, "Task List"),
    (3, "Task"),
    (4, "Message"),
    (5, "Bug"),
    (6, "Project Contract"),
    (7, "Employee Contract"),
    (8, "Employee"),
    (9, "assets"),
    (10, "assets assignment"),
    (11, "Tickets"),
)

APP_MODULE = [
    "dashboard",
    "project",
    "backlog",
    "release",
    "task",
    "tasklist",
    "project_people",
    "message",
    "files",
    "time",
    "project_gantt",
    "project_report",
    "client_company",
    "client",
    "employee",
    "report",
    "work_type",
    "jobs",
    "role",
    "profile",
    "company_configuration",
    "account_type",
    "resign_employee",
    "account_master",
    "employee_contract",
    "invoice",
    "pricing_plan",
    "receipt",
    "payments_made",
    "payment_receive",
    "vendor",
    "expense",
    "profit_loss",
    "group",
    "bug",
    "project_category",
    "designation",
    "department",
    "employee_contract",
    "attendance",
    "holiday",
]

MODULE_ACTION_ARRAY = ["list", "add", "edit", "delete", "view"]

CLIENT_PERMS_MODULES = [
    "project",
    "backlog",
    "release",
    "task",
    "tasklist",
    "message",
    "files",
    "time",
    "project_gantt",
]

BOSNIA_AND_HERZEGOVINA = "Bosnia and Herzegovina"

C_EUROPE_DESC = "Central Europe Standard Time"
W_EUROPE_DESC = "W. Europe Standard Time"
AFRICA_DESC = "W. Central Africa Standard Time"
ARAB_DESC = "Arab Standard Time"
ROMANCE_DESC = "Romance Standard Time"
C_AMERICA_DESC = "Central America Standard Time"
SA_WESTERN_DESC = "SA Western Standard Time"
SA_DESC = "South Africa Standard Time"
SA_PACIFIC_DESC = "SA Pacific Standard Time"
SINGAPORE_DESC = "Singapore Standard Time"
FLE_DESC = "FLE Standard Time"
SE_ASIA_DESC = "SE Asia Standard Time"
EASTERN_DESC = "Eastern Standard Time"
CENTRAL_DESC = "Central Standard Time"
MOUNTAIN_DESC = "Mountain Standard Time"

EUROPE_NAME = "(UTC+01:00) Belgrade, Bratislava, Budapest, Ljubljana, Prague"
W_EUROPE_NAME = "(UTC+01:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna"
AFRICA_NAME = "(UTC+01:00) West Central Africa"
BHR_NAME = "(UTC+03:00) Kuwait, Riyadh"
BEL_NAME = "(UTC+01:00) Brussels, Copenhagen, Madrid, Paris"
BOL_NAME = "(UTC-04:00) Georgetown, La Paz, Manaus, San Juan"
C_AMERICA_NAME = "(UTC-06:00) Central America"
HARARE_AND_PRET0RIA_NAME = "(UTC+02:00) Harare, Pretoria"
RIO_BRANCO_NAME = "(UTC-05:00) Bogota, Lima, Quito, Rio Branco"
SINGAPORE_NAME = "(UTC+08:00) Kuala Lumpur, Singapore"
EUROPE_SOFIA_NAME = "(UTC+02:00) Helsinki, Kyiv, Riga, Sofia, Tallinn, Vilnius"
KHM_NAME = "(UTC+07:00) Bangkok, Hanoi, Jakarta"
EASTERN_NAME = "(UTC-05:00) Eastern Time (US & Canada)"
US_CENTRAL_NAME = "(UTC-06:00) Central Time (US & Canada)"
US_MOUNTAIN_NAME = "(UTC-07:00) Mountain Time (US & Canada)"
ARIZONA_ = "(UTC-07:00) Arizona"

UTC_M_08_00 = "UTC-08:00"
UTC_M_07_00 = "UTC-07:00"
UTC_M_06_00 = "UTC-06:00"
UTC_M_05_00 = "UTC-05:00"
UTC_M_04_00 = "UTC-04:00"
UTC_M_03_00 = "UTC-03:00"
UTC_P_01_00 = "UTC+01:00"
UTC_P_02_00 = "UTC+02:00"
UTC_P_03_00 = "UTC+03:00"
UTC_P_06_00 = "UTC+06:00"
UTC_P_04_00 = "UTC+04:00"
UTC_P_07_00 = "UTC+07:00"
UTC_P_08_00 = "UTC+08:00"
UTC_P_10_00 = "UTC+10:00"
UTC_P_11_00 = "UTC+11:00"

COUNTRY_TIMEZONE_LIST = [
    {
        "IsoAlpha3": "AFG",
        "timeZone": ["Asia/Kabul"],
        "timeZoneArray": [
            {"description": "Afghanistan Standard Time", "name": "(UTC+04:30) Kabul", "value": "UTC+04:30"}
        ],
        "country": "Afghanistan",
        "countryCode": "AF",
    },
    {
        "IsoAlpha3": "ALB",
        "timeZone": ["Europe/Tirane"],
        "timeZoneArray": [
            {
                "description": C_EUROPE_DESC,
                "name": EUROPE_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Albania",
        "countryCode": "AL",
    },
    {
        "IsoAlpha3": "DZA",
        "timeZone": ["Africa/Algiers"],
        "timeZoneArray": [
            {
                "description": AFRICA_DESC,
                "name": AFRICA_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Algeria",
        "countryCode": "DZ",
    },
    {
        "IsoAlpha3": "ARG",
        "timeZone": [
            "America/Argentina/Buenos_Aires",
            "America/Argentina/Cordoba",
            "America/Argentina/Salta",
            "America/Argentina/Jujuy",
            "America/Argentina/Tucuman",
            "America/Argentina/Catamarca",
            "America/Argentina/La_Rioja",
            "America/Argentina/San_Juan",
            "America/Argentina/Mendoza",
            "America/Argentina/San_Luis",
            "America/Argentina/Rio_Gallegos",
            "America/Argentina/Ushuaia",
        ],
        "timeZoneArray": [
            {"description": "Argentina Standard Time", "name": "(UTC-03:00) City of Buenos Aires", "value": UTC_M_03_00}
        ],
        "country": "Argentina",
        "countryCode": "AR",
    },
    {
        "IsoAlpha3": "ARM",
        "timeZone": ["Asia/Yerevan"],
        "timeZoneArray": [
            {"description": "Caucasus Standard Time", "name": "(UTC+04:00) Yerevan", "value": UTC_P_04_00}
        ],
        "country": "Armenia",
        "countryCode": "AM",
    },
    {
        "IsoAlpha3": "AUS",
        "timeZone": [
            "Australia/Lord_Howe",
            "Antarctica/Macquarie",
            "Australia/Hobart",
            "Australia/Currie",
            "Australia/Melbourne",
            "Australia/Sydney",
            "Australia/Broken_Hill",
            "Australia/Brisbane",
            "Australia/Lindeman",
            "Australia/Adelaide",
            "Australia/Darwin",
            "Australia/Perth",
            "Australia/Eucla",
        ],
        "timeZoneArray": [
            {
                "description": "Central Pacific Standard Time",
                "name": "(UTC+11:00) Solomon Is., New Caledonia",
                "value": UTC_P_11_00,
            },
            {"description": "Tasmania Standard Time", "name": "(UTC+10:00) Hobart", "value": UTC_P_10_00},
            {
                "description": "AUS Eastern Standard Time",
                "name": "(UTC+10:00) Canberra, Melbourne, Sydney",
                "value": UTC_P_10_00,
            },
            {"description": "Cen. Australia Standard Time", "name": "(UTC+09:30) Adelaide", "value": "UTC+09:30"},
            {"description": "E. Australia Standard Time", "name": "(UTC+10:00) Brisbane", "value": UTC_P_10_00},
            {"description": "AUS Central Standard Time", "name": "(UTC+09:30) Darwin", "value": "UTC+09:30"},
            {"description": "W. Australia Standard Time", "name": "(UTC+08:00) Perth", "value": UTC_P_08_00},
        ],
        "country": "Australia",
        "countryCode": "AU",
    },
    {
        "IsoAlpha3": "AUT",
        "timeZone": ["Europe/Vienna"],
        "timeZoneArray": [
            {
                "description": W_EUROPE_DESC,
                "name": W_EUROPE_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Austria",
        "countryCode": "AT",
    },
    {
        "IsoAlpha3": "AZE",
        "timeZone": ["Asia/Baku"],
        "timeZoneArray": [
            {"description": "Azerbaijan Standard Time", "name": "(UTC+04:00) Baku", "value": UTC_P_04_00}
        ],
        "country": "Azerbaijan",
        "countryCode": "AZ",
    },
    {
        "IsoAlpha3": "BHR",
        "timeZone": ["Asia/Bahrain"],
        "timeZoneArray": [
            {"description": ARAB_DESC, "name": BHR_NAME, "value": UTC_P_03_00}
        ],
        "country": "Bahrain",
        "countryCode": "BH",
    },
    {
        "IsoAlpha3": "BGD",
        "timeZone": ["Asia/Dhaka"],
        "timeZoneArray": [
            {"description": "Bangladesh Standard Time", "name": "(UTC+06:00) Dhaka", "value": UTC_P_06_00}
        ],
        "country": "Bangladesh",
        "countryCode": "BD",
    },
    {
        "IsoAlpha3": "BLR",
        "timeZone": ["Europe/Minsk"],
        "timeZoneArray": [{"description": "Belarus Standard Time", "name": "(UTC+03:00) Minsk", "value": UTC_P_03_00}],
        "country": "Belarus",
        "countryCode": "BY",
    },
    {
        "IsoAlpha3": "BEL",
        "timeZone": ["Europe/Brussels"],
        "timeZoneArray": [
            {
                "description": ROMANCE_DESC,
                "name": BEL_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Belgium",
        "countryCode": "BE",
    },
    {
        "IsoAlpha3": "BLZ",
        "timeZone": ["America/Belize"],
        "timeZoneArray": [
            {
                "description": C_AMERICA_DESC,
                "name": C_AMERICA_NAME,
                "value": UTC_M_06_00,
            }
        ],
        "country": "Belize",
        "countryCode": "BZ",
    },
    {
        "IsoAlpha3": "BTN",
        "timeZone": ["Asia/Thimphu"],
        "timeZoneArray": [
            {"description": "Bangladesh Standard Time", "name": "(UTC+06:00) Dhaka", "value": UTC_P_06_00}
        ],
        "country": "Bhutan",
        "countryCode": "BT",
    },
    {
        "IsoAlpha3": "BOL",
        "timeZone": ["America/La_Paz"],
        "timeZoneArray": [
            {
                "description": SA_WESTERN_DESC,
                "name": BOL_NAME,
                "value": UTC_M_04_00,
            }
        ],
        "country": "Bolivia",
        "countryCode": "BO",
    },
    {
        "IsoAlpha3": "BIH",
        "timeZone": ["Europe/Sarajevo"],
        "timeZoneArray": [
            {
                "description": C_EUROPE_DESC,
                "name": EUROPE_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": BOSNIA_AND_HERZEGOVINA,
        "countryCode": "BA",
    },
    {
        "IsoAlpha3": "BWA",
        "timeZone": ["Africa/Gaborone"],
        "timeZoneArray": [
            {"description": SA_DESC, "name": HARARE_AND_PRET0RIA_NAME, "value": UTC_P_02_00}
        ],
        "country": "Botswana",
        "countryCode": "BW",
    },
    {
        "IsoAlpha3": "BRA",
        "timeZone": [
            "America/Noronha",
            "America/Belem",
            "America/Fortaleza",
            "America/Recife",
            "America/Araguaina",
            "America/Maceio",
            "America/Bahia",
            "America/Sao_Paulo",
            "America/Campo_Grande",
            "America/Cuiaba",
            "America/Santarem",
            "America/Porto_Velho",
            "America/Boa_Vista",
            "America/Manaus",
            "America/Eirunepe",
            "America/Rio_Branco",
        ],
        "timeZoneArray": [
            {"description": "UTC-02", "name": "(UTC-02:00) Coordinated Universal Time-02", "value": "UTC-02:00"},
            {"description": "SA Eastern Standard Time", "name": "(UTC-03:00) Cayenne, Fortaleza", "value": UTC_M_03_00},
            {"description": "Bahia Standard Time", "name": "(UTC-03:00) Salvador", "value": UTC_M_03_00},
            {"description": "E. South America Standard Time", "name": "(UTC-03:00) Brasilia", "value": UTC_M_03_00},
            {"description": "Central Brazilian Standard Time", "name": "(UTC-04:00) Cuiaba", "value": UTC_M_04_00},
            {
                "description": SA_WESTERN_DESC,
                "name": BOL_NAME,
                "value": UTC_M_04_00,
            },
            {
                "description": SA_PACIFIC_DESC,
                "name": RIO_BRANCO_NAME,
                "value": UTC_M_05_00,
            },
        ],
        "country": "Brazil",
        "countryCode": "BR",
    },
    {
        "IsoAlpha3": "BRN",
        "timeZone": ["Asia/Brunei"],
        "timeZoneArray": [
            {
                "description": SINGAPORE_DESC,
                "name": SINGAPORE_NAME,
                "value": UTC_P_08_00,
            }
        ],
        "country": "Brunei",
        "countryCode": "BN",
    },
    {
        "IsoAlpha3": "BGR",
        "timeZone": ["Europe/Sofia"],
        "timeZoneArray": [
            {
                "description": FLE_DESC,
                "name": EUROPE_SOFIA_NAME,
                "value": UTC_P_02_00,
            }
        ],
        "country": "Bulgaria",
        "countryCode": "BG",
    },
    {
        "IsoAlpha3": "KHM",
        "timeZone": ["Asia/Phnom_Penh"],
        "timeZoneArray": [
            {
                "description": SE_ASIA_DESC,
                "name": KHM_NAME,
                "value": UTC_P_07_00,
            }
        ],
        "country": "Cambodia",
        "countryCode": "KH",
    },
    {
        "IsoAlpha3": "CMR",
        "timeZone": ["Africa/Douala"],
        "timeZoneArray": [
            {
                "description": AFRICA_DESC,
                "name": AFRICA_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Cameroon",
        "countryCode": "CM",
    },
    {
        "IsoAlpha3": "CAN",
        "timeZone": [
            "America/St_Johns",
            "America/Halifax",
            "America/Glace_Bay",
            "America/Moncton",
            "America/Goose_Bay",
            "America/Blanc-Sablon",
            "America/Toronto",
            "America/Nipigon",
            "America/Thunder_Bay",
            "America/Iqaluit",
            "America/Pangnirtung",
            "America/Atikokan",
            "America/Winnipeg",
            "America/Rainy_River",
            "America/Resolute",
            "America/Rankin_Inlet",
            "America/Regina",
            "America/Swift_Current",
            "America/Edmonton",
            "America/Cambridge_Bay",
            "America/Yellowknife",
            "America/Inuvik",
            "America/Creston",
            "America/Dawson_Creek",
            "America/Fort_Nelson",
            "America/Vancouver",
            "America/Whitehorse",
            "America/Dawson",
        ],
        "timeZoneArray": [
            {"description": "Newfoundland Standard Time", "name": "(UTC-03:30) Newfoundland", "value": "UTC-03:30"},
            {
                "description": "Atlantic Standard Time",
                "name": "(UTC-04:00) Atlantic Time (Canada)",
                "value": UTC_M_04_00,
            },
            {
                "description": SA_WESTERN_DESC,
                "name": BOL_NAME,
                "value": UTC_M_04_00,
            },
            {
                "description": EASTERN_DESC,
                "name": EASTERN_NAME,
                "value": UTC_M_05_00,
            },
            {
                "description": SA_PACIFIC_DESC,
                "name": RIO_BRANCO_NAME,
                "value": UTC_M_05_00,
            },
            {
                "description": CENTRAL_DESC,
                "name": US_CENTRAL_NAME,
                "value": UTC_M_06_00,
            },
            {"description": "Canada Central Standard Time", "name": "(UTC-06:00) Saskatchewan", "value": UTC_M_06_00},
            {
                "description": MOUNTAIN_DESC,
                "name": US_MOUNTAIN_NAME,
                "value": UTC_M_07_00,
            },
            {"description": "US Mountain Standard Time", "name": "(UTC-07:00) Arizona", "value": UTC_M_07_00},
            {
                "description": "Pacific Standard Time",
                "name": "(UTC-08:00) Pacific Time (US & Canada)",
                "value": UTC_M_08_00,
            },
        ],
        "country": "Canada",
        "countryCode": "CA",
    },
    {
        "IsoAlpha3": "CHL",
        "timeZone": ["America/Santiago", "Pacific/Easter"],
        "timeZoneArray": [
            {"description": "Pacific SA Standard Time", "name": "(UTC-04:00) Santiago", "value": UTC_M_04_00},
            {
                "description": SA_PACIFIC_DESC,
                "name": RIO_BRANCO_NAME,
                "value": UTC_M_05_00,
            },
        ],
        "country": "Chile",
        "countryCode": "CL",
    },
    {
        "IsoAlpha3": "CHN",
        "timeZone": ["Asia/Shanghai", "Asia/Urumqi"],
        "timeZoneArray": [
            {
                "description": "China Standard Time",
                "name": "(UTC+08:00) Beijing, Chongqing, Hong Kong, Urumqi",
                "value": UTC_P_08_00,
            },
            {"description": "Central Asia Standard Time", "name": "(UTC+06:00) Astana", "value": UTC_P_06_00},
        ],
        "country": "China",
        "countryCode": "CN",
    },
    {
        "IsoAlpha3": "COL",
        "timeZone": ["America/Bogota"],
        "timeZoneArray": [
            {
                "description": SA_PACIFIC_DESC,
                "name": RIO_BRANCO_NAME,
                "value": UTC_M_05_00,
            }
        ],
        "country": "Colombia",
        "countryCode": "CO",
    },
    {
        "IsoAlpha3": "COD",
        "timeZone": ["Africa/Kinshasa", "Africa/Lubumbashi"],
        "timeZoneArray": [
            {
                "description": AFRICA_DESC,
                "name": AFRICA_NAME,
                "value": UTC_P_01_00,
            },
            {"description": SA_DESC, "name": HARARE_AND_PRET0RIA_NAME, "value": UTC_P_02_00},
        ],
        "country": "Congo (DRC)",
        "countryCode": "CD",
    },
    {
        "IsoAlpha3": "CRI",
        "timeZone": ["America/Costa_Rica"],
        "timeZoneArray": [
            {
                "description": C_AMERICA_DESC,
                "name": C_AMERICA_NAME,
                "value": UTC_M_06_00,
            }
        ],
        "country": "Costa Rica",
        "countryCode": "CR",
    },
    {
        "IsoAlpha3": "CIV",
        "timeZone": ["Africa/Abidjan"],
        "timeZoneArray": [
            {"description": "Greenwich Standard Time", "name": "(UTC+00:00) Monrovia, Reykjavik", "value": "UTC+00:00"}
        ],
        "country": "Côte d’Ivoire",
        "countryCode": "CI",
    },
    {
        "IsoAlpha3": "HRV",
        "timeZone": ["Europe/Zagreb"],
        "timeZoneArray": [
            {
                "description": C_EUROPE_DESC,
                "name": EUROPE_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Croatia",
        "countryCode": "HR",
    },
    {
        "IsoAlpha3": "CUB",
        "timeZone": ["America/Havana"],
        "timeZoneArray": [
            {
                "description": EASTERN_DESC,
                "name": EASTERN_NAME,
                "value": UTC_M_05_00,
            }
        ],
        "country": "Cuba",
        "countryCode": "CU",
    },
    {
        "IsoAlpha3": "CZE",
        "timeZone": ["Europe/Prague"],
        "timeZoneArray": [
            {
                "description": C_EUROPE_DESC,
                "name": EUROPE_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Czech Republic",
        "countryCode": "CZ",
    },
    {
        "IsoAlpha3": "DNK",
        "timeZone": ["Europe/Copenhagen"],
        "timeZoneArray": [
            {
                "description": ROMANCE_DESC,
                "name": BEL_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Denmark",
        "countryCode": "DK",
    },
    {
        "IsoAlpha3": "DJI",
        "timeZone": ["Africa/Djibouti"],
        "timeZoneArray": [
            {"description": "E. Africa Standard Time", "name": "(UTC+03:00) Nairobi", "value": UTC_P_03_00}
        ],
        "country": "Djibouti",
        "countryCode": "DJ",
    },
    {
        "IsoAlpha3": "DOM",
        "timeZone": ["America/Santo_Domingo"],
        "timeZoneArray": [
            {
                "description": SA_WESTERN_DESC,
                "name": BOL_NAME,
                "value": UTC_M_04_00,
            }
        ],
        "country": "Dominican Republic",
        "countryCode": "DO",
    },
    {
        "IsoAlpha3": "ECU",
        "timeZone": ["America/Guayaquil", "Pacific/Galapagos"],
        "timeZoneArray": [
            {
                "description": SA_PACIFIC_DESC,
                "name": RIO_BRANCO_NAME,
                "value": UTC_M_05_00,
            },
            {
                "description": C_AMERICA_DESC,
                "name": C_AMERICA_NAME,
                "value": UTC_M_06_00,
            },
        ],
        "country": "Ecuador",
        "countryCode": "EC",
    },
    {
        "IsoAlpha3": "EGY",
        "timeZone": ["Africa/Cairo"],
        "timeZoneArray": [{"description": "Egypt Standard Time", "name": "(UTC+02:00) Cairo", "value": UTC_P_02_00}],
        "country": "Egypt",
        "countryCode": "EG",
    },
    {
        "IsoAlpha3": "SLV",
        "timeZone": ["America/El_Salvador"],
        "timeZoneArray": [
            {
                "description": C_AMERICA_DESC,
                "name": C_AMERICA_NAME,
                "value": UTC_M_06_00,
            }
        ],
        "country": "El Salvador",
        "countryCode": "SV",
    },
    {
        "IsoAlpha3": "ERI",
        "timeZone": ["Africa/Asmara"],
        "timeZoneArray": [
            {"description": "E. Africa Standard Time", "name": "(UTC+03:00) Nairobi", "value": UTC_P_03_00}
        ],
        "country": "Eritrea",
        "countryCode": "ER",
    },
    {
        "IsoAlpha3": "EST",
        "timeZone": ["Europe/Tallinn"],
        "timeZoneArray": [
            {
                "description": FLE_DESC,
                "name": EUROPE_SOFIA_NAME,
                "value": UTC_P_02_00,
            }
        ],
        "country": "Estonia",
        "countryCode": "EE",
    },
    {
        "IsoAlpha3": "ETH",
        "timeZone": ["Africa/Addis_Ababa"],
        "timeZoneArray": [
            {"description": "E. Africa Standard Time", "name": "(UTC+03:00) Nairobi", "value": UTC_P_03_00}
        ],
        "country": "Ethiopia",
        "countryCode": "ET",
    },
    {
        "IsoAlpha3": "FRO",
        "timeZone": ["Atlantic/Faroe"],
        "timeZoneArray": [
            {
                "description": "GMT Standard Time",
                "name": "(UTC+00:00) Dublin, Edinburgh, Lisbon, London",
                "value": "UTC+00:00",
            }
        ],
        "country": "Faroe Islands",
        "countryCode": "FO",
    },
    {
        "IsoAlpha3": "FIN",
        "timeZone": ["Europe/Helsinki"],
        "timeZoneArray": [
            {
                "description": FLE_DESC,
                "name": EUROPE_SOFIA_NAME,
                "value": UTC_P_02_00,
            }
        ],
        "country": "Finland",
        "countryCode": "FI",
    },
    {
        "IsoAlpha3": "FRA",
        "timeZone": ["Europe/Paris"],
        "timeZoneArray": [
            {
                "description": ROMANCE_DESC,
                "name": BEL_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "France",
        "countryCode": "FR",
    },
    {
        "IsoAlpha3": "GEO",
        "timeZone": ["Asia/Tbilisi"],
        "timeZoneArray": [
            {"description": "Georgian Standard Time", "name": "(UTC+04:00) Tbilisi", "value": UTC_P_04_00}
        ],
        "country": "Georgia",
        "countryCode": "GE",
    },
    {
        "IsoAlpha3": "DEU",
        "timeZone": ["Europe/Berlin", "Europe/Busingen"],
        "timeZoneArray": [
            {
                "description": W_EUROPE_DESC,
                "name": W_EUROPE_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Germany",
        "countryCode": "DE",
    },
    {
        "IsoAlpha3": "GRC",
        "timeZone": ["Europe/Athens"],
        "timeZoneArray": [
            {"description": "GTB Standard Time", "name": "(UTC+02:00) Athens, Bucharest", "value": UTC_P_02_00}
        ],
        "country": "Greece",
        "countryCode": "GR",
    },
    {
        "IsoAlpha3": "GRL",
        "timeZone": ["America/Godthab", "America/Danmarkshavn", "America/Scoresbysund", "America/Thule"],
        "timeZoneArray": [
            {"description": "Greenland Standard Time", "name": "(UTC-03:00) Greenland", "value": UTC_M_03_00},
            {"description": "UTC", "name": "UTC"},
            {"description": "Azores Standard Time", "name": "(UTC-01:00) Azores", "value": "UTC-01:00"},
            {
                "description": "Atlantic Standard Time",
                "name": "(UTC-04:00) Atlantic Time (Canada)",
                "value": UTC_M_04_00,
            },
        ],
        "country": "Greenland",
        "countryCode": "GL",
    },
    {
        "IsoAlpha3": "GTM",
        "timeZone": ["America/Guatemala"],
        "timeZoneArray": [
            {
                "description": C_AMERICA_DESC,
                "name": C_AMERICA_NAME,
                "value": UTC_M_06_00,
            }
        ],
        "country": "Guatemala",
        "countryCode": "GT",
    },
    {
        "IsoAlpha3": "HTI",
        "timeZone": ["America/Port-au-Prince"],
        "timeZoneArray": [
            {
                "description": EASTERN_DESC,
                "name": EASTERN_NAME,
                "value": UTC_M_05_00,
            }
        ],
        "country": "Haiti",
        "countryCode": "HT",
    },
    {
        "IsoAlpha3": "HND",
        "timeZone": ["America/Tegucigalpa"],
        "timeZoneArray": [
            {
                "description": C_AMERICA_DESC,
                "name": C_AMERICA_NAME,
                "value": UTC_M_06_00,
            }
        ],
        "country": "Honduras",
        "countryCode": "HN",
    },
    {
        "IsoAlpha3": "HKG",
        "timeZone": ["Asia/Hong_Kong"],
        "timeZoneArray": [
            {
                "description": "China Standard Time",
                "name": "(UTC+08:00) Beijing, Chongqing, Hong Kong, Urumqi",
                "value": UTC_P_08_00,
            }
        ],
        "country": "Hong Kong SAR",
        "countryCode": "HK",
    },
    {
        "IsoAlpha3": "HUN",
        "timeZone": ["Europe/Budapest"],
        "timeZoneArray": [
            {
                "description": C_EUROPE_DESC,
                "name": EUROPE_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Hungary",
        "countryCode": "HU",
    },
    {
        "IsoAlpha3": "ISL",
        "timeZone": ["Atlantic/Reykjavik"],
        "timeZoneArray": [
            {"description": "Greenwich Standard Time", "name": "(UTC+00:00) Monrovia, Reykjavik", "value": "UTC+00:00"}
        ],
        "country": "Iceland",
        "countryCode": "IS",
    },
    {
        "IsoAlpha3": "IND",
        "timeZone": ["Asia/Kolkata"],
        "timeZoneArray": [
            {
                "description": "India Standard Time",
                "name": "(UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi",
                "value": "UTC+05:30",
            }
        ],
        "country": "India",
        "countryCode": "IN",
    },
    {
        "IsoAlpha3": "IDN",
        "timeZone": ["Asia/Jakarta", "Asia/Pontianak", "Asia/Makassar", "Asia/Jayapura"],
        "timeZoneArray": [
            {
                "description": SE_ASIA_DESC,
                "name": KHM_NAME,
                "value": UTC_P_07_00,
            },
            {
                "description": SINGAPORE_DESC,
                "name": SINGAPORE_NAME,
                "value": UTC_P_08_00,
            },
            {"description": "Tokyo Standard Time", "name": "(UTC+09:00) Osaka, Sapporo, Tokyo", "value": "UTC+09:00"},
        ],
        "country": "Indonesia",
        "countryCode": "Description",
    },
    {
        "IsoAlpha3": "IRN",
        "timeZone": ["Asia/Tehran"],
        "timeZoneArray": [{"description": "Iran Standard Time", "name": "(UTC+03:30) Tehran", "value": "UTC+03:30"}],
        "country": "Iran",
        "countryCode": "IR",
    },
    {
        "IsoAlpha3": "IRQ",
        "timeZone": ["Asia/Baghdad"],
        "timeZoneArray": [{"description": "Arabic Standard Time", "name": "(UTC+03:00) Baghdad", "value": UTC_P_03_00}],
        "country": "Iraq",
        "countryCode": "IQ",
    },
    {
        "IsoAlpha3": "IRL",
        "timeZone": ["Europe/Dublin"],
        "timeZoneArray": [
            {
                "description": "GMT Standard Time",
                "name": "(UTC+00:00) Dublin, Edinburgh, Lisbon, London",
                "value": "UTC+00:00",
            }
        ],
        "country": "Ireland",
        "countryCode": "IE",
    },
    {
        "IsoAlpha3": "ISR",
        "timeZone": ["Asia/Jerusalem"],
        "timeZoneArray": [
            {"description": "Israel Standard Time", "name": "(UTC+02:00) Jerusalem", "value": UTC_P_02_00}
        ],
        "country": "Israel",
        "countryCode": "IL",
    },
    {
        "IsoAlpha3": "ITA",
        "timeZone": ["Europe/Rome"],
        "timeZoneArray": [
            {
                "description": W_EUROPE_DESC,
                "name": W_EUROPE_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Italy",
        "countryCode": "IT",
    },
    {
        "IsoAlpha3": "JAM",
        "timeZone": ["America/Jamaica"],
        "timeZoneArray": [
            {
                "description": SA_PACIFIC_DESC,
                "name": RIO_BRANCO_NAME,
                "value": UTC_M_05_00,
            }
        ],
        "country": "Jamaica",
        "countryCode": "JM",
    },
    {
        "IsoAlpha3": "JPN",
        "timeZone": ["Asia/Tokyo"],
        "timeZoneArray": [
            {"description": "Tokyo Standard Time", "name": "(UTC+09:00) Osaka, Sapporo, Tokyo", "value": "UTC+09:00"}
        ],
        "country": "Japan",
        "countryCode": "JP",
    },
    {
        "IsoAlpha3": "JOR",
        "timeZone": ["Asia/Amman"],
        "timeZoneArray": [{"description": "Jordan Standard Time", "name": "(UTC+02:00) Amman", "value": UTC_P_02_00}],
        "country": "Jordan",
        "countryCode": "JO",
    },
    {
        "IsoAlpha3": "KAZ",
        "timeZone": ["Asia/Almaty", "Asia/Qyzylorda", "Asia/Aqtobe", "Asia/Aqtau", "Asia/Oral"],
        "timeZoneArray": [
            {"description": "Central Asia Standard Time", "name": "(UTC+06:00) Astana", "value": UTC_P_06_00},
            {"description": "West Asia Standard Time", "name": "(UTC+05:00) Ashgabat, Tashkent", "value": "UTC+05:00"},
        ],
        "country": "Kazakhstan",
        "countryCode": "KZ",
    },
    {
        "IsoAlpha3": "KEN",
        "timeZone": ["Africa/Nairobi"],
        "timeZoneArray": [
            {"description": "E. Africa Standard Time", "name": "(UTC+03:00) Nairobi", "value": UTC_P_03_00}
        ],
        "country": "Kenya",
        "countryCode": "KE",
    },
    {
        "IsoAlpha3": "KOR",
        "timeZone": ["Asia/Seoul"],
        "timeZoneArray": [{"description": "Korea Standard Time", "name": "(UTC+09:00) Seoul", "value": "UTC+09:00"}],
        "country": "Korea",
        "countryCode": "KR",
    },
    {
        "IsoAlpha3": "KWT",
        "timeZone": ["Asia/Kuwait"],
        "timeZoneArray": [
            {"description": ARAB_DESC, "name": BHR_NAME, "value": UTC_P_03_00}
        ],
        "country": "Kuwait",
        "countryCode": "KW",
    },
    {
        "IsoAlpha3": "KGZ",
        "timeZone": ["Asia/Bishkek"],
        "timeZoneArray": [
            {"description": "Central Asia Standard Time", "name": "(UTC+06:00) Astana", "value": UTC_P_06_00}
        ],
        "country": "Kyrgyzstan",
        "countryCode": "KG",
    },
    {
        "IsoAlpha3": "LAO",
        "timeZone": ["Asia/Vientiane"],
        "timeZoneArray": [
            {
                "description": SE_ASIA_DESC,
                "name": KHM_NAME,
                "value": UTC_P_07_00,
            }
        ],
        "country": "Laos",
        "countryCode": "LA",
    },
    {
        "IsoAlpha3": "LVA",
        "timeZone": ["Europe/Riga"],
        "timeZoneArray": [
            {
                "description": FLE_DESC,
                "name": EUROPE_SOFIA_NAME,
                "value": UTC_P_02_00,
            }
        ],
        "country": "Latvia",
        "countryCode": "LV",
    },
    {
        "IsoAlpha3": "LBN",
        "timeZone": ["Asia/Beirut"],
        "timeZoneArray": [
            {"description": "Middle East Standard Time", "name": "(UTC+02:00) Beirut", "value": UTC_P_02_00}
        ],
        "country": "Lebanon",
        "countryCode": "LB",
    },
    {
        "IsoAlpha3": "LBY",
        "timeZone": ["Africa/Tripoli"],
        "timeZoneArray": [{"description": "Libya Standard Time", "name": "(UTC+02:00) Tripoli", "value": UTC_P_02_00}],
        "country": "Libya",
        "countryCode": "LY",
    },
    {
        "IsoAlpha3": "LIE",
        "timeZone": ["Europe/Vaduz"],
        "timeZoneArray": [
            {
                "description": W_EUROPE_DESC,
                "name": W_EUROPE_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Liechtenstein",
        "countryCode": "LI",
    },
    {
        "IsoAlpha3": "LTU",
        "timeZone": ["Europe/Vilnius"],
        "timeZoneArray": [
            {
                "description": FLE_DESC,
                "name": EUROPE_SOFIA_NAME,
                "value": UTC_P_02_00,
            }
        ],
        "country": "Lithuania",
        "countryCode": "LT",
    },
    {
        "IsoAlpha3": "LUX",
        "timeZone": ["Europe/Luxembourg"],
        "timeZoneArray": [
            {
                "description": W_EUROPE_DESC,
                "name": W_EUROPE_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Luxembourg",
        "countryCode": "LU",
    },
    {
        "IsoAlpha3": "MAC",
        "timeZone": ["Asia/Macau"],
        "timeZoneArray": [
            {
                "description": "China Standard Time",
                "name": "(UTC+08:00) Beijing, Chongqing, Hong Kong, Urumqi",
                "value": UTC_P_08_00,
            }
        ],
        "country": "Macao SAR",
        "countryCode": "MO",
    },
    {
        "IsoAlpha3": "MKD",
        "timeZone": ["Europe/Skopje"],
        "timeZoneArray": [
            {
                "description": C_EUROPE_DESC,
                "name": EUROPE_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Macedonia, FYRO",
        "countryCode": "MK",
    },
    {
        "IsoAlpha3": "MYS",
        "timeZone": ["Asia/Kuala_Lumpur", "Asia/Kuching"],
        "timeZoneArray": [
            {
                "description": SINGAPORE_DESC,
                "name": SINGAPORE_NAME,
                "value": UTC_P_08_00,
            }
        ],
        "country": "Malaysia",
        "countryCode": "MY",
    },
    {
        "IsoAlpha3": "MDV",
        "timeZone": ["Indian/Maldives"],
        "timeZoneArray": [
            {"description": "West Asia Standard Time", "name": "(UTC+05:00) Ashgabat, Tashkent", "value": "UTC+05:00"}
        ],
        "country": "Maldives",
        "countryCode": "MV",
    },
    {
        "IsoAlpha3": "MLI",
        "timeZone": ["Africa/Bamako"],
        "timeZoneArray": [
            {"description": "Greenwich Standard Time", "name": "(UTC+00:00) Monrovia, Reykjavik", "value": "UTC+00:00"}
        ],
        "country": "Mali",
        "countryCode": "ML",
    },
    {
        "IsoAlpha3": "MLT",
        "timeZone": ["Europe/Malta"],
        "timeZoneArray": [
            {
                "description": W_EUROPE_DESC,
                "name": W_EUROPE_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Malta",
        "countryCode": "MT",
    },
    {
        "IsoAlpha3": "MEX",
        "timeZone": [
            "America/Mexico_City",
            "America/Cancun",
            "America/Merida",
            "America/Monterrey",
            "America/Matamoros",
            "America/Mazatlan",
            "America/Chihuahua",
            "America/Ojinaga",
            "America/Hermosillo",
            "America/Tijuana",
            "America/Bahia_Banderas",
        ],
        "timeZoneArray": [
            {
                "description": "Central Standard Time (Mexico)",
                "name": "(UTC-06:00) Guadalajara, Mexico City, Monterrey",
                "value": UTC_M_06_00,
            },
            {"description": "Eastern Standard Time (Mexico)", "name": "(UTC-05:00) Chetumal", "value": UTC_M_05_00},
            {
                "description": CENTRAL_DESC,
                "name": US_CENTRAL_NAME,
                "value": UTC_M_06_00,
            },
            {
                "description": "Mountain Standard Time (Mexico)",
                "name": "(UTC-07:00) Chihuahua, La Paz, Mazatlan",
                "value": UTC_M_07_00,
            },
            {
                "description": MOUNTAIN_DESC,
                "name": US_MOUNTAIN_NAME,
                "value": UTC_M_07_00,
            },
            {"description": "US Mountain Standard Time", "name": "(UTC-07:00) Arizona", "value": UTC_M_07_00},
            {
                "description": "Pacific Standard Time",
                "name": "(UTC-08:00) Pacific Time (US & Canada)",
                "value": UTC_M_08_00,
            },
        ],
        "country": "Mexico",
        "countryCode": "MX",
    },
    {
        "IsoAlpha3": "MDA",
        "timeZone": ["Europe/Chisinau"],
        "timeZoneArray": [
            {"description": "E. Europe Standard Time", "name": "(UTC+02:00) Chisinau", "value": UTC_P_02_00}
        ],
        "country": "Moldova",
        "countryCode": "MD",
    },
    {
        "IsoAlpha3": "MCO",
        "timeZone": ["Europe/Monaco"],
        "timeZoneArray": [
            {
                "description": W_EUROPE_DESC,
                "name": W_EUROPE_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Monaco",
        "countryCode": "MC",
    },
    {
        "IsoAlpha3": "MNG",
        "timeZone": ["Asia/Ulaanbaatar", "Asia/Hovd", "Asia/Choibalsan"],
        "timeZoneArray": [
            {"description": "Ulaanbaatar Standard Time", "name": "(UTC+08:00) Ulaanbaatar", "value": UTC_P_08_00}
        ],
        "country": "Mongolia",
        "countryCode": "MN",
    },
    {
        "IsoAlpha3": "MNE",
        "timeZone": ["Europe/Podgorica"],
        "timeZoneArray": [
            {
                "description": C_EUROPE_DESC,
                "name": EUROPE_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Montenegro",
        "countryCode": "ME",
    },
    {
        "IsoAlpha3": "MAR",
        "timeZone": ["Africa/Casablanca"],
        "timeZoneArray": [
            {"description": "Morocco Standard Time", "name": "(UTC+00:00) Casablanca", "value": "UTC+00:00"}
        ],
        "country": "Morocco",
        "countryCode": "MA",
    },
    {
        "IsoAlpha3": "MMR",
        "timeZone": ["Asia/Rangoon"],
        "timeZoneArray": [
            {"description": "Myanmar Standard Time", "name": "(UTC+06:30) Yangon (Rangoon)", "value": "UTC+06:30"}
        ],
        "country": "Myanmar",
        "countryCode": "MM",
    },
    {
        "IsoAlpha3": "NPL",
        "timeZone": ["Asia/Kathmandu"],
        "timeZoneArray": [
            {"description": "Nepal Standard Time", "name": "(UTC+05:45) Kathmandu", "value": "UTC+05:45"}
        ],
        "country": "Nepal",
        "countryCode": "NP",
    },
    {
        "IsoAlpha3": "NLD",
        "timeZone": ["Europe/Amsterdam"],
        "timeZoneArray": [
            {
                "description": W_EUROPE_DESC,
                "name": W_EUROPE_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Netherlands",
        "countryCode": "NL",
    },
    {
        "IsoAlpha3": "NZL",
        "timeZone": ["Pacific/Auckland", "Pacific/Chatham"],
        "timeZoneArray": [
            {
                "description": "New Zealand Standard Time",
                "name": "(UTC+12:00) Auckland, Wellington",
                "value": "UTC+12:00",
            }
        ],
        "country": "New Zealand",
        "countryCode": "NZ",
    },
    {
        "IsoAlpha3": "NIC",
        "timeZone": ["America/Managua"],
        "timeZoneArray": [
            {
                "description": C_AMERICA_DESC,
                "name": C_AMERICA_NAME,
                "value": UTC_M_06_00,
            }
        ],
        "country": "Nicaragua",
        "countryCode": "NI",
    },
    {
        "IsoAlpha3": "NGA",
        "timeZone": ["Africa/Lagos"],
        "timeZoneArray": [
            {
                "description": AFRICA_DESC,
                "name": AFRICA_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Nigeria",
        "countryCode": "NG",
    },
    {
        "IsoAlpha3": "NOR",
        "timeZone": ["Europe/Oslo"],
        "timeZoneArray": [
            {
                "description": W_EUROPE_DESC,
                "name": W_EUROPE_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Norway",
        "countryCode": "NO",
    },
    {
        "IsoAlpha3": "OMN",
        "timeZone": ["Asia/Muscat"],
        "timeZoneArray": [
            {"description": "Arabian Standard Time", "name": "(UTC+04:00) Abu Dhabi, Muscat", "value": UTC_P_04_00}
        ],
        "country": "Oman",
        "countryCode": "OM",
    },
    {
        "IsoAlpha3": "PAK",
        "timeZone": ["Asia/Karachi"],
        "timeZoneArray": [
            {"description": "Pakistan Standard Time", "name": "(UTC+05:00) Islamabad, Karachi", "value": "UTC+05:00"}
        ],
        "country": "Pakistan",
        "countryCode": "PK",
    },
    {
        "IsoAlpha3": "PAN",
        "timeZone": ["America/Panama"],
        "timeZoneArray": [
            {
                "description": SA_PACIFIC_DESC,
                "name": RIO_BRANCO_NAME,
                "value": UTC_M_05_00,
            }
        ],
        "country": "Panama",
        "countryCode": "PA",
    },
    {
        "IsoAlpha3": "PRY",
        "timeZone": ["America/Asuncion"],
        "timeZoneArray": [
            {"description": "Paraguay Standard Time", "name": "(UTC-04:00) Asuncion", "value": UTC_M_04_00}
        ],
        "country": "Paraguay",
        "countryCode": "PY",
    },
    {
        "IsoAlpha3": "PER",
        "timeZone": ["America/Lima"],
        "timeZoneArray": [
            {
                "description": SA_PACIFIC_DESC,
                "name": RIO_BRANCO_NAME,
                "value": UTC_M_05_00,
            }
        ],
        "country": "Peru",
        "countryCode": "PE",
    },
    {
        "IsoAlpha3": "PHL",
        "timeZone": ["Asia/Manila"],
        "timeZoneArray": [
            {
                "description": SINGAPORE_DESC,
                "name": SINGAPORE_NAME,
                "value": UTC_P_08_00,
            }
        ],
        "country": "Philippines",
        "countryCode": "PH",
    },
    {
        "IsoAlpha3": "POL",
        "timeZone": ["Europe/Warsaw"],
        "timeZoneArray": [
            {
                "description": "Central European Standard Time",
                "name": "(UTC+01:00) Sarajevo, Skopje, Warsaw, Zagreb",
                "value": UTC_P_01_00,
            }
        ],
        "country": "Poland",
        "countryCode": "PL",
    },
    {
        "IsoAlpha3": "PRT",
        "timeZone": ["Europe/Lisbon", "Atlantic/Madeira", "Atlantic/Azores"],
        "timeZoneArray": [
            {
                "description": "GMT Standard Time",
                "name": "(UTC+00:00) Dublin, Edinburgh, Lisbon, London",
                "value": "UTC+00:00",
            },
            {"description": "Azores Standard Time", "name": "(UTC-01:00) Azores", "value": "UTC-01:00"},
        ],
        "country": "Portugal",
        "countryCode": "PT",
    },
    {
        "IsoAlpha3": "PRI",
        "timeZone": ["America/Puerto_Rico"],
        "timeZoneArray": [
            {
                "description": SA_WESTERN_DESC,
                "name": BOL_NAME,
                "value": UTC_M_04_00,
            }
        ],
        "country": "Puerto Rico",
        "countryCode": "PR",
    },
    {
        "IsoAlpha3": "QAT",
        "timeZone": ["Asia/Qatar"],
        "timeZoneArray": [
            {"description": ARAB_DESC, "name": BHR_NAME, "value": UTC_P_03_00}
        ],
        "country": "Qatar",
        "countryCode": "QA",
    },
    {
        "IsoAlpha3": "REU",
        "timeZone": ["Indian/Reunion"],
        "timeZoneArray": [
            {"description": "Mauritius Standard Time", "name": "(UTC+04:00) Port Louis", "value": UTC_P_04_00}
        ],
        "country": "Réunion",
        "countryCode": "RE",
    },
    {
        "IsoAlpha3": "ROU",
        "timeZone": ["Europe/Bucharest"],
        "timeZoneArray": [
            {"description": "GTB Standard Time", "name": "(UTC+02:00) Athens, Bucharest", "value": UTC_P_02_00}
        ],
        "country": "Romania",
        "countryCode": "RO",
    },
    {
        "IsoAlpha3": "RUS",
        "timeZone": [
            "Europe/Kaliningrad",
            "Europe/Moscow",
            "Europe/Simferopol",
            "Europe/Volgograd",
            "Europe/Astrakhan",
            "Europe/Samara",
            "Europe/Ulyanovsk",
            "Asia/Yekaterinburg",
            "Asia/Omsk",
            "Asia/Novosibirsk",
            "Asia/Barnaul",
            "Asia/Novokuznetsk",
            "Asia/Krasnoyarsk",
            "Asia/Irkutsk",
            "Asia/Chita",
            "Asia/Yakutsk",
            "Asia/Khandyga",
            "Asia/Vladivostok",
            "Asia/Ust-Nera",
            "Asia/Magadan",
            "Asia/Sakhalin",
            "Asia/Srednekolymsk",
            "Asia/Kamchatka",
            "Asia/Anadyr",
        ],
        "timeZoneArray": [
            {"description": "Kaliningrad Standard Time", "name": "(UTC+02:00) Kaliningrad", "value": UTC_P_02_00},
            {
                "description": "Russian Standard Time",
                "name": "(UTC+03:00) Moscow, St. Petersburg, Volgograd",
                "value": UTC_P_03_00,
            },
            {"description": "Russia Time Zone 3", "name": "(UTC+04:00) Izhevsk, Samara", "value": UTC_P_04_00},
            {"description": "Ekaterinburg Standard Time", "name": "(UTC+05:00) Ekaterinburg", "value": "UTC+05:00"},
            {"description": "N. Central Asia Standard Time", "name": "(UTC+07:00) Novosibirsk", "value": UTC_P_07_00},
            {"description": "North Asia Standard Time", "name": "(UTC+07:00) Krasnoyarsk", "value": UTC_P_07_00},
            {"description": "North Asia East Standard Time", "name": "(UTC+08:00) Irkutsk", "value": UTC_P_08_00},
            {"description": "Yakutsk Standard Time", "name": "(UTC+09:00) Yakutsk", "value": "UTC+09:00"},
            {"description": "Vladivostok Standard Time", "name": "(UTC+10:00) Vladivostok", "value": UTC_P_10_00},
            {"description": "Magadan Standard Time", "name": "(UTC+11:00) Magadan", "value": UTC_P_11_00},
            {"description": "Russia Time Zone 10", "name": "(UTC+11:00) Chokurdakh", "value": UTC_P_11_00},
            {
                "description": "Russia Time Zone 11",
                "name": "(UTC+12:00) Anadyr, Petropavlovsk-Kamchatsky",
                "value": "UTC+12:00",
            },
        ],
        "country": "Russia",
        "countryCode": "RU",
    },
    {
        "IsoAlpha3": "RWA",
        "timeZone": ["Africa/Kigali"],
        "timeZoneArray": [
            {"description": SA_DESC, "name": HARARE_AND_PRET0RIA_NAME, "value": UTC_P_02_00}
        ],
        "country": "Rwanda",
        "countryCode": "RW",
    },
    {
        "IsoAlpha3": "SAU",
        "timeZone": ["Asia/Riyadh"],
        "timeZoneArray": [
            {"description": ARAB_DESC, "name": BHR_NAME, "value": UTC_P_03_00}
        ],
        "country": "Saudi Arabia",
        "countryCode": "SA",
    },
    {
        "IsoAlpha3": "SEN",
        "timeZone": ["Africa/Dakar"],
        "timeZoneArray": [
            {"description": "Greenwich Standard Time", "name": "(UTC+00:00) Monrovia, Reykjavik", "value": "UTC+00:00"}
        ],
        "country": "Senegal",
        "countryCode": "SN",
    },
    {
        "IsoAlpha3": "SRB",
        "timeZone": ["Europe/Belgrade"],
        "timeZoneArray": [
            {
                "description": C_EUROPE_DESC,
                "name": EUROPE_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Serbia",
        "countryCode": "RS",
    },
    {
        "IsoAlpha3": "SGP",
        "timeZone": ["Asia/Singapore"],
        "timeZoneArray": [
            {
                "description": SINGAPORE_DESC,
                "name": SINGAPORE_NAME,
                "value": UTC_P_08_00,
            }
        ],
        "country": "Singapore",
        "countryCode": "SG",
    },
    {
        "IsoAlpha3": "SVK",
        "timeZone": ["Europe/Bratislava"],
        "timeZoneArray": [
            {
                "description": C_EUROPE_DESC,
                "name": EUROPE_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Slovakia",
        "countryCode": "SK",
    },
    {
        "IsoAlpha3": "SVN",
        "timeZone": ["Europe/Ljubljana"],
        "timeZoneArray": [
            {
                "description": C_EUROPE_DESC,
                "name": EUROPE_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Slovenia",
        "countryCode": "SI",
    },
    {
        "IsoAlpha3": "SOM",
        "timeZone": ["Africa/Mogadishu"],
        "timeZoneArray": [
            {"description": "E. Africa Standard Time", "name": "(UTC+03:00) Nairobi", "value": UTC_P_03_00}
        ],
        "country": "Somalia",
        "countryCode": "SO",
    },
    {
        "IsoAlpha3": "ZAF",
        "timeZone": ["Africa/Johannesburg"],
        "timeZoneArray": [
            {"description": SA_DESC, "name": HARARE_AND_PRET0RIA_NAME, "value": UTC_P_02_00}
        ],
        "country": "South Africa",
        "countryCode": "ZA",
    },
    {
        "IsoAlpha3": "ESP",
        "timeZone": ["Europe/Madrid", "Africa/Ceuta", "Atlantic/Canary"],
        "timeZoneArray": [
            {
                "description": ROMANCE_DESC,
                "name": BEL_NAME,
                "value": UTC_P_01_00,
            },
            {
                "description": "GMT Standard Time",
                "name": "(UTC+00:00) Dublin, Edinburgh, Lisbon, London",
                "value": "UTC+00:00",
            },
        ],
        "country": "Spain",
        "countryCode": "ES",
    },
    {
        "IsoAlpha3": "LKA",
        "timeZone": ["Asia/Colombo"],
        "timeZoneArray": [
            {"description": "Sri Lanka Standard Time", "name": "(UTC+05:30) Sri Jayawardenepura", "value": "UTC+05:30"}
        ],
        "country": "Sri Lanka",
        "countryCode": "LK",
    },
    {
        "IsoAlpha3": "SWE",
        "timeZone": ["Europe/Stockholm"],
        "timeZoneArray": [
            {
                "description": W_EUROPE_DESC,
                "name": W_EUROPE_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Sweden",
        "countryCode": "SE",
    },
    {
        "IsoAlpha3": "CHE",
        "timeZone": ["Europe/Zurich"],
        "timeZoneArray": [
            {
                "description": W_EUROPE_DESC,
                "name": W_EUROPE_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Switzerland",
        "countryCode": "CH",
    },
    {
        "IsoAlpha3": "SYR",
        "timeZone": ["Asia/Damascus"],
        "timeZoneArray": [{"description": "Syria Standard Time", "name": "(UTC+02:00) Damascus", "value": UTC_P_02_00}],
        "country": "Syria",
        "countryCode": "SY",
    },
    {
        "IsoAlpha3": "TWN",
        "timeZone": ["Asia/Taipei"],
        "timeZoneArray": [{"description": "Taipei Standard Time", "name": "(UTC+08:00) Taipei", "value": UTC_P_08_00}],
        "country": "Taiwan",
        "countryCode": "TW",
    },
    {
        "IsoAlpha3": "TJK",
        "timeZone": ["Asia/Dushanbe"],
        "timeZoneArray": [
            {"description": "West Asia Standard Time", "name": "(UTC+05:00) Ashgabat, Tashkent", "value": "UTC+05:00"}
        ],
        "country": "Tajikistan",
        "countryCode": "TJ",
    },
    {
        "IsoAlpha3": "THA",
        "timeZone": ["Asia/Bangkok"],
        "timeZoneArray": [
            {
                "description": SE_ASIA_DESC,
                "name": KHM_NAME,
                "value": UTC_P_07_00,
            }
        ],
        "country": "Thailand",
        "countryCode": "TH",
    },
    {
        "IsoAlpha3": "TTO",
        "timeZone": ["America/Port_of_Spain"],
        "timeZoneArray": [
            {
                "description": SA_WESTERN_DESC,
                "name": BOL_NAME,
                "value": UTC_M_04_00,
            }
        ],
        "country": "Trinidad and Tobago",
        "countryCode": "TT",
    },
    {
        "IsoAlpha3": "TUN",
        "timeZone": ["Africa/Tunis"],
        "timeZoneArray": [
            {
                "description": AFRICA_DESC,
                "name": AFRICA_NAME,
                "value": UTC_P_01_00,
            }
        ],
        "country": "Tunisia",
        "countryCode": "TN",
    },
    {
        "IsoAlpha3": "TUR",
        "timeZone": ["Europe/Istanbul"],
        "timeZoneArray": [
            {"description": "Turkey Standard Time", "name": "(UTC+02:00) Istanbul", "value": UTC_P_02_00}
        ],
        "country": "Turkey",
        "countryCode": "TR",
    },
    {
        "IsoAlpha3": "TKM",
        "timeZone": ["Asia/Ashgabat"],
        "timeZoneArray": [
            {"description": "West Asia Standard Time", "name": "(UTC+05:00) Ashgabat, Tashkent", "value": "UTC+05:00"}
        ],
        "country": "Turkmenistan",
        "countryCode": "TM",
    },
    {
        "IsoAlpha3": "UKR",
        "timeZone": ["Europe/Kiev", "Europe/Uzhgorod", "Europe/Zaporozhye"],
        "timeZoneArray": [
            {
                "description": FLE_DESC,
                "name": EUROPE_SOFIA_NAME,
                "value": UTC_P_02_00,
            }
        ],
        "country": "Ukraine",
        "countryCode": "UA",
    },
    {
        "IsoAlpha3": "ARE",
        "timeZone": ["Asia/Dubai"],
        "timeZoneArray": [
            {"description": "Arabian Standard Time", "name": "(UTC+04:00) Abu Dhabi, Muscat", "value": UTC_P_04_00}
        ],
        "country": "United Arab Emirates",
        "countryCode": "AE",
    },
    {
        "IsoAlpha3": "GBR",
        "timeZone": ["Europe/London"],
        "timeZoneArray": [
            {
                "description": "GMT Standard Time",
                "name": "(UTC+00:00) Dublin, Edinburgh, Lisbon, London",
                "value": "UTC+00:00",
            }
        ],
        "country": "United Kingdom",
        "countryCode": "GB",
    },
    {
        "IsoAlpha3": "USA",
        "timeZone": [
            "America/New_York",
            "America/Detroit",
            "America/Kentucky/Louisville",
            "America/Kentucky/Monticello",
            "America/Indiana/Indianapolis",
            "America/Indiana/Vincennes",
            "America/Indiana/Winamac",
            "America/Indiana/Marengo",
            "America/Indiana/Petersburg",
            "America/Indiana/Vevay",
            "America/Chicago",
            "America/Indiana/Tell_City",
            "America/Indiana/Knox",
            "America/Menominee",
            "America/North_Dakota/Center",
            "America/North_Dakota/New_Salem",
            "America/North_Dakota/Beulah",
            "America/Denver",
            "America/Boise",
            "America/Phoenix",
            "America/Los_Angeles",
            "America/Anchorage",
            "America/Juneau",
            "America/Sitka",
            "America/Metlakatla",
            "America/Yakutat",
            "America/Nome",
            "America/Adak",
            "Pacific/Honolulu",
        ],
        "timeZoneArray": [
            {
                "description": EASTERN_DESC,
                "name": EASTERN_NAME,
                "value": UTC_M_05_00,
            },
            {"description": "US Eastern Standard Time", "name": "(UTC-05:00) Indiana (East)", "value": UTC_M_05_00},
            {
                "description": CENTRAL_DESC,
                "name": US_CENTRAL_NAME,
                "value": UTC_M_06_00,
            },
            {
                "description": MOUNTAIN_DESC,
                "name": US_MOUNTAIN_NAME,
                "value": UTC_M_07_00,
            },
            {"description": "US Mountain Standard Time", "name": "(UTC-07:00) Arizona", "value": UTC_M_07_00},
            {
                "description": "Pacific Standard Time",
                "name": "(UTC-08:00) Pacific Time (US & Canada)",
                "value": UTC_M_08_00,
            },
            {"description": "Alaskan Standard Time", "name": "(UTC-09:00) Alaska", "value": "UTC-09:00"},
            {"description": "Hawaiian Standard Time", "name": "(UTC-10:00) Hawaii", "value": "UTC-10:00"},
        ],
        "country": "United States",
        "countryCode": "US",
    },
    {
        "IsoAlpha3": "URY",
        "timeZone": ["America/Montevideo"],
        "timeZoneArray": [
            {"description": "Montevideo Standard Time", "name": "(UTC-03:00) Montevideo", "value": UTC_M_03_00}
        ],
        "country": "Uruguay",
        "countryCode": "UY",
    },
    {
        "IsoAlpha3": "UZB",
        "timeZone": ["Asia/Samarkand", "Asia/Tashkent"],
        "timeZoneArray": [
            {"description": "West Asia Standard Time", "name": "(UTC+05:00) Ashgabat, Tashkent", "value": "UTC+05:00"}
        ],
        "country": "Uzbekistan",
        "countryCode": "UZ",
    },
    {
        "IsoAlpha3": "VEN",
        "timeZone": ["America/Caracas"],
        "timeZoneArray": [
            {"description": "Venezuela Standard Time", "name": "(UTC-04:00) Caracas", "value": UTC_M_04_00}
        ],
        "country": "Venezuela",
        "countryCode": "VE",
    },
    {
        "IsoAlpha3": "VNM",
        "timeZone": ["Asia/Ho_Chi_Minh"],
        "timeZoneArray": [
            {
                "description": SE_ASIA_DESC,
                "name": KHM_NAME,
                "value": UTC_P_07_00,
            }
        ],
        "country": "Vietnam",
        "countryCode": "VN",
    },
    {
        "IsoAlpha3": "YEM",
        "timeZone": ["Asia/Aden"],
        "timeZoneArray": [
            {"description": ARAB_DESC, "name": BHR_NAME, "value": UTC_P_03_00}
        ],
        "country": "Yemen",
        "countryCode": "YE",
    },
    {
        "IsoAlpha3": "ZWE",
        "timeZone": ["Africa/Harare"],
        "timeZoneArray": [
            {"description": SA_DESC, "name": HARARE_AND_PRET0RIA_NAME, "value": UTC_P_02_00}
        ],
        "country": "Zimbabwe",
        "countryCode": "ZW",
    },
]

COUNTRY_LIST = [
    {"name": "Afghanistan", "dial_code": "+93", "code": "AF", "description": "Afghanistan (+93)"},
    {"name": "Albania", "dial_code": "+355", "code": "AL", "description": "Albania (+355)"},
    {"name": "Algeria", "dial_code": "+213", "code": "DZ", "description": "Algeria (+213)"},
    {"name": "American Samoa", "dial_code": "+1684", "code": "AS", "description": "American Samoa (+1684)"},
    {"name": "Andorra", "dial_code": "+376", "code": "AD", "description": "Andorra (+376)"},
    {"name": "Angola", "dial_code": "+244", "code": "AO", "description": "Angola (+244)"},
    {"name": "Anguilla", "dial_code": "+1264", "code": "AI", "description": "Anguilla (+1264)"},
    {"name": "Antarctica", "dial_code": "+672", "code": "AQ", "description": "Antarctica (+672)"},
    {"name": "Antigua and Barbuda", "dial_code": "+1268", "code": "AG", "description": "Antigua and Barbuda (+1268)"},
    {"name": "Argentina", "dial_code": "+54", "code": "AR", "description": "Argentina (+54)"},
    {"name": "Armenia", "dial_code": "+374", "code": "AM", "description": "Armenia (+374)"},
    {"name": "Aruba", "dial_code": "+297", "code": "AW", "description": "Aruba (+297)"},
    {"name": "Australia", "dial_code": "+61", "code": "AU", "description": "Australia (+61)"},
    {"name": "Austria", "dial_code": "+43", "code": "AT", "description": "Austria (+43)"},
    {"name": "Azerbaijan", "dial_code": "+994", "code": "AZ", "description": "Azerbaijan (+994)"},
    {"name": "Bahamas", "dial_code": "+1242", "code": "BS", "description": "Bahamas (+1242)"},
    {"name": "Bahrain", "dial_code": "+973", "code": "BH", "description": "Bahrain (+973)"},
    {"name": "Bangladesh", "dial_code": "+880", "code": "BD", "description": "Bangladesh (+880)"},
    {"name": "Barbados", "dial_code": "+1246", "code": "BB", "description": "Barbados (+1246)"},
    {"name": "Belarus", "dial_code": "+375", "code": "BY", "description": "Belarus (+375)"},
    {"name": "Belgium", "dial_code": "+32", "code": "BE", "description": "Belgium (+32)"},
    {"name": "Belize", "dial_code": "+501", "code": "BZ", "description": "Belize (+501)"},
    {"name": "Benin", "dial_code": "+229", "code": "BJ", "description": "Benin (+229)"},
    {"name": "Bermuda", "dial_code": "+1441", "code": "BM", "description": "Bermuda (+1441)"},
    {"name": "Bhutan", "dial_code": "+975", "code": "BT", "description": "Bhutan (+975)"},
    {
        "name": "Bolivia, Plurinational State of bolivia",
        "dial_code": "+591",
        "code": "BO",
        "description": "Bolivia, Plurinational State of bolivia (+591)",
    },
    {
        "name": BOSNIA_AND_HERZEGOVINA,
        "dial_code": "+387",
        "code": "BA",
        "description": "Bosnia and Herzegovina (+387)",
    },
    {"name": "Botswana", "dial_code": "+267", "code": "BW", "description": "Botswana (+267)"},
    {"name": "Bouvet Island", "dial_code": "+47", "code": "BV", "description": "Bouvet Island (+47)"},
    {"name": "Brazil", "dial_code": "+55", "code": "BR", "description": "Brazil (+55)"},
    {"name": "Brunei Darussalam", "dial_code": "+673", "code": "BN", "description": "Brunei Darussalam (+673)"},
    {"name": "Bulgaria", "dial_code": "+359", "code": "BG", "description": "Bulgaria (+359)"},
    {"name": "Burkina Faso", "dial_code": "+226", "code": "BF", "description": "Burkina Faso (+226)"},
    {"name": "Burundi", "dial_code": "+257", "code": "BI", "description": "Burundi (+257)"},
    {"name": "Cambodia", "dial_code": "+855", "code": "KH", "description": "Cambodia (+855)"},
    {"name": "Cameroon", "dial_code": "+237", "code": "CM", "description": "Cameroon (+237)"},
    {"name": "Canada", "dial_code": "+1", "code": "CA", "description": "Canada (+1)"},
    {"name": "Cape Verde", "dial_code": "+238", "code": "CV", "description": "Cape Verde (+238)"},
    {"name": "Cayman Islands", "dial_code": "+ 345", "code": "KY", "description": "Cayman Islands (+ 345)"},
    {
        "name": "Central African Republic",
        "dial_code": "+236",
        "code": "CF",
        "description": "Central African Republic (+236)",
    },
    {"name": "Chad", "dial_code": "+235", "code": "TD", "description": "Chad (+235)"},
    {"name": "Chile", "dial_code": "+56", "code": "CL", "description": "Chile (+56)"},
    {"name": "China", "dial_code": "+86", "code": "CN", "description": "China (+86)"},
    {"name": "Christmas Island", "dial_code": "+61", "code": "CX", "description": "Christmas Island (+61)"},
    {
        "name": "Cocos (Keeling) Islands",
        "dial_code": "+61",
        "code": "CC",
        "description": "Cocos (Keeling) Islands (+61)",
    },
    {"name": "Colombia", "dial_code": "+57", "code": "CO", "description": "Colombia (+57)"},
    {"name": "Comoros", "dial_code": "+269", "code": "KM", "description": "Comoros (+269)"},
    {"name": "Congo", "dial_code": "+242", "code": "CG", "description": "Congo (+242)"},
    {
        "name": "Congo, The Democratic Republic of the Congo",
        "dial_code": "+243",
        "code": "CD",
        "description": "Congo, The Democratic Republic of the Congo (+243)",
    },
    {"name": "Cook Islands", "dial_code": "+682", "code": "CK", "description": "Cook Islands (+682)"},
    {"name": "Costa Rica", "dial_code": "+506", "code": "CR", "description": "Costa Rica (+506)"},
    {"name": "Cote d'Ivoire", "dial_code": "+225", "code": "CI", "description": "Cote d'Ivoire (+225)"},
    {"name": "Croatia", "dial_code": "+385", "code": "HR", "description": "Croatia (+385)"},
    {"name": "Cuba", "dial_code": "+53", "code": "CU", "description": "Cuba (+53)"},
    {"name": "Cyprus", "dial_code": "+357", "code": "CY", "description": "Cyprus (+357)"},
    {"name": "Czech Republic", "dial_code": "+420", "code": "CZ", "description": "Czech Republic (+420)"},
    {"name": "Denmark", "dial_code": "+45", "code": "DK", "description": "Denmark (+45)"},
    {"name": "Djibouti", "dial_code": "+253", "code": "DJ", "description": "Djibouti (+253)"},
    {"name": "Dominica", "dial_code": "+1767", "code": "DM", "description": "Dominica (+1767)"},
    {"name": "Dominican Republic", "dial_code": "+1849", "code": "DO", "description": "Dominican Republic (+1849)"},
    {"name": "Ecuador", "dial_code": "+593", "code": "EC", "description": "Ecuador (+593)"},
    {"name": "Egypt", "dial_code": "+20", "code": "EG", "description": "Egypt (+20)"},
    {"name": "El Salvador", "dial_code": "+503", "code": "SV", "description": "El Salvador (+503)"},
    {"name": "Equatorial Guinea", "dial_code": "+240", "code": "GQ", "description": "Equatorial Guinea (+240)"},
    {"name": "Eritrea", "dial_code": "+291", "code": "ER", "description": "Eritrea (+291)"},
    {"name": "Estonia", "dial_code": "+372", "code": "EE", "description": "Estonia (+372)"},
    {"name": "Ethiopia", "dial_code": "+251", "code": "ET", "description": "Ethiopia (+251)"},
    {
        "name": "Falkland Islands (Malvinas)",
        "dial_code": "+500",
        "code": "FK",
        "description": "Falkland Islands (Malvinas) (+500)",
    },
    {"name": "Faroe Islands", "dial_code": "+298", "code": "FO", "description": "Faroe Islands (+298)"},
    {"name": "Fiji", "dial_code": "+679", "code": "FJ", "description": "Fiji (+679)"},
    {"name": "Finland", "dial_code": "+358", "code": "FI", "description": "Finland (+358)"},
    {"name": "France", "dial_code": "+33", "code": "FR", "description": "France (+33)"},
    {"name": "French Guiana", "dial_code": "+594", "code": "GF", "description": "French Guiana (+594)"},
    {"name": "French Polynesia", "dial_code": "+689", "code": "PF", "description": "French Polynesia (+689)"},
    {
        "name": "French Southern Territories",
        "dial_code": "+262",
        "code": "TF",
        "description": "French Southern Territories (+262)",
    },
    {"name": "Gabon", "dial_code": "+241", "code": "GA", "description": "Gabon (+241)"},
    {"name": "Gambia", "dial_code": "+220", "code": "GM", "description": "Gambia (+220)"},
    {"name": "Georgia", "dial_code": "+995", "code": "GE", "description": "Georgia (+995)"},
    {"name": "Germany", "dial_code": "+49", "code": "DE", "description": "Germany (+49)"},
    {"name": "Ghana", "dial_code": "+233", "code": "GH", "description": "Ghana (+233)"},
    {"name": "Gibraltar", "dial_code": "+350", "code": "GI", "description": "Gibraltar (+350)"},
    {"name": "Greece", "dial_code": "+30", "code": "GR", "description": "Greece (+30)"},
    {"name": "Greenland", "dial_code": "+299", "code": "GL", "description": "Greenland (+299)"},
    {"name": "Grenada", "dial_code": "+1473", "code": "GD", "description": "Grenada (+1473)"},
    {"name": "Guadeloupe", "dial_code": "+590", "code": "GP", "description": "Guadeloupe (+590)"},
    {"name": "Guam", "dial_code": "+1671", "code": "GU", "description": "Guam (+1671)"},
    {"name": "Guatemala", "dial_code": "+502", "code": "GT", "description": "Guatemala (+502)"},
    {"name": "Guernsey", "dial_code": "+44", "code": "GG", "description": "Guernsey (+44)"},
    {"name": "Guinea", "dial_code": "+224", "code": "GN", "description": "Guinea (+224)"},
    {"name": "Guinea-Bissau", "dial_code": "+245", "code": "GW", "description": "Guinea-Bissau (+245)"},
    {"name": "Guyana", "dial_code": "+592", "code": "GY", "description": "Guyana (+592)"},
    {"name": "Haiti", "dial_code": "+509", "code": "HT", "description": "Haiti (+509)"},
    {
        "name": "Heard Island and Mcdonald Islands",
        "dial_code": "+0",
        "code": "HM",
        "description": "Heard Island and Mcdonald Islands (+0)",
    },
    {
        "name": "Holy See (Vatican City State)",
        "dial_code": "+379",
        "code": "VA",
        "description": "Holy See (Vatican City State) (+379)",
    },
    {"name": "Honduras", "dial_code": "+504", "code": "HN", "description": "Honduras (+504)"},
    {"name": "Hong Kong", "dial_code": "+852", "code": "HK", "description": "Hong Kong (+852)"},
    {"name": "Hungary", "dial_code": "+36", "code": "HU", "description": "Hungary (+36)"},
    {"name": "Iceland", "dial_code": "+354", "code": "IS", "description": "Iceland (+354)"},
    {"name": "India", "dial_code": "+91", "code": "IN", "description": "India (+91)"},
    {"name": "Indonesia", "dial_code": "+62", "code": "ID", "description": "Indonesia (+62)"},
    {
        "name": "Iran, Islamic Republic of Persian Gulf",
        "dial_code": "+98",
        "code": "IR",
        "description": "Iran, Islamic Republic of Persian Gulf (+98)",
    },
    {"name": "Iraq", "dial_code": "+964", "code": "IQ", "description": "Iraq (+964)"},
    {"name": "Ireland", "dial_code": "+353", "code": "IE", "description": "Ireland (+353)"},
    {"name": "Isle of Man", "dial_code": "+44", "code": "IM", "description": "Isle of Man (+44)"},
    {"name": "Israel", "dial_code": "+972", "code": "IL", "description": "Israel (+972)"},
    {"name": "Italy", "dial_code": "+39", "code": "IT", "description": "Italy (+39)"},
    {"name": "Jamaica", "dial_code": "+1876", "code": "JM", "description": "Jamaica (+1876)"},
    {"name": "Japan", "dial_code": "+81", "code": "JP", "description": "Japan (+81)"},
    {"name": "Jersey", "dial_code": "+44", "code": "JE", "description": "Jersey (+44)"},
    {"name": "Jordan", "dial_code": "+962", "code": "JO", "description": "Jordan (+962)"},
    {"name": "Kazakhstan", "dial_code": "+7", "code": "KZ", "description": "Kazakhstan (+7)"},
    {"name": "Kenya", "dial_code": "+254", "code": "KE", "description": "Kenya (+254)"},
    {"name": "Kiribati", "dial_code": "+686", "code": "KI", "description": "Kiribati (+686)"},
    {
        "name": "Korea, Democratic People's Republic of Korea",
        "dial_code": "+850",
        "code": "KP",
        "description": "Korea, Democratic People's Republic of Korea (+850)",
    },
    {
        "name": "Korea, Republic of South Korea",
        "dial_code": "+82",
        "code": "KR",
        "description": "Korea, Republic of South Korea (+82)",
    },
    {"name": "Kosovo", "dial_code": "+383", "code": "XK", "description": "Kosovo (+383)"},
    {"name": "Kuwait", "dial_code": "+965", "code": "KW", "description": "Kuwait (+965)"},
    {"name": "Kyrgyzstan", "dial_code": "+996", "code": "KG", "description": "Kyrgyzstan (+996)"},
    {"name": "Laos", "dial_code": "+856", "code": "LA", "description": "Laos (+856)"},
    {"name": "Latvia", "dial_code": "+371", "code": "LV", "description": "Latvia (+371)"},
    {"name": "Lebanon", "dial_code": "+961", "code": "LB", "description": "Lebanon (+961)"},
    {"name": "Lesotho", "dial_code": "+266", "code": "LS", "description": "Lesotho (+266)"},
    {"name": "Liberia", "dial_code": "+231", "code": "LR", "description": "Liberia (+231)"},
    {
        "name": "Libyan Arab Jamahiriya",
        "dial_code": "+218",
        "code": "LY",
        "description": "Libyan Arab Jamahiriya (+218)",
    },
    {"name": "Liechtenstein", "dial_code": "+423", "code": "LI", "description": "Liechtenstein (+423)"},
    {"name": "Lithuania", "dial_code": "+370", "code": "LT", "description": "Lithuania (+370)"},
    {"name": "Luxembourg", "dial_code": "+352", "code": "LU", "description": "Luxembourg (+352)"},
    {"name": "Macao", "dial_code": "+853", "code": "MO", "description": "Macao (+853)"},
    {"name": "Macedonia", "dial_code": "+389", "code": "MK", "description": "Macedonia (+389)"},
    {"name": "Madagascar", "dial_code": "+261", "code": "MG", "description": "Madagascar (+261)"},
    {"name": "Malawi", "dial_code": "+265", "code": "MW", "description": "Malawi (+265)"},
    {"name": "Malaysia", "dial_code": "+60", "code": "MY", "description": "Malaysia (+60)"},
    {"name": "Maldives", "dial_code": "+960", "code": "MV", "description": "Maldives (+960)"},
    {"name": "Mali", "dial_code": "+223", "code": "ML", "description": "Mali (+223)"},
    {"name": "Malta", "dial_code": "+356", "code": "MT", "description": "Malta (+356)"},
    {"name": "Marshall Islands", "dial_code": "+692", "code": "MH", "description": "Marshall Islands (+692)"},
    {"name": "Martinique", "dial_code": "+596", "code": "MQ", "description": "Martinique (+596)"},
    {"name": "Mauritania", "dial_code": "+222", "code": "MR", "description": "Mauritania (+222)"},
    {"name": "Mauritius", "dial_code": "+230", "code": "MU", "description": "Mauritius (+230)"},
    {"name": "Mayotte", "dial_code": "+262", "code": "YT", "description": "Mayotte (+262)"},
    {"name": "Mexico", "dial_code": "+52", "code": "MX", "description": "Mexico (+52)"},
    {
        "name": "Micronesia, Federated States of Micronesia",
        "dial_code": "+691",
        "code": "FM",
        "description": "Micronesia, Federated States of Micronesia (+691)",
    },
    {"name": "Moldova", "dial_code": "+373", "code": "MD", "description": "Moldova (+373)"},
    {"name": "Monaco", "dial_code": "+377", "code": "MC", "description": "Monaco (+377)"},
    {"name": "Mongolia", "dial_code": "+976", "code": "MN", "description": "Mongolia (+976)"},
    {"name": "Montenegro", "dial_code": "+382", "code": "ME", "description": "Montenegro (+382)"},
    {"name": "Montserrat", "dial_code": "+1664", "code": "MS", "description": "Montserrat (+1664)"},
    {"name": "Morocco", "dial_code": "+212", "code": "MA", "description": "Morocco (+212)"},
    {"name": "Mozambique", "dial_code": "+258", "code": "MZ", "description": "Mozambique (+258)"},
    {"name": "Myanmar", "dial_code": "+95", "code": "MM", "description": "Myanmar (+95)"},
    {"name": "Namibia", "dial_code": "+264", "code": "NA", "description": "Namibia (+264)"},
    {"name": "Nauru", "dial_code": "+674", "code": "NR", "description": "Nauru (+674)"},
    {"name": "Nepal", "dial_code": "+977", "code": "NP", "description": "Nepal (+977)"},
    {"name": "Netherlands", "dial_code": "+31", "code": "NL", "description": "Netherlands (+31)"},
    {"name": "Netherlands Antilles", "dial_code": "+599", "code": "AN", "description": "Netherlands Antilles (+599)"},
    {"name": "New Caledonia", "dial_code": "+687", "code": "NC", "description": "New Caledonia (+687)"},
    {"name": "New Zealand", "dial_code": "+64", "code": "NZ", "description": "New Zealand (+64)"},
    {"name": "Nicaragua", "dial_code": "+505", "code": "NI", "description": "Nicaragua (+505)"},
    {"name": "Niger", "dial_code": "+227", "code": "NE", "description": "Niger (+227)"},
    {"name": "Nigeria", "dial_code": "+234", "code": "NG", "description": "Nigeria (+234)"},
    {"name": "Niue", "dial_code": "+683", "code": "NU", "description": "Niue (+683)"},
    {"name": "Norfolk Island", "dial_code": "+672", "code": "NF", "description": "Norfolk Island (+672)"},
    {
        "name": "Northern Mariana Islands",
        "dial_code": "+1670",
        "code": "MP",
        "description": "Northern Mariana Islands (+1670)",
    },
    {"name": "Norway", "dial_code": "+47", "code": "NO", "description": "Norway (+47)"},
    {"name": "Oman", "dial_code": "+968", "code": "OM", "description": "Oman (+968)"},
    {"name": "Pakistan", "dial_code": "+92", "code": "PK", "description": "Pakistan (+92)"},
    {"name": "Palau", "dial_code": "+680", "code": "PW", "description": "Palau (+680)"},
    {
        "name": "Palestinian Territory, Occupied",
        "dial_code": "+970",
        "code": "PS",
        "description": "Palestinian Territory, Occupied (+970)",
    },
    {"name": "Panama", "dial_code": "+507", "code": "PA", "description": "Panama (+507)"},
    {"name": "Papua New Guinea", "dial_code": "+675", "code": "PG", "description": "Papua New Guinea (+675)"},
    {"name": "Paraguay", "dial_code": "+595", "code": "PY", "description": "Paraguay (+595)"},
    {"name": "Peru", "dial_code": "+51", "code": "PE", "description": "Peru (+51)"},
    {"name": "Philippines", "dial_code": "+63", "code": "PH", "description": "Philippines (+63)"},
    {"name": "Pitcairn", "dial_code": "+64", "code": "PN", "description": "Pitcairn (+64)"},
    {"name": "Poland", "dial_code": "+48", "code": "PL", "description": "Poland (+48)"},
    {"name": "Portugal", "dial_code": "+351", "code": "PT", "description": "Portugal (+351)"},
    {"name": "Puerto Rico", "dial_code": "+1939", "code": "PR", "description": "Puerto Rico (+1939)"},
    {"name": "Qatar", "dial_code": "+974", "code": "QA", "description": "Qatar (+974)"},
    {"name": "Romania", "dial_code": "+40", "code": "RO", "description": "Romania (+40)"},
    {"name": "Russia", "dial_code": "+7", "code": "RU", "description": "Russia (+7)"},
    {"name": "Rwanda", "dial_code": "+250", "code": "RW", "description": "Rwanda (+250)"},
    {"name": "Reunion", "dial_code": "+262", "code": "RE", "description": "Reunion (+262)"},
    {"name": "Saint Barthelemy", "dial_code": "+590", "code": "BL", "description": "Saint Barthelemy (+590)"},
    {
        "name": "Saint Helena, Ascension and Tristan Da Cunha",
        "dial_code": "+290",
        "code": "SH",
        "description": "Saint Helena, Ascension and Tristan Da Cunha (+290)",
    },
    {
        "name": "Saint Kitts and Nevis",
        "dial_code": "+1869",
        "code": "KN",
        "description": "Saint Kitts and Nevis (+1869)",
    },
    {"name": "Saint Lucia", "dial_code": "+1758", "code": "LC", "description": "Saint Lucia (+1758)"},
    {"name": "Saint Martin", "dial_code": "+590", "code": "MF", "description": "Saint Martin (+590)"},
    {
        "name": "Saint Pierre and Miquelon",
        "dial_code": "+508",
        "code": "PM",
        "description": "Saint Pierre and Miquelon (+508)",
    },
    {
        "name": "Saint Vincent and the Grenadines",
        "dial_code": "+1784",
        "code": "VC",
        "description": "Saint Vincent and the Grenadines (+1784)",
    },
    {"name": "Samoa", "dial_code": "+685", "code": "WS", "description": "Samoa (+685)"},
    {"name": "San Marino", "dial_code": "+378", "code": "SM", "description": "San Marino (+378)"},
    {"name": "Sao Tome and Principe", "dial_code": "+239", "code": "ST", "description": "Sao Tome and Principe (+239)"},
    {"name": "Saudi Arabia", "dial_code": "+966", "code": "SA", "description": "Saudi Arabia (+966)"},
    {"name": "Senegal", "dial_code": "+221", "code": "SN", "description": "Senegal (+221)"},
    {"name": "Serbia", "dial_code": "+381", "code": "RS", "description": "Serbia (+381)"},
    {"name": "Seychelles", "dial_code": "+248", "code": "SC", "description": "Seychelles (+248)"},
    {"name": "Sierra Leone", "dial_code": "+232", "code": "SL", "description": "Sierra Leone (+232)"},
    {"name": "Singapore", "dial_code": "+65", "code": "SG", "description": "Singapore (+65)"},
    {"name": "Slovakia", "dial_code": "+421", "code": "SK", "description": "Slovakia (+421)"},
    {"name": "Slovenia", "dial_code": "+386", "code": "SI", "description": "Slovenia (+386)"},
    {"name": "Solomon Islands", "dial_code": "+677", "code": "SB", "description": "Solomon Islands (+677)"},
    {"name": "Somalia", "dial_code": "+252", "code": "SO", "description": "Somalia (+252)"},
    {"name": "South Africa", "dial_code": "+27", "code": "ZA", "description": "South Africa (+27)"},
    {"name": "South Sudan", "dial_code": "+211", "code": "SS", "description": "South Sudan (+211)"},
    {
        "name": "South Georgia and the South Sandwich Islands",
        "dial_code": "+500",
        "code": "GS",
        "description": "South Georgia and the South Sandwich Islands (+500)",
    },
    {"name": "Spain", "dial_code": "+34", "code": "ES", "description": "Spain (+34)"},
    {"name": "Sri Lanka", "dial_code": "+94", "code": "LK", "description": "Sri Lanka (+94)"},
    {"name": "Sudan", "dial_code": "+249", "code": "SD", "description": "Sudan (+249)"},
    {"name": "Suriname", "dial_code": "+597", "code": "SR", "description": "Suriname (+597)"},
    {"name": "Svalbard and Jan Mayen", "dial_code": "+47", "code": "SJ", "description": "Svalbard and Jan Mayen (+47)"},
    {"name": "Swaziland", "dial_code": "+268", "code": "SZ", "description": "Swaziland (+268)"},
    {"name": "Sweden", "dial_code": "+46", "code": "SE", "description": "Sweden (+46)"},
    {"name": "Switzerland", "dial_code": "+41", "code": "CH", "description": "Switzerland (+41)"},
    {"name": "Syrian Arab Republic", "dial_code": "+963", "code": "SY", "description": "Syrian Arab Republic (+963)"},
    {"name": "Taiwan", "dial_code": "+886", "code": "TW", "description": "Taiwan (+886)"},
    {"name": "Tajikistan", "dial_code": "+992", "code": "TJ", "description": "Tajikistan (+992)"},
    {
        "name": "Tanzania, United Republic of Tanzania",
        "dial_code": "+255",
        "code": "TZ",
        "description": "Tanzania, United Republic of Tanzania (+255)",
    },
    {"name": "Thailand", "dial_code": "+66", "code": "TH", "description": "Thailand (+66)"},
    {"name": "Timor-Leste", "dial_code": "+670", "code": "TL", "description": "Timor-Leste (+670)"},
    {"name": "Togo", "dial_code": "+228", "code": "TG", "description": "Togo (+228)"},
    {"name": "Tokelau", "dial_code": "+690", "code": "TK", "description": "Tokelau (+690)"},
    {"name": "Tonga", "dial_code": "+676", "code": "TO", "description": "Tonga (+676)"},
    {"name": "Trinidad and Tobago", "dial_code": "+1868", "code": "TT", "description": "Trinidad and Tobago (+1868)"},
    {"name": "Tunisia", "dial_code": "+216", "code": "TN", "description": "Tunisia (+216)"},
    {"name": "Turkey", "dial_code": "+90", "code": "TR", "description": "Turkey (+90)"},
    {"name": "Turkmenistan", "dial_code": "+993", "code": "TM", "description": "Turkmenistan (+993)"},
    {
        "name": "Turks and Caicos Islands",
        "dial_code": "+1649",
        "code": "TC",
        "description": "Turks and Caicos Islands (+1649)",
    },
    {"name": "Tuvalu", "dial_code": "+688", "code": "TV", "description": "Tuvalu (+688)"},
    {"name": "Uganda", "dial_code": "+256", "code": "UG", "description": "Uganda (+256)"},
    {"name": "Ukraine", "dial_code": "+380", "code": "UA", "description": "Ukraine (+380)"},
    {"name": "United Arab Emirates", "dial_code": "+971", "code": "AE", "description": "United Arab Emirates (+971)"},
    {"name": "United Kingdom", "dial_code": "+44", "code": "GB", "description": "United Kingdom (+44)"},
    {"name": "United States", "dial_code": "+1", "code": "US", "description": "United States (+1)"},
    {"name": "Uruguay", "dial_code": "+598", "code": "UY", "description": "Uruguay (+598)"},
    {"name": "Uzbekistan", "dial_code": "+998", "code": "UZ", "description": "Uzbekistan (+998)"},
    {"name": "Vanuatu", "dial_code": "+678", "code": "VU", "description": "Vanuatu (+678)"},
    {
        "name": "Venezuela, Bolivarian Republic of Venezuela",
        "dial_code": "+58",
        "code": "VE",
        "description": "Venezuela, Bolivarian Republic of Venezuela (+58)",
    },
    {"name": "Vietnam", "dial_code": "+84", "code": "VN", "description": "Vietnam (+84)"},
    {
        "name": "Virgin Islands, British",
        "dial_code": "+1284",
        "code": "VG",
        "description": "Virgin Islands, British (+1284)",
    },
    {"name": "Virgin Islands, U.S.", "dial_code": "+1340", "code": "VI", "description": "Virgin Islands, U.S. (+1340)"},
    {"name": "Wallis and Futuna", "dial_code": "+681", "code": "WF", "description": "Wallis and Futuna (+681)"},
    {"name": "Yemen", "dial_code": "+967", "code": "YE", "description": "Yemen (+967)"},
    {"name": "Zambia", "dial_code": "+260", "code": "ZM", "description": "Zambia (+260)"},
    {"name": "Zimbabwe", "dial_code": "+263", "code": "ZW", "description": "Zimbabwe (+263)"},
]

COMPANY_INDUSTRY = (
    (1, "Agency (Design/Development)"),
    (2, "Agency (Marketing/Advertising)"),
    (3, "Construction/Engineering"),
    (4, "Consultancy (I.T/Management)"),
    (5, "Education"),
    (6, "Electronics and Electrical"),
    (7, "Entertainment and Media"),
    (8, "Finance/Banking/Insurance"),
    (9, "Government"),
    (10, "Health and Medical"),
    (11, "Hospitality"),
    (12, "Manufacturing"),
    (13, "Not for Profit"),
    (14, "Professional Services"),
    (15, "Retail/E-commerce"),
    (16, "Technology (Hardware)"),
    (17, "Technology (Software)"),
    (18, "Transport/Distribution"),
    (19, "Utilities/Energy"),
    (20, "Other"),
)

COMPANY_DEPARTMENT = (
    (1, "Creative"),
    (2, "Customer Support"),
    (3, "Finance"),
    (4, "I.T."),
    (5, "Marketing"),
    (6, "Operations"),
    (7, "People/Human Resources"),
    (8, "PMO (Project Management)"),
    (9, "Product"),
    (10, "Sales"),
    (11, "Other"),
)

COMPANY_JOB_LEVEL = (
    (1, "Student"),
    (2, "C Level, Partner, Founder"),
    (3, "VP/Head of"),
    (4, "Snr. Director, Director, Associate Director"),
    (5, "Snr. Manager, Group Manager, Principal"),
    (6, "Other"),
    (7, "Manager, Lead, Coordinator"),
    (8, "Project Manager"),
    (9, "Strategist, Specialist, Analyst, Assistant Manager"),
)

PRICING_PLAN_CHOICES = ((1, "Custom"), (2, "Dedicated"), (3, "Hourly"))

BILLING_INTERVAL_CHOICES = (
    (1, "Daily"),
    (2, "Weekly"),
    (3, "Monthly"),
    (4, "Every 3 Monthly"),
    (5, "Every 6 Monthly"),
    (6, "Monthly"),
)

INVOICE_STATUS = (
    (1, "Open"),
    (2, "Paid"),
    (3, "Due"),
    (4, "Cancel"),
)
TXN_STATUS_PENDING = 1
TXN_STATUS_APPROVE = 2
TXN_STATUS_SUCCESS = 3
TXN_STATUS_FAILED = 4
TXN_STATUS = (
    (TXN_STATUS_PENDING, "Pending"),
    (TXN_STATUS_APPROVE, "Approved"),
    (TXN_STATUS_SUCCESS, "Success"),
    (TXN_STATUS_FAILED, "Failed"),
)

TXN_TYPE_RECEIPT = 1
TXN_TYPE_PAYMENT = 2
TXN_TYPE_CASH_BACK = 3
TXN_TYPE_REFUND = 4
TXN_TYPE_SALE = 5
TXN_TYPE_DEPOSIT = 6
TXN_TYPE_WITHDRAWAL = 7
TXN_TYPE_TRANSFER = 8
TXN_TYPE = (
    (TXN_TYPE_RECEIPT, "Receipt"),
    (TXN_TYPE_PAYMENT, "Payment"),
    (TXN_TYPE_CASH_BACK, "Cash Back"),
    (TXN_TYPE_REFUND, "Refund"),
    (TXN_TYPE_SALE, "Sale"),
    (TXN_TYPE_DEPOSIT, "Deposit"),
    (TXN_TYPE_WITHDRAWAL, "Withdrawal"),
    (TXN_TYPE_TRANSFER, "Transfer"),
)

# SALARY_TYPE
SALARY_TYPE_MONTHLY = 0
SALARY_TYPE_YEARLY = 1
SALARY_TYPE = ((SALARY_TYPE_MONTHLY, "Monthly"), (SALARY_TYPE_YEARLY, "Yearly"))

# Asset, Liability, Equity, Income, Expense
# GROUP_TYPE
GROUP_TYPE_ASSET = 'asset'
GROUP_TYPE_LIABILITY = 'liabilities'
GROUP_TYPE_INCOME = 'income'
GROUP_TYPE_EXPENSE = 'expense'

GROUP_TYPE = (
    (GROUP_TYPE_ASSET, "Asset"),
    (GROUP_TYPE_LIABILITY, "Liabilities"),
    (GROUP_TYPE_INCOME, "Income"),
    (GROUP_TYPE_EXPENSE, "Expense"),
)
# PAYMENT_MODE
PAYMENT_MODE_CASH = 1
PAYMENT_MODE_CARD = 2
PAYMENT_MODE_WALLET = 3
PAYMENT_MODE_NET_BANKING = 4
PAYMENT_MODE_NET_UPI = 5
PAYMENT_MODE = (
    (PAYMENT_MODE_CASH, "Cash"),
    (PAYMENT_MODE_CARD, "Card"),
    (PAYMENT_MODE_WALLET, "Wallet"),
    (PAYMENT_MODE_NET_BANKING, "Net Banking"),
    (PAYMENT_MODE_NET_UPI, "UPI"),
)

BILLABLE_YES = 1
BILLABLE_NO = 2
BILLABLE_LIST = ((BILLABLE_YES, "Yes"), (BILLABLE_NO, "No"))

# RESIGN_TYPE
RESIGN_TYPE_RESIGNED = 1
RESIGN_TYPE_TERMINATION = 2
RESIGN_TYPE_ABSCONDING = 3
RESIGN_TYPE = (
    (RESIGN_TYPE_RESIGNED, "Resigned"),
    (RESIGN_TYPE_TERMINATION, "Termination"),
    (RESIGN_TYPE_ABSCONDING, "Absconding"),
)

# Resign Reason
RESIGN_REASON_PERSONAL = 0
RESIGN_REASON_HIGH_SALARY = 1
RESIGN_REASON_PREFERRED_LOCATION = 2
RESIGN_REASON_HEALTH = 3
RESIGN_REASON_BETTER_GROWTH = 4
RESIGN_REASON_PERFORMANCE_RELATED = 5
RESIGN_REASON_DISCIPLINARY_ISSUE = 6
RESIGN_REASON = (
    (RESIGN_REASON_PERSONAL, "Personal"),
    (RESIGN_REASON_HIGH_SALARY, "High Salary"),
    (RESIGN_REASON_PREFERRED_LOCATION, "Preferred Location"),
    (RESIGN_REASON_HEALTH, "Health"),
    (RESIGN_REASON_BETTER_GROWTH, "Better Growth"),
    (RESIGN_REASON_PERFORMANCE_RELATED, "Performance Related"),
    (RESIGN_REASON_DISCIPLINARY_ISSUE, "Disciplinary Issue"),
)
# ACCOUNT_TYPE
ACCOUNT_TYPE_ACCOUNT = 1
ACCOUNT_TYPE_ACCOUNT_TYPE = 2
ACCOUNT_TYPE = ((ACCOUNT_TYPE_ACCOUNT, "Account"), (ACCOUNT_TYPE_ACCOUNT_TYPE, "Account Type"))
COUNTRY_DICT = {
    "AF": "Afghanistan",
    "AL": "Albania",
    "DZ": "Algeria",
    "AS": "American Samoa",
    "AD": "Andorra",
    "AO": "Angola",
    "AI": "Anguilla",
    "AQ": "Antarctica",
    "AG": "Antigua and Barbuda",
    "AR": "Argentina",
    "AM": "Armenia",
    "AW": "Aruba",
    "AU": "Australia",
    "AT": "Austria",
    "AZ": "Azerbaijan",
    "BS": "Bahamas",
    "BH": "Bahrain",
    "BD": "Bangladesh",
    "BB": "Barbados",
    "BY": "Belarus",
    "BE": "Belgium",
    "BZ": "Belize",
    "BJ": "Benin",
    "BM": "Bermuda",
    "BT": "Bhutan",
    "BO": "Bolivia, Plurinational State of bolivia",
    "BA": BOSNIA_AND_HERZEGOVINA,
    "BW": "Botswana",
    "BV": "Bouvet Island",
    "BR": "Brazil",
    "BN": "Brunei Darussalam",
    "BG": "Bulgaria",
    "BF": "Burkina Faso",
    "BI": "Burundi",
    "KH": "Cambodia",
    "CM": "Cameroon",
    "CA": "Canada",
    "CV": "Cape Verde",
    "KY": "Cayman Islands",
    "CF": "Central African Republic",
    "TD": "Chad",
    "CL": "Chile",
    "CN": "China",
    "CX": "Christmas Island",
    "CC": "Cocos (Keeling) Islands",
    "CO": "Colombia",
    "KM": "Comoros",
    "CG": "Congo",
    "CD": "Congo, The Democratic Republic of the Congo",
    "CK": "Cook Islands",
    "CR": "Costa Rica",
    "CI": "Cote d'Ivoire",
    "HR": "Croatia",
    "CU": "Cuba",
    "CY": "Cyprus",
    "CZ": "Czech Republic",
    "DK": "Denmark",
    "DJ": "Djibouti",
    "DM": "Dominica",
    "DO": "Dominican Republic",
    "EC": "Ecuador",
    "EG": "Egypt",
    "SV": "El Salvador",
    "GQ": "Equatorial Guinea",
    "ER": "Eritrea",
    "EE": "Estonia",
    "ET": "Ethiopia",
    "FK": "Falkland Islands (Malvinas)",
    "FO": "Faroe Islands",
    "FJ": "Fiji",
    "FI": "Finland",
    "FR": "France",
    "GF": "French Guiana",
    "PF": "French Polynesia",
    "TF": "French Southern Territories",
    "GA": "Gabon",
    "GM": "Gambia",
    "GE": "Georgia",
    "DE": "Germany",
    "GH": "Ghana",
    "GI": "Gibraltar",
    "GR": "Greece",
    "GL": "Greenland",
    "GD": "Grenada",
    "GP": "Guadeloupe",
    "GU": "Guam",
    "GT": "Guatemala",
    "GG": "Guernsey",
    "GN": "Guinea",
    "GW": "Guinea-Bissau",
    "GY": "Guyana",
    "HT": "Haiti",
    "HM": "Heard Island and Mcdonald Islands",
    "VA": "Holy See (Vatican City State)",
    "HN": "Honduras",
    "HK": "Hong Kong",
    "HU": "Hungary",
    "IS": "Iceland",
    "IN": "India",
    "ID": "Indonesia",
    "IR": "Iran, Islamic Republic of Persian Gulf",
    "IQ": "Iraq",
    "IE": "Ireland",
    "IM": "Isle of Man",
    "IL": "Israel",
    "IT": "Italy",
    "JM": "Jamaica",
    "JP": "Japan",
    "JE": "Jersey",
    "JO": "Jordan",
    "KZ": "Kazakhstan",
    "KE": "Kenya",
    "KI": "Kiribati",
    "KP": "Korea, Democratic People's Republic of Korea",
    "KR": "Korea, Republic of South Korea",
    "XK": "Kosovo",
    "KW": "Kuwait",
    "KG": "Kyrgyzstan",
    "LA": "Laos",
    "LV": "Latvia",
    "LB": "Lebanon",
    "LS": "Lesotho",
    "LR": "Liberia",
    "LY": "Libyan Arab Jamahiriya",
    "LI": "Liechtenstein",
    "LT": "Lithuania",
    "LU": "Luxembourg",
    "MO": "Macao",
    "MK": "Macedonia",
    "MG": "Madagascar",
    "MW": "Malawi",
    "MY": "Malaysia",
    "MV": "Maldives",
    "ML": "Mali",
    "MT": "Malta",
    "MH": "Marshall Islands",
    "MQ": "Martinique",
    "MR": "Mauritania",
    "MU": "Mauritius",
    "YT": "Mayotte",
    "MX": "Mexico",
    "FM": "Micronesia, Federated States of Micronesia",
    "MD": "Moldova",
    "MC": "Monaco",
    "MN": "Mongolia",
    "ME": "Montenegro",
    "MS": "Montserrat",
    "MA": "Morocco",
    "MZ": "Mozambique",
    "MM": "Myanmar",
    "NA": "Namibia",
    "NR": "Nauru",
    "NP": "Nepal",
    "NL": "Netherlands",
    "AN": "Netherlands Antilles",
    "NC": "New Caledonia",
    "NZ": "New Zealand",
    "NI": "Nicaragua",
    "NE": "Niger",
    "NG": "Nigeria",
    "NU": "Niue",
    "NF": "Norfolk Island",
    "MP": "Northern Mariana Islands",
    "NO": "Norway",
    "OM": "Oman",
    "PK": "Pakistan",
    "PW": "Palau",
    "PS": "Palestinian Territory, Occupied",
    "PA": "Panama",
    "PG": "Papua New Guinea",
    "PY": "Paraguay",
    "PE": "Peru",
    "PH": "Philippines",
    "PN": "Pitcairn",
    "PL": "Poland",
    "PT": "Portugal",
    "PR": "Puerto Rico",
    "QA": "Qatar",
    "RO": "Romania",
    "RU": "Russia",
    "RW": "Rwanda",
    "RE": "Reunion",
    "BL": "Saint Barthelemy",
    "SH": "Saint Helena, Ascension and Tristan Da Cunha",
    "KN": "Saint Kitts and Nevis",
    "LC": "Saint Lucia",
    "MF": "Saint Martin",
    "PM": "Saint Pierre and Miquelon",
    "VC": "Saint Vincent and the Grenadines",
    "WS": "Samoa",
    "SM": "San Marino",
    "ST": "Sao Tome and Principe",
    "SA": "Saudi Arabia",
    "SN": "Senegal",
    "RS": "Serbia",
    "SC": "Seychelles",
    "SL": "Sierra Leone",
    "SG": "Singapore",
    "SK": "Slovakia",
    "SI": "Slovenia",
    "SB": "Solomon Islands",
    "SO": "Somalia",
    "ZA": "South Africa",
    "SS": "South Sudan",
    "GS": "South Georgia and the South Sandwich Islands",
    "ES": "Spain",
    "LK": "Sri Lanka",
    "SD": "Sudan",
    "SR": "Suriname",
    "SJ": "Svalbard and Jan Mayen",
    "SZ": "Swaziland",
    "SE": "Sweden",
    "CH": "Switzerland",
    "SY": "Syrian Arab Republic",
    "TW": "Taiwan",
    "TJ": "Tajikistan",
    "TZ": "Tanzania, United Republic of Tanzania",
    "TH": "Thailand",
    "TL": "Timor-Leste",
    "TG": "Togo",
    "TK": "Tokelau",
    "TO": "Tonga",
    "TT": "Trinidad and Tobago",
    "TN": "Tunisia",
    "TR": "Turkey",
    "TM": "Turkmenistan",
    "TC": "Turks and Caicos Islands",
    "TV": "Tuvalu",
    "UG": "Uganda",
    "UA": "Ukraine",
    "AE": "United Arab Emirates",
    "GB": "United Kingdom",
    "US": "United States",
    "UY": "Uruguay",
    "UZ": "Uzbekistan",
    "VU": "Vanuatu",
    "VE": "Venezuela, Bolivarian Republic of Venezuela",
    "VN": "Vietnam",
    "VG": "Virgin Islands, British",
    "VI": "Virgin Islands, U.S.",
    "WF": "Wallis and Futuna",
    "YE": "Yemen",
    "ZM": "Zambia",
    "ZW": "Zimbabwe",
}

DEDICATED_DURATION = (
    (1, "1 Month"),
    (2, "2 Month"),
    (3, "3 Month"),
    (4, "4 Month"),
    (5, "5 Month"),
    (6, "6 Month"),
    (7, "7 Month"),
    (8, "8 Month"),
    (9, "9 Month"),
    (10, "10 Month"),
    (11, "11 Month"),
    (12, "12 Month"),
)

# BUG TYPE
BUG_TYPE_CRITICAL = 1
BUG_TYPE_LOW = 2
BUG_TYPE = (
    (BUG_TYPE_CRITICAL, "Backlogs"),
    (BUG_TYPE_LOW, "Tasks"),
)

# BUG_STATUS
BUG_STATUS_OPEN = 1
BUG_STATUS_IN_PROGRESS = 2
BUG_STATUS_RESOLVED = 3
BUG_STATUS_TESTING = 4
BUG_STATUS_CLOSED = 5
BUG_STATUS_REOPEN = 6
BUG_STATUS = (
    (BUG_STATUS_OPEN, "Open"),
    (BUG_STATUS_IN_PROGRESS, "In Progress"),
    (BUG_STATUS_RESOLVED, "Resolved"),
    (BUG_STATUS_TESTING, "Testing"),
    (BUG_STATUS_CLOSED, "Closed"),
    (BUG_STATUS_REOPEN, "Reopen"),
)

"""
Pricing plan status
"""
PRICING_PLAN_DUE = 1
PRICING_PLAN_PAID = 2
PRICING_PLAN_STATUS = ((PRICING_PLAN_DUE, "Due"), (PRICING_PLAN_PAID, "Paid"))

"""
TEMPLATE PAGE TYPE
"""
PROJECT_DOCUMENT = 1
OTHER_PROJECT = 2
PAGE_TYPE = (
    (PROJECT_DOCUMENT, "Document"),
    (OTHER_PROJECT, "Other"),
)

"""
CONFIG TYPE
"""
CONFIG_MODULE_TYPE_LEAVE_PLAN = 1
CONFIG_MODULE_TYPE = ((CONFIG_MODULE_TYPE_LEAVE_PLAN, "Leave Plan"),)

CONFIG_FIELD_TYPE_TEXT_BOX = 1
CONFIG_FIELD_TYPE_RADIO = 2
CONFIG_FIELD_TYPE_DROPDOWN = 3
CONFIG_FIELD_TYPE = (
    (CONFIG_FIELD_TYPE_TEXT_BOX, "Textbox"),
    (CONFIG_FIELD_TYPE_RADIO, "Radio"),
    (CONFIG_FIELD_TYPE_DROPDOWN, "Dropdown"),
)
"""
WORKFLOW TYPE
"""
WORKFLOW_STATUS_TODOLIST = 1
WORKFLOW_STATUS_IN_PROGRESS = 2
WORKFLOW_STATUS_DONE = 3
WORKFLOW_TYPE = (
    (WORKFLOW_STATUS_TODOLIST, "TodoList"),
    (WORKFLOW_STATUS_IN_PROGRESS, "In-Progress"),
    (WORKFLOW_STATUS_DONE, "Done"),
)

"""
ASSIGN DURATION
"""

MONTHLY = 1
YEARLY = 2
ASSIGN_DURATION = ((MONTHLY, "Monthly"), (YEARLY, "Yearly"))

"""
PROBATION LEAVE TYPE
"""

PROBATION_PAID_LEAVE = 1
PROBATION_UNPAID_LEAVE = 2
PROBATION_LEAVE_TYPE = ((PROBATION_PAID_LEAVE, "Paid Leave"), (PROBATION_UNPAID_LEAVE, "Unpaid Leave"))

"""
RESIGN LEAVE TYPE 
"""

FREEZE = 1
NOT_FREEZE = 2
RESIGN_LEAVE_TYPE = ((FREEZE, "Freeze"), (NOT_FREEZE, "Not Freeze"))

"""
Reset Leave Balance
"""

RESET_LEAVE_NEVER = 1
RESET_LEAVE_YEARLY = 2
RESET_LEAVE_BALANCE = (
    (RESET_LEAVE_NEVER, "Never"),
    (RESET_LEAVE_YEARLY, "Yearly"),
)
"""
Workflow Priority
"""

WORKFLOW_PRIORITY_TODOLIST = 1
WORKFLOW_PRIORITY_IN_PROGRESS = 2
WORKFLOW_PRIORITY_DONE = 3
WORKFLOW_PRIORITY = (
    (WORKFLOW_PRIORITY_TODOLIST, 1),
    (WORKFLOW_PRIORITY_IN_PROGRESS, 2),
    (WORKFLOW_PRIORITY_DONE, 100),
)

"""
Workflow color code
"""
WORKFLOW_COLOR_CODE_TODOLIST = 1
WORKFLOW_COLOR_CODE_IN_PROGRESS = 2
WORKFLOW_COLOR_CODE_DONE = 3
WORKFLOW_COLOR_CODE = (
    (WORKFLOW_COLOR_CODE_TODOLIST, "label-default"),
    (WORKFLOW_COLOR_CODE_IN_PROGRESS, "label-primary"),
    (WORKFLOW_COLOR_CODE_DONE, "label-success"),
)

"""
Task Log Type
"""

LOG_TYPE_CREATE = 1
LOG_TYPE_UPDATE = 2
LOG_TYPE_DELETE = 3
LOG_TYPE_STATUS_UPDATE = 4
TASK_LOG_TYPE = (
    (LOG_TYPE_CREATE, "Create"),
    (LOG_TYPE_UPDATE, "Update"),
    (LOG_TYPE_DELETE, "Delete"),
    (LOG_TYPE_STATUS_UPDATE, "Status"),
)

"""
Task Due
"""
IS_DUE = 1
IS_NOT_DUE = 2

TASK_DUE = (
    (IS_DUE, "Is Due"),
    (IS_NOT_DUE, "Not Due"),
)

PROJECT_WORKING_HOURS = 8

"""
HR constant for live
"""
PEERBITS_HR = ["62de864c8fbdd2000a38e0fa"]
YELOWSOFT_HR = ["62eb910b81763c000777b839"]
DIGIPAY_HR = ["62eb9f4a81763c000777cbb3"]

"""
LIVE Constant role
"""
USER_ROLE_EXECUTIVE = "605315671128e1321fefdece"
USER_ROLE_MANAGER = "6065612a1128e16d97ad5129"
USER_ROLE_ADMIN = "606561301128e16d97ad512e"
USER_ROLE_HR = "61c1725edbe81001a1e33b63"
USER_ROLE_IT_ADMIN = "62c6dd2ce8dd0800080e4b6c"

"""
KAFKA TOPIC
"""
KAFKA_ATTENDANC_PUNCH = "attendace_punch"
KAFKA_PAYROLL_ADD_DATA = "payroll_add_data"
KAFKA_ATTENDANC_SUMMARY = "attendace_summary"
KAFKA_ATTENDANC_SUMMARY_SCHEDULAR = "attendace_summary_schedular"
KAFKA_PAYROLL_ATTENDANC_EXPORT = "payroll_attendance_export"
KAFKA_UPDATE_ATTENDANCE = "update_attendance"
KAFKA_PAYROLL_ADD_DATA_V2 = "payroll_add_data_v2"

"""
Attendance type
"""
ATTENDANCE_TYPE_IN = 1
ATTENDANCE_TYPE_OUT = 2
ATTENDANCE_TYPE = ((ATTENDANCE_TYPE_IN, "In"), (ATTENDANCE_TYPE_OUT, "Out"))

ATTENDANCE_STATUS_PENDING = 1
ATTENDANCE_STATUS_APPROVED = 2
ATTENDANCE_STATUS_REJECTED = 3
ATTENDANCE_STATUS_CANCEL = 4

ATTENDANCE_STATUS = (
    (ATTENDANCE_STATUS_PENDING, "Pending"),
    (ATTENDANCE_STATUS_APPROVED, "Approved"),
    (ATTENDANCE_STATUS_REJECTED, "Rejected"),
    (ATTENDANCE_STATUS_CANCEL, "Cancel"),
)

LOG_TYPE_WORKFROMHOME = 1
LOG_TYPE_REGULARIZE = 2
LOG_TYPE = ((LOG_TYPE_WORKFROMHOME, "Work Form Home"), (LOG_TYPE_REGULARIZE, "Regularize"))