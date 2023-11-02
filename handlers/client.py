import logging
import asyncio
from sre_parse import State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import update
from telebot.types import CallbackQuery, InlineKeyboardButton
from create_bot import API_TOKEN, types, dp, bot, Dispatcher, executor as ex
from buttons.buttons_main import *
from CIST.cist import *
from Links.Links import *
from HugeTexts.Texts import *
from HugeTexts import *
import os
import json
import aiogram.dispatcher.filters.state
import math
from HugeTexts.TextAboutPresents import *
from HugeTexts.TextAboutCalcSpecialities import *

@dp.message_handler(commands=['show_notes'])
async def show_notes(message: types.Message):
    user_id = message.from_user.id

    conn, cursor = connect_db('events.db')
    cursor.execute("SELECT * FROM events WHERE user_id = ?", (user_id,))
    events = cursor.fetchall()
    conn.close()

    if not events:
        await message.answer("У вас нет сохраненных заметок.")
    else:
        response = "Ваши заметки:\n\n"
        for event in events:
            event_text = event[2]
            event_date = event[3]
            response += f"- {event_text} ({event_date})\n"
        await message.answer(response)

@dp.message_handler(commands=['start'])
async def start(message: types.Message, state: FSMContext):
    await message.reply(f"Hello👋, Select a language please👇\nПривіт👋, Обери мову будь ласка👇",
                        reply_markup=MultilingualismMarkup)

    #------------------------
    await state.finish()
    global Ukr_score, Math_score, Hist_score, Phys_score, Foreign_score, Biology, Chemistry, TotalScore
    Ukr_score = None
    Math_score = None
    Hist_score = None
    Phys_score = None
    Foreign_score = None
    Biology = None
    Chemistry = None
    TotalScore = None
    marked_subjects = []
    #-------------------------

#-----------------------------------------------------------------------------------------------------------------
@dp.message_handler(content_types=['text'])
async def main_menu(message: types.Message):
    global user_status
    global user_status_e
    global Language

    if message.text == "English 🇬🇧":
        await message.reply(f"Hi, {message.from_user.username}!\nI'm EduHelpBot!")
        await bot.send_message(message.chat.id, "Processing...", reply_markup=ApplicantAndStudentMarkup)  # for multi

    elif message.text == "Change language 🇬🇧🇺🇦":
        await bot.send_message(message.chat.id, "Processing...", reply_markup=MultilingualismMarkup)

    elif message.text == "Student 👨‍🎓":
        user_status_e = "Student"
        await bot.send_message(message.chat.id, "Processing...", reply_markup=KeyBoardClient)

    elif message.text == "'Goodies' for students 🎁":
        await bot.send_message(message.chat.id, f"{FirstText_en}", reply_markup=CoursesAndFreeFirst_en)

    elif message.text == "List of functions ⚙️":
        if user_status_e == "Student":
            await message.reply(f"Hello, {message.from_user.username}!\nThanks to me, you have the opportunity to 👇\n"
                                f"\n💠 View the schedule ✔️"
                                f"\n💠 Use the notes ✔️"
                                f"\n💠 Get information about access to free resources NURE ✔️")
        else:
            # elif message.text == "The list of functions ⚙":
            await message.reply(f"Hello, {message.from_user.username}!\nThanks to me, you have the opportunity to 👇\n"
                                f"\n💠 Get information about departments and specialities ✔️"
                                f"\n💠 Get information about NURE ✔️"
                                f"\n💠 Get information about the main contacts of NURE ✔️"
                                f"\n💠 Get information on admission documents ✔️"
                                f"\n💠 Calculate the competition score ✔️")

    elif message.text == "Notifications 🔔":
        Language = "Eng"
        await message.answer("Let’s add another event! Enter the name of the event:\n\nExample: Meeting Friends")
        await CreateEventStates.WaitingEvent.set()


    elif message.text == "Contacts ✉️":
        await message.reply("My link is: https://t.me/EduHelpBot\nMy authors are: "
                            f"\n1) https://t.me/YGODHIK \n2) https://t.me/oldnavy_1\n"
                            f"3) https://t.me/sofia_chueva")

    elif message.text == "Next ➡️":
        await bot.send_message(message.chat.id, "Processing...", reply_markup=markup)

    elif message.text == "Back ⬅️":
        await message.reply("Processing...", reply_markup=KeyBoardClient)

    elif message.text == "Main menu 🚪":
        await bot.send_message(message.chat.id, "Processing...", reply_markup=KeyBoardClient)

    elif message.text == "Choosing a status👤":
        await message.reply("Processing...", reply_markup=ApplicantAndStudentMarkup)

    # --------------TIMETABLE--------------
    elif message.text == "Getting a timetable 🗓":
        await bot.send_message(message.chat.id, "Go to the list of faculties", reply_markup=ListOfFacultiesMarkup)

    elif message.text == "List of faculties 🎓":
        await bot.send_message(message.chat.id, "Choose the faculty 👇", reply_markup=KiuFacultyMarkup)

    elif message.text == "Faculty - KIU":
        await bot.send_message(message.chat.id, "Choose the course 👇", reply_markup=NumberOfCoursesMarkup)

    elif message.text == "Second course ⚜":
        await bot.send_message(message.chat.id, "Choose the group 👇", reply_markup=GroupsMarkup)

    elif message.text == "KBIKS-21-5 🎓":
        await bot.send_message(message.chat.id, classes_today("kbiks-21-5", "second"), reply_markup=GroupsMarkup, parse_mode='HTML')

    elif message.text == "KBIKS-21-6 🎓":
        await bot.send_message(message.chat.id, classes_today("kbiks-21-6", "second"), reply_markup=GroupsMarkup, parse_mode='HTML')

    elif message.text == "KBIKS-21-4 🎓":
        await bot.send_message(message.chat.id, classes_today("kbiks-21-4", "second"), reply_markup=GroupsMarkup, parse_mode='HTML')

    elif message.text == "KBIKS-21-3 🎓":
        await bot.send_message(message.chat.id, classes_today("kbiks-21-3", "second"), reply_markup=GroupsMarkup, parse_mode='HTML')

    elif message.text == "KBIKS-21-2 🎓":
        await bot.send_message(message.chat.id, classes_today("kbiks-21-2", "second"), reply_markup=GroupsMarkup, parse_mode='HTML')

    elif message.text == "KBIKS-21-1 🎓":
        await bot.send_message(message.chat.id, classes_today("kbiks-21-1", "second"), reply_markup=GroupsMarkup, parse_mode='HTML')

    elif message.text == "KBIKSu-21-1 🎓":
        await bot.send_message(message.chat.id, classes_today("kbiksu-21-1", "second"), reply_markup=GroupsMarkup, parse_mode='HTML')

    # ------------------------APPLICANT-------------------------
    elif message.text == "Applicant 👤":
        user_status_e = "Applicant"
        await bot.send_message(message.chat.id, "Processing...", reply_markup=MenuApplicantMarkup)

    elif message.text == "Main contacts ✉️":
        await bot.send_message(message.chat.id, f"{MainContacts}", parse_mode='HTML')

    elif message.text == "Submission of documents 📄":
        await bot.send_message(message.chat.id, f'{MainText}'
        f'✨Introductory campaign on the site:✨\n'
        f'<a href="{EnteringTheCompany}">Click Here</a> 👈\n\n'
        f'✨Procedure of the admission in 2023:✨'
        f'<a href="{ProcedureOfTheAdmission}">\nClick Here</a> 🎯\n\n'
        f'✨Rules of admission:✨'
        f'<a href="{RulesOfAdmission}">\nClick Here</a> 👈\n\n'
        f'✨Competitive offers:✨'
        f'<a href="{CompetitiveOffers}">\nClick here</a> 🎯\n\n'
        f'✨Tuition fee and Amount set of students:✨'
        f'<a href="{TuitionFee}">\nClick here</a> 👈\n\n'
        f'✨Сoefficients of subjects:✨'
        f'<a href="{Coefficients}">\nClick here</a> 🎯\n\n'
        f'✨Score conversion:✨'
        f'<a href="{ScoreConv}">\nClick here</a> 👈\n\n'
        f'✨All about the motivation list:✨'
        f'<a href="{MotivList}">\nClick here</a> 🎯\n\n'
        f'✨Incentives:✨'
        f'<a href="{Benefit}">\nClick here</a> 👈\n\n', parse_mode='HTML')

    elif message.text == "Calculation of the competition score 🧮":
        text = f"✨ Hi {message.from_user.username}! I see you want to calculate your competitive score!" \
               f"\nChoose the type of the test below, which you have passed 👇"
        await bot.send_message(message.chat.id, text=text, reply_markup=IKB_en)

    elif message.text == "About the university🎓":
        await bot.send_message(message.chat.id, f"{AboutNureText}", parse_mode='HTML')

    elif message.text == "About departments🗂":
        await bot.send_message(message.chat.id, f"{AboutDepartmant}", reply_markup=DepartmentsMarkup)

    elif message.text =="About the specialities🧑‍💻":
        photo_path = os.path.abspath('Photo/photo.jpg')
        with open(photo_path, "rb") as photo:
            await bot.send_photo(chat_id=message.chat.id,  photo=photo, caption=f"{AboutSpecialities}",
                                 reply_markup=SpecialitesMarkup)



    #------------------- НА УКРАЇНСЬКІЙ МОВІ---------------------------
    elif message.text == "Українська 🇺🇦":
        await message.reply(f"Привіт, {message.from_user.username}!\nЯ EduHelpBot!")
        await bot.send_message(message.chat.id, "Обробка...", reply_markup=UkrApplicantAndStudentMarkup)

    elif message.text == "Змінити мову 🇺🇦🇬🇧":
        await bot.send_message(message.chat.id, "Обробка...", reply_markup=MultilingualismMarkup)

    elif message.text == "'Плюшки' студентам 🎁":
        await bot.send_message(message.chat.id, f"{FirstText}", reply_markup=CoursesAndFreeFirst)

    elif message.text == "Студент 👨‍🎓":
        user_status = "Студент"
        await bot.send_message(message.chat.id, "Обробка...", reply_markup=UkrKeyBoardClient)

    elif message.text == "Список функцій ⚙️":
        if user_status == "Студент":
            await message.reply(f"Привіт, {message.from_user.username}!\nЗавдяки мені у тебе є можливість 👇\n"
                                f"\n💠 Подивитися розклад ✔️"
                                f"\n💠 Скористатися нотатками ✔️"
                                f"\n💠 Отримати інформацію про доступ до безкоштовних ресурсів ХНУРЕ ✔️")# parse_mode='Markdown')
        else:
            await message.reply(f"Привіт, {message.from_user.username}!\nЗавдяки мені у тебе є можливість 👇\n"
                                f"\n💠 Отримати інформацію про кафедри та спеціальності ✔️"
                                f"\n💠 Отримати інформацію про ХНУРЕ ✔️"
                                f"\n💠 Отримати інформацію щодо головних контактів ХНУРЕ ✔️"
                                f"\n💠 Отримати інформацію щодо документів для вступу ✔️"
                                f"\n💠 Розрахувати конкурсний бал ✔️")

    elif message.text == "Сповіщення 🔔":
        Language = "Ukr"
        await message.answer("Додамо нову подію! Введіть назву події:\n\nПриклад: Зустріч з друзями")
        await CreateEventStates.WaitingEvent.set()

    elif message.text == "Контакти ✉️":
        await message.reply("Мій тег: https://t.me/EduHelpBot\nМої автори: "
                            f"\n1) https://t.me/YGODHIK \n2) https://t.me/oldnavy_1\n"
                            f"3) https://t.me/sofia_chueva")

    #elif message.text == "Про бот🤖":
        #await message.reply("Цей бот створений нашою командою, щоб зробити навчання зручнішим.")

    elif message.text == "Далі ➡️":
        await bot.send_message(message.chat.id, "Обробка...", reply_markup=Ukrmarkup)

    elif message.text == "Назад ⬅️":
        await message.reply("Обробка...", reply_markup=UkrKeyBoardClient)

    elif message.text == "Головне меню 🚪":
        await bot.send_message(message.chat.id, "Обробка...", reply_markup=UkrKeyBoardClient)

    # --------------TIMETABLE--------------
    elif message.text == "Отримання розкладу 🗓":
        await bot.send_message(message.chat.id, "Перейти до переліку факультетів", reply_markup=UkrListOfFacultiesMarkup)

    elif message.text == "Список факультетів 🎓":
        await bot.send_message(message.chat.id, "Оберіть факультет 👇", reply_markup=UkrKiuFacultyMarkup)

    elif message.text == "Факультет - КІУ":
        await bot.send_message(message.chat.id, "Оберіть курс 👇", reply_markup=Ukr_NumberOfCoursesMarkup)

    elif message.text == "Другий курс ⚜":
        await bot.send_message(message.chat.id, "Оберіть групу 👇", reply_markup=Ukr_GroupsMarkup)

    elif message.text == "КБІКС-21-5 🎓":
        await bot.send_message(message.chat.id, classes_today("kbiks-21-5", "second"), reply_markup=Ukr_GroupsMarkup,
                               parse_mode='HTML')

    elif message.text == "КБІКС-21-6 🎓":
        await bot.send_message(message.chat.id, classes_today("kbiks-21-6", "second"), reply_markup=Ukr_GroupsMarkup,
                               parse_mode='HTML')

    elif message.text == "КБІКС-21-4 🎓":
        await bot.send_message(message.chat.id, classes_today("kbiks-21-4", "second"), reply_markup=Ukr_GroupsMarkup,
                               parse_mode='HTML')

    elif message.text == "КБІКС-21-3 🎓":
        await bot.send_message(message.chat.id, classes_today("kbiks-21-3", "second"), reply_markup=Ukr_GroupsMarkup,
                               parse_mode='HTML')

    elif message.text == "КБІКС-21-2 🎓":
        await bot.send_message(message.chat.id, classes_today("kbiks-21-2", "second"), reply_markup=Ukr_GroupsMarkup,
                               parse_mode='HTML')

    elif message.text == "КБІКС-21-1 🎓":
        await bot.send_message(message.chat.id, classes_today("kbiks-21-1", "second"), reply_markup=Ukr_GroupsMarkup,
                               parse_mode='HTML')

    elif message.text == "КБІКСу-21-1 🎓":
        await bot.send_message(message.chat.id, classes_today("kbiksu-21-1", "second"), reply_markup=Ukr_GroupsMarkup,
                               parse_mode='HTML')

