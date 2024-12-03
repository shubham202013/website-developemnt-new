"""
Currency list
"""
dollar = '&#36;'
bgn = '&#1083;&#1074;'
dkk = '&#107;&#114;'
egp = '&#163;'
hnl = '&#76;'
irr = '&#65020;'
lkr = '&#8360;'

CURRENCY_CHOICES = (
    ('AED', '&#1583;.&#1573;'),
    ('AFN', '&#65;&#102;'),
    ('ALL', '&#76;&#101;&#107;'),
    ('ANG', '&#402;'),
    ('AOA', '&#75;&#122;'),
    ('ARS', dollar),
    ('AUD', dollar),
    ('AWG', '&#402;'),
    ('AZN', '&#1084;&#1072;&#1085;'),
    ('BAM', '&#75;&#77;'),
    ('BBD', dollar),
    ('BDT', '&#2547;'),
    ('BGN', bgn),
    ('BHD', '.&#1583;.&#1576;'),
    ('BIF', '&#70;&#66;&#117;'),
    ('BMD', dollar),
    ('BND', dollar),
    ('BOB', '&#36;&#98;'),
    ('BRL', '&#82;&#36;'),
    ('BSD', dollar),
    ('BTN', '&#78;&#117;&#46;'),
    ('BWP', '&#80;'),
    ('BYR', '&#112;&#46;'),
    ('BZD', '&#66;&#90;&#36;'),
    ('CAD', dollar),
    ('CDF', '&#70;&#67;'),
    ('CHF', '&#67;&#72;&#70;'),
    ('CLP', dollar),
    ('CNY', '&#165;'),
    ('COP', 'COP'),
    ('CRC', '&#8353;'),
    ('CUP', '&#8396;'),
    ('CVE', dollar),
    ('CZK', '&#75;&#269;'),
    ('DJF', '&#70;&#100;&#106;'),
    ('DKK', dkk),
    ('DOP', '&#82;&#68;&#36;'),
    ('DZD', '&#1583;&#1580;'),
    ('EGP', egp),
    ('ETB', '&#66;&#114;'),
    ('EUR', '&#8364;'),
    ('FJD', dollar),
    ('FKP', egp),
    ('GBP', egp),
    ('GEL', '&#4314;'),
    ('GHS', '&#162;'),
    ('GIP', egp),
    ('GMD', '&#68;'),
    ('GNF', '&#70;&#71;'),
    ('GTQ', '&#81;'),
    ('GYD', dollar),
    ('HKD', dollar),
    ('HNL', hnl),
    ('HRK', '&#107;&#110;'),
    ('HTG', '&#71;'),
    ('HUF', '&#70;&#116;'),
    ('IDR', '&#82;&#112;'),
    ('ILS', '&#8362;'),
    ('INR', '&#8377;'),
    ('IQD', '&#1593;.&#1583;'),
    ('IRR', irr),
    ('ISK', dkk),
    ('JEP', egp),
    ('JMD', '&#74;&#36;'),
    ('JOD', '&#74;&#68;'),
    ('JPY', '&#165;'),
    ('KES', '&#75;&#83;&#104;'),
    ('KGS', bgn),
    ('KHR', '&#6107;'),
    ('KMF', '&#67;&#70;'),
    ('KPW', '&#8361;'),
    ('KRW', '&#8361;'),
    ('KWD', '&#1583;.&#1603;'),
    ('KYD', dollar),
    ('KZT', bgn),
    ('LAK', '&#8365;'),
    ('LBP', egp),
    ('LKR', lkr),
    ('LRD', dollar),
    ('LSL', hnl),
    ('LTL', '&#76;&#116;'),
    ('LVL', '&#76;&#115;'),
    ('LYD', '&#1604;.&#1583;'),
    ('MAD', '&#1583;.&#1605;.'),
    ('MDL', hnl),
    ('MGA', '&#65;&#114;'),
    ('MKD', '&#1076;&#1077;&#1085;'),
    ('MMK', '&#75;'),
    ('MNT', '&#8366;'),
    ('MOP', '&#77;&#79;&#80;&#36;'),
    ('MRO', '&#85;&#77;'),
    ('MUR', lkr),
    ('MVR', '.&#1923;'),
    ('MWK', '&#77;&#75;'),
    ('MXN', dollar),
    ('MYR', '&#82;&#77;'),
    ('MZN', '&#77;&#84;'),
    ('NAD', dollar),
    ('NGN', '&#8358;'),
    ('NIO', '&#67;&#36;'),
    ('NOK', dkk),
    ('NPR', lkr),
    ('NZD', dollar),
    ('OMR', irr),
    ('PAB', '&#66;&#47;&#46;'),
    ('PEN', '&#83;&#47;&#46;'),
    ('PGK', '&#75;'),
    ('PHP', 'PHP'),
    ('PKR', lkr),
    ('PLN', '&#122;&#322;'),
    ('PYG', '&#71;&#115;'),
    ('QAR', irr),
    ('RON', '&#108;&#101;&#105;'),
    ('RSD', '&#1044;&#1080;&#1085;&#46;'),
    ('RUB', '&#1088;&#1091;&#1073;'),
    ('RWF', '&#1585;.&#1587;'),
    ('SAR', irr),
    ('SBD', dollar),
    ('SCR', lkr),
    ('SDG', 'SDG'),
    ('SEK', dkk),
    ('SGD', dollar),
    ('SHP', egp),
    ('SLL', '&#76;&#101;'),
    ('SOS', '&#83;'),
    ('SRD', dollar),
    ('STD', '&#68;&#98;'),
    ('SVC', dollar),
    ('SYP', egp),
    ('SZL', hnl),
    ('THB', '&#3647;'),
    ('TJS', '&#84;&#74;&#83;'),
    ('TMT', '&#109;'),
    ('TND', '&#1583;.&#1578;'),
    ('TOP', '&#84;&#36;'),
    ('TRY', '&#8356;'),
    ('TTD', dollar),
    ('TWD', '&#78;&#84;&#36;'),
    ('UAH', '&#8372;'),
    ('UGX', '&#85;&#83;&#104;'),
    ('USD', dollar),
    ('UYU', '&#36;&#85;'),
    ('UZS', bgn),
    ('VEF', '&#66;&#115;'),
    ('VND', '&#8363;'),
    ('VUV', '&#86;&#84;'),
    ('WST', '&#87;&#83;&#36;'),
    ('XAF', '&#70;&#67;&#70;&#65;'),
    ('XCD', dollar),
    ('XPF', '&#70;'),
    ('YER', irr),
    ('ZAR', '&#82;'),
    ('ZMK', '&#90;&#75;'),
    ('ZWL', '&#90;&#36;'),

)

"""
Timezone list
"""
pacific_midway = 'Pacific/Midway'
us_samoa = 'US/Samoa'
us_hawaii = 'US/Hawaii'
us_alaska = 'US/Alaska'
us_pacific = 'US/Pacific'
america_tijuana = 'America/Tijuana'
us_arizona = 'US/Arizona'
us_mountain = 'US/Mountain'
america_chihuahua = 'America/Chihuahua'
america_mazatlan = 'America/Mazatlan'
america_mexico_city = 'America/Mexico_City'
america_monterrey = 'America/Monterrey'
canada_saskatchewan = 'Canada/Saskatchewan'
us_central = 'US/Central'
america_new_york = 'America/New_York'
us_east_indiana = 'US/East-Indiana'
america_bogota = 'America/Bogota'
america_lima = 'America/Lima'
america_caracas = 'America/Caracas'
canada_atlantic = 'Canada/Atlantic'
america_la_paz = 'America/La_Paz'
america_santiago = 'America/Santiago'
canada_newfoundland = 'Canada/Newfoundland'
america_buenos_aires = 'America/Buenos_Aires'
greenland = 'Greenland'
atlantic_stanley = 'Atlantic/Stanley'
atlantic_azores = 'Atlantic/Azores'
atlantic_cape_verde = 'Atlantic/Cape_Verde'
africa_casablanca = 'Africa/Casablanca'
europe_dublin = 'Europe/Dublin'
europe_lisbon = 'Europe/Lisbon'
europe_london = 'Europe/London'
europe_tirane = 'Europe/Tirane'
africa_monrovia = 'Africa/Monrovia'
europe_amsterdam = 'Europe/Amsterdam'
europe_belgrade = 'Europe/Belgrade'
europe_berlin = 'Europe/Berlin'
europe_bratislava = 'Europe/Bratislava'
europe_brussels = 'Europe/Brussels'
europe_budapest = 'Europe/Budapest'
europe_copenhagen = 'Europe/Copenhagen'
europe_ljubljana = 'Europe/Ljubljana'
europe_madrid = 'Europe/Madrid'
europe_paris = 'Europe/Paris'
europe_prague = 'Europe/Prague'
europe_rome = 'Europe/Rome'
europe_sarajevo = 'Europe/Sarajevo'
europe_skopje = 'Europe/Skopje'
europe_stockholm = 'Europe/Stockholm'
europe_vienna = 'Europe/Vienna'
europe_warsaw = 'Europe/Warsaw'
europe_zagreb = 'Europe/Zagreb'
europe_athens = 'Europe/Athens'
europe_bucharest = 'Europe/Bucharest'
africa_cairo = 'Africa/Cairo'
africa_harare = 'Africa/Harare'
europe_helsinki = 'Europe/Helsinki'
europe_istanbul = 'Europe/Istanbul'
asia_jerusalem = 'Asia/Jerusalem'
europe_kiev = 'Europe/Kiev'
europe_minsk = 'Europe/Minsk'
europe_riga = 'Europe/Riga'
europe_sofia = 'Europe/Sofia'
europe_tallinn = 'Europe/Tallinn'
europe_vilnius = 'Europe/Vilnius'
asia_baghdad = 'Asia/Baghdad'
asia_kuwait = 'Asia/Kuwait'
africa_nairobi = 'Africa/Nairobi'
asia_riyadh = 'Asia/Riyadh'
europe_moscow = 'Europe/Moscow'
asia_tehran = 'Asia/Tehran'
asia_baku = 'Asia/Baku'
europe_volgograd = 'Europe/Volgograd'
asia_muscat = 'Asia/Muscat'
asia_tbilisi = 'Asia/Tbilisi'
asia_yerevan = 'Asia/Yerevan'
asia_kabul = 'Asia/Kabul'
asia_karachi = 'Asia/Karachi'
asia_tashkent = 'Asia/Tashkent'
asia_kolkata = 'Asia/Kolkata'
asia_kathmandu = 'Asia/Kathmandu'
asia_yekaterinburg = 'Asia/Yekaterinburg'
asia_almaty = 'Asia/Almaty'
asia_dhaka = 'Asia/Dhaka'
asia_novosibirsk = 'Asia/Novosibirsk'
asia_bangkok = 'Asia/Bangkok'
asia_jakarta = 'Asia/Jakarta'
asia_krasnoyarsk = 'Asia/Krasnoyarsk'
asia_chongqing = 'Asia/Chongqing'
asia_hong_kong = 'Asia/Hong_Kong'
asia_kuala_lumpur = 'Asia/Kuala_Lumpur'
australia_perth = 'Australia/Perth'
asia_singapore = 'Asia/Singapore'
asia_taipei = 'Asia/Taipei'
asia_ulaanbaatar = 'Asia/Ulaanbaatar'
asia_urumqi = 'Asia/Urumqi'
asia_irkutsk = 'Asia/Irkutsk'
asia_seoul = 'Asia/Seoul'
asia_tokyo = 'Asia/Tokyo'
australia_adelaide = 'Australia/Adelaide'
australia_darwin = 'Australia/Darwin'
asia_yakutsk = 'Asia/Yakutsk'
australia_brisbane = 'Australia/Brisbane'
australia_canberra = 'Australia/Canberra'
pacific_guam = 'Pacific/Guam'
Australia_hobart = 'Australia/Hobart'
Australia_melbourne = 'Australia/Melbourne'
Pacific_port_moresby = 'Pacific/Port_Moresby'
Australia_sydney = 'Australia/Sydney'
asia_vladivostok = 'Asia/Vladivostok'
asia_magadan = 'Asia/Magadan'
pacific_auckland = 'Pacific/Auckland'
pacific_fiji = 'Pacific/Fiji'

