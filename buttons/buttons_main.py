from tkinter import Button
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup
import Links
from HugeTexts.TextsAboutSpecialities import *

# BUTTONS
Button1 = KeyboardButton("List of functions ⚙️")
Button1_ukr = KeyboardButton("Список функцій ⚙️")
Button2 = KeyboardButton("Contacts ✉️")
Button2_ukr = KeyboardButton("Контакти ✉️")
Button3 = KeyboardButton("About Bot🤖")
Button3_ukr = KeyboardButton("Про бот🤖")
Button4 = KeyboardButton("Next ➡️")
Button4_ukr = KeyboardButton("Далі ➡️")
Button5 = KeyboardButton("English 🇬🇧")   # for multi
Button6 = KeyboardButton("Back ⬅️")
Button6_ukr = KeyboardButton("Назад ⬅️")
Button7 = KeyboardButton("Choosing a status👤")
Button7_ukr = KeyboardButton("Вибір статусу👤")
Button8 = KeyboardButton("Українська 🇺🇦")       # for multi
Button9 = KeyboardButton("Main menu 🚪")
Button9_ukr = KeyboardButton("Головне меню 🚪")
Button10 = KeyboardButton("Getting a timetable 🗓")
Button10_ukr = KeyboardButton("Отримання розкладу 🗓")
Button11 = KeyboardButton("List of faculties 🎓")
Button11_ukr = KeyboardButton("Список факультетів 🎓")
Button12 = KeyboardButton("Faculty - KIU")
Button12_ukr = KeyboardButton("Факультет - КІУ")
Button13 = KeyboardButton("List of Courses 🗓")
Button13_ukr = KeyboardButton("Список курсів 🗓")
Button14 = KeyboardButton("Second course ⚜")
Button14_ukr = KeyboardButton("Другий курс ⚜")
Button15 = KeyboardButton("List of Groups 🗓")
Button15_ukr = KeyboardButton("Список груп 🗓")
Button16 = KeyboardButton("KBIKS-21-5 🎓")
Button16_ukr = KeyboardButton("КБІКС-21-5 🎓")
Button17 = KeyboardButton("KBIKS-21-6 🎓")
Button17_ukr = KeyboardButton("КБІКС-21-6 🎓")
Button18 = KeyboardButton("KBIKS-21-4 🎓")
Button18_ukr = KeyboardButton("КБІКС-21-4 🎓")
Button19 = KeyboardButton("KBIKS-21-3 🎓")
Button19_ukr = KeyboardButton("КБІКС-21-3 🎓")
Button20 = KeyboardButton("KBIKS-21-2 🎓")
Button20_ukr = KeyboardButton("КБІКС-21-2 🎓")
Button21 = KeyboardButton("KBIKSu-21-1 🎓")
Button21_ukr = KeyboardButton("КБІКСу-21-1 🎓")
Button22 = KeyboardButton("KBIKS-21-1 🎓")
Button22_ukr = KeyboardButton("КБІКС-21-1 🎓")
Button23 = KeyboardButton("Student 👨‍🎓")
Button23_ukr = KeyboardButton("Студент 👨‍🎓")
Button24 = KeyboardButton("Applicant 👤")
Button24_ukr = KeyboardButton("Абітурієнт 👤")
Button25 = KeyboardButton("Main contacts ✉️")
Button25_ukr = KeyboardButton("Головні контакти ✉️")
Button26 = KeyboardButton("Change language 🇬🇧🇺🇦")
Button26_ukr = KeyboardButton("Змінити мову 🇺🇦🇬🇧")
Button27 = KeyboardButton("Submission of documents 📄")
Button27_ukr = KeyboardButton("Подача документів 📄")
Button28 = KeyboardButton("Calculation of the competition score 🧮")
Button28_ukr = KeyboardButton("Підрахунок конкурного балу 🧮")
# Button29 = KeyboardButton("NMT")
# Button29_ukr = KeyboardButton("НМТ")
# Button30 = KeyboardButton("ZNO")
# Button30_ukr = KeyboardButton("ЗНО")
Button31 = KeyboardButton("About the university🎓")
Button31_ukr = KeyboardButton("Про університет🎓")
Button32 = KeyboardButton("About departments🗂")
Button32_ukr = KeyboardButton("Про кафедри🗂")

#-------------------------------INLINE BUTTONS -----------------------#
Button38 = KeyboardButton("About the specialities🧑‍💻")
Button38_ukr = KeyboardButton("Про спеціальності🧑‍💻")