#--------------------АБІТУРІЄНТ--------------------
    elif message.text == "Вибір статусу👤":
        await message.reply("Обробка...", reply_markup=UkrApplicantAndStudentMarkup)

    elif message.text == "Абітурієнт 👤":
        user_status = "Абітурієнт"
        await bot.send_message(message.chat.id, "Обробка...", reply_markup=UkrMenuApplicantMarkup)

    elif message.text == "Головні контакти ✉️":
        await bot.send_message(message.chat.id, f"{MainContacts_ukr}", parse_mode='HTML')

    elif message.text == "Про університет🎓":
        await bot.send_message(message.chat.id, f"{AboutNureText_ukr}", parse_mode='HTML')

    elif message.text == "Про кафедри🗂":
        await bot.send_message(message.chat.id, f"{AboutDepartmant_ukr}", reply_markup=UkrDepartmentsMarkup)

    elif message.text == "Про спеціальності🧑‍💻":
        photo_path = os.path.abspath('Photo/photo.jpg')
        with open(photo_path, "rb") as photo:
            await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"{AboutSpecialities_ukr}",
                                 reply_markup=Ukr_SpecialitesMarkup)

    elif message.text == "Подача документів 📄":
        await bot.send_message(message.chat.id, f'{MainText_ukr}'
        f'✨Вступна кампанія на сайті:✨\n'
        f'<a href="{EnteringTheCompany}">Натисніть тут</a> 👈\n\n'
        f'✨Порядок прийому у 2023 році:✨'
        f'<a href="{ProcedureOfTheAdmission}">\nНатисніть тут</a> 🎯\n\n'
        f'✨Правила прийому:✨'
        f'<a href="{RulesOfAdmission}">\nНатисніть тут</a> 👈\n\n'
        f'✨Конкурентні пропозиції✨'
        f'<a href="{CompetitiveOffers}">\nНатисніть тут</a> 🎯\n\n'
        f'✨Вартість навчання та розмір набору студентів:✨'
        f'<a href="{TuitionFee}">\nНатисніть тут</a> 👈\n\n'
        f'✨Коефіцієнти на предмети✨'
        f'<a href="{Coefficients}">\nНатисніть тут</a> 🎯\n\n'
        f'✨Переведення балів:✨'
        f'<a href="{ScoreConv}">\nНатисніть тут</a> 👈\n\n'
        f'✨Все про мотиваційний лист:✨'
        f'<a href="{MotivList}">\nНатисніть тут</a> 🎯\n\n'
        f'✨Пільги✨'
        f'<a href="{Benefit}">\nНатисніть тут</a> 👈\n\n', parse_mode='HTML')


    elif message.text == "Підрахунок конкурного балу 🧮":
        text = f"✨ Привіт {message.from_user.username}! Бачу, ти хочеш розрахувати свій конкурсний бал!" \
               f"\nВибери будь ласка тип тесту нижче, який ти пройшов 👇"
        await bot.send_message(message.chat.id, text=text, reply_markup=IKB)

#-------------------------------------------------------
    async def handle_score(message: types.Message):
        Score = message.text
        await bot.send_message(message.chat.id, f"Твій бал з цього предмету: {Score}")

class ScoreFormState(StatesGroup):
    INPUT_SCORE = State()

subjects = {
    "Укр": "Українська мова",
    "Іст": "Історія України",
    "Мат": "Математика",
    "Фіз": "Фізика",
    "Хім": "Хімія",
    "Біо": "Біологія",
    "Іно": "Іноземна Мова",
    "Під": "Підрахувати 🧮",
    "Від": "Відміна 🔄"
    # Добавьте другие предметы сюда
}

SubjectsAndCoef = {
    'Укр': 0.3,
    'Мат': 0.5,
    'Іст': 0.2,
    'Іно': 0.3
}

Ukr_score = None
Math_score = None
Hist_score = None
Foreign_score = None
Biology = None
Phys_score = None
Chemistry = None

scores_entered = False
#--------------------------------------------------