TIME_M_11_00 = "-11:00"
TIME_M_08_00 = "-08:00"
TIME_M_07_00 = "-07:00"
TIME_M_06_00 = "-06:00"
TIME_M_05_00 = "-05:00"
TIME_M_04_00 = "-04:00"
TIME_M_03_00 = "-03:00"
TIME_M_01_00 = "-01:00"
TIME_P_01_00 = "+01:00"
TIME_P_02_00 = "+02:00"
TIME_P_03_00 = "+03:00"
TIME_P_04_00 = "+04:00"
TIME_P_05_00 = "+05:00"
TIME_P_06_00 = "+06:00"
TIME_P_07_00 = "+07:00"
TIME_P_08_00 = "+08:00"
TIME_P_09_00 = "+09:00"
TIME_P_10_00 = "+10:00"
TIME_P_12_00 = "+12:00"

TIMEZONE_OFFSET_CHOICES = (
    (pacific_midway, TIME_M_11_00),
    (us_samoa, TIME_M_11_00),
    (us_hawaii, "-10:00"),
    (us_alaska, "-09:00"),
    (us_pacific, TIME_M_08_00),
    (america_tijuana, TIME_M_08_00),
    (us_arizona, TIME_M_07_00),
    (us_mountain, TIME_M_07_00),
    (america_chihuahua, TIME_M_07_00),
    (america_mazatlan, TIME_M_07_00),
    (america_mexico_city, TIME_M_06_00),
    (america_monterrey, TIME_M_06_00),
    (canada_saskatchewan, TIME_M_06_00),
    (us_central, TIME_M_06_00),
    (america_new_york, TIME_M_05_00),
    (us_east_indiana, TIME_M_05_00),
    (america_bogota, TIME_M_05_00),
    (america_lima, TIME_M_05_00),
    (america_caracas, "-04:30"),
    (canada_atlantic, TIME_M_04_00),
    (america_la_paz, TIME_M_04_00),
    (america_santiago, TIME_M_04_00),
    (canada_newfoundland, "-03:30"),
    (america_buenos_aires, TIME_M_03_00),
    (greenland, TIME_M_03_00),
    (atlantic_stanley, "-02:00"),
    (atlantic_azores, TIME_M_01_00),
    (atlantic_cape_verde, TIME_M_01_00),
    (africa_casablanca, "00:00"),
    (europe_dublin, "00:00"),
    (europe_lisbon, "00:00"),
    (europe_london, "00:00"),
    (europe_tirane, TIME_P_02_00),
    (africa_monrovia, "00:00"),
    (europe_amsterdam, TIME_P_01_00),
    (europe_belgrade, TIME_P_01_00),
    (europe_berlin, TIME_P_01_00),
    (europe_bratislava, TIME_P_01_00),
    (europe_brussels, TIME_P_01_00),
    (europe_budapest, TIME_P_01_00),
    (europe_copenhagen, TIME_P_01_00),
    (europe_ljubljana, TIME_P_01_00),
    (europe_madrid, TIME_P_01_00),
    (europe_paris, TIME_P_01_00),
    (europe_prague, TIME_P_01_00),
    (europe_rome, TIME_P_01_00),
    (europe_sarajevo, TIME_P_01_00),
    (europe_skopje, TIME_P_01_00),
    (europe_stockholm, TIME_P_01_00),
    (europe_vienna, TIME_P_01_00),
    (europe_warsaw, TIME_P_01_00),
    (europe_zagreb, TIME_P_01_00),
    (europe_athens, TIME_P_02_00),
    (europe_bucharest, TIME_P_02_00),
    (africa_cairo, TIME_P_02_00),
    (africa_harare, TIME_P_02_00),
    (europe_helsinki, TIME_P_02_00),
    (europe_istanbul, TIME_P_02_00),
    (asia_jerusalem, TIME_P_02_00),
    (europe_kiev, TIME_P_02_00),
    (europe_minsk, TIME_P_02_00),
    (europe_riga, TIME_P_02_00),
    (europe_sofia, TIME_P_02_00),
    (europe_tallinn, TIME_P_02_00),
    (europe_vilnius, TIME_P_02_00),
    (asia_baghdad, TIME_P_03_00),
    (asia_kuwait, TIME_P_03_00),
    (africa_nairobi, TIME_P_03_00),
    (asia_riyadh, TIME_P_03_00),
    (europe_moscow, TIME_P_03_00),
    (asia_tehran, "+03:30"),
    (asia_baku, TIME_P_04_00),
    (europe_volgograd, TIME_P_04_00),
    (asia_muscat, TIME_P_04_00),
    (asia_tbilisi, TIME_P_04_00),
    (asia_yerevan, TIME_P_04_00),
    (asia_kabul, "+04:30"),
    (asia_karachi, TIME_P_05_00),
    (asia_tashkent, TIME_P_05_00),
    (asia_kolkata, "+05:30"),
    (asia_kathmandu, "+05:45"),
    (asia_yekaterinburg, TIME_P_06_00),
    (asia_almaty, TIME_P_06_00),
    (asia_dhaka, TIME_P_06_00),
    (asia_novosibirsk, TIME_P_07_00),
    (asia_bangkok, TIME_P_07_00),
    (asia_jakarta, TIME_P_07_00),
    (asia_krasnoyarsk, TIME_P_08_00),
    (asia_chongqing, TIME_P_08_00),
    (asia_hong_kong, TIME_P_08_00),
    (asia_kuala_lumpur, TIME_P_08_00),
    (australia_perth, TIME_P_08_00),
    (asia_singapore, TIME_P_08_00),
    (asia_taipei, TIME_P_08_00),
    (asia_ulaanbaatar, TIME_P_08_00),
    (asia_urumqi, TIME_P_08_00),
    (asia_irkutsk, TIME_P_09_00),
    (asia_seoul, TIME_P_09_00),
    (asia_tokyo, TIME_P_09_00),
    (australia_adelaide, "+09:30"),
    (australia_darwin, "+09:30"),
    (asia_yakutsk, TIME_P_10_00),
    (australia_brisbane, TIME_P_10_00),
    (australia_canberra, TIME_P_10_00),
    (pacific_guam, TIME_P_10_00),
    (Australia_hobart, TIME_P_10_00),
    (Australia_melbourne, TIME_P_10_00),
    (Pacific_port_moresby, TIME_P_10_00),
    (Australia_sydney, TIME_P_10_00),
    (asia_vladivostok, "+11:00"),
    (asia_magadan, TIME_P_12_00),
    (pacific_auckland, TIME_P_12_00),
    (pacific_fiji, TIME_P_12_00),
)
TIMEZONE_CHOICES = (
    (pacific_midway, "(GMT-11:00) Midway Island"),
    (us_samoa, "(GMT-11:00) Samoa"),
    (us_hawaii, "(GMT-10:00) Hawaii"),
    (us_alaska, "(GMT-09:00) Alaska"),
    (us_pacific, "(GMT-08:00) Pacific Time (US &amp; Canada)"),
    (america_tijuana, "(GMT-08:00) Tijuana"),
    (us_arizona, "(GMT-07:00) Arizona"),
    (us_mountain, "(GMT-07:00) Mountain Time (US &amp; Canada)"),
    (america_chihuahua, "(GMT-07:00) Chihuahua"),
    (america_mazatlan, "(GMT-07:00) Mazatlan"),
    (america_mexico_city, "(GMT-06:00) Mexico City"),
    (america_monterrey, "(GMT-06:00) Monterrey"),
    (canada_saskatchewan, "(GMT-06:00) Saskatchewan"),
    (us_central, "(GMT-06:00) Central Time (US &amp; Canada)"),
    (america_new_york, "(GMT-05:00) Eastern Time (US & Canada)"),
    (us_east_indiana, "(GMT-05:00) Indiana (East)"),
    (america_bogota, "(GMT-05:00) Bogota"),
    (america_lima, "(GMT-05:00) Lima"),
    (america_caracas, "(GMT-04:30) Caracas"),
    (canada_atlantic, "(GMT-04:00) Atlantic Time (Canada)"),
    (america_la_paz, "(GMT-04:00) La Paz"),
    (america_santiago, "(GMT-04:00) Santiago"),
    (canada_newfoundland, "(GMT-03:30) Newfoundland"),
    (america_buenos_aires, "(GMT-03:00) Buenos Aires"),
    (greenland, "(GMT-03:00) Greenland"),
    (atlantic_stanley, "(GMT-02:00) Stanley"),
    (atlantic_azores, "(GMT-01:00) Azores"),
    (atlantic_cape_verde, "(GMT-01:00) Cape Verde Is."),
    (africa_casablanca, "(GMT) Casablanca"),
    (europe_dublin, "(GMT) Dublin"),
    (europe_lisbon, "(GMT) Lisbon"),
    (europe_london, "(GMT) London"),
    (europe_tirane, "(GMT+02:00) Europe"),
    (africa_monrovia, "(GMT) Monrovia"),
    (europe_amsterdam, "(GMT+01:00) Amsterdam"),
    (europe_belgrade, "(GMT+01:00) Belgrade"),
    (europe_berlin, "(GMT+01:00) Berlin"),
    (europe_bratislava, "(GMT+01:00) Bratislava"),
    (europe_brussels, "(GMT+01:00) Brussels"),
    (europe_budapest, "(GMT+01:00) Budapest"),
    (europe_copenhagen, "(GMT+01:00) Copenhagen"),
    (europe_ljubljana, "(GMT+01:00) Ljubljana"),
    (europe_madrid, "(GMT+01:00) Madrid"),
    (europe_paris, "(GMT+01:00) Paris"),
    (europe_prague, "(GMT+01:00) Prague"),
    (europe_rome, "(GMT+01:00) Rome"),
    (europe_sarajevo, "(GMT+01:00) Sarajevo"),
    (europe_skopje, "(GMT+01:00) Skopje"),
    (europe_stockholm, "(GMT+01:00) Stockholm"),
    (europe_vienna, "(GMT+01:00) Vienna"),
    (europe_warsaw, "(GMT+01:00) Warsaw"),
    (europe_zagreb, "(GMT+01:00) Zagreb"),
    (europe_athens, "(GMT+02:00) Athens"),
    (europe_bucharest, "(GMT+02:00) Bucharest"),
    (africa_cairo, "(GMT+02:00) Cairo"),
    (africa_harare, "(GMT+02:00) Harare"),
    (europe_helsinki, "(GMT+02:00) Helsinki"),
    (europe_istanbul, "(GMT+02:00) Istanbul"),
    (asia_jerusalem, "(GMT+02:00) Jerusalem"),
    (europe_kiev, "(GMT+02:00) Kyiv"),
    (europe_minsk, "(GMT+02:00) Minsk"),
    (europe_riga, "(GMT+02:00) Riga"),
    (europe_sofia, "(GMT+02:00) Sofia"),
    (europe_tallinn, "(GMT+02:00) Tallinn"),
    (europe_vilnius, "(GMT+02:00) Vilnius"),
    (asia_baghdad, "(GMT+03:00) Baghdad"),
    (asia_kuwait, "(GMT+03:00) Kuwait"),
    (africa_nairobi, "(GMT+03:00) Nairobi"),
    (asia_riyadh, "(GMT+03:00) Riyadh"),
    (europe_moscow, "(GMT+03:00) Moscow"),
    (asia_tehran, "(GMT+03:30) Tehran"),
    (asia_baku, "(GMT+04:00) Baku"),
    (europe_volgograd, "(GMT+04:00) Volgograd"),
    (asia_muscat, "(GMT+04:00) Muscat"),
    (asia_tbilisi, "(GMT+04:00) Tbilisi"),
    (asia_yerevan, "(GMT+04:00) Yerevan"),
    (asia_kabul, "(GMT+04:30) Kabul"),
    (asia_karachi, "(GMT+05:00) Karachi"),
    (asia_tashkent, "(GMT+05:00) Tashkent"),
    (asia_kolkata, "(GMT+05:30) Kolkata"),
    (asia_kathmandu, "(GMT+05:45) Kathmandu"),
    (asia_yekaterinburg, "(GMT+06:00) Ekaterinburg"),
    (asia_almaty, "(GMT+06:00) Almaty"),
    (asia_dhaka, "(GMT+06:00) Dhaka"),
    (asia_novosibirsk, "(GMT+07:00) Novosibirsk"),
    (asia_bangkok, "(GMT+07:00) Bangkok"),
    (asia_jakarta, "(GMT+07:00) Jakarta"),
    (asia_krasnoyarsk, "(GMT+08:00) Krasnoyarsk"),
    (asia_chongqing, "(GMT+08:00) Chongqing"),
    (asia_hong_kong, "(GMT+08:00) Hong Kong"),
    (asia_kuala_lumpur, "(GMT+08:00) Kuala Lumpur"),
    (australia_perth, "(GMT+08:00) Perth"),
    (asia_singapore, "(GMT+08:00) Singapore"),
    (asia_taipei, "(GMT+08:00) Taipei"),
    (asia_ulaanbaatar, "(GMT+08:00) Ulaan Bataar"),
    (asia_urumqi, "(GMT+08:00) Urumqi"),
    (asia_irkutsk, "(GMT+09:00) Irkutsk"),
    (asia_seoul, "(GMT+09:00) Seoul"),
    (asia_tokyo, "(GMT+09:00) Tokyo"),
    (australia_adelaide, "(GMT+09:30) Adelaide"),
    (australia_darwin, "(GMT+09:30) Darwin"),
    (asia_yakutsk, "(GMT+10:00) Yakutsk"),
    (australia_brisbane, "(GMT+10:00) Brisbane"),
    (australia_canberra, "(GMT+10:00) Canberra"),
    (pacific_guam, "(GMT+10:00) Guam"),
    (Australia_hobart, "(GMT+10:00) Hobart"),
    (Australia_melbourne, "(GMT+10:00) Melbourne"),
    (Pacific_port_moresby, "(GMT+10:00) Port Moresby"),
    (Australia_sydney, "(GMT+10:00) Sydney"),
    (asia_vladivostok, "(GMT+11:00) Vladivostok"),
    (asia_magadan, "(GMT+12:00) Magadan"),
    (pacific_auckland, "(GMT+12:00) Auckland"),
    (pacific_fiji, "(GMT+12:00) Fiji"),
)