#-------------------------------INLINE BUTTONS -----------------------#
Button39 = InlineKeyboardButton(text="051 Economic", callback_data="EconomicClick")
Button40 = InlineKeyboardButton(text="More about specialty", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-051-ekonomika")
Button41 = InlineKeyboardButton(text="113 Applied mathematics", callback_data="MathematicsClick")
Button42 = InlineKeyboardButton(text="More about speciality", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-113-prikladna-matematika")
Button43 = InlineKeyboardButton(text="121 Software Engineering", callback_data="SoftClick")
Button44 = InlineKeyboardButton(text="More about speciality", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-121-inzheneriya-programnogo-zabezpechennya")
Button45 = InlineKeyboardButton(text="122 Computer science", callback_data="ComSciClick")
Button46 = InlineKeyboardButton(text="More about speciality", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/122-komp-yuterninauki")
Button47 = InlineKeyboardButton(text="123 Computer engineering", callback_data="ComIngClick")
Button48 = InlineKeyboardButton(text="More about speciality", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-123-komp-yuterna-inzheneriya")
Button49 = InlineKeyboardButton(text="124 System analysis", callback_data="ComSysAnalysingClick")
Button50 = InlineKeyboardButton(text="More about speciality", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-124-sistemniy-analiz")
Button51 = InlineKeyboardButton(text="125 CyberSecurity", callback_data="CyberClick")
Button52 = InlineKeyboardButton(text="More about speciality", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-125-kiberbezpeka-ta-zakhyst-informatsii")
Button53 = InlineKeyboardButton(text="126 Information systems and technologies", callback_data="InfoClick")
Button54 = InlineKeyboardButton(text="More about speciality", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-126-informatsiyni-sistemi-ta-tehnologiyi")
Button55 = InlineKeyboardButton(text="163 Biomedical Engineering", callback_data="BioClick")
Button56 = InlineKeyboardButton(text="More about speciality", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-163-biomedichna-inzheneriya")
Button57 = InlineKeyboardButton(text="171 Electronics", callback_data="ElecClick")
Button58 = InlineKeyboardButton(text="More about speciality", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-171-elektronika")
Button59 = InlineKeyboardButton(text="172 Telecommunications and Radio Engineering", callback_data="TeleClick")
Button60 = InlineKeyboardButton(text="More about speciality", url="https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-172-elektronni-komunikatsii-ta-radiotekhnika")
Button61 = InlineKeyboardButton(text="173 Avionics", callback_data="AviClick")
Button62 = InlineKeyboardButton(text="More about speciality", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-173-avionika")
Button63 = InlineKeyboardButton(text="175 Information and measurement technologies", callback_data="InfTechClick")
Button64 = InlineKeyboardButton(text="More about speciality", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-175-informatsijno-vymiriuvalni-tekhnolohii")
Button65 = InlineKeyboardButton(text="176 Micro- and nanosystem technology", callback_data="MicroClick")
Button66 = InlineKeyboardButton(text="More about speciality", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-176-mikro-ta-nanosystemna-tekhnika")
Button67 = InlineKeyboardButton(text="186 Publishing and Printing", callback_data="PubClick")
Button68 = InlineKeyboardButton(text="More about speciality", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-186-vidavnitstvo-ta-poligrafiya")

#-------------------------------ІНЛАЙН КНОПКИ ПРО СПЕЦІАЛЬНОСТІ НА УКР-----------------------#
Button39_ukr = InlineKeyboardButton(text="051 Економіка", callback_data="Economic")
Button40_ukr = InlineKeyboardButton(text="Більше про спеціальність", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-051-ekonomika")
Button41_ukr = InlineKeyboardButton(text="113 Прикладна Математика", callback_data="Mathematics")
Button42_ukr = InlineKeyboardButton(text="Більше про спеціальність", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-113-prikladna-matematika")
Button43_ukr = InlineKeyboardButton(text="121 Програмна Інженерія", callback_data="Soft")
Button44_ukr = InlineKeyboardButton(text="Більше про спеціальність", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-121-inzheneriya-programnogo-zabezpechennya")
Button45_ukr = InlineKeyboardButton(text="122 Комп'ютерні Науки", callback_data="ComSci")
Button46_ukr = InlineKeyboardButton(text="Більше про спеціальність", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/122-komp-yuterninauki")
Button47_ukr = InlineKeyboardButton(text="123 Комп'ютерна Інженерія", callback_data="ComIng")
Button48_ukr = InlineKeyboardButton(text="Більше про спеціальність", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-123-komp-yuterna-inzheneriya")
Button49_ukr = InlineKeyboardButton(text="124 Системний Аналіз", callback_data="ComSysAnalysing")
Button50_ukr = InlineKeyboardButton(text="Більше про спеціальність", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-124-sistemniy-analiz")
Button51_ukr = InlineKeyboardButton(text="125 Кібербезпека", callback_data="Cyber")
Button52_ukr = InlineKeyboardButton(text="Більше про спеціальність", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-125-kiberbezpeka-ta-zakhyst-informatsii")
Button53_ukr = InlineKeyboardButton(text="126 Інформаційні Системи та Технології", callback_data="Info")
Button54_ukr = InlineKeyboardButton(text="Більше про спеціальність", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-126-informatsiyni-sistemi-ta-tehnologiyi")
Button55_ukr = InlineKeyboardButton(text="163 Біомедична Інженерія", callback_data="Bio")
Button56_ukr = InlineKeyboardButton(text="Більше про спеціальність", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-163-biomedichna-inzheneriya")
Button57_ukr = InlineKeyboardButton(text="171 Електроніка", callback_data="Elec")
Button58_ukr = InlineKeyboardButton(text="Більше про спеціальність", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-171-elektronika")
Button59_ukr = InlineKeyboardButton(text="172 Електронні комунікації та радіотехніка", callback_data="Tele")
Button60_ukr = InlineKeyboardButton(text="Більше про спеціальність", url="https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-172-elektronni-komunikatsii-ta-radiotekhnika")
Button61_ukr = InlineKeyboardButton(text="173 Авіоніка", callback_data="Avi")
Button62_ukr = InlineKeyboardButton(text="Більше про спеціальність", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-173-avionika")
Button63_ukr = InlineKeyboardButton(text="175 Інформаційно-вимірювальні технології", callback_data="InfTech")
Button64_ukr = InlineKeyboardButton(text="Більше про спеціальність", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-175-informatsijno-vymiriuvalni-tekhnolohii")
Button65_ukr = InlineKeyboardButton(text="176 Мікро- and наносистемна техніка", callback_data="Micro")
Button66_ukr = InlineKeyboardButton(text="Більше про спеціальність", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-176-mikro-ta-nanosystemna-tekhnika")
Button67_ukr = InlineKeyboardButton(text="186 Видавництво та Поліграфія", callback_data="Pub")
Button68_ukr = InlineKeyboardButton(text="Більше про спеціальність", url = "https://nure.ua/abituriyentam/spetsialnosti-ta-spetsializatsiyi/spetsialnist-186-vidavnitstvo-ta-poligrafiya")


#--------------------------Departments--------------------------#
Button69 = InlineKeyboardButton(text='(ICS)-Information control system',
                                url="https://nure.ua/en/department/department-of-information-control-system-ics")
Button70 = InlineKeyboardButton(text='(AI)-Artificial Intelligence',
                                url="https://nure.ua/en/department/artificial-intelligence-department-ai")
Button71 = InlineKeyboardButton(text='(SysEng)-System Engineering',
                                url="https://nure.ua/en/department/department-of-systems-engineering-syseng")
Button72 = InlineKeyboardButton(text='(SE)-Software Engineering',
                                url="https://nure.ua/en/department/department-of-software-engineering")
Button73 = InlineKeyboardButton(text='(MST)-Media Systems and Technologies',
                                url="https://nure.ua/en/department/department-of-media-systems-and-technologies-mst")
Button74 = InlineKeyboardButton(text='(CITS)-Computer intelligent technologies and systems',
                                url="https://nure.ua/en/department/department-of-somputer-intelligent-technologies-and-systems-cits")
Button75 = InlineKeyboardButton(text='(EC)-Electronic Computers',
                                url="https://nure.ua/en/department/department-of-electronic-computers")
Button76 = InlineKeyboardButton(text='(ITS)-Information Technology Security',
                                url="https://nure.ua/en/department/department-of-information-technology-security-its")
Button77 = InlineKeyboardButton(text='(DA)-Design Automation',
                                url="https://nure.ua/en/department/design-automation-department")
Button78 = InlineKeyboardButton(text='Philosophy',
                                url="https://nure.ua/en/department/philosophy-department")
Button79 = InlineKeyboardButton(text='(Ukr)-Ukrainian Studies',
                                url="https://nure.ua/en/department/department-of-ukrainian-studies-us")
Button80 = InlineKeyboardButton(text='(CITAM)-Computer-Integrated Technologies, Automation and Mechatronics',
                                url="https://nure.ua/en/department/department-of-computer-integrated-tech-nologies-auto-mation-and-me-chatronics-citam")
Button81 = InlineKeyboardButton(text='(DOED)-Design and Operation of Electronic Devices',
                                url="https://nure.ua/en/department/department-of-design-and-operation-of-electronic-devices")
Button82 = InlineKeyboardButton(text='Physics',
                                url="https://nure.ua/en/department/department-of-physics")
Button83 = InlineKeyboardButton(text='Occupational Safety',
                                url="https://nure.ua/en/department/occupational-safety-department")
Button84 = InlineKeyboardButton(text='(INF)-Informatics',
                                url="https://nure.ua/en/department/department-of-informatics-inf")
Button85 = InlineKeyboardButton(text='(AM)-Applied Mathematics',
                                url="https://nure.ua/en/department/department-of-applied-mathematics-am")
Button86 = InlineKeyboardButton(text='Higher Mathematics',
                                url="https://nure.ua/en/department/department-of-higher-mathematics")
Button87 = InlineKeyboardButton(text='Economic Сybernetics and Management of Economic Security',
                                url="https://nure.ua/en/department/department-of-economic-sybernetics-and-management-of-economic-security")
Button88 = InlineKeyboardButton(text='Infocommunication Engineering V.V. Popovsky',
                                url="https://nure.ua/en/department/department-of-infocommunication-engineering")
Button89 = InlineKeyboardButton(text='(INE)-Information and Network Engineering',
                                url="https://nure.ua/en/department/department-of-information-and-network-engineering-ine")
Button90 = InlineKeyboardButton(text='(IMT)-Information and Measurement Technology',
                                url="https://nure.ua/en/department/department-of-information-and-measurement-technology-imt")
Button91 = InlineKeyboardButton(text='(LT)-Language Training',
                                url="https://nure.ua/en/department/department-of-language-training-lt")
Button92 = InlineKeyboardButton(text='(BME)-Biomedical Engineering',
                                url="https://nure.ua/en/department/department-of-biomedical-engineering-bme")
Button93 = InlineKeyboardButton(text='Microelectronics, Electronic Devices and Appliances',
                                url="https://nure.ua/en/department/department-of-microelectronics-electronic-devices-and-appliances")
Button94 = InlineKeyboardButton(text='(PFEE)-Physical Foundations of Electronic Engineering',
                                url="https://nure.ua/en/department/physical-foundations-of-electronic-engineering-department-pfee")
Button95 = InlineKeyboardButton(text='(PES)-Physical Education and Sports',
                                url="https://nure.ua/en/department/department-of-physical-education-and-sports")
Button96 = InlineKeyboardButton(text='(MTS)-Microprocessor Technologies and Systems',
                                url="https://nure.ua/en/department/department-of-microprocessor-technologies-and-systems-mts")
Button97 = InlineKeyboardButton(text='Computer Radio Engineering and Technical Information Security Systems',
                                url="https://nure.ua/en/department/department-of-computer-radio-engineering-and-technical-information-security-systems")
Button98 = InlineKeyboardButton(text='(RTICS)-Radiotechnologies Information and Communication Systems',
                                url="https://nure.ua/en/department/department-of-radiotechnologies-information-and-communication-systems-rtics")
Button99 = InlineKeyboardButton(text='(MEIRES)-Media Engineering and Information Radioelectronic Systems',
                                url="https://nure.ua/en/department/department-of-media-engineering-and-information-radioelectronic-systems-meires")
Button100 = InlineKeyboardButton(text='Foreign Languages',
                                url="https://nure.ua/en/department/foreign-languages-department")

#-------------------------------------КАФЕДРИ НА УКР.МОВІ---------------------------------------------#
Button69_ukr = InlineKeyboardButton(text='(ІУС)-Інформаційно управляючі системи',
                                url="https://nure.ua/department/kafedra-informatsiynih-upravlyayuchih-sistem-ius")
Button70_ukr = InlineKeyboardButton(text='(ШІ)-Штучний інтелект',
                                url="https://nure.ua/department/kafedra-shtuchnogo-intelektu")
Button71_ukr = InlineKeyboardButton(text='(СТ)-Системотехніка',
                                url="https://nure.ua/department/kafedra-sistemotehniki")
Button72_ukr = InlineKeyboardButton(text='(ПІ)-Програмна інженерія',
                                url="https://nure.ua/department/kafedra-programnoyi-inzheneriyi-pi")
Button73_ukr = InlineKeyboardButton(text='(МСТ)-Медіасистеми та технології',
                                url="https://nure.ua/department/kafedra-mediasistem-ta-tehnologiy-mst")
Button74_ukr = InlineKeyboardButton(text='(КІТС)-Комп’ютерні інтелектуальні технології та системи',
                                url="https://nure.ua/department/kafedra-komp-juternih-intelektualnih-tehnologij-ta-sistem")
Button75_ukr = InlineKeyboardButton(text='(ЕОМ)-Електронно обчислювальні машини',
                                url="https://nure.ua/department/kafedra-elektronnih-obchislyuvalnih-mashin-eom")
Button76_ukr = InlineKeyboardButton(text='(БІТ)-Безпека інформаційних технологій',
                                url="https://nure.ua/department/kafedra-bezpeki-informatsiynih-tehnologiy-bit")
Button77_ukr = InlineKeyboardButton(text='(АПОТ)-Автоматизація проектування обчислювальної техніки',
                                url="https://nure.ua/department/kafedra-avtomatizatsiyi-proektuvannya-obchislyuvalnoyi-tehniki-apot")
Button78_ukr = InlineKeyboardButton(text='Філософія',
                                url="https://nure.ua/department/kafedra-filosofiyi")
Button79_ukr = InlineKeyboardButton(text='(Укр)-Українознавство',
                                url="https://nure.ua/department/kafedra-ukrayinoznavstva-ukr")
Button80_ukr = InlineKeyboardButton(text='(КІТАМ)-Комп"’"ютерно-інтегрованs технології, автоматизація та мехатроніка',
                                url="https://nure.ua/department/kafedra-komp-yuterno-integrovanih-tehnologiy-avtomatizatsiyi-ta-mehatroniki-kitam")
Button81_ukr = InlineKeyboardButton(text='(ПЕЕА)-Проектування та експлуатації електронних апаратів',
                                url="https://nure.ua/department/kafedra-proektuvannya-ta-ekspluatatsiyi-elektronnih-aparativ-peea")
Button82_ukr = InlineKeyboardButton(text='Фізика',
                                url="https://nure.ua/department/kafedra-fiziki")
Button83_ukr = InlineKeyboardButton(text='(ОП)-Охорона праці',
                                url="https://nure.ua/department/kafedra-ohoroni-pratsi-op")
Button84_ukr = InlineKeyboardButton(text='(ІНФ)-Інформатика',
                                url="https://nure.ua/department/kafedra-informatiki-inf")
Button85_ukr = InlineKeyboardButton(text='(ПМ)-Прикладна математика',
                                url="https://nure.ua/department/kafedra-prikladnoyi-matematiki-pm")
Button86_ukr = InlineKeyboardButton(text='(ВМ)-Вища математика',
                                url="https://nure.ua/department/kafedra-vishhoyi-matematiki-vm")
Button87_ukr = InlineKeyboardButton(text='(ЕК)-Економічна кібернетика та управління економічною безпекою',
                                url="https://nure.ua/department/kafedra-ekonomichnoyi-kibernetiki-ta-upravlinnya-ekonomichnoyu-bezpekoyu-ek")
Button88_ukr = InlineKeyboardButton(text='(ІКІ)-Інфокомунікаційна інженерія ім. В.В. Поповського',
                                url="https://nure.ua/department/kafedra-infokomunikatsiynoyi-inzheneriyi-iki")
Button89_ukr = InlineKeyboardButton(text='(ІМІ)-Інформаційно-мережна інженерія',
                                url="https://nure.ua/department/kafedra-informatsiyno-merezhnoyi-inzheneriyi-imi")
Button90_ukr = InlineKeyboardButton(text='(ІВТ)-Інформаційно-вимірювальні технології',
                                url="https://nure.ua/department/kafedra-informacijno-vimirjuvalnih-tehnologij-ivt")
Button91_ukr = InlineKeyboardButton(text='(МП)-Мовна підготовка',
                                url="https://nure.ua/department/kafedra-movnoyi-pidgotovki-mp")
Button92_ukr = InlineKeyboardButton(text='(БМІ)-Біомедична інженерія',
                                url="https://nure.ua/department/kafedra-biomedichnoyi-inzheneriyi-bmi")
Button93_ukr = InlineKeyboardButton(text='(МЕЕПП)-Мікроелектроніка, електронних приладів та пристроїв ',
                                url="https://nure.ua/department/kafedra-mikroelektroniki-elektronnih-priladiv-ta-pristroyiv-meepp")
Button94_ukr = InlineKeyboardButton(text='(ФОЕТ)-Фізичні основи електронної техніки',
                                url="https://nure.ua/department/kafedra-fizichnih-osnov-elektronnoi-tehniki-foet")
Button95_ukr = InlineKeyboardButton(text='(ФВС)-Фізичне виховання та спорт',
                                url="https://nure.ua/department/kafedra-fizichnogo-vihovannya-ta-sportu-fvs")
Button96_ukr = InlineKeyboardButton(text='(МТС)-Мікропроцесорні технології і системи',
                                url="https://nure.ua/department/kafedra-mikroprocesornih-tehnologij-i-sistem-mts")
Button97_ukr = InlineKeyboardButton(text="(КРіСТЗІ)-Комп’ютерна радіоінженерія та системи технічного захисту інформації",
                                url="https://nure.ua/department/kafedra-komp-yuternoyi-radioinzheneriyi-ta-sistem-tehnichnogo-zahistu-informatsiyi-kristzi")
Button98_ukr = InlineKeyboardButton(text='(РТІКС)-Радіотехнології інформаційно-комунікаційних систем',
                                url="https://nure.ua/department/kafedra-radiotehnologiy-informatsiyno-komunikatsiynih-sistem-rtiks")
Button99_ukr = InlineKeyboardButton(text='(МІРЕС)-Медіаінженерія та інформаційні радіоелектронні системи',
                                url="https://nure.ua/department/kafedra-mediainzheneriyi-ta-informatsiynih-radioelektronnih-sistem-mires")
Button100_ukr = InlineKeyboardButton(text='Іноземні мови',
                                url="https://nure.ua/department/kafedra-inozemnih-mov")

Button101_ukr = KeyboardButton("Сповіщення 🔔")
Button102_eng = KeyboardButton("Notifications 🔔")
NotifKeyboard = ReplyKeyboardMarkup(row_width = 2)




# кнопки плюшки
AboutFreeProducts = KeyboardButton("'Плюшки' студентам 🎁")
AboutFreeProducts_en = KeyboardButton("'Goodies' for students 🎁")

# BUTTONS

MultilingualismMarkup = ReplyKeyboardMarkup(resize_keyboard=True)
MultilingualismMarkup.add(Button5, Button8)                         # for multiling

ApplicantAndStudentMarkup = ReplyKeyboardMarkup(resize_keyboard=True)
ApplicantAndStudentMarkup.insert(Button23).insert(Button24).add(Button26)

UkrApplicantAndStudentMarkup = ReplyKeyboardMarkup(resize_keyboard=True)
UkrApplicantAndStudentMarkup.insert(Button23_ukr).insert(Button24_ukr).add(Button26_ukr)  # for multiling

#------------------клавіатура для студента------------------------
KeyBoardClient = ReplyKeyboardMarkup(resize_keyboard=True)
KeyBoardClient.add(Button1, Button2).add(AboutFreeProducts_en, Button4).add(Button7)

UkrKeyBoardClient = ReplyKeyboardMarkup(resize_keyboard=True)
UkrKeyBoardClient.add(Button1_ukr, Button2_ukr).add(AboutFreeProducts, Button4_ukr).add(Button7_ukr)  # for multiling



markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(Button10).insert(Button102_eng).add(Button6)

Ukrmarkup = ReplyKeyboardMarkup(resize_keyboard=True)
Ukrmarkup.add(Button10_ukr).insert(Button101_ukr).add(Button6_ukr)        # for multiling

# markup2 = ReplyKeyboardMarkup(resize_keyboard=True)
# markup2.add(Button9)

ListOfFacultiesMarkup = ReplyKeyboardMarkup(resize_keyboard=True)
ListOfFacultiesMarkup.add(Button11).insert(Button9)

UkrListOfFacultiesMarkup = ReplyKeyboardMarkup(resize_keyboard=True)     # for multiling
UkrListOfFacultiesMarkup.add(Button11_ukr).insert(Button9_ukr)

KiuFacultyMarkup = ReplyKeyboardMarkup(resize_keyboard=True)
KiuFacultyMarkup.add(Button12).insert(Button9)

UkrKiuFacultyMarkup = ReplyKeyboardMarkup(resize_keyboard=True)        # for multiling
UkrKiuFacultyMarkup.add(Button12_ukr).insert(Button9_ukr)

# ListOfCoursesMarkup = ReplyKeyboardMarkup(resize_keyboard=True)
# ListOfCoursesMarkup.add(Button13).insert(Button9)

NumberOfCoursesMarkup = ReplyKeyboardMarkup(resize_keyboard=True)
NumberOfCoursesMarkup.add(Button14).insert(Button9)

Ukr_NumberOfCoursesMarkup = ReplyKeyboardMarkup(resize_keyboard=True)    # for multiling
Ukr_NumberOfCoursesMarkup.add(Button14_ukr).insert(Button9_ukr)

# ListOfGroupsMarkup = ReplyKeyboardMarkup(resize_keyboard=True)
# ListOfGroupsMarkup.add(Button15).insert(Button9)

MenuApplicantMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
MenuApplicantMarkup.add(Button25, Button31).add(Button27, Button32).add(Button28, Button38).add(Button1).add(Button7)

UkrMenuApplicantMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
UkrMenuApplicantMarkup.add(Button25_ukr, Button31_ukr).add(Button27_ukr, Button32_ukr).\
    add(Button28_ukr, Button38_ukr).add(Button1_ukr).add(Button7_ukr)                                   # for multiling

DepartmentsMarkup = InlineKeyboardMarkup(row_width=1)
DepartmentsMarkup.add(Button69, Button70, Button71, Button72, Button73, Button74, Button75, Button76,
                      Button77, Button78, Button79, Button80, Button81, Button82, Button83, Button84, Button85,
                      Button86, Button87, Button88, Button89, Button90, Button91, Button92, Button93, Button94,
                      Button95, Button96, Button97, Button98, Button99, Button100)

UkrDepartmentsMarkup = InlineKeyboardMarkup(row_width=1)              # for multiling
UkrDepartmentsMarkup.add(Button69_ukr, Button70_ukr, Button71_ukr, Button72_ukr, Button73_ukr, Button74_ukr,
                         Button75_ukr, Button76_ukr, Button77_ukr, Button78_ukr, Button79_ukr, Button80_ukr,
                         Button81_ukr, Button82_ukr, Button83_ukr, Button84_ukr, Button85_ukr, Button86_ukr,
                         Button87_ukr, Button88_ukr, Button89_ukr, Button90_ukr, Button91_ukr, Button92_ukr,
                         Button93_ukr, Button94_ukr, Button95_ukr, Button96_ukr, Button97_ukr, Button98_ukr,
                         Button99_ukr, Button100_ukr)

SpecialitesMarkup = InlineKeyboardMarkup(row_width=2)
SpecialitesMarkup.add(Button39).add(Button41).add(Button43).\
    add(Button45).add(Button47).add(Button49).add(Button51).\
    add(Button53).add(Button55).add(Button57).add(Button59).\
    add(Button61).add(Button63).add(Button65).add(Button67)

Ukr_SpecialitesMarkup = InlineKeyboardMarkup(row_width=2)
Ukr_SpecialitesMarkup.add(Button39_ukr).add(Button41_ukr).add(Button43_ukr).\
    add(Button45_ukr).add(Button47_ukr).add(Button49_ukr).add(Button51_ukr).\
    add(Button53_ukr).add(Button55_ukr).add(Button57_ukr).add(Button59_ukr).\
    add(Button61_ukr).add(Button63_ukr).add(Button65_ukr).add(Button67_ukr)

SpecialitesEconomicMarkup = InlineKeyboardMarkup(row_width=2)
SpecialitesEconomicMarkup.add(Button40)

Ukr_SpecialitesEconomicMarkup = InlineKeyboardMarkup(row_width=2)   # for Multilingualism
Ukr_SpecialitesEconomicMarkup.add(Button40_ukr)

SpecialitesMathMarkup = InlineKeyboardMarkup(row_width=2)
SpecialitesMathMarkup.add(Button42)

Ukr_SpecialitesMathMarkup = InlineKeyboardMarkup(row_width=2)   # for Multilingualism
Ukr_SpecialitesMathMarkup.add(Button42_ukr)

SpecialitesSoftEngMarkup = InlineKeyboardMarkup(row_width=2)
SpecialitesSoftEngMarkup.add(Button44)

Ukr_SpecialitesSoftEngMarkup = InlineKeyboardMarkup(row_width=2)    # for Multilingualism
Ukr_SpecialitesSoftEngMarkup.add(Button44_ukr)

SpecialitesCompSciMarkup = InlineKeyboardMarkup(row_width=2)
SpecialitesCompSciMarkup.add(Button46)

Ukr_SpecialitesCompSciMarkup = InlineKeyboardMarkup(row_width=2)    # for Multilingualism
Ukr_SpecialitesCompSciMarkup.add(Button46_ukr)

SpecialitesCompIngMarkup = InlineKeyboardMarkup(row_width=2)
SpecialitesCompIngMarkup.add(Button48)

Ukr_SpecialitesCompIngMarkup = InlineKeyboardMarkup(row_width=2)    # for Multilingualism
Ukr_SpecialitesCompIngMarkup.add(Button48_ukr)

SpecialitesCompSysAnalysingMarkup = InlineKeyboardMarkup(row_width=2)
SpecialitesCompSysAnalysingMarkup.add(Button50)

Ukr_SpecialitesCompSysAnalysingMarkup = InlineKeyboardMarkup(row_width=2)   # for Multilingualism
Ukr_SpecialitesCompSysAnalysingMarkup.add(Button50_ukr)

SpecialitesCyberMarkup = InlineKeyboardMarkup(row_width=2)
SpecialitesCyberMarkup.add(Button52)

Ukr_SpecialitesCyberMarkup = InlineKeyboardMarkup(row_width=2)   # for Multilingualism
Ukr_SpecialitesCyberMarkup.add(Button52_ukr)

SpecialitesInfoMarkup = InlineKeyboardMarkup(row_width=2)
SpecialitesInfoMarkup.add(Button54)

Ukr_SpecialitesInfoMarkup = InlineKeyboardMarkup(row_width=2)   # for Multilingualism
Ukr_SpecialitesInfoMarkup.add(Button54_ukr)

SpecialitesBioMarkup = InlineKeyboardMarkup(row_width=2)
SpecialitesBioMarkup.add(Button56)

Ukr_SpecialitesBioMarkup = InlineKeyboardMarkup(row_width=2)    # for Multilingualism
Ukr_SpecialitesBioMarkup.add(Button56_ukr)

SpecialitesElecMarkup = InlineKeyboardMarkup(row_width=2)
SpecialitesElecMarkup.add(Button58)

Ukr_SpecialitesElecMarkup = InlineKeyboardMarkup(row_width=2)   # for Multilingualism
Ukr_SpecialitesElecMarkup.add(Button58_ukr)

SpecialitesTeleMarkup = InlineKeyboardMarkup(row_width=2)
SpecialitesTeleMarkup.add(Button60)

Ukr_SpecialitesTeleMarkup = InlineKeyboardMarkup(row_width=2)   # for Multilingualism
Ukr_SpecialitesTeleMarkup.add(Button60_ukr)

SpecialitesAvioMarkup = InlineKeyboardMarkup(row_width=2)
SpecialitesAvioMarkup.add(Button62)

Ukr_SpecialitesAvioMarkup = InlineKeyboardMarkup(row_width=2)   # for Multilingualism
Ukr_SpecialitesAvioMarkup.add(Button62_ukr)

SpecialitesMetTechMarkup = InlineKeyboardMarkup(row_width=2)
SpecialitesMetTechMarkup.add(Button64)

Ukr_SpecialitesMetTechMarkup = InlineKeyboardMarkup(row_width=2)    # for Multilingualism
Ukr_SpecialitesMetTechMarkup.add(Button64_ukr)

SpecialitesMicroMarkup = InlineKeyboardMarkup(row_width=2)
SpecialitesMicroMarkup.add(Button66)

Ukr_SpecialitesMicroMarkup = InlineKeyboardMarkup(row_width=2)  # for Multilingualism
Ukr_SpecialitesMicroMarkup.add(Button66_ukr)

SpecialitesPubMarkup = InlineKeyboardMarkup(row_width=2)
SpecialitesPubMarkup.add(Button68)

Ukr_SpecialitesPubMarkup = InlineKeyboardMarkup(row_width=2)    # for Multilingualism
Ukr_SpecialitesPubMarkup.add(Button68_ukr)

GroupsMarkup = ReplyKeyboardMarkup(resize_keyboard=True)
GroupsMarkup.insert(Button22).insert(Button21).add(Button20) \
    .insert(Button19).add(Button18).insert(Button16).add(Button17).insert(Button9)

Ukr_GroupsMarkup = ReplyKeyboardMarkup(resize_keyboard=True)                          # for multiling
Ukr_GroupsMarkup.insert(Button22_ukr).insert(Button21_ukr).add(Button20_ukr) \
    .insert(Button19_ukr).add(Button18_ukr).insert(Button16_ukr).add(Button17_ukr).insert(Button9_ukr)




#------------------Розрахунок балу на укр-------------------------
CompetitionMarkup = InlineKeyboardMarkup(row_width=2)
#Кнопки
Uranian = InlineKeyboardButton(text="Українська мова", callback_data="Укр")
History = InlineKeyboardButton(text="Історія України", callback_data="Іст")
Math = InlineKeyboardButton(text="Математика", callback_data="Мат")
Physics = InlineKeyboardButton(text="Фізика", callback_data="Фіз")
Chemistry = InlineKeyboardButton(text="Хімія", callback_data="Хім")
Biology = InlineKeyboardButton(text="Біологія", callback_data="Біо")
ForeignLanguage = InlineKeyboardButton(text="Іноземна мова", callback_data="Іно")
CalculatingBall = InlineKeyboardButton(text="Підрахунок 🧮", callback_data="Під")
Cancel = InlineKeyboardButton(text="Відміна 🔄", callback_data="Від")


#-----------------Розрахунок балу на англ---------------------
CompetitionMarkup_en = InlineKeyboardMarkup(row_width=2)
#Кнопки для англ----------------------------------------------------------------
Uranian_en = InlineKeyboardButton(text="Ukrainian language", callback_data="Укр_en")
History_en = InlineKeyboardButton(text="History of Ukraine", callback_data="Іст_en")
Math_en = InlineKeyboardButton(text="Mathematics", callback_data="Мат_en")
Physics_en = InlineKeyboardButton(text="Physics", callback_data="Фіз_en")
Chemistry_en = InlineKeyboardButton(text="Chemistry", callback_data="Хім_en")
Biology_en = InlineKeyboardButton(text="Biology", callback_data="Біо_en")
ForeignLanguage_en = InlineKeyboardButton(text="Foreign language", callback_data="Іно_en")
CalculatingBall_en = InlineKeyboardButton(text="Counting 🧮", callback_data="Під_en")
Cancel_en = InlineKeyboardButton(text="Cancel 🔄", callback_data="Від_en")


#Додавання кнопок в клавіатуру для укр------------------
CompetitionMarkup.add(Uranian).add(Math).add(History).add(Physics).add(Chemistry).add(Biology).add(ForeignLanguage)

#Додавання кнопок в клавіатуру для англ------------------
CompetitionMarkup_en.add(Uranian_en).add(Math_en).add(History_en).add(Physics_en).add(Chemistry_en).add(Biology_en).add(ForeignLanguage_en)

#---------------------------на укр----------------------------------------------
SpecialitesCalculatingMarkup = InlineKeyboardMarkup(row_width=2)
CalcEconomic = InlineKeyboardButton(text="051 Економіка", callback_data="Eco")
CalcMath = InlineKeyboardButton(text="113 Прикладна Математика ", callback_data="Mat")
CalcIngSoft = InlineKeyboardButton(text="121 Інженерія Програмного Забезпечення", callback_data="Ing")
CalcCompS = InlineKeyboardButton(text="122 Комп’ютерні науки ", callback_data="Com")
CalcCompEn = InlineKeyboardButton(text="123 Комп’ютерна інженерія", callback_data="Eng")
CalcSystAny = InlineKeyboardButton(text="124 Системний аналіз", callback_data="Sys")
CalcCyber = InlineKeyboardButton(text="125 Кібербезпека та захист інформації", callback_data="Cyb")
CalcInfo = InlineKeyboardButton(text="126 Інформаційні системи та технології", callback_data="Inf")
CalcBio = InlineKeyboardButton(text="163 Біомедична інженерія", callback_data="Byo")
CalcElec = InlineKeyboardButton(text="171 Електроніка ", callback_data="Ele")
CalcElecRadio = InlineKeyboardButton(text="172 Електронні комунікації та радіотехніка", callback_data="Rad")
CalcAvio = InlineKeyboardButton(text="173 Авіоніка", callback_data="Avion")
CalcAuto = InlineKeyboardButton(text="174 Автоматизація, комп’ютерноінтегровані технології та робототехніка", callback_data="Aut")
CalcInfoCalc = InlineKeyboardButton(text="175 Інформаційно-вимірювальні технології", callback_data="Cal")
CalcPolig = InlineKeyboardButton(text="186 Видавництво та поліграфія", callback_data="Pol")


#---------------------------на англ----------------------------------------------
SpecialitesCalculatingMarkup_en = InlineKeyboardMarkup(row_width=2)
CalcEconomic_en = InlineKeyboardButton(text="051 Economics", callback_data="Eco_en")
CalcMath_en = InlineKeyboardButton(text="113 Applied Mathematics", callback_data="Mat_en")
CalcIngSoft_en = InlineKeyboardButton(text="121 Software Engineering", callback_data="Ing_en")
CalcCompS_en = InlineKeyboardButton(text="122 Computer science ", callback_data="Com_en")
CalcCompEn_en = InlineKeyboardButton(text="123 Computer engineering", callback_data="Eng_en")
CalcSystAny_en = InlineKeyboardButton(text="124 System analysis", callback_data="Sys_en")
CalcCyber_en = InlineKeyboardButton(text="125 Cybersecurity and information protection", callback_data="Cyb_en")
CalcInfo_en = InlineKeyboardButton(text="126 Information systems and technologies", callback_data="Inf_en")
CalcBio_en = InlineKeyboardButton(text="163 Biomedical engineering", callback_data="Byo_en")
CalcElec_en = InlineKeyboardButton(text="171 Electronics ", callback_data="Ele_en")
CalcElecRadio_en = InlineKeyboardButton(text="172 Electronic communications and radio engineering", callback_data="Rad_en")
CalcAvio_en = InlineKeyboardButton(text="173 Avionics", callback_data="Avi_en")
CalcAuto_en = InlineKeyboardButton(text="174 Automation, computer-integrated technologies and robotics", callback_data="Aut_en")
CalcInfoCalc_en = InlineKeyboardButton(text="175 Information and measurement technologies", callback_data="Cal_en")
CalcPolig_en = InlineKeyboardButton(text="186 Publishing and printing", callback_data="Pol_en")


#---------------------------для укр----------------------------------------------
SpecialitesCalculatingMarkup.add(CalcEconomic).add(CalcMath).add(CalcIngSoft).add(CalcCompS).add(CalcCompEn).add(CalcSystAny).\
                             add(CalcCyber).add(CalcInfo).add(CalcBio).add(CalcElec).add(CalcElecRadio).add(CalcAvio).add(CalcAuto).\
                             add(CalcInfoCalc).add(CalcPolig)

#---------------------------для англ----------------------------------------------
SpecialitesCalculatingMarkup_en.add(CalcEconomic_en).add(CalcMath_en).add(CalcIngSoft_en).add(CalcCompS_en).add(CalcCompEn_en).add(CalcSystAny_en).\
                             add(CalcCyber_en).add(CalcInfo_en).add(CalcBio_en).add(CalcElec_en).add(CalcElecRadio_en).add(CalcAvio).add(CalcAuto_en).\
                             add(CalcInfoCalc_en).add(CalcPolig_en)

#---------------------------для укр----------------------------------------------
YesNo = InlineKeyboardMarkup(row_width=2)
Yes = InlineKeyboardButton(text="163 Біомедична Інженерія", callback_data="Yes")
No = InlineKeyboardButton(text="Інші", callback_data="No")
YesNo.add(CalcBio, No)

#---------------------------для англ----------------------------------------------
YesNo_en = InlineKeyboardMarkup(row_width=2)
Yes_en = InlineKeyboardButton(text="163 Biomedical engineering", callback_data="Yes_en")
No_en = InlineKeyboardButton(text="Others", callback_data="No_en")
YesNo_en.add(CalcBio_en, No_en)


#---------------------------для укр----------------------------------------------
SpecialOnlyForBio = InlineKeyboardMarkup(row_width=2)
SpecialOnlyForBio.add(CalcBio).add(Cancel)

SpecialitesCalculatingWithoutBioMarkup = InlineKeyboardMarkup(row_width=2)
SpecialitesCalculatingWithoutBioMarkup.add(CalcEconomic).add(CalcMath).add(CalcIngSoft).add(CalcCompS).add(CalcCompEn).add(CalcSystAny).\
                             add(CalcCyber).add(CalcInfo).add(CalcElec).add(CalcElecRadio).add(CalcAvio).add(CalcAuto).\
                             add(CalcInfoCalc).add(CalcPolig)

SpecialitesCalculatingMarkup12 = InlineKeyboardMarkup()
yes_button = InlineKeyboardButton("Да", callback_data="biology_required_yes")
no_button = InlineKeyboardButton("Нет", callback_data="biology_required_no")
SpecialitesCalculatingMarkup12.row(yes_button, no_button)


#---------------------------для англ----------------------------------------------
SpecialOnlyForBio_en = InlineKeyboardMarkup(row_width=2)
SpecialOnlyForBio_en.add(CalcBio_en).add(Cancel_en)

SpecialitesCalculatingWithoutBioMarkup_en = InlineKeyboardMarkup(row_width=2)
SpecialitesCalculatingWithoutBioMarkup_en.add(CalcEconomic_en).add(CalcMath_en).add(CalcIngSoft_en).add(CalcCompS_en).add(CalcCompEn_en).add(CalcSystAny_en).\
                             add(CalcCyber_en).add(CalcInfo_en).add(CalcElec_en).add(CalcElecRadio_en).add(CalcAvio_en).add(CalcAuto_en).\
                             add(CalcInfoCalc_en).add(CalcPolig_en)

SpecialitesCalculatingMarkup12_en = InlineKeyboardMarkup()
yes_button_en = InlineKeyboardButton("Yes", callback_data="biology_required_yes_en")
no_button_en = InlineKeyboardButton("No", callback_data="biology_required_no_en")
SpecialitesCalculatingMarkup12_en.row(yes_button_en, no_button_en)


#---------------------------для укр---------------------------
IKB = InlineKeyboardMarkup()
ZNO = InlineKeyboardButton(text="ЗНО", callback_data="ЗНО")
NMT = InlineKeyboardButton(text="НМТ", callback_data="НМТ")
IKB.add(ZNO)

#---------------------------для англ-----------------------------
IKB_en = InlineKeyboardMarkup()
ZNO_en = InlineKeyboardButton(text="EIT", callback_data="ЗНО_en")
NMT_en = InlineKeyboardButton(text="NMT", callback_data="НМТ_en")
IKB_en.add(ZNO_en)


#---------------------------для укр-----------------------------------------------------------------
CoursesAndFreeFirst = InlineKeyboardMarkup()
AboutOffice = InlineKeyboardButton(text="Продукція Microsoft Office 365", callback_data = "Office")
AboutCoursera = InlineKeyboardButton(text="Coursera платформа", callback_data = "Coursera")
AboutUdemy = InlineKeyboardButton(text="Udemy платформа", callback_data = "Udemy")
AboutEdx = InlineKeyboardButton(text="edX платформа", callback_data = "Edx")
AboutJet = InlineKeyboardButton(text="Продукція JetBrains", callback_data = "Jet")
CoursesAndFreeFirst.add(AboutOffice).add(AboutCoursera).add(AboutUdemy).add(AboutEdx).add(AboutJet)


#---------------------------для англ----------------------------------------------------------------
CoursesAndFreeFirst_en = InlineKeyboardMarkup()
AboutOffice_en = InlineKeyboardButton(text="Microsoft Office 365 products", callback_data="Office_en")
AboutCoursera_en = InlineKeyboardButton(text="Coursera platform", callback_data="Coursera_en")
AboutUdemy_en = InlineKeyboardButton(text="Udemy platform", callback_data="Udemy_en")
AboutEdx_en = InlineKeyboardButton(text="edX platform", callback_data="Edx_en")
AboutJet_en = InlineKeyboardButton(text="JetBrains products", callback_data="Jet_en")
CoursesAndFreeFirst_en.add(AboutOffice_en).add(AboutCoursera_en).add(AboutUdemy_en).add(AboutEdx_en).add(AboutJet_en)

#---------------------------для англ-----------------------------------------------------------------
CoursesAndFreeSecond_en = InlineKeyboardMarkup()
AboutOfficeSecond_en = InlineKeyboardButton(text="Get instructions", url="https://nure.ua/universytet/it-prostir-nure/programne-zabezpechennja/produkti-microsoft-dlja-studentiv-hnure")
CoursesAndFreeSecond_en.add(AboutOfficeSecond_en)

CoursesAndFreeThird_en = InlineKeyboardMarkup()
AboutCourseraSecond_en = InlineKeyboardButton(text="Get instructions", url="https://software.nure.ua/coursera-edx-nure/")
CoursesAndFreeThird_en.add(AboutCourseraSecond_en)

CoursesAndFreeFourth_en = InlineKeyboardMarkup()
AboutUdemySecond_en = InlineKeyboardButton(text="Get instructions", url="https://software.nure.ua/udemy/")
CoursesAndFreeFourth_en.add(AboutUdemySecond_en)

CoursesAndFreeFive_en = InlineKeyboardMarkup()
AboutEdxSecond_en = InlineKeyboardButton(text="Get instructions", url="https://software.nure.ua/coursera-edx-nure/")
CoursesAndFreeFive_en.add(AboutEdxSecond_en)

CoursesAndFreeSix_en = InlineKeyboardMarkup()
AboutPyCharmSecond_en = InlineKeyboardButton(text="Get instructions", url="https://www.jetbrains.com/shop/eform/students")
CoursesAndFreeSix_en.add(AboutPyCharmSecond_en)


#---------------------------для укр----------------------------------------------------------------
CoursesAndFreeSecond = InlineKeyboardMarkup()
AboutOfficeSecond = InlineKeyboardButton(text="Отримати інструкцію", url="https://nure.ua/universytet/it-prostir-nure/programne-zabezpechennja/produkti-microsoft-dlja-studentiv-hnure")
CoursesAndFreeSecond.add(AboutOfficeSecond)

CoursesAndFreeThird = InlineKeyboardMarkup()
AboutCourseraSecond = InlineKeyboardButton(text="Отримати інструкцію", url="https://software.nure.ua/coursera-edx-nure/")
CoursesAndFreeThird.add(AboutCourseraSecond)

CoursesAndFreeFourth = InlineKeyboardMarkup()
AboutUdemySecond = InlineKeyboardButton(text="Отримати інструкцію", url="https://software.nure.ua/udemy/")
CoursesAndFreeFourth.add(AboutUdemySecond)

CoursesAndFreeFive = InlineKeyboardMarkup()
AboutEdxSecond = InlineKeyboardButton(text="Отримати інструкцію", url="https://software.nure.ua/coursera-edx-nure/")
CoursesAndFreeFive.add(AboutEdxSecond)

CoursesAndFreeSix = InlineKeyboardMarkup()
AboutPyCharmSecond = InlineKeyboardButton(text="Отримати інструкцію", url="https://www.jetbrains.com/shop/eform/students")
CoursesAndFreeSix.add(AboutPyCharmSecond)