@dp.callback_query_handler(lambda callback_query: True)
async def answer(callback_query: types.CallbackQuery, state: FSMContext):
    chat_id = callback_query.from_user.id

    if callback_query.data == "EconomicClick":
        photoPass = os.path.abspath('Photo/photo2.jpg')
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutEconomic}",
                                 reply_markup=SpecialitesEconomicMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "MathematicsClick":
        photoPass = os.path.abspath("Photo/photo3.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutMath}",
                                 reply_markup=SpecialitesMathMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "SoftClick":
        photoPass = os.path.abspath("Photo/photo4.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutSoftEng}",
                                 reply_markup=SpecialitesSoftEngMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "ComSciClick":
        photoPass = os.path.abspath("Photo/photo5.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutCompScience}",
                                 reply_markup=SpecialitesCompSciMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "ComIngClick":
        photoPass = os.path.abspath("Photo/photo6.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutCompIng}",
                                 reply_markup=SpecialitesCompIngMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "ComSysAnalysingClick":
        photoPass = os.path.abspath("Photo/phtot7.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutSysAnalysis}",
                                 reply_markup=SpecialitesCompSysAnalysingMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "CyberClick":
        photoPass = os.path.abspath("Photo/photo8.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutCyberSecurity}",
                                 reply_markup=SpecialitesCyberMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "InfoClick":
        photoPass = os.path.abspath("Photo/photo9.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutInformT}",
                                 reply_markup=SpecialitesInfoMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "BioClick":
        photoPass = os.path.abspath("Photo/photo10.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutBioEng}",
                                 reply_markup=SpecialitesBioMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "ElecClick":
        photoPass = os.path.abspath("Photo/photo11.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutElectronic}",
                                 reply_markup=SpecialitesElecMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "TeleClick":
        photoPass = os.path.abspath("Photo/photo12.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutTelecom}",
                                 reply_markup=SpecialitesTeleMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "AviClick":
        photoPass = os.path.abspath("Photo/photo13.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutAvionics}",
                                 reply_markup=SpecialitesAvioMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "InfTechClick":
        photoPass = os.path.abspath("Photo/photo14.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutMet}",
                                 reply_markup=SpecialitesMetTechMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "MicroClick":
        photoPass = os.path.abspath("Photo/photo15.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutMicro}",
                                 reply_markup=SpecialitesMicroMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "PubClick":
        photoPass = os.path.abspath("Photo/photo16.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutPol}",
                                 reply_markup=SpecialitesPubMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

#-------------------------НА УКРАЇНСЬКІЙ МОВІ-------------------------------
    elif callback_query.data == "Economic":
        photoPass = os.path.abspath('Photo/photo2.jpg')
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutEconomic_ukr}",
                                 reply_markup=Ukr_SpecialitesEconomicMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Mathematics":
        photoPass = os.path.abspath("Photo/photo3.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutMath_ukr}",
                                 reply_markup=Ukr_SpecialitesMathMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Soft":
        photoPass = os.path.abspath("Photo/photo4.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutSoftEng_ukr}",
                                 reply_markup=Ukr_SpecialitesSoftEngMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "ComSci":
        photoPass = os.path.abspath("Photo/photo5.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutCompScience_ukr}",
                                 reply_markup=Ukr_SpecialitesCompSciMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "ComIng":
        photoPass = os.path.abspath("Photo/photo6.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutCompIng_ukr}",
                                 reply_markup=Ukr_SpecialitesCompIngMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "ComSysAnalysing":
        photoPass = os.path.abspath("Photo/phtot7.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutSysAnalysis_ukr}",
                                 reply_markup=Ukr_SpecialitesCompSysAnalysingMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Cyber":
        photoPass = os.path.abspath("Photo/photo8.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutCyberSecurity_ukr}",
                                 reply_markup=Ukr_SpecialitesCyberMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Info":
        photoPass = os.path.abspath("Photo/photo9.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutInformT_ukr}",
                                 reply_markup=Ukr_SpecialitesInfoMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Bio":
        photoPass = os.path.abspath("Photo/photo10.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutBioEng_ukr}",
                                 reply_markup=Ukr_SpecialitesBioMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Elec":
        photoPass = os.path.abspath("Photo/photo11.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutElectronic_ukr}",
                                 reply_markup=Ukr_SpecialitesElecMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Tele":
        photoPass = os.path.abspath("Photo/photo12.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutTelecom_ukr}",
                                 reply_markup=Ukr_SpecialitesTeleMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Avi":
        photoPass = os.path.abspath("Photo/photo13.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutAvionics_ukr}",
                                 reply_markup=Ukr_SpecialitesAvioMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "InfTech":
        photoPass = os.path.abspath("Photo/photo14.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutMet_ukr}",
                                 reply_markup=Ukr_SpecialitesMetTechMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Micro":
        photoPass = os.path.abspath("Photo/photo15.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutMicro_ukr}",
                                 reply_markup=Ukr_SpecialitesMicroMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Pub":
        photoPass = os.path.abspath("Photo/photo16.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutPol_ukr}",
                                 reply_markup=Ukr_SpecialitesPubMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)




#----------------------------плюшки на укр-----------------------------------------------------------
    elif callback_query.data == "Office":
        photoPass = os.path.abspath("Photo/photo20.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutOfficeText}",
                                 reply_markup=CoursesAndFreeSecond)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Coursera":
        photoPass = os.path.abspath("Photo/image21.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutCourseraText}",
                                 reply_markup=CoursesAndFreeThird)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Udemy":
        photoPass = os.path.abspath("Photo/image22.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutUdemyText}",
                                 reply_markup=CoursesAndFreeFourth)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Edx":
        photoPass = os.path.abspath("Photo/image23.png")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutUdemyText}",
                                 reply_markup=CoursesAndFreeFive)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Jet":
        photoPass = os.path.abspath("Photo/img_3.png")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutJetBrainsText}",
                                 reply_markup=CoursesAndFreeSix)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)


# ----------------------плюшки на англ-------------------------------------------------------------------------------
    elif callback_query.data == "Office_en":
        photoPass = os.path.abspath("Photo/photo20.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutOfficeText_en}",
                                 reply_markup=CoursesAndFreeSecond_en)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Coursera_en":
        photoPass = os.path.abspath("Photo/image21.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutCourseraText_en}",
                                 reply_markup=CoursesAndFreeThird_en)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Udemy_en":
        photoPass = os.path.abspath("Photo/image22.jpg")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutUdemyText_en}",
                                 reply_markup=CoursesAndFreeFourth_en)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Edx_en":
        photoPass = os.path.abspath("Photo/image23.png")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutUdemyText_en}",
                                 reply_markup=CoursesAndFreeFive_en)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Jet_en":
        photoPass = os.path.abspath("Photo/img_3.png")
        with open(photoPass, "rb") as photo:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo, caption=f"{AboutJetBrainsText_en}",
                                 reply_markup=CoursesAndFreeSix_en)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

#----------------------------------------------------------------------------------------------------------------------

    elif callback_query.data == "ЗНО":
        await bot.send_message(chat_id, "Для того, щоб мені допомогти розрахувати твій конкурсний бал, мені потрібно, щоб ти обрав ті предмети, з яких у тебе були іспити" \
    "\n\nДивись нижче👇", reply_markup=CompetitionMarkup)
        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "ЗНО_en":
        await bot.send_message(chat_id, "In order to help me calculate your competitive score, I need you to select the subjects in which you have had exams" \
    "\n\nSee below👇", reply_markup=CompetitionMarkup_en)
        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)


    elif callback_query.data == "НМТ":
        await bot.send_message(chat_id, "Для того, щоб мені допомогти розрахувати твій конкурсний бал, мені потрібно, щоб ти обрав ті предмети, з яких у тебе були іспити"
        "\n\nДивись нижче👇", reply_markup=CompetitionMarkup)
        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "НМТ_en":
        await bot.send_message(chat_id, "In order to help me calculate your competitive score, I need you to select the subjects in which you have had exams" \
    "\n\nSee below👇", reply_markup=CompetitionMarkup_en)
        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)


    elif callback_query.data == "Укр":
        subject = callback_query.data
        subject_name = subjects[subject]
        ButtonName = "Українська Мова"
        await bot.send_message(chat_id,
        f"Дякую, ти обрав предмет -> <u><b>{ButtonName}</b></u> 🇺🇦\n"                                              
        f"Нижче тобі потрібно ввести свій бал з цього предмету 👇\n"
        f"Наприклад <code>170.5</code>", parse_mode='HTML')
        await ScoreFormState.INPUT_SCORE.set()
        await state.update_data(subject=subject)
        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Іст":
        subject = callback_query.data
        subject_name = subjects[subject]
        ButtonName = "Історія України"
        await bot.send_message(chat_id,
        f"Дякую, ти обрав предмет -> <u><b>{ButtonName}</b></u> \n"
        f"Нижче тобі потрібно ввести свій бал з цього предмету 👇\n"
        f"Наприклад <code>170.5</code>", parse_mode='HTML')

        await ScoreFormState.INPUT_SCORE.set()
        await state.update_data(subject=subject)
        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Мат":
        subject = callback_query.data
        subject_name = subjects[subject]
        ButtonName = "Математика"
        await bot.send_message(chat_id,
        f"Дякую, ти обрав предмет -> <u><b>{ButtonName}</b></u> \n"
        f"Нижче тобі потрібно ввести свій бал з цього предмету 👇\n"
        f"Наприклад <code>170.5</code>", parse_mode='HTML')

        await ScoreFormState.INPUT_SCORE.set()
        await state.update_data(subject=subject)
        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Фіз":
        subject = callback_query.data
        subject_name = subjects[subject]
        ButtonName = "Фізика"
        await bot.send_message(chat_id,
        f"Дякую, ти обрав предмет -> <u><b>{ButtonName}</b></u> \n"
        f"Нижче тобі потрібно ввести свій бал з цього предмету 👇\n"
        f"Наприклад <code>170.5</code>", parse_mode='HTML')

        await ScoreFormState.INPUT_SCORE.set()
        await state.update_data(subject=subject)
        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Хім":
        subject = callback_query.data
        subject_name = subjects[subject]
        ButtonName = "Хімія"
        await bot.send_message(chat_id,
        f"Дякую, ти обрав предмет -> <u><b>{ButtonName}</b></u> \n"
        f"Нижче тобі потрібно ввести свій бал з цього предмету 👇\n"
        f"Наприклад <code>170.5</code>", parse_mode='HTML')

        await ScoreFormState.INPUT_SCORE.set()
        await state.update_data(subject=subject)
        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Біо":
        subject = callback_query.data
        subject_name = subjects[subject]
        ButtonName = "Біологія"
        await bot.send_message(chat_id,
        f"Дякую, ти обрав предмет -> <u><b>{ButtonName}</b></u> 🔢\n"
        f"Нижче тобі потрібно ввести свій бал з цього предмету 👇\n"
        f"Наприклад <code>170.5</code>", parse_mode='HTML')

        await ScoreFormState.INPUT_SCORE.set()
        await state.update_data(subject=subject)
        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Гео":
        subject = callback_query.data
        subject_name = subjects[subject]
        ButtonName = "Географія"
        await bot.send_message(chat_id,
        f"Дякую, ти обрав предмет -> <u><b>{ButtonName}</b></u> 🔢\n"
        f"Нижче тобі потрібно ввести свій бал з цього предмету 👇\n"
        f"Наприклад <code>170.5</code>", parse_mode='HTML')

        await ScoreFormState.INPUT_SCORE.set()
        await state.update_data(subject=subject)
        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Іно":
        subject = callback_query.data
        subject_name = subjects[subject]
        ButtonName = "Іноземна Мова"
        await bot.send_message(chat_id,
        f"Дякую, ти обрав предмет -> <u><b>{ButtonName}</b></u> 🔢\n"
        f"Нижче тобі потрібно ввести свій бал з цього предмету 👇\n"
        f"Наприклад <code>170.5</code>", parse_mode='HTML')

        await ScoreFormState.INPUT_SCORE.set()
        await state.update_data(subject=subject)
        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

    elif callback_query.data == "Від":
        await state.finish()
        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)
        global Ukr_score, Math_score, Hist_score, Phys_score, Foreign_score, Biology, Chemistry, TotalScore
        Ukr_score = None
        Math_score = None
        Hist_score = None
        Phys_score = None
        Foreign_score = None
        Biology = None
        Chemistry = None
        TotalScore = None
        marked_subjects = []
        await bot.send_message(chat_id, "Ви успішно обнулили дані!\nОтримайте клавіатуру нижче 👇", reply_markup=CompetitionMarkup)

    elif callback_query.data == "Під":
        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)
        try:
            if Hist_score != None and Biology == None:
                if Ukr_score == None or Math_score == None:
                    raise TypeError
                else:
                    await bot.send_message(chat_id, f"Кул!\n"
                    f"Тепер тобі потрібно обрати ту спеціальність відповідно до якої тобі потрібно"
                    f"розрахувати балл✨\n"
                    f"Дивись нижче 👇", reply_markup=SpecialitesCalculatingMarkup)
                    await bot.answer_callback_query(callback_query.id, text='', show_alert=False)
                    return

            if Foreign_score != None and Biology == None:
                if Ukr_score == None or Math_score == None:
                    raise TypeError
                else:
                    await bot.send_message(chat_id, f"Кул!\n"
                    f"Тепер тобі потрібно обрати ту спеціальність відповідно до якої тобі потрібно"
                    f"розрахувати балл✨\n"
                    f"Дивись нижче 👇", reply_markup=SpecialitesCalculatingMarkup)
                    await bot.answer_callback_query(callback_query.id, text='', show_alert=False)
                    return

            if Biology != None and Ukr_score != None:
                await bot.send_message(chat_id, f"Кул!\n\nРозрахунок спеціальності '163 Біомедична Інженерія' відбувається окремо від всіх інших спеціальностей❗"
                                            f"\n\nТобі потрібно нижче натиснути відповідну кнопку", reply_markup=YesNo)
                return


            if Phys_score != None and Biology == None:
                if Ukr_score == None or Math_score == None:
                    raise TypeError
                else:
                    await bot.send_message(chat_id, f"Кул!\n"
                    f"Тепер тобі потрібно обрати ту спеціальність відповідно до якої тобі потрібно"
                    f"розрахувати балл✨\n"
                    f"Дивись нижче 👇", reply_markup=SpecialitesCalculatingMarkup)
                    await bot.answer_callback_query(callback_query.id, text='', show_alert=False)
                    return

            if Chemistry != None and Biology == None:
                if Ukr_score == None or Math_score == None:
                    raise TypeError
                else:
                    await bot.send_message(chat_id, f"Кул!\n"
                    f"Тепер тобі потрібно обрати ту спеціальність відповідно до якої тобі потрібно"
                    f"розрахувати балл✨\n"
                    f"Дивись нижче 👇", reply_markup=SpecialitesCalculatingMarkup)
                    await bot.answer_callback_query(callback_query.id, text='', show_alert=False)
                    return

            else:
                raise TypeError

        except TypeError as e:
            print("Ошибка TypeError:", e)
            await bot.send_message(chat_id, "Повинно бути введено 3 предмети щонайменше ❗\n"
                                            "З них — 2 обов'зкових (Мат, Укр) та 1 на вибір ❗")
            return

    elif callback_query.data == "Yes":
        if Ukr_score == None:
            raise TypeError
        else:
            await bot.send_message(chat_id, f"Кул!\n\nРозрахунок спеціальності '163 Біомедична Інженерія' відбувається окремо від всіх інших спеціальностей❗"
                                            f"\n\nТобі потрібно нижче натиснути відповідну кнопку", reply_markup=SpecialOnlyForBio)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)
            return
    elif callback_query.data == "No":
        if Ukr_score == None or Math_score == None:
            await bot.send_message(chat_id, "Для розрахунку інших спеціальностей ви повинні ввести 3 предмети щонайменше ❗\n"
                                            "З них — 2 обов'зкових (Мат, Укр) та 1 на вибір ❗")
        else:
            await bot.send_message(chat_id, f"Кул!\n"
                    f"Тепер тобі потрібно обрати ту спеціальність відповідно до якої тобі потрібно"
                    f"розрахувати балл✨\n"
                    f"Дивись нижче 👇", reply_markup=SpecialitesCalculatingWithoutBioMarkup)
            await bot.answer_callback_query(callback_query.id, text='', show_alert=False)
            return

    elif callback_query.data == "Eco":
        EconomicBudj = 176.72
        EconomicContr = 149.23
        if Hist_score != None:
            TotalScoreFirst = (0.35 * Ukr_score + 0.4 * Math_score + 0.25 * Hist_score) / (0.35 + 0.4 + 0.25) * 1.07 * 1.02
            TotalScoreSecond = (0.35 * Ukr_score + 0.4 * Math_score + 0.25 * Hist_score) / (0.35 + 0.4 + 0.25) * 1.07 * 1.00
            await bot.send_message(chat_id, f"✨051 Економіка✨\n"
            f"Тримай результати 👇\n\n"
            f"<i>Середній бал ЗНО на бюджет у 2022 році — {EconomicBudj}</i>\n"
            f"<i>Середній бал ЗНО на контракт у 2022 році — {EconomicContr}</i>\n"
            f"Ваш балл — <i>{min(round(TotalScoreFirst, 3), 200)}</i> (1 пріорітет)\n"
            f"Ваш балл — <i>{min(round(TotalScoreSecond, 3), 200)}</i> (2 пріорітет)\n",
            parse_mode="HTML")

        elif Foreign_score != None:
            TotalScoreFirst = (0.35 * Ukr_score + 0.4 * Math_score + 0.25 * Foreign_score) / (0.35 + 0.4 + 0.25) * 1.07 * 1.02
            TotalScoreSecond = (0.35 * Ukr_score + 0.4 * Math_score + 0.25 * Foreign_score) / (0.35 + 0.4 + 0.25) * 1.07 * 1.00
            await bot.send_message(chat_id, f"✨051 Економіка✨\n"
            f"Тримай результати 👇\n\n"
            f"<i>Середній бал ЗНО на бюджет у 2022 році — {EconomicBudj}</i>\n"
            f"<i>Середній бал ЗНО на контракт у 2022 році — {EconomicContr}</i>\n"
            f"Ваш балл — <i>{min(round(TotalScoreFirst, 3), 200)}</i> (1 пріорітет)\n"
            f"Ваш балл — <i>{min(round(TotalScoreSecond, 3), 200)}</i> (2 пріорітет)\n",
            parse_mode="HTML")

        elif Biology != None:
            TotalScoreFirst = (0.35 * Ukr_score + 0.4 * Math_score + 0.20 * Biology) / (0.35 + 0.4 + 0.20) * 1.07 * 1.02
            TotalScoreSecond = (0.35 * Ukr_score + 0.4 * Math_score + 0.20 * Biology) / (0.35 + 0.4 + 0.20) * 1.07 * 1.00
            await bot.send_message(chat_id, f"✨051 Економіка✨\n"
            f"Тримай результати 👇\n\n"
            f"<i>Середній бал ЗНО на бюджет у 2022 році — {EconomicBudj}</i>\n"
            f"<i>Середній бал ЗНО на контракт у 2022 році — {EconomicContr}</i>\n"
            f"Ваш балл — <i>{min(round(TotalScoreFirst, 3), 200)}</i> (1 пріорітет)\n"
            f"Ваш балл — <i>{min(round(TotalScoreSecond, 3), 200)}</i> (2 пріорітет)\n",
            parse_mode="HTML")

        elif Phys_score != None:
            TotalScoreFirst = (0.35 * Ukr_score + 0.4 * Math_score + 0.20 * Phys_score) / (0.35 + 0.4 + 0.20) * 1.07 * 1.02
            TotalScoreSecond = (0.35 * Ukr_score + 0.4 * Math_score + 0.20 * Phys_score) / (0.35 + 0.4 + 0.20) * 1.07 * 1.00
            await bot.send_message(chat_id, f"✨051 Економіка✨\n"
            f"Тримай результати 👇\n\n"
            f"<i>Середній бал ЗНО на бюджет у 2022 році — {EconomicBudj}</i>\n"
            f"<i>Середній бал ЗНО на контракт у 2022 році — {EconomicContr}</i>\n"
            f"Ваш балл — <i>{min(round(TotalScoreFirst, 3), 200)}</i> (1 пріорітет)\n"
            f"Ваш балл — <i>{min(round(TotalScoreSecond, 3), 200)}</i> (2 пріорітет)\n",
            parse_mode="HTML")

        elif Chemistry != None:
            TotalScoreFirst = (0.35 * Ukr_score + 0.4 * Math_score + 0.20 * Chemistry) / (0.35 + 0.4 + 0.20) * 1.07 * 1.02
            TotalScoreSecond = (0.35 * Ukr_score + 0.4 * Math_score + 0.20 * Chemistry) / (0.35 + 0.4 + 0.20) * 1.07 * 1.00
            await bot.send_message(chat_id, f"✨051 Економіка✨\n"
            f"Тримай результати 👇\n\n"
            f"<i>Середній бал ЗНО на бюджет у 2022 році — {EconomicBudj}</i>\n"
            f"<i>Середній бал ЗНО на контракт у 2022 році — {EconomicContr}</i>\n"
            f"Ваш балл — <i>{min(round(TotalScoreFirst, 3), 200)}</i> (1 пріорітет)\n"
            f"Ваш балл — <i>{min(round(TotalScoreSecond, 3), 200)}</i> (2 пріорітет)\n",
            parse_mode="HTML")

    elif callback_query.data == "Mat":
        MathBudj = 177.81
        MathContr = 164.78
        if Hist_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"✨113 Прикладна математика✨\n"
            f"Тримай результати 👇\n\n"
            f"<i>Середній бал ЗНО на бюджет у 2022 році — {MathBudj}</i>\n"
            f"<i>Середній бал ЗНО на контракт у 2022 році — {MathContr}</i>\n"
            f"Ваш балл — <i>{min(round(TotalScoreFirst, 3), 200)}</i> (1 пріорітет)\n"
            f"Ваш балл — <i>{min(round(TotalScoreSecond, 3), 200)}</i> (2 пріорітет)\n",
            parse_mode="HTML")

        elif Foreign_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.3 * Foreign_score) / (0.3 + 0.5 + 0.3) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.3 * Foreign_score) / (0.3 + 0.5 + 0.3) * 1.07 * 1.00
            await bot.send_message(chat_id, f"✨113 Прикладна математика✨\n"
            f"Тримай результати 👇\n\n"
            f"<i>Середній бал ЗНО на бюджет у 2022 році — {MathBudj}</i>\n"
            f"<i>Середній бал ЗНО на контракт у 2022 році — {MathContr}</i>\n"
            f"Ваш балл — <i>{min(round(TotalScoreFirst, 3), 200)}</i> (1 пріорітет)\n"
            f"Ваш балл — <i>{min(round(TotalScoreSecond, 3), 200)}</i> (2 пріорітет)\n",
            parse_mode="HTML")

        elif Biology != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.00
            await bot.send_message(chat_id, f"✨113 Прикладна математика✨\n"
            f"Тримай результати 👇\n\n"
            f"<i>Середній бал ЗНО на бюджет у 2022 році — {MathBudj}</i>\n"
            f"<i>Середній бал ЗНО на контракт у 2022 році — {MathContr}</i>\n"
            f"Ваш балл — <i>{min(round(TotalScoreFirst, 3), 200)}</i> (1 пріорітет)\n"
            f"Ваш балл — <i>{min(round(TotalScoreSecond, 3), 200)}</i> (2 пріорітет)\n",
            parse_mode="HTML")

        elif Phys_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.4 * Phys_score) / (0.3 + 0.5 + 0.4) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.4 * Phys_score) / (0.3 + 0.5 + 0.4) * 1.07 *  1.00
            await bot.send_message(chat_id, f"✨113 Прикладна математика✨\n"
            f"Тримай результати 👇\n\n"
            f"<i>Середній бал ЗНО на бюджет у 2022 році — {MathBudj}</i>\n"
            f"<i>Середній бал ЗНО на контракт у 2022 році — {MathContr}</i>\n"
            f"Ваш балл — <i>{min(round(TotalScoreFirst, 3), 200)}</i> (1 пріорітет)\n"
            f"Ваш балл — <i>{min(round(TotalScoreSecond, 3), 200)}</i> (2 пріорітет)\n",
            parse_mode="HTML")

        elif Chemistry != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"✨113 Прикладна математика✨\n"
            f"Тримай результати 👇\n\n"
            f"<i>Середній бал ЗНО на бюджет у 2022 році — {MathBudj}</i>\n"
            f"<i>Середній бал ЗНО на контракт у 2022 році — {MathContr}</i>\n"
            f"Ваш балл — <i>{min(round(TotalScoreFirst, 3), 200)}</i> (1 пріорітет)\n"
            f"Ваш балл — <i>{min(round(TotalScoreSecond, 3), 200)}</i> (2 пріорітет)\n",
            parse_mode="HTML")

    elif callback_query.data == "Ing":
        IngProgBudj = 190.25
        IngProgCont = 167.17
        if Hist_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"✨121 Інженерія програмного забезпечення✨\n"
            f"Тримай результати 👇\n\n"
            f"<i>Середній бал ЗНО на бюджет у 2022 році — {IngProgBudj}</i>\n"
            f"<i>Середній бал ЗНО на контракт у 2022 році — {IngProgCont}</i>\n"
            f"Ваш балл — <i>{min(round(TotalScoreFirst, 3), 200)}</i> (1 пріорітет)\n"
            f"Ваш балл — <i>{min(round(TotalScoreSecond, 3), 200)}</i> (2 пріорітет)\n",
            parse_mode="HTML")

        elif Foreign_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.3 * Foreign_score) / (0.3 + 0.5 + 0.3) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.3 * Foreign_score) / (0.3 + 0.5 + 0.3) * 1.07 * 1.00
            await bot.send_message(chat_id, f"✨121 Інженерія програмного забезпечення✨\n"
            f"Тримай результати 👇\n\n"
            f"<i>Середній бал ЗНО на бюджет у 2022 році — {IngProgBudj}</i>\n"
            f"<i>Середній бал ЗНО на контракт у 2022 році — {IngProgCont}</i>\n"
            f"Ваш балл — <i>{min(round(TotalScoreFirst, 3), 200)}</i> (1 пріорітет)\n"
            f"Ваш балл — <i>{min(round(TotalScoreSecond, 3), 200)}</i> (2 пріорітет)\n",
            parse_mode="HTML")

        elif Biology != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.00
            await bot.send_message(chat_id, f"✨121 Інженерія програмного забезпечення✨\n"
            f"Тримай результати 👇\n\n"
            f"<i>Середній бал ЗНО на бюджет у 2022 році — {IngProgBudj}</i>\n"
            f"<i>Середній бал ЗНО на контракт у 2022 році — {IngProgCont}</i>\n"
            f"Ваш балл — <i>{min(round(TotalScoreFirst, 3), 200)}</i> (1 пріорітет)\n"
            f"Ваш балл — <i>{min(round(TotalScoreSecond, 3), 200)}</i> (2 пріорітет)\n",
            parse_mode="HTML")

        elif Phys_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.4 * Phys_score) / (0.3 + 0.5 + 0.4) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.4 * Phys_score) / (0.3 + 0.5 + 0.4) * 1.07 *  1.00
            await bot.send_message(chat_id, f"✨121 Інженерія програмного забезпечення✨\n"
            f"Тримай результати 👇\n\n"
            f"<i>Середній бал ЗНО на бюджет у 2022 році — {IngProgBudj}</i>\n"
            f"<i>Середній бал ЗНО на контракт у 2022 році — {IngProgCont}</i>\n"
            f"Ваш балл — <i>{min(round(TotalScoreFirst, 3), 200)}</i> (1 пріорітет)\n"
            f"Ваш балл — <i>{min(round(TotalScoreSecond, 3), 200)}</i> (2 пріорітет)\n",
            parse_mode="HTML")

        elif Chemistry != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"✨121 Інженерія програмного забезпечення✨\n"
            f"Тримай результати 👇\n\n"
            f"<i>Середній бал ЗНО на бюджет у 2022 році — {IngProgBudj}</i>\n"
            f"<i>Середній бал ЗНО на контракт у 2022 році — {IngProgCont}</i>\n"
            f"Ваш балл — <i>{min(round(TotalScoreFirst, 3), 200)}</i> (1 пріорітет)\n"
            f"Ваш балл — <i>{min(round(TotalScoreSecond, 3), 200)}</i> (2 пріорітет)\n",
            parse_mode="HTML")

    elif callback_query.data == "Com":
        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)
        if Hist_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutKnFirst}{min(round(TotalScoreFirst, 3), 200)} (1 пріорітет)\nВаш бал — {min(round(TotalScoreSecond, 3), 200)} (2 пріорітет)\n {AboutKnSecond}", parse_mode="HTML")

        elif Foreign_score != None:

            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.3 * Foreign_score) / (0.3 + 0.5 + 0.3) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.3 * Foreign_score) / (0.3 + 0.5 + 0.3) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutKnFirst}{min(round(TotalScoreFirst, 3), 200)} (1 пріорітет)\nВаш бал — {min(round(TotalScoreSecond, 3), 200)} (2 пріорітет)\n {AboutKnSecond}", parse_mode="HTML")

        elif Biology != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutKnFirst}{min(round(TotalScoreFirst, 3), 200)} (1 пріорітет)\nВаш бал — {min(round(TotalScoreSecond, 3), 200)} (2 пріорітет)\n {AboutKnSecond}", parse_mode="HTML")

        elif Phys_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.4 * Phys_score) / (0.3 + 0.5 + 0.4) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.4 * Phys_score) / (0.3 + 0.5 + 0.4) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutKnFirst}{min(round(TotalScoreFirst, 3), 200)} (1 пріорітет)\nВаш бал — {min(round(TotalScoreSecond, 3), 200)} (2 пріорітет)\n {AboutKnSecond}", parse_mode="HTML")

        elif Chemistry != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutKnFirst}{min(round(TotalScoreFirst, 3), 200)} (1 пріорітет)\nВаш бал — {min(round(TotalScoreSecond, 3), 200)} (2 пріорітет)\n {AboutKnSecond}", parse_mode="HTML")

    elif callback_query.data == "Eng":
        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)
        if Hist_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutIngFistPart} <i>{min(round(TotalScoreFirst, 3), 200)}</i> {AboutIngSecondPart} <i>{min(round(TotalScoreSecond, 3), 200)}</i>", parse_mode="HTML")

        elif Foreign_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.3 * Foreign_score) / (0.3 + 0.5 + 0.3) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.3 * Foreign_score) / (0.3 + 0.5 + 0.3) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutIngFistPart} {min(round(TotalScoreFirst, 3), 200)} {AboutIngSecondPart} {min(round(TotalScoreSecond, 3), 200)}", parse_mode="HTML")

        elif Biology != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutIngFistPart} {min(round(TotalScoreFirst, 3), 200)} {AboutIngSecondPart} {min(round(TotalScoreSecond, 3), 200)}", parse_mode="HTML")


        elif Phys_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.4 * Phys_score) / (0.3 + 0.5 + 0.4) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.4 * Phys_score) / (0.3 + 0.5 + 0.4) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutIngFistPart} {min(round(TotalScoreFirst, 3), 200)} {AboutIngSecondPart} {min(round(TotalScoreSecond, 3), 200)}", parse_mode="HTML")


        elif Chemistry != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutIngFistPart} {min(round(TotalScoreFirst, 3), 200)} {AboutIngSecondPart} {min(round(TotalScoreSecond, 3), 200)}", parse_mode="HTML")

    elif callback_query.data == "Sys":

        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)
        if Hist_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutSysFist} <i>{min(round(TotalScoreFirst, 3), 200)}</i> {AboutSysSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>", parse_mode="HTML")

        elif Foreign_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.3 * Foreign_score) / (0.3 + 0.5 + 0.3) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.3 * Foreign_score) / (0.3 + 0.5 + 0.3) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutSysFist} <i>{min(round(TotalScoreFirst, 3), 200)}</i> {AboutSysSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>", parse_mode="HTML")

        elif Biology != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutSysFist} <i>{min(round(TotalScoreFirst, 3), 200)}</i> {AboutSysSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>", parse_mode="HTML")


        elif Phys_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.4 * Phys_score) / (0.3 + 0.5 + 0.4) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.4 * Phys_score) / (0.3 + 0.5 + 0.4) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutSysFist} <i>{min(round(TotalScoreFirst, 3), 200)}</i> {AboutSysSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>", parse_mode="HTML")


        elif Chemistry != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutSysFist} <i>{min(round(TotalScoreFirst, 3), 200)}</i> {AboutSysSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>", parse_mode="HTML")

    elif callback_query.data == "Cyb":

        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)
        if Hist_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutCybFirst} {AboutCybBallFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutCybBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutCybSecond}", parse_mode="HTML")

        elif Foreign_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.3 * Foreign_score) / (0.3 + 0.5 + 0.3) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.3 * Foreign_score) / (0.3 + 0.5 + 0.3) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutCybFirst} {AboutCybBallFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutCybBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutCybSecond}", parse_mode="HTML")

        elif Biology != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutCybFirst} {AboutCybBallFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutCybBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutCybSecond}", parse_mode="HTML")

        elif Phys_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.4 * Phys_score) / (0.3 + 0.5 + 0.4) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.4 * Phys_score) / (0.3 + 0.5 + 0.4) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutCybFirst} {AboutCybBallFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutCybBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutCybSecond}", parse_mode="HTML")


        elif Chemistry != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutCybFirst} {AboutCybBallFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutCybBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutCybSecond}", parse_mode="HTML")

    elif callback_query.data == "Inf":

        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)
        if Hist_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutInfSystemFirst} {AboutInfSystemBallFist} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutInfSystemBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutInfSystemSecond}", parse_mode="HTML")

        elif Foreign_score != None:
            TotalScoreFirst = (0.3   * Ukr_score + 0.5 * Math_score + 0.3 * Foreign_score) / (0.3 + 0.5 + 0.3) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.3 * Foreign_score) / (0.3 + 0.5 + 0.3) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutInfSystemFirst} {AboutInfSystemBallFist} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutInfSystemBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutInfSystemSecond}", parse_mode="HTML")

        elif Biology != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutInfSystemFirst} {AboutInfSystemBallFist} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutInfSystemBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutInfSystemSecond}", parse_mode="HTML")


        elif Phys_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.4 * Phys_score) / (0.3 + 0.5 + 0.4) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.4 * Phys_score) / (0.3 + 0.5 + 0.4) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutInfSystemFirst} {AboutInfSystemBallFist} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutInfSystemBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutInfSystemSecond}", parse_mode="HTML")


        elif Chemistry != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutInfSystemFirst} {AboutInfSystemBallFist} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutInfSystemBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutInfSystemSecond}", parse_mode="HTML")

    elif callback_query.data == "Byo":

        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)
        if Biology != None:
            if Hist_score != None:
                TotalScoreFirst = ((0.35 * Ukr_score + 0.5 * Biology + 0.3 * Hist_score) / (0.35 + 0.5 + 0.3)) * 1.07 * 1.02
                TotalScoreSecond = ((0.35 * Ukr_score + 0.5 * Biology + 0.3 * Hist_score) / (0.35 + 0.5 + 0.3)) * 1.07 * 1.00
                await bot.send_message(chat_id, f"{AboutBioFirst}  <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutBioSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>", parse_mode="HTML")

            elif Math_score != None:
                TotalScoreFirst = (0.35 * Ukr_score + 0.5 * Biology + 0.35 * Math_score) / (0.35 + 0.5 + 0.35) * 1.07 * 1.02
                TotalScoreSecond = (0.35 * Ukr_score + 0.5 * Biology + 0.35 * Math_score) / (0.35 + 0.5 + 0.35) * 1.07 * 1.00
                await bot.send_message(chat_id, f"{AboutBioFirst}  <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutBioSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>", parse_mode="HTML")

            elif Foreign_score != None:
                TotalScoreFirst = (0.35 * Ukr_score + 0.5 * Biology + 0.3 * Foreign_score) / (0.35 + 0.5 + 0.3) * 1.07 * 1.02
                TotalScoreSecond = (0.35 * Ukr_score + 0.5 * Biology + 0.3 * Foreign_score) / (0.35 + 0.5 + 0.3) * 1.07 * 1.00
                await bot.send_message(chat_id, f"{AboutBioFirst}  <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutBioSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>", parse_mode="HTML")

            elif Phys_score != None:
                TotalScoreFirst = (0.35 * Ukr_score + 0.5 * Biology + 0.5 * Phys_score) / (0.35 + 0.5 + 0.5) * 1.07 * 1.02
                TotalScoreSecond = (0.35 * Ukr_score + 0.5 * Biology + 0.5 * Phys_score) / (0.35 + 0.5 + 0.5) * 1.07 * 1.00
                await bot.send_message(chat_id, f"{AboutBioFirst}  <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutBioSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>", parse_mode="HTML")

            elif Chemistry != None:
                TotalScoreFirst = (0.35 * Ukr_score + 0.5 * Biology + 0.5 * Chemistry) / (0.35 + 0.5 + 0.5) * 1.07 * 1.02
                TotalScoreSecond = (0.35 * Ukr_score + 0.5 * Biology + 0.5 * Chemistry) / (0.35 + 0.5 + 0.5) * 1.07 * 1.00
                await bot.send_message(chat_id, f"{AboutBioFirst}  <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutBioSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>", parse_mode="HTML")

        else:
            await bot.send_message(chat_id, f"{AboutBioInform}")
            return

    elif callback_query.data == "Ele":
        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

        if Hist_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutElectronikFirst} {AboutElectronikFirstBall} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutElectronikSecondBall} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutElectronikSecond}", parse_mode="HTML")

        elif Foreign_score != None:
            TotalScoreFirst = (0.3  * Ukr_score + 0.5 * Math_score + 0.25 * Foreign_score) / (0.3 + 0.5 + 0.25) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.25 * Foreign_score) / (0.3 + 0.5 + 0.25) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutElectronikFirst} {AboutElectronikFirstBall} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutElectronikSecondBall} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutElectronikSecond}", parse_mode="HTML")

        elif Biology != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutElectronikFirst} {AboutElectronikFirstBall} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutElectronikSecondBall} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutElectronikSecond}", parse_mode="HTML")


        elif Phys_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.5 * Phys_score) / (0.3 + 0.5 + 0.5) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.5 * Phys_score) / (0.3 + 0.5 + 0.5) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutElectronikFirst} {AboutElectronikFirstBall} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutElectronikSecondBall} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutElectronikSecond}", parse_mode="HTML")


        elif Chemistry != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutElectronikFirst} {AboutElectronikFirstBall} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutElectronikSecondBall} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutElectronikSecond}", parse_mode="HTML")

    elif callback_query.data == "Rad":
        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

        if Hist_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutTeleFirst} {AboutTeleBallFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutTeleBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutTeleSecond}", parse_mode="HTML")

        elif Foreign_score != None:
            TotalScoreFirst = (0.3  * Ukr_score + 0.5 * Math_score + 0.25 * Foreign_score) / (0.3 + 0.5 + 0.25) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.25 * Foreign_score) / (0.3 + 0.5 + 0.25) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutTeleFirst} {AboutTeleBallFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutTeleBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutTeleSecond}", parse_mode="HTML")

        elif Biology != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutTeleFirst} {AboutTeleBallFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutTeleBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutTeleSecond}", parse_mode="HTML")

        elif Phys_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.5 * Phys_score) / (0.3 + 0.5 + 0.5) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.5 * Phys_score) / (0.3 + 0.5 + 0.5) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutTeleFirst} {AboutTeleBallFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutTeleBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutTeleSecond}", parse_mode="HTML")

        elif Chemistry != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutTeleFirst} {AboutTeleBallFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutTeleBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutTeleSecond}", parse_mode="HTML")

    elif callback_query.data == "Avion":
        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

        if Hist_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutAvioFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutAvioSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>" , parse_mode="HTML")

        elif Foreign_score != None:
            TotalScoreFirst = (0.3  * Ukr_score + 0.5 * Math_score + 0.25 * Foreign_score) / (0.3 + 0.5 + 0.25) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.25 * Foreign_score) / (0.3 + 0.5 + 0.25) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutAvioFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutAvioSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>", parse_mode="HTML")

        elif Biology != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutAvioFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutAvioSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>" , parse_mode="HTML")

        elif Phys_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.5 * Phys_score) / (0.3 + 0.5 + 0.5) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.5 * Phys_score) / (0.3 + 0.5 + 0.5) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutAvioFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutAvioSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>" , parse_mode="HTML")

        elif Chemistry != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutAvioFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutAvioSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>" , parse_mode="HTML")

    elif callback_query.data == "Aut":
        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

        if Hist_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutAuto} {AboutAutoBallFirst}<i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutAutoBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutAutoSecond}", parse_mode="HTML")

        elif Foreign_score != None:
            TotalScoreFirst = (0.3  * Ukr_score + 0.5 * Math_score + 0.25 * Foreign_score) / (0.3 + 0.5 + 0.25) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.25 * Foreign_score) / (0.3 + 0.5 + 0.25) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutAuto} {AboutAutoBallFirst}<i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutAutoBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutAutoSecond}", parse_mode="HTML")

        elif Biology != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutAuto} {AboutAutoBallFirst}<i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutAutoBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutAutoSecond}", parse_mode="HTML")

        elif Phys_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.5 * Phys_score) / (0.3 + 0.5 + 0.5) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.5 * Phys_score) / (0.3 + 0.5 + 0.5) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutAuto} {AboutAutoBallFirst}<i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutAutoBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutAutoSecond}", parse_mode="HTML")
        elif Chemistry != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutAuto} {AboutAutoBallFirst}<i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutAutoBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutAutoSecond}", parse_mode="HTML")

    elif callback_query.data == "Cal":
        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

        if Hist_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutMetroFirst} {AboutMetroBallFirst}<i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutMetroBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutMetroSecond}", parse_mode="HTML")

        elif Foreign_score != None:
            TotalScoreFirst = (0.3  * Ukr_score + 0.5 * Math_score + 0.25 * Foreign_score) / (0.3 + 0.5 + 0.25) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.25 * Foreign_score) / (0.3 + 0.5 + 0.25) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutMetroFirst} {AboutMetroBallFirst}<i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutMetroBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutMetroSecond}", parse_mode="HTML")

        elif Biology != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutMetroFirst} {AboutMetroBallFirst}<i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutMetroBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutMetroSecond}", parse_mode="HTML")

        elif Phys_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.5 * Phys_score) / (0.3 + 0.5 + 0.5) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.5 * Phys_score) / (0.3 + 0.5 + 0.5) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutMetroFirst} {AboutMetroBallFirst}<i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutMetroBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutMetroSecond}", parse_mode="HTML")
        elif Chemistry != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutMetroFirst} {AboutMetroBallFirst}<i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutMetroBallSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i> {AboutMetroSecond}", parse_mode="HTML")

    elif callback_query.data == "Mic":
        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

        if Hist_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutMicroFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutMicroSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>", parse_mode="HTML")

        elif Foreign_score != None:
            TotalScoreFirst = (0.3  * Ukr_score + 0.5 * Math_score + 0.25 * Foreign_score) / (0.3 + 0.5 + 0.25) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.25 * Foreign_score) / (0.3 + 0.5 + 0.25) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutMicroFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutMicroSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>", parse_mode="HTML")

        elif Biology != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutMicroFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutMicroSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>", parse_mode="HTML")

        elif Phys_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.5 * Phys_score) / (0.3 + 0.5 + 0.5) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.5 * Phys_score) / (0.3 + 0.5 + 0.5) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutMicroFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutMicroSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>", parse_mode="HTML")
        elif Chemistry != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutMicroFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutMicroSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>", parse_mode="HTML")

    elif callback_query.data == "Pol":
        await bot.answer_callback_query(callback_query.id, text='', show_alert=False)

        if Hist_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutPolFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutPolSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>", parse_mode="HTML")

        elif Foreign_score != None:
            TotalScoreFirst = (0.3  * Ukr_score + 0.5 * Math_score + 0.25 * Foreign_score) / (0.3 + 0.5 + 0.25) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.25 * Foreign_score) / (0.3 + 0.5 + 0.25) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutPolFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutPolSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>", parse_mode="HTML")

        elif Biology != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.20 * Biology) / (0.3 + 0.5 + 0.20) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutPolFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutPolSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>", parse_mode="HTML")

        elif Phys_score != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.5 * Phys_score) / (0.3 + 0.5 + 0.5) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.5 * Phys_score) / (0.3 + 0.5 + 0.5) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutPolFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutPolSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>", parse_mode="HTML")
        elif Chemistry != None:
            TotalScoreFirst = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.02
            TotalScoreSecond = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Chemistry) / (0.3 + 0.5 + 0.2) * 1.07 * 1.00
            await bot.send_message(chat_id, f"{AboutPolFirst} <i>{min(round(TotalScoreFirst, 3), 200)} </i> {AboutPolSecond} <i>{min(round(TotalScoreSecond, 3), 200)}</i>", parse_mode="HTML")






#-------------------------------------------------------------
@dp.message_handler(state=ScoreFormState.INPUT_SCORE)
async def handle_score_input(message: types.Message, state: FSMContext):
    global Ukr_score, Math_score, Hist_score, \
           Phys_score, Foreign_score, Biology, \
           Chemistry, TotalScore

    scores = {
        'Укр': 0,
        'Мат': 0,
        'Іст': 0,
        "Фіз": 0,
        "Хім": 0,
        "Біо": 0,
        "Гео": 0,
        "Іно": 0
    }

    try:
        Score = float(message.text)
    except ValueError:
        await bot.send_message(message.chat.id, "Некоректний ввод, повторіть спробу ще раз!")
        return

    data = await state.get_data()
    subject = data.get('subject')
    subject_name = subjects.get(subject)
    Scores = data.get('Scores', {})
    marked_subjects = data.get('marked_subjects', [])
    if Score >= 100 and Score <= 200:
        if subject == 'Укр':
            Ukr_score = Score
        elif subject == 'Мат':
            Math_score = Score
        elif subject == 'Іст':
            Hist_score = Score
        elif subject == 'Фіз':
            Phys_score = Score
        elif subject == 'Іно':
            Foreign_score = Score
        elif subject == 'Біо':
            Biology = Score
        elif subject == 'Хім':
            Chemistry = Score

        await state.finish()
        await bot.send_message(
            message.chat.id,
            f"Твій бал з предмету '{subject_name}'-> {Score}. \nДякую за надану інформацію!",
        )
        marked_subjects.append(subject)
        NewKeyboard = types.InlineKeyboardMarkup(row_width=1)
        for subj, subj_name in subjects.items():
            if subj in marked_subjects:
                subj_button = types.InlineKeyboardButton(text=f"{subj_name} ✅", callback_data=subj)
            else:
                subj_button = types.InlineKeyboardButton(text=subj_name, callback_data=subj)
            NewKeyboard.row(subj_button)

        await bot.send_message(message.chat.id, "Обери нижче предмет:", reply_markup=NewKeyboard)
        await state.update_data(Scores=Scores, marked_subjects=marked_subjects)

        #if Ukr_score != 0 and Math_score != 0 and Hist_score != 0:
            #scores_entered = True
            #TotalScore = (0.3 * Ukr_score + 0.5 * Math_score + 0.2 * Hist_score) / (0.3 + 0.5 + 0.2) * 1.07 * 1
            #await bot.send_message(message.chat.id, f"Твій КБ: {round(TotalScore, 3)}")
    else:
        if Score < 100:
            await bot.send_message(message.chat.id, f"Ваш введений бал <b>'{message.text}'</b> не може бути менше 100\n"
                                              "Перевірте правильність вводу!", parse_mode="HTML")
        elif Score > 200:
            await bot.send_message(message.chat.id, f"Ваш введений бал <b>'{message.text}'</b> не може бути більше 200'\n"
                                                    "Перевірте правильність вводу!", parse_mode="HTML")


# Определяем состояния для диалога с пользователем
class CreateEventStates(StatesGroup):
    WaitingEvent = State()  # Ожидание названия события
    WaitingDate = State()  # Ожидание ввода даты
    WaitingTime = State()  # Ожидание ввода времени
    WaitingReminder = State()  # Ожидание ввода информации о напоминании

# Обработчик текстовых сообщений в состоянии ожидания названия события
@dp.message_handler(state=CreateEventStates.WaitingEvent)
async def process_event_text(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['event_text'] = message.text
    if Language == "Ukr":
        await message.answer("Чудово! Тепер введіть дату події у форматі DD-MM-YYYY:\n\nПриклад: 20-05-2023")
        await CreateEventStates.WaitingDate.set()
    else:
        await message.answer("Great! Now enter the event date in DD-MM-YYYY format:\n\nExample: 20-05-2023")
        await CreateEventStates.WaitingDate.set()


# Обработчик текстовых сообщений в состоянии ожидания даты события
@dp.message_handler(state=CreateEventStates.WaitingDate)
async def process_event_date(message: types.Message, state: FSMContext):
    try:
        event_date = datetime.strptime(message.text, "%d-%m-%Y")

        if event_date.date() < datetime.now().date():
            if Language == "Ukr":
                await message.answer("Ви не можете створити нотатку на вчорашній день!")
                return
            else:
                await message.answer("You cannot create a note for yesterday! Please enter a valid date.")
                return

        async with state.proxy() as data:
            data['event_date'] = event_date
        if Language == "Ukr":
            await message.answer("Гаразд! Тепер введіть час події у форматі HH: MM:\n\nПриклад: 18:30")
            await CreateEventStates.WaitingTime.set()
        else:
            await message.answer("All right! Now enter the event time in HH: MM format:\n\nExample: 18:30")
            await CreateEventStates.WaitingTime.set()
    except ValueError:
        if Language == "Ukr":
            await message.answer("Невірний формат дати! Введіть дату у форматі ДД-MM-ГГГГ.\n\nПриклад: 23-03-2013")
        else:
            await message.answer("Invalid date format! Enter a date in the format DD-MM-YYYY.\n\nExample: 23-03-2013")



# Обработчик текстовых сообщений в состоянии ожидания времени события
@dp.message_handler(state=CreateEventStates.WaitingTime)
async def process_event_time(message: types.Message, state: FSMContext):
    try:
        event_time = datetime.strptime(message.text, "%H:%M").time()

        # Создаем объект datetime для текущего дня и времени
        current_datetime = datetime.combine(datetime.now().date(), datetime.now().time())

        # Создаем объект datetime для введенной даты события и времени
        event_datetime = datetime.combine((await state.get_data()).get('event_date'), event_time)

        # Проверяем, что время события больше текущего времени
        if event_datetime <= current_datetime:
            if Language == "Ukr":
                await message.answer("Ви не можете створити нотатку у минулому або з поточним часом. Будь ласка, введіть правильний час.")
                return
            else:
                await message.answer("You cannot create a note in the past or with the current time. Please enter a valid time.")
                return
        async with state.proxy() as data:
            data['event_time'] = event_time
        if Language == "Ukr":
            await message.answer("Відмінно! Тепер введіть кількість днів, тижнів або годин "
                                 "за котре потрібно нагадати про подію:\n\nПриклад: 2 дня, 3 часа, 30 хвилин")
        else:
            await message.answer("Excellent! Now enter the number of days, weeks or hours "
                                 "for which you need to remind about the event:\n\nExample: 2 days, 3 hours, 30 minutes")
        await CreateEventStates.WaitingReminder.set()
    except ValueError:
        if Language == "Ukr":
            await message.answer("Невірний формат нагадування! Введіть нагадування у форматі'Номер Єдиниці', "
                                 "наприклад, «2 дні», «3 години», «30 хвилин».")
        else:
            await message.answer("Invalid reminder format! Enter a reminder in the format'Unity number', "
                                 "for example, «2 days», «3 hours», «30 minutes».")



@dp.message_handler(state=CreateEventStates.WaitingReminder)
async def process_event_reminder(message: types.Message, state: FSMContext):
    try:
        reminder_info = message.text.split()
        delta_value = int(reminder_info[0])
        delta_unit = reminder_info[1].strip()

        if Language == "Ukr":  # Определение интервала времени напоминания
            if delta_unit == 'дня' or delta_unit == 'днів' or delta_unit == 'день':
                reminder_delta = timedelta(days=delta_value)
            elif delta_unit == 'тижня' or delta_unit == 'тижнів' or delta_unit == "тиждень":
                reminder_delta = timedelta(weeks=delta_value)
            elif delta_unit == 'година' or delta_unit == 'години' or delta_unit == 'годин' or delta_unit == 'годину':
                reminder_delta = timedelta(hours=delta_value)
            elif delta_unit == 'хвилин' or delta_unit == 'хвилини' or delta_unit == 'хвилину':
                reminder_delta = timedelta(minutes=delta_value)
            else:
                raise ValueError

        else:
            if delta_unit == 'day' or delta_unit == 'days':
                reminder_delta = timedelta(days=delta_value)
            elif delta_unit == 'weak' or delta_unit == 'weaks':
                reminder_delta = timedelta(weeks=delta_value)
            elif delta_unit == 'hour' or delta_unit == 'hours':
                reminder_delta = timedelta(hours=delta_value)
            elif delta_unit == 'minutes' or delta_unit == 'minute':
                reminder_delta = timedelta(minutes=delta_value)
            else:
                raise ValueError



        event_date = datetime.combine((await state.get_data()).get('event_date'),
                                      (await state.get_data()).get('event_time'))
        reminder_time = event_date - reminder_delta
        reminder_time_five_minutes = event_date - timedelta(minutes=5)

        async with state.proxy() as data:
            event_text = data['event_text']
            event_date_str = event_date.strftime("%d-%m-%Y %H:%M")
            reminder_time_str = reminder_time.strftime("%d-%m-%Y %H:%M")
            reminder_time_five_minutes_str = reminder_time_five_minutes.strftime("%d-%m-%Y %H:%M")
            user_id = message.from_user.id

            # Записываем событие в базу данных
            conn, cursor = connect_db('events.db')
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    event_text TEXT,
                    event_date TEXT,
                    reminder_time TEXT,
                    reminder_time_five_minutes TEXT,
                    notified INTEGER DEFAULT 0
                )
            """)
            conn.commit()
            cursor.execute(
                "INSERT INTO events (user_id, event_text, event_date, reminder_time, reminder_time_five_minutes) VALUES (?, ?, ?, ?, ?)",
                (user_id, event_text, event_date_str, reminder_time_str, reminder_time_five_minutes_str))
            conn.commit()
            conn.close()
        if Language == "Ukr":
            await message.answer(f"Подія «{event_text}» була успішно додана! "
                                 f"Згадаю про нього ({reminder_time_str}).")
        else:
            await message.answer(f"Event «{event_text}» was successful added! "
                                 f"I'll remember him ({reminder_time_str}).")

        await state.finish()
    except (ValueError, IndexError):
        # Обработка ошибок
        if Language == "Ukr":
            await message.answer("Була помилка в збереженні події.")

        else:
            await message.answer("There was an error saving the event.")


async def event_reminder():
    print('reminder started up')
    while True:

        # Получаем текущее время
        current_time = datetime.now().strftime("%d-%m-%Y %H:%M")

        # Запрос к базе данных для получения событий, у которых наступило время
        conn = sqlite3.connect('events.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM events WHERE (reminder_time = ? OR reminder_time_five_minutes = ?)",
                       (current_time, current_time))
        events = cursor.fetchall()

        # Отправляем уведомления о событиях пользователям и удаляем записи
        for event in events:
            user_id = event[1]
            event_text = event[2]
            event_date = event[3]
            reminder_time = event[4]
            reminder_time_five_minutes = event[5]

            if current_time == reminder_time:
                # Отправляем уведомление за указанное время
                if Language == "Ukr":
                    await bot.send_message(user_id, f"Згадка:\n{event_text}\nДата та час: {event_date}")
                else:
                    await bot.send_message(user_id, f"Reminder:\n{event_text}\nData and time: {event_date}")

            elif current_time == reminder_time_five_minutes:
                # Отправляем уведомление за 5 минут до события
                if Language == "Ukr":
                    await bot.send_message(user_id,
                                           f"Нагадування (за 5 хвилин до події):\n{event_text}\nДата и час: {event_date}")
                else:
                    await bot.send_message(user_id,
                                           f"Reminder (5 minutes before the event):\n{event_text}\nDate and time: {event_date}")


                event_id = event[0]
                cursor.execute("DELETE FROM events WHERE id = ?", (event_id,))
                conn.commit()

            # if current_time[11:13] >= event_time[11:13] and current_time[14:16] >= event_time[14:16]:
            #    print("Into the delete fucn!!!")
            #    # Удаляем событие из базы данных
            #    event_id = event[0]
            #    await cursor.execute("DELETE FROM events WHERE id = ?", (event_id,))
            #    await conn.commit()

        conn.close()
        await asyncio.sleep(60)  # Проверяем каждую минуту


def reg_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(main_menu, commands=['Help'])