"""
Source : https://gist.github.com/josephilipraja/8341837
"""
COUNTRY = {
    'AD': {'name': 'ANDORRA', 'code': '376'},
    'AE': {'name': 'UNITED ARAB EMIRATES', 'code': '971'},
    'AF': {'name': 'AFGHANISTAN', 'code': '93'},
    'AG': {'name': 'ANTIGUA AND BARBUDA', 'code': '1268'},
    'AI': {'name': 'ANGUILLA', 'code': '1264'},
    'AL': {'name': 'ALBANIA', 'code': '355'},
    'AM': {'name': 'ARMENIA', 'code': '374'},
    'AN': {'name': 'NETHERLANDS ANTILLES', 'code': '599'},
    'AO': {'name': 'ANGOLA', 'code': '244'},
    'AQ': {'name': 'ANTARCTICA', 'code': '672'},
    'AR': {'name': 'ARGENTINA', 'code': '54'},
    'AS': {'name': 'AMERICAN SAMOA', 'code': '1684'},
    'AT': {'name': 'AUSTRIA', 'code': '43'},
    'AU': {'name': 'AUSTRALIA', 'code': '61'},
    'AW': {'name': 'ARUBA', 'code': '297'},
    'AZ': {'name': 'AZERBAIJAN', 'code': '994'},
    'BA': {'name': 'BOSNIA AND HERZEGOVINA', 'code': '387'},
    'BB': {'name': 'BARBADOS', 'code': '1246'},
    'BD': {'name': 'BANGLADESH', 'code': '880'},
    'BE': {'name': 'BELGIUM', 'code': '32'},
    'BF': {'name': 'BURKINA FASO', 'code': '226'},
    'BG': {'name': 'BULGARIA', 'code': '359'},
    'BH': {'name': 'BAHRAIN', 'code': '973'},
    'BI': {'name': 'BURUNDI', 'code': '257'},
    'BJ': {'name': 'BENIN', 'code': '229'},
    'BL': {'name': 'SAINT BARTHELEMY', 'code': '590'},
    'BM': {'name': 'BERMUDA', 'code': '1441'},
    'BN': {'name': 'BRUNEI DARUSSALAM', 'code': '673'},
    'BO': {'name': 'BOLIVIA', 'code': '591'},
    'BR': {'name': 'BRAZIL', 'code': '55'},
    'BS': {'name': 'BAHAMAS', 'code': '1242'},
    'BT': {'name': 'BHUTAN', 'code': '975'},
    'BW': {'name': 'BOTSWANA', 'code': '267'},
    'BY': {'name': 'BELARUS', 'code': '375'},
    'BZ': {'name': 'BELIZE', 'code': '501'},
    'CA': {'name': 'CANADA', 'code': '1'},
    'CC': {'name': 'COCOS (KEELING) ISLANDS', 'code': '61'},
    'CD': {'name': 'CONGO, THE DEMOCRATIC REPUBLIC OF THE', 'code': '243'},
    'CF': {'name': 'CENTRAL AFRICAN REPUBLIC', 'code': '236'},
    'CG': {'name': 'CONGO', 'code': '242'},
    'CH': {'name': 'SWITZERLAND', 'code': '41'},
    'CI': {'name': 'COTE D IVOIRE', 'code': '225'},
    'CK': {'name': 'COOK ISLANDS', 'code': '682'},
    'CL': {'name': 'CHILE', 'code': '56'},
    'CM': {'name': 'CAMEROON', 'code': '237'},
    'CN': {'name': 'CHINA', 'code': '86'},
    'CO': {'name': 'COLOMBIA', 'code': '57'},
    'CR': {'name': 'COSTA RICA', 'code': '506'},
    'CU': {'name': 'CUBA', 'code': '53'},
    'CV': {'name': 'CAPE VERDE', 'code': '238'},
    'CX': {'name': 'CHRISTMAS ISLAND', 'code': '61'},
    'CY': {'name': 'CYPRUS', 'code': '357'},
    'CZ': {'name': 'CZECH REPUBLIC', 'code': '420'},
    'DE': {'name': 'GERMANY', 'code': '49'},
    'DJ': {'name': 'DJIBOUTI', 'code': '253'},
    'DK': {'name': 'DENMARK', 'code': '45'},
    'DM': {'name': 'DOMINICA', 'code': '1767'},
    'DO': {'name': 'DOMINICAN REPUBLIC', 'code': '1809'},
    'DZ': {'name': 'ALGERIA', 'code': '213'},
    'EC': {'name': 'ECUADOR', 'code': '593'},
    'EE': {'name': 'ESTONIA', 'code': '372'},
    'EG': {'name': 'EGYPT', 'code': '20'},
    'ER': {'name': 'ERITREA', 'code': '291'},
    'ES': {'name': 'SPAIN', 'code': '34'},
    'ET': {'name': 'ETHIOPIA', 'code': '251'},
    'FI': {'name': 'FINLAND', 'code': '358'},
    'FJ': {'name': 'FIJI', 'code': '679'},
    'FK': {'name': 'FALKLAND ISLANDS (MALVINAS)', 'code': '500'},
    'FM': {'name': 'MICRONESIA, FEDERATED STATES OF', 'code': '691'},
    'FO': {'name': 'FAROE ISLANDS', 'code': '298'},
    'FR': {'name': 'FRANCE', 'code': '33'},
    'GA': {'name': 'GABON', 'code': '241'},
    'GB': {'name': 'UNITED KINGDOM', 'code': '44'},
    'GD': {'name': 'GRENADA', 'code': '1473'},
    'GE': {'name': 'GEORGIA', 'code': '995'},
    'GH': {'name': 'GHANA', 'code': '233'},
    'GI': {'name': 'GIBRALTAR', 'code': '350'},
    'GL': {'name': 'GREENLAND', 'code': '299'},
    'GM': {'name': 'GAMBIA', 'code': '220'},
    'GN': {'name': 'GUINEA', 'code': '224'},
    'GQ': {'name': 'EQUATORIAL GUINEA', 'code': '240'},
    'GR': {'name': 'GREECE', 'code': '30'},
    'GT': {'name': 'GUATEMALA', 'code': '502'},
    'GU': {'name': 'GUAM', 'code': '1671'},
    'GW': {'name': 'GUINEA-BISSAU', 'code': '245'},
    'GY': {'name': 'GUYANA', 'code': '592'},
    'HK': {'name': 'HONG KONG', 'code': '852'},
    'HN': {'name': 'HONDURAS', 'code': '504'},
    'HR': {'name': 'CROATIA', 'code': '385'},
    'HT': {'name': 'HAITI', 'code': '509'},
    'HU': {'name': 'HUNGARY', 'code': '36'},
    'ID': {'name': 'INDONESIA', 'code': '62'},
    'IE': {'name': 'IRELAND', 'code': '353'},
    'IL': {'name': 'ISRAEL', 'code': '972'},
    'IM': {'name': 'ISLE OF MAN', 'code': '44'},
    'IN': {'name': 'INDIA', 'code': '91'},
    'IQ': {'name': 'IRAQ', 'code': '964'},
    'IR': {'name': 'IRAN, ISLAMIC REPUBLIC OF', 'code': '98'},
    'IS': {'name': 'ICELAND', 'code': '354'},
    'IT': {'name': 'ITALY', 'code': '39'},
    'JM': {'name': 'JAMAICA', 'code': '1876'},
    'JO': {'name': 'JORDAN', 'code': '962'},
    'JP': {'name': 'JAPAN', 'code': '81'},
    'KE': {'name': 'KENYA', 'code': '254'},
    'KG': {'name': 'KYRGYZSTAN', 'code': '996'},
    'KH': {'name': 'CAMBODIA', 'code': '855'},
    'KI': {'name': 'KIRIBATI', 'code': '686'},
    'KM': {'name': 'COMOROS', 'code': '269'},
    'KN': {'name': 'SAINT KITTS AND NEVIS', 'code': '1869'},
    'KP': {'name': 'KOREA DEMOCRATIC PEOPLES REPUBLIC OF', 'code': '850'},
    'KR': {'name': 'KOREA REPUBLIC OF', 'code': '82'},
    'KW': {'name': 'KUWAIT', 'code': '965'},
    'KY': {'name': 'CAYMAN ISLANDS', 'code': '1345'},
    'KZ': {'name': 'KAZAKSTAN', 'code': '7'},
    'LA': {'name': 'LAO PEOPLES DEMOCRATIC REPUBLIC', 'code': '856'},
    'LB': {'name': 'LEBANON', 'code': '961'},
    'LC': {'name': 'SAINT LUCIA', 'code': '1758'},
    'LI': {'name': 'LIECHTENSTEIN', 'code': '423'},
    'LK': {'name': 'SRI LANKA', 'code': '94'},
    'LR': {'name': 'LIBERIA', 'code': '231'},
    'LS': {'name': 'LESOTHO', 'code': '266'},
    'LT': {'name': 'LITHUANIA', 'code': '370'},
    'LU': {'name': 'LUXEMBOURG', 'code': '352'},
    'LV': {'name': 'LATVIA', 'code': '371'},
    'LY': {'name': 'LIBYAN ARAB JAMAHIRIYA', 'code': '218'},
    'MA': {'name': 'MOROCCO', 'code': '212'},
    'MC': {'name': 'MONACO', 'code': '377'},
    'MD': {'name': 'MOLDOVA, REPUBLIC OF', 'code': '373'},
    'ME': {'name': 'MONTENEGRO', 'code': '382'},
    'MF': {'name': 'SAINT MARTIN', 'code': '1599'},
    'MG': {'name': 'MADAGASCAR', 'code': '261'},
    'MH': {'name': 'MARSHALL ISLANDS', 'code': '692'},
    'MK': {'name': 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF', 'code': '389'},
    'ML': {'name': 'MALI', 'code': '223'},
    'MM': {'name': 'MYANMAR', 'code': '95'},
    'MN': {'name': 'MONGOLIA', 'code': '976'},
    'MO': {'name': 'MACAU', 'code': '853'},
    'MP': {'name': 'NORTHERN MARIANA ISLANDS', 'code': '1670'},
    'MR': {'name': 'MAURITANIA', 'code': '222'},
    'MS': {'name': 'MONTSERRAT', 'code': '1664'},
    'MT': {'name': 'MALTA', 'code': '356'},
    'MU': {'name': 'MAURITIUS', 'code': '230'},
    'MV': {'name': 'MALDIVES', 'code': '960'},
    'MW': {'name': 'MALAWI', 'code': '265'},
    'MX': {'name': 'MEXICO', 'code': '52'},
    'MY': {'name': 'MALAYSIA', 'code': '60'},
    'MZ': {'name': 'MOZAMBIQUE', 'code': '258'},
    'NA': {'name': 'NAMIBIA', 'code': '264'},
    'NC': {'name': 'NEW CALEDONIA', 'code': '687'},
    'NE': {'name': 'NIGER', 'code': '227'},
    'NG': {'name': 'NIGERIA', 'code': '234'},
    'NI': {'name': 'NICARAGUA', 'code': '505'},
    'NL': {'name': 'NETHERLANDS', 'code': '31'},
    'NO': {'name': 'NORWAY', 'code': '47'},
    'NP': {'name': 'NEPAL', 'code': '977'},
    'NR': {'name': 'NAURU', 'code': '674'},
    'NU': {'name': 'NIUE', 'code': '683'},
    'NZ': {'name': 'NEW ZEALAND', 'code': '64'},
    'OM': {'name': 'OMAN', 'code': '968'},
    'PA': {'name': 'PANAMA', 'code': '507'},
    'PE': {'name': 'PERU', 'code': '51'},
    'PF': {'name': 'FRENCH POLYNESIA', 'code': '689'},
    'PG': {'name': 'PAPUA NEW GUINEA', 'code': '675'},
    'PH': {'name': 'PHILIPPINES', 'code': '63'},
    'PK': {'name': 'PAKISTAN', 'code': '92'},
    'PL': {'name': 'POLAND', 'code': '48'},
    'PM': {'name': 'SAINT PIERRE AND MIQUELON', 'code': '508'},
    'PN': {'name': 'PITCAIRN', 'code': '870'},
    'PR': {'name': 'PUERTO RICO', 'code': '1'},
    'PT': {'name': 'PORTUGAL', 'code': '351'},
    'PW': {'name': 'PALAU', 'code': '680'},
    'PY': {'name': 'PARAGUAY', 'code': '595'},
    'QA': {'name': 'QATAR', 'code': '974'},
    'RO': {'name': 'ROMANIA', 'code': '40'},
    'RS': {'name': 'SERBIA', 'code': '381'},
    'RU': {'name': 'RUSSIAN FEDERATION', 'code': '7'},
    'RW': {'name': 'RWANDA', 'code': '250'},
    'SA': {'name': 'SAUDI ARABIA', 'code': '966'},
    'SB': {'name': 'SOLOMON ISLANDS', 'code': '677'},
    'SC': {'name': 'SEYCHELLES', 'code': '248'},
    'SD': {'name': 'SUDAN', 'code': '249'},
    'SE': {'name': 'SWEDEN', 'code': '46'},
    'SG': {'name': 'SINGAPORE', 'code': '65'},
    'SH': {'name': 'SAINT HELENA', 'code': '290'},
    'SI': {'name': 'SLOVENIA', 'code': '386'},
    'SK': {'name': 'SLOVAKIA', 'code': '421'},
    'SL': {'name': 'SIERRA LEONE', 'code': '232'},
    'SM': {'name': 'SAN MARINO', 'code': '378'},
    'SN': {'name': 'SENEGAL', 'code': '221'},
    'SO': {'name': 'SOMALIA', 'code': '252'},
    'SR': {'name': 'SURINAME', 'code': '597'},
    'ST': {'name': 'SAO TOME AND PRINCIPE', 'code': '239'},
    'SV': {'name': 'EL SALVADOR', 'code': '503'},
    'SY': {'name': 'SYRIAN ARAB REPUBLIC', 'code': '963'},
    'SZ': {'name': 'SWAZILAND', 'code': '268'},
    'TC': {'name': 'TURKS AND CAICOS ISLANDS', 'code': '1649'},
    'TD': {'name': 'CHAD', 'code': '235'},
    'TG': {'name': 'TOGO', 'code': '228'},
    'TH': {'name': 'THAILAND', 'code': '66'},
    'TJ': {'name': 'TAJIKISTAN', 'code': '992'},
    'TK': {'name': 'TOKELAU', 'code': '690'},
    'TL': {'name': 'TIMOR-LESTE', 'code': '670'},
    'TM': {'name': 'TURKMENISTAN', 'code': '993'},
    'TN': {'name': 'TUNISIA', 'code': '216'},
    'TO': {'name': 'TONGA', 'code': '676'},
    'TR': {'name': 'TURKEY', 'code': '90'},
    'TT': {'name': 'TRINIDAD AND TOBAGO', 'code': '1868'},
    'TV': {'name': 'TUVALU', 'code': '688'},
    'TW': {'name': 'TAIWAN, PROVINCE OF CHINA', 'code': '886'},
    'TZ': {'name': 'TANZANIA, UNITED REPUBLIC OF', 'code': '255'},
    'UA': {'name': 'UKRAINE', 'code': '380'},
    'UG': {'name': 'UGANDA', 'code': '256'},
    'US': {'name': 'UNITED STATES', 'code': '1'},
    'UY': {'name': 'URUGUAY', 'code': '598'},
    'UZ': {'name': 'UZBEKISTAN', 'code': '998'},
    'VA': {'name': 'HOLY SEE (VATICAN CITY STATE)', 'code': '39'},
    'VC': {'name': 'SAINT VINCENT AND THE GRENADINES', 'code': '1784'},
    'VE': {'name': 'VENEZUELA', 'code': '58'},
    'VG': {'name': 'VIRGIN ISLANDS, BRITISH', 'code': '1284'},
    'VI': {'name': 'VIRGIN ISLANDS, U.S.', 'code': '1340'},
    'VN': {'name': 'VIET NAM', 'code': '84'},
    'VU': {'name': 'VANUATU', 'code': '678'},
    'WF': {'name': 'WALLIS AND FUTUNA', 'code': '681'},
    'WS': {'name': 'SAMOA', 'code': '685'},
    'XK': {'name': 'KOSOVO', 'code': '381'},
    'YE': {'name': 'YEMEN', 'code': '967'},
    'YT': {'name': 'MAYOTTE', 'code': '262'},
    'ZA': {'name': 'SOUTH AFRICA', 'code': '27'},
    'ZM': {'name': 'ZAMBIA', 'code': '260'},
    'ZW': {'name': 'ZIMBABWE', 'code': '263'}
}

"""
currency by country code
"""
CURRENCIES_BY_COUNTRY_CODE = {
    'BD': ('BDT',),
    'BE': ('EUR',),
    'BF': ('XOF',),
    'BG': ('BGN',),
    'BA': ('BAM',),
    'BB': ('BBD',),
    'WF': ('XPF',),
    'BL': ('EUR',),
    'BM': ('BMD',),
    'BN': ('BND',),
    'BO': ('BOB',),
    'BH': ('BHD',),
    'BI': ('BIF',),
    'BJ': ('XOF',),
    'BT': ('BTN', 'INR'),
    'JM': ('JMD',),
    'BV': ('NOK',),
    'BW': ('BWP',),
    'WS': ('WST',),
    'BQ': ('USD',),
    'BR': ('BRL',),
    'BS': ('BSD',),
    'JE': ('GBP',),
    'BY': ('BYR',),
    'BZ': ('BZD',),
    'RU': ('RUB',),
    'RW': ('RWF',),
    'RS': ('RSD',),
    'TL': ('USD',),
    'RE': ('EUR',),
    'TM': ('TMT',),
    'TJ': ('TJS',),
    'RO': ('RON',),
    'TK': ('NZD',),
    'GW': ('XOF',),
    'GU': ('USD',),
    'GT': ('GTQ',),
    'GS': ('GBP',),
    'GR': ('EUR',),
    'GQ': ('XAF',),
    'GP': ('EUR',),
    'JP': ('JPY',),
    'GY': ('GYD',),
    'GG': ('GBP',),
    'GF': ('EUR',),
    'GE': ('GEL',),
    'GD': ('XCD',),
    'GB': ('GBP',),
    'GA': ('XAF',),
    'SV': ('USD',),
    'GN': ('GNF',),
    'GM': ('GMD',),
    'GL': ('DKK',),
    'GI': ('GIP',),
    'GH': ('GHS',),
    'OM': ('OMR',),
    'TN': ('TND',),
    'IL': ('ILS',),
    'JO': ('JOD',),
    'HR': ('HRK',),
    'HT': ('HTG', 'USD'),
    'HU': ('HUF',),
    'HK': ('HKD',),
    'HN': ('HNL',),
    'HM': ('AUD',),
    'VE': ('VEF',),
    'PR': ('USD',),
    'PS': ('None',),
    'PW': ('USD',),
    'PT': ('EUR',),
    'SJ': ('NOK',),
    'PY': ('PYG',),
    'IQ': ('IQD',),
    'PA': ('PAB', 'USD'),
    'PF': ('XPF',),
    'PG': ('PGK',),
    'PE': ('PEN',),
    'PK': ('PKR',),
    'PH': ('PHP',),
    'PN': ('NZD',),
    'PL': ('PLN',),
    'PM': ('EUR',),
    'ZM': ('ZMW',),
    'EH': ('MAD',),
    'EE': ('EUR',),
    'EG': ('EGP',),
    'ZA': ('ZAR',),
    'EC': ('USD',),
    'IT': ('EUR',),
    'VN': ('VND',),
    'SB': ('SBD',),
    'ET': ('ETB',),
    'SO': ('SOS',),
    'ZW': ('USD', 'ZAR', 'BWP', 'GBP', 'EUR'),
    'SA': ('SAR',),
    'ES': ('EUR',),
    'ER': ('ETB', 'ERN'),
    'ME': ('EUR',),
    'MD': ('MDL',),
    'MG': ('MGA',),
    'MF': ('EUR',),
    'MA': ('MAD',),
    'MC': ('EUR',),
    'UZ': ('UZS',),
    'MM': ('MMK',),
    'ML': ('XOF',),
    'MO': ('MOP',),
    'MN': ('MNT',),
    'MH': ('USD',),
    'MK': ('MKD',),
    'MU': ('MUR',),
    'MT': ('EUR',),
    'MW': ('MWK',),
    'MV': ('MVR',),
    'MQ': ('EUR',),
    'MP': ('USD',),
    'MS': ('XCD',),
    'MR': ('MRO',),
    'IM': ('GBP',),
    'UG': ('UGX',),
    'MY': ('MYR',),
    'MX': ('MXN',),
    'AT': ('EUR',),
    'FR': ('EUR',),
    'IO': ('USD',),
    'SH': ('SHP',),
    'FI': ('EUR',),
    'FJ': ('FJD',),
    'FK': ('FKP',),
    'FM': ('USD',),
    'FO': ('DKK',),
    'NI': ('NIO',),
    'NL': ('EUR',),
    'NO': ('NOK',),
    'NA': ('NAD', 'ZAR'),
    'NC': ('XPF',),
    'NE': ('XOF',),
    'NF': ('AUD',),
    'NG': ('NGN',),
    'NZ': ('NZD',),
    'NP': ('NPR',),
    'NR': ('AUD',),
    'NU': ('NZD',),
    'CK': ('NZD',),
    'CI': ('XOF',),
    'CH': ('CHF',),
    'CO': ('COP',),
    'CN': ('CNY',),
    'CM': ('XAF',),
    'CL': ('CLP',),
    'CC': ('AUD',),
    'CA': ('CAD',),
    'LB': ('LBP',),
    'CG': ('XAF',),
    'CF': ('XAF',),
    'CD': ('CDF',),
    'CZ': ('CZK',),
    'CY': ('EUR',),
    'CX': ('AUD',),
    'CR': ('CRC',),
    'CW': ('ANG',),
    'CV': ('CVE',),
    'CU': ('CUP', 'CUC'),
    'SZ': ('SZL',),
    'SY': ('SYP',),
    'SX': ('ANG',),
    'KG': ('KGS',),
    'KE': ('KES',),
    'SS': ('SSP',),
    'SR': ('SRD',),
    'KI': ('AUD',),
    'KH': ('KHR',),
    'KN': ('XCD',),
    'KM': ('KMF',),
    'ST': ('STD',),
    'SK': ('EUR',),
    'KR': ('KRW',),
    'SI': ('EUR',),
    'KP': ('KPW',),
    'KW': ('KWD',),
    'SN': ('XOF',),
    'SM': ('EUR',),
    'SL': ('SLL',),
    'SC': ('SCR',),
    'KZ': ('KZT',),
    'KY': ('KYD',),
    'SG': ('SGD',),
    'SE': ('SEK',),
    'SD': ('SDG',),
    'DO': ('DOP',),
    'DM': ('XCD',),
    'DJ': ('DJF',),
    'DK': ('DKK',),
    'VG': ('USD',),
    'DE': ('EUR',),
    'YE': ('YER',),
    'DZ': ('DZD',),
    'US': ('USD',),
    'UY': ('UYU',),
    'YT': ('EUR',),
    'UM': ('USD',),
    'TZ': ('TZS',),
    'LC': ('XCD',),
    'LA': ('LAK',),
    'TV': ('TVD', 'AUD'),
    'TW': ('TWD',),
    'TT': ('TTD',),
    'TR': ('TRY',),
    'LK': ('LKR',),
    'LI': ('CHF',),
    'LV': ('EUR',),
    'TO': ('TOP',),
    'LT': ('LTL',),
    'LU': ('EUR',),
    'LR': ('LRD',),
    'LS': ('LSL', 'ZAR'),
    'TH': ('THB',),
    'TF': ('EUR',),
    'TG': ('XOF',),
    'TD': ('XAF',),
    'TC': ('USD',),
    'LY': ('LYD',),
    'VA': ('EUR',),
    'VC': ('XCD',),
    'AE': ('AED',),
    'AD': ('EUR',),
    'AG': ('XCD',),
    'AF': ('AFN',),
    'AI': ('XCD',),
    'VI': ('USD',),
    'IS': ('ISK',),
    'IR': ('IRR',),
    'AM': ('AMD',),
    'AL': ('ALL',),
    'AO': ('AOA',),
    'AN': ('ANG',),
    'AQ': ('NONE',),
    'AS': ('USD',),
    'AR': ('ARS',),
    'AU': ('AUD',),
    'VU': ('VUV',),
    'AW': ('AWG',),
    'IN': ('INR',),
    'AX': ('EUR',),
    'AZ': ('AZN',),
    'IE': ('EUR',),
    'ID': ('IDR',),
    'UA': ('UAH',),
    'QA': ('QAR',),
    'MZ': ('MZN',),
}

ONE_DAY_TIMESTAMP = 86400

"""
Error response code
"""
ERROR_CODE_WRONG_CREDENTIALS = 1004
ERROR_CODE_TOKEN_EXPIRED = 1005
ERROR_CODE_DATA_NOT_FOUND = 4001
ERROR_CODE_CAN_NOT_PERFORM_OPERATION = 4002
ERROR_CODE_REQUEST_DATA_NOT_VALID = 4003
ERROR_CODE_DATA_NOT_SAVED = 4005
ERROR_CODE_FEATURE_NOT_ENABLED = 4006
ERROR_CODE_WRONG_PASSWORD = 1003
ERROR_CODE_NOT_PERMITTED = 8001

"""
User type
"""

USER_TYPE_SUPER_ADMIN = 0
USER_TYPE_COMPANY_ADMIN = 1
USER_TYPE_TEAM = 2
USER_TYPE_CLIENT = 3
USER_TYPE_EMPLOYEE = 4
USER_TYPE_CRM = 5
USER_TYPE_CHOICES = (
    (USER_TYPE_SUPER_ADMIN, "Super Admin"),
    (USER_TYPE_COMPANY_ADMIN, "Company Admin"),
    (USER_TYPE_TEAM, "Team"),
    (USER_TYPE_CLIENT, "Client"),
    (USER_TYPE_EMPLOYEE, "Employee"),
)

PARTIAL_LEAVE_STATUS_PENDING = 1
PARTIAL_LEAVE_STATUS_APPROVED = 2
PARTIAL_LEAVE_STATUS_REJECTED = 3
PARTIAL_LEAVE_STATUS_CANCEL = 4

PARTIAL_LEAVE_STATUS = (
    (PARTIAL_LEAVE_STATUS_PENDING, "Pending"),
    (PARTIAL_LEAVE_STATUS_APPROVED, "Approved"),
    (PARTIAL_LEAVE_STATUS_REJECTED, "Rejected"),
    (PARTIAL_LEAVE_STATUS_CANCEL, "Cancel"),
)

TOTAL_PARTIAL_LEAVE = 1
PARTIAL_LEAVE_MINUTES = 60

PARTIAL_LEAVE_EARLY_GO = 1
PARTIAL_LEAVE_LATE_COMING = 2
PARTIAL_LEAVE_TYPE = ((PARTIAL_LEAVE_EARLY_GO, "Early Out"), (PARTIAL_LEAVE_LATE_COMING, "Late In"))

# LANGUAGE
LANGUAGE: tuple = (
    ("hi", "Hindi"),
    ("en", "English")
)

TOKEN_TYPE = "Token"

PERMISSION_METHOD: tuple = (
    ('GET', 'view'),
    ('POST', 'add'),
    ('PUT', 'add'),
    ('PATCH', 'add'),
    ('DELETE', 'delete')
)

PERMISSION_METHOD_DICT = dict(PERMISSION_METHOD)

# Time Format

TIME_FORMAT_12: str = 'hh:mm:aaa'
TIME_FORMAT_24: str = 'HH:mm'
TIME_FORMAT_CHOICES: tuple = (
    (TIME_FORMAT_12, 'hh:mm:aaa', {'mobile_format': "hh:mm A"}),
    (TIME_FORMAT_24, 'hh:mm', {"mobile_format": "hh:mm"})
)

LANGUAGE_CHOICES = (("en", "English"),)
# Date Format

DATE_FORMAT_MDY_SLASH: str = 'MM/dd/yyyy'
DATE_FORMAT_DMY_SLASH: str = 'dd/MM/yyyy'
DATE_FORMAT_DMY_DASH: str = 'dd-MM-yyyy'
DATE_FORMAT_MDY_DASH: str = 'MM-dd-yyyy'
DATE_FORMAT_CHOICES: tuple = (
    (DATE_FORMAT_MDY_SLASH, 'mm/dd/yyyy', {"mobile_format": "MM/DD/YYYY"}),
    (DATE_FORMAT_DMY_SLASH, 'dd/mm/yyyy', {"mobile_format": "DD/MM/YYYY"}),
    (DATE_FORMAT_DMY_DASH, 'dd-mm-yyyy', {"mobile_format": "DD-MM-YYYY"}),
    (DATE_FORMAT_MDY_DASH, 'mm-dd-yyyy', {"mobile_format": "MM-DD-YYYY"})
)

# MEASUREMENT_UNIT
MEASUREMENT_UNIT_MILLIMETER: str = "mm"
MEASUREMENT_UNIT_CM: str = "cm"
MEASUREMENT_UNIT_INCHES: str = "in"
MEASUREMENT_UNIT_FEET: str = "ft"
MEASUREMENT_UNIT_METER: str = "m"
MEASUREMENT_UNIT: tuple = (
    (MEASUREMENT_UNIT_MILLIMETER, "Millimeter(mm)"),
    (MEASUREMENT_UNIT_CM, "Centimeter(cm)"),
    (MEASUREMENT_UNIT_INCHES, "Inches(in)"),
    (MEASUREMENT_UNIT_FEET, "Feet(ft)"),
    (MEASUREMENT_UNIT_METER, "Meter(m)"),
)

# Timezone Dict

TIMEZONE_DICT: dict = {
    'Pacific/Midway': TIME_M_11_00, 'US/Samoa': TIME_M_11_00, 'US/Hawaii': '-10:00', 'US/Alaska': '-09:00',
    'US/Pacific': TIME_M_08_00, 'America/Tijuana': TIME_M_08_00, 'US/Arizona': TIME_M_07_00,
    'US/Mountain': TIME_M_07_00,
    'America/Chihuahua': TIME_M_07_00, 'America/Mazatlan': TIME_M_07_00, 'America/Mexico_City': TIME_M_06_00,
    'America/Monterrey': TIME_M_06_00, 'Canada/Saskatchewan': TIME_M_06_00, 'US/Central': TIME_M_06_00,
    'US/Eastern': TIME_M_05_00, 'US/East-Indiana': TIME_M_05_00, 'America/Bogota': TIME_M_05_00,
    'America/Lima': TIME_M_05_00, 'America/Caracas': '-04:30', 'Canada/Atlantic': TIME_M_04_00,
    'America/La_Paz': TIME_M_04_00, 'America/Santiago': TIME_M_04_00, 'Canada/Newfoundland': '-03:30',
    'America/Buenos_Aires': TIME_M_03_00, 'Greenland': TIME_M_03_00, 'Atlantic/Stanley': '-02:00',
    'Atlantic/Azores': TIME_M_01_00, 'Atlantic/Cape_Verde': TIME_M_01_00, 'Europe/Amsterdam': TIME_P_01_00,
    'Europe/Belgrade': TIME_P_01_00, 'Europe/Berlin': TIME_P_01_00, 'Europe/Bratislava': TIME_P_01_00,
    'Europe/Brussels': TIME_P_01_00, 'Europe/Budapest': TIME_P_01_00, 'Europe/Copenhagen': TIME_P_01_00,
    'Europe/Ljubljana': TIME_P_01_00, 'Europe/Madrid': TIME_P_01_00, 'Europe/Paris': TIME_P_01_00,
    'Europe/Prague': TIME_P_01_00, 'Europe/Rome': TIME_P_01_00, 'Europe/Sarajevo': TIME_P_01_00,
    'Europe/Skopje': TIME_P_01_00, 'Europe/Stockholm': TIME_P_01_00, 'Europe/Vienna': TIME_P_01_00,
    'Europe/Warsaw': TIME_P_01_00, 'Europe/Zagreb': TIME_P_01_00, 'Europe/Athens': TIME_P_02_00,
    'Europe/Bucharest': TIME_P_02_00, 'Africa/Cairo': TIME_P_02_00, 'Africa/Harare': TIME_P_02_00,
    'Europe/Helsinki': TIME_P_02_00, 'Europe/Istanbul': TIME_P_02_00, 'Asia/Jerusalem': TIME_P_02_00,
    'Europe/Kiev': TIME_P_02_00, 'Europe/Minsk': TIME_P_02_00, 'Europe/Riga': TIME_P_02_00,
    'Europe/Sofia': TIME_P_02_00,
    'Europe/Tallinn': TIME_P_02_00, 'Europe/Vilnius': TIME_P_02_00, 'Asia/Baghdad': TIME_P_03_00,
    'Asia/Kuwait': TIME_P_03_00, 'Africa/Nairobi': TIME_P_03_00, 'Asia/Riyadh': TIME_P_03_00,
    'Europe/Moscow': TIME_P_03_00, 'Asia/Tehran': '+03:30', 'Asia/Baku': TIME_P_04_00,
    'Europe/Volgograd': TIME_P_04_00, 'Asia/Muscat': TIME_P_04_00, 'Asia/Tbilisi': TIME_P_04_00,
    'Asia/Yerevan': TIME_P_04_00, 'Asia/Kabul': '+04:30', 'Asia/Karachi': TIME_P_05_00, 'Asia/Tashkent': TIME_P_05_00,
    'Asia/Kolkata': '+05:30', 'Asia/Kathmandu': '+05:45', 'Asia/Yekaterinburg': TIME_P_06_00,
    'Asia/Almaty': TIME_P_06_00, 'Asia/Dhaka': TIME_P_06_00, 'Asia/Novosibirsk': TIME_P_07_00,
    'Asia/Bangkok': TIME_P_07_00, 'Asia/Jakarta': TIME_P_07_00, 'Asia/Krasnoyarsk': TIME_P_08_00,
    'Asia/Chongqing': TIME_P_08_00, 'Asia/Hong_Kong': TIME_P_08_00, 'Asia/Kuala_Lumpur': TIME_P_08_00,
    'Australia/Perth': TIME_P_08_00, 'Asia/Singapore': TIME_P_08_00, 'Asia/Taipei': TIME_P_08_00,
    'Asia/Ulaanbaatar': TIME_P_08_00, 'Asia/Urumqi': TIME_P_08_00, 'Asia/Irkutsk': TIME_P_09_00,
    'Asia/Seoul': TIME_P_09_00, 'Asia/Tokyo': TIME_P_09_00, 'Australia/Adelaide': '+09:30',
    'Australia/Darwin': '+09:30', 'Asia/Yakutsk': TIME_P_10_00, 'Australia/Brisbane': TIME_P_10_00,
    'Australia/Canberra': TIME_P_10_00, 'Pacific/Guam': TIME_P_10_00, 'Australia/Hobart': TIME_P_10_00,
    'Australia/Melbourne': TIME_P_10_00, 'Pacific/Port_Moresby': TIME_P_10_00, 'Australia/Sydney': TIME_P_10_00,
    'Asia/Vladivostok': '+11:00', 'Asia/Magadan': TIME_P_12_00, 'Pacific/Auckland': TIME_P_12_00,
    'Pacific/Fiji': TIME_P_12_00
}

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

CURRENT_USER = "CURRENT_USER"
COMPANY_TIMEZONE = "COMPANY_TIMEZONE"

MODULE_ACTION_ARRAY = ["list", "add", "edit", "delete", "view"]

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

VARIABLE_CYCLE_QUATERLY = 1
VARIABLE_CYCLE_YEARLY = 2
VARIABLE_CYCL = (
    (VARIABLE_CYCLE_QUATERLY, "Quaterly"),
    (VARIABLE_CYCLE_YEARLY, "Yearly"),
)

# OKR_STATUS
OKR_STATUS_PENDING = 1
OKR_STATUS_ARCHIVED = 2
OKR_STATUS_COMPLETED = 3
OKR_STATUS = (
    (OKR_STATUS_PENDING, "Pending"),
    (OKR_STATUS_ARCHIVED, "Archived"),
    (OKR_STATUS_COMPLETED, "Complete"),
)

# OKR_STATUS
OKR_RESULT_TYPE_NUMBER = 1
OKR_RESULT_TYPE_DONE_NOT_DONE = 2
OKR_RESULT_TYPE_CURRENCY = 3
OKR_RESULT_TYPE = (
    (OKR_RESULT_TYPE_NUMBER, "Number"),
    (OKR_RESULT_TYPE_DONE_NOT_DONE, "Done Not Done"),
    (OKR_RESULT_TYPE_CURRENCY, "Currency"),
)

OKR_CYCLE_TYPE_MONTHLY = 1
OKR_CYCLE_TYPE_WEEKLY = 2
OKR_CYCLE_TYPE_YEARLY = 3
OKR_CYCLE_TYPE = (
    (OKR_CYCLE_TYPE_MONTHLY, "Monthly"),
    (OKR_CYCLE_TYPE_WEEKLY, "Weekly"),
    (OKR_CYCLE_TYPE_YEARLY, "Yearly"),
)

MAX_TARGET_PERCENTAGE = 100

# Notification constants

ASSIGN_PROJECT = 1
ASSIGN_TASK = 2
LEAVE_REQUEST = 3
KPI_DATA = 4
DUE_PROJECT = 5
ATTENDANCE_REQUEST = 6
MEETING = 7
HAND_BOOK = 8

NOTIFICATION_TYPE = (
    (ASSIGN_PROJECT, "Assign Project"),
    (ASSIGN_TASK, "Assign Task"),
    (LEAVE_REQUEST, "Leave Request"),
    (KPI_DATA, "KPI Data"),
    (DUE_PROJECT, "Due Project"),
    (ATTENDANCE_REQUEST, "Attendance Request"),
    (MEETING, "Meeting"),
    (HAND_BOOK, "Hand Book"),
)

IS_EMAIL_YES = 1
IS_EMAIL_NO = 2
IS_EMAIL = ((IS_EMAIL_YES, "Yes"), (IS_EMAIL_NO, "No"))

IS_NOTIFICTION_YES = 1
IS_NOTIFICATION_NO = 2
IS_EMAIL = ((IS_EMAIL_YES, "Yes"), (IS_EMAIL_NO, "No"))

PROJECT_TASK_NOTIFICATION = 1
SPRINT_NOTIFICATION = 2
BACKLOG_TASK_NOTIFICATION = 3
RELEASE_NOTIFICATION = 4
PROJECT_DOCUMENT_NOTIFICATION = 5
EMPLOYEE_NOTIFICATION = 6
CONTRACT_NOTIFICATION = 7
RESIGN_EMPLOYEE_NOTIFICATION = 8
ATTENDANCE_REQUEST_NOTIFICATION = 9
WORK_FROM_HOME_NOTIFICATION = 10
LEAVE_NOTIFICATION = 11
COMPOFF_NOTIFICATION = 12
PARTIAL_LEAVE_NOTIFICATION = 13

NOTIFICATION_PERMISSION = (
    (PROJECT_TASK_NOTIFICATION, "Project Task"),
    (SPRINT_NOTIFICATION, "Sprint"),
    (BACKLOG_TASK_NOTIFICATION, "Backlog Task"),
    (RELEASE_NOTIFICATION, "Release"),
    (PROJECT_DOCUMENT_NOTIFICATION, "Project Document"),
    (EMPLOYEE_NOTIFICATION, "Employee"),
    (CONTRACT_NOTIFICATION, "Employee Contract"),
    (RESIGN_EMPLOYEE_NOTIFICATION, "Resign"),
    (ATTENDANCE_REQUEST_NOTIFICATION, "Attendance Request"),
    (WORK_FROM_HOME_NOTIFICATION, "Work From Home"),
    (LEAVE_NOTIFICATION, "Leave"),
    (COMPOFF_NOTIFICATION, "Compensatory Off"),
    (PARTIAL_LEAVE_NOTIFICATION, "Partial Leave"),
)

DELETENOTIFICATION_DAYS = 7

ANNOUNCEMENT = 1
POST = 2
ANNOUNCEMENT_TYPE = ((ANNOUNCEMENT, "Announcement"), (POST, "Post"))

# Meeting Constants

"""
Meeting type constant
"""

TEMPLATE_TYPE_CONDUCT = "63c538dc4ba69054aaa78f94"
TEMPLATE_TYPE_APPRECIATION = "63c538c64ba69054aaa78f89"
TEMPLATE_TYPE_PIP = "63c538b94ba69054aaa78f57"
TEMPLATE_TYPE_AREA_OF_IMPROVEMENT = "63c538b24ba69054aaa78f26"
TEMPLATE_TYPE_INCREMENT_APPRAISAL = "63cfba8c9eecc7000ab168d3"

# Payroll Component Tax Type
TAX_EXEMPT_TAXABLE = 1
TAX_EXEMPT_TAX_EXEMPT = 2
TAX_EXEMPT = ((TAX_EXEMPT_TAXABLE, "Taxable"), (TAX_EXEMPT_TAX_EXEMPT, "TaxExempt"))

# Payroll Component Type

PAYROLL_COMPONENT_TYPE_EARNING = 1
PAYROLL_COMPONENT_TYPE_DEDUCTION = 2
PAYROLL_COMPONENT_TYPE = (
    (PAYROLL_COMPONENT_TYPE_EARNING, "Earning"),
    (PAYROLL_COMPONENT_TYPE_DEDUCTION, "Deduction"),
)

# Payroll Status

PAYROLL_STATUS_INITIATED = 1
PAYROLL_STATUS_DONE = 2
PAYROLL_STATUS = ((PAYROLL_STATUS_INITIATED, "Initiated"), (PAYROLL_STATUS_DONE, "Done"))

# CTC And Special Allownce Constant Component Id

CTC_COMPONENT_CODE = "62f0a78f4ba6901dab49741a"
SPECIAL_ALLOWANCE_COMPONENT_CODE = "62f09d384ba6901719454a67"
PF_COMPONENT_CODE = "63d391854ba6904e04fa194e"

# Salary Component Value Type

SALARY_COMPONENT_VALUE_TYPE_FIX = 1
SALARY_COMPONENT_VALUE_TYPE_STATIC = 2
SALARY_COMPONENT_VALUE_TYPE = (
    (SALARY_COMPONENT_VALUE_TYPE_FIX, "Fix"),
    (SALARY_COMPONENT_VALUE_TYPE_STATIC, "Static"),
)

# Payroll Settlement Category Type

PAYROLL_SETTLEMENT_CATEGORY_TYPE_DEBIT = 1
PAYROLL_SETTLEMENT_CATEGORY_TYPE_CREDIT = 2
PAYROLL_SETTLEMENT_CATEGORY_TYPE = (
    (PAYROLL_SETTLEMENT_CATEGORY_TYPE_DEBIT, "Debit"),
    (PAYROLL_SETTLEMENT_CATEGORY_TYPE_CREDIT, "Credit"),
)

# Payroll Employee Type

PAYROLL_EMPLOYEE_TYPE_ACTIVE = 1
PAYROLL_EMPLOYEE_TYPE_DEACTIVATE = 2
EMPLOYEE_TYPE = ((PAYROLL_EMPLOYEE_TYPE_ACTIVE, "Active"), (PAYROLL_EMPLOYEE_TYPE_DEACTIVATE, "Relive"))

# User ROle Constants

ROLE_CODE_USER_ADMIN = '645dee92239a52c518c961c0'
ROLE_CODE_HR = '645def3fd9c7704855721457'
ROLE_CODE_IT_ADMIN = '645def4e021073f2f94d801d'
ROLE_CODE_MANAGER = '645def4e021073f2f94d801d'
ROLE_CODE_EXECUTIVE = '645def630b8514c9c824e4b8'
ROLE_CODE_CLIENT = ' "645e0c38a6b5a56fa0a01e06"'
USER_ROLE_CODE_CHOICES = (
    (ROLE_CODE_USER_ADMIN, "Company Admin"),
    (ROLE_CODE_HR, "HR"),
    (ROLE_CODE_IT_ADMIN, "IT Admin"),
    (ROLE_CODE_MANAGER, "Manager"),
    (ROLE_CODE_EXECUTIVE, "Employee"),
    (ROLE_CODE_CLIENT, "Client"),
)

# Module config constants

MODULE_HR = 'AKOY12'
MODULE_ACCOUNT = 'LOHJ23'
MODULE_PROJECT = 'VUH69U'
MODULE_ITSM = 'VYHI2K'
MODULE_TYPE = (
    (MODULE_HR, "AKOY12"),
    (MODULE_ACCOUNT, "LOHJ23"),
    (MODULE_PROJECT, "VUH69U"),
    (MODULE_ITSM, "VYHI2K"),
)

MODULE_WITH_PERMISSION = (
    (MODULE_PROJECT, 1),
    (MODULE_HR, 2),
    (MODULE_ITSM, 3),
    (MODULE_ACCOUNT, 4)
)

EVENT_STATUS_START = 1
EVENT_STATUS_STOP = 2

EVENT_STATUS = ((EVENT_STATUS_START, "Start"), (EVENT_STATUS_STOP, "Stop"))

# Meeting Constants

""" Meeting repeat type """
REPEAT_DAILY = 1
REPEAT_WEEKLY = 2
REPEAT_MONTHLY = 3

MEETING_REPEAT_TYPE = (
    (REPEAT_DAILY, "Daily"),
    (REPEAT_WEEKLY, "Weekly"),
    (REPEAT_MONTHLY, "Monthly"),
)

"""Meeting Status"""
MEETING_PENDING = 1
MEETING_START = 2
MEETING_COMPLETE = 3

MEETING_STATUS = (
    (MEETING_PENDING, "Pending"),
    (MEETING_START, "Start"),
    (MEETING_COMPLETE, "Completed"),
)

"""
Dynamic Module Key
"""
GMAIL_MODULE_KEY = 'gmail_001'
SLACK_MODULE_KEY = 'slack_001'

"""
OKR V2 Constants
"""

'''
Objective Tye
'''

OBJECTIVE_TYPE_TEAM = 1
OBJECTIVE_TYPE_INDIVIDUAL = 2

OBJECTIVE_TYPE = (
    (OBJECTIVE_TYPE_TEAM, 'Team Objective'),
    (OBJECTIVE_TYPE_INDIVIDUAL, 'Individual Objective')
)

'''
Objective Duration
'''
OBJECTIVE_DURATION_Q1 = 1
OBJECTIVE_DURATION_Q2 = 2
OBJECTIVE_DURATION_Q3 = 3
OBJECTIVE_DURATION_Q4 = 4

OBJECTIVE_DURATION = (
    (OBJECTIVE_DURATION_Q1, 'Q1'),
    (OBJECTIVE_DURATION_Q2, 'Q2'),
    (OBJECTIVE_DURATION_Q3, 'Q3'),
    (OBJECTIVE_DURATION_Q4, 'Q4')
)

OBJECTIVE_DURATION_Q1_MONTH = [1, 2, 3]
OBJECTIVE_DURATION_Q2_MONTH = [4, 5, 6]
OBJECTIVE_DURATION_Q3_MONTH = [7, 8, 9]
OBJECTIVE_DURATION_Q4_MONTH = [1, 2, 3]

'''
OKR Key Result Unit Measurement
'''

OKR_UNIT_MEASUREMENT_AS_PERCENTAGE = 1
OKR_UNIT_MEASUREMENT_AS_NUMBER = 2
OKR_UNIT_MEASUREMENT_AS_CURRENCY = 3

OKR_UNIT_MEASUREMENT = (
    (OKR_UNIT_MEASUREMENT_AS_PERCENTAGE, 'Count as Percentage'),
    (OKR_UNIT_MEASUREMENT_AS_NUMBER, 'Count as Number'),
    (OKR_UNIT_MEASUREMENT_AS_CURRENCY, 'Count as Currency')
)

# Define interval constants
INTERVAL_WEEKLY = 1
INTERVAL_MONTHLY = 2
INTERVAL_QUARTERLY = 3

# OKR Result Constants

KEY_RESULT_SHOULD_INCREASE = 1
KEY_RESULT_SHOULD_DECREASE = 2
KEY_RESULT_SHOULD_BE_EQUAL = 3
KEY_RESULT_SHOULD_SHOULD_NOT_EXCEED = 4
KEY_RESULT_SHOULD_NOT_FALL_BELOW = 5

# Process Calculate constants
CALCULATE_LAST_ENTERED_VALUE = 1
CALCULATE_TOTAL_OF_ALL_ENTERED_VALUES = 2
CALCULATE_AVERAGE_OF_ALL_ENTERED_VALUE = 3

# Key Result Score Status
KEY_RESULT_SCORE_LOG_ABOVE_PLAN = 1
KEY_RESULT_SCORE_LOG_ON_PLAN = 2
KEY_RESULT_SCORE_LOG_MODERATE = 3
KEY_RESULT_SCORE_LOG_HIGH_RISK = 4

# Kafka Constants

KAFKA_ADD_KEY_RESULT = 'add_key_result'
SEND_MEETING_MAIL_NOTIFICATION = "meeting_mail_notification"

KAFKA_ADD_OKR_AND_KEY_RESULT = 'add_okr_and_key_result'
KAFKA_ADD_SCHEDULE_KEY_RESULT_NEW = 'add_okr_and_key_result_new'
UPDATE_KEY_RESULT_TYPE = 'update_key_result_type'
CRM_DEFAULT_COMPANY_SETUP = 'crm_default_company_setup'

DELETE_ALL_DATA_OF_COMPANY = 'delete_all_data_of_company'

SURVEY_STATUS_COMPLETED = 3
SURVEY_STATUS_STARTED = 1

SURVEY_TYPE_NPS = 1
SURVEY_TYPE_CSAT = 2
SURVEY_TYPE_CES = 3

# Slack Notification Constants

BACKLOG_SLACK_NOTIFICATION = 1
TASK_SLACK_NOTIFICATION = 2
SPRINT_SLACK_NOTIFICATION = 3
RELEASE_SLACK_NOTIFICATION = 4
MESSAGE_SLACK_NOTIFICATION = 5
TASK_STATUS_CHANGE_SLACK_NOTIFICATION = 6

SLACK_NOTIFICATION = (
    (BACKLOG_SLACK_NOTIFICATION, 'Backlog'),
    (TASK_SLACK_NOTIFICATION, 'Task'),
    (SPRINT_SLACK_NOTIFICATION, 'Sprint'),
    (RELEASE_SLACK_NOTIFICATION, 'Release'),
    (MESSAGE_SLACK_NOTIFICATION, 'Message'),
    (TASK_STATUS_CHANGE_SLACK_NOTIFICATION, 'Task Status Change'),
)

CHANNEL_TYPE_PRIVATE = 'private'
CHANNEL_TYPE_PUBLIC = 'public'

DEFAULT_COMPANY_ID = '663f62859123b835eb16666c'

CRM_SERVICE_TYPE = 5

SEND_CLIENT_CHANGE_PASSWORD_MAIL_NOTIFICATION = "send_client_change_password_mail_notification"

TRANSACTION_NO = 'asc_005'  # transaction_no
JOURNAL_NO = 'asc_004'  # journal_no


ACCOUNT_INVOICE_CONFIG_SUFFIX = 'asc_007'
ACCOUNT_INVOICE_CONFIG_PREFIX = 'asc_006'