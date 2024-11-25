from aiogram import types
from aiogram.types import CallbackQuery, InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from keyboards.inline.vaqt import soat_keyboard
from keyboards.inline.hafta_kunlari import hafta_kunlari_Keyboard
from keyboards.inline.band_qilish import band_qilish_Keyboard, check_Keyboard, username_Keyboard
from keyboards.inline.kurslar import kurslar_Keyboard
from utils.send_message import send_to_group  
from data.config import GROUP_ID  
from loader import dp
from states.personalData import PersonalData





@dp.callback_query_handler(text='band')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Qaysi kunga band qilmoqchisiz?", reply_markup=hafta_kunlari_Keyboard)



@dp.callback_query_handler(text='backend')
async def select_backend(call: CallbackQuery, state: FSMContext):
    teacher = "Og'abek Jumayev"
    course = "Backend"
    msg = "<b>Ismi-sharifi:</b>\nOg'abek Jumayev\n\n"
    msg += "<b>Tug'ilgan yili va joyi: </b>\n24-iyul 2006-yil; \nToshkent shaxri.\n\n"
    msg += "<b>Ish tajribasi: :</b>\nTramlin IT akademiyasi Backend bo'yicha Support teacher\n\n"
    msg += "<b>Texnik ko'nikmalari: </b>\nC, Python, Django, Django Rest, SQLite, MySQL, PostgreSQL, Git, GitHub, HTML, CSS, Java Script, Telegram Bot, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)n\n"
    msg += "<b>Tillar: </b>\nO'zbek tili (Ona tili);\nIngliz tili (B2);\nArab tili (O'qiy olish);\nYapon tili (N3).\n\n"
    await call.message.answer(msg, reply_markup=band_qilish_Keyboard)
    await state.update_data({'teacher': teacher})
    await state.update_data({'course': course})
    await call.message.delete()




@dp.callback_query_handler(text='frontend')
async def select_frontend(call: CallbackQuery, state: FSMContext):
    teacher = "Miraziz Mirahmadov"
    course = "Frontend"
    msg = "<b>Ismi-sharifi:</b>\nMiraziz Mirahmadov\n\n"
    msg += "<b>Tug'ilgan yili va joyi: </b>\n12-iyul 2001-yil; \nToshkent shaxri\n\n"
    msg += "<b>Ish tajribasi: :</b>\nTramlin IT akademiyasi Frontend bo'yicha Support teacher\n\n"
    msg += "<b>Texnik ko'nikmalari: </b>\nC, Python, Django, Django Rest, SQLite, MySQL, PostgreSQL, Git, GitHub, HTML, CSS, Java Script, Telegram Bot, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)n\n"
    msg += "<b>Tillar: </b>\nO'zbek tili (Ona tili);\nIngliz tili (B2);\nArab tili (O'qiy olish);\nYapon tili (N3).\n\n"
    await call.message.answer(msg, reply_markup=band_qilish_Keyboard)
    await state.update_data({'teacher': teacher})
    await state.update_data({'course': course})
    await call.message.delete()





@dp.callback_query_handler(text='cyber')
async def select_cyber(call: CallbackQuery, state: FSMContext):
    teacher = "Miraziz Mirahmadov"
    course = "Cybersecurity"
    msg = "<b>Ismi-sharifi:</b>\nMiraziz Mirahmadov\n\n"
    msg += "<b>Tug'ilgan yili va joyi: </b>\n12-iyul 2001-yil; \nToshkent shaxri.\n\n"
    msg += "<b>Ish tajribasi: :</b>\nTramlin IT akademiyasi Cybersecurity bo'yicha Support teacher\n\n"
    msg += "<b>Texnik ko'nikmalari: </b>\nC, Python, Django, Django Rest, SQLite, MySQL, PostgreSQL, Git, GitHub, HTML, CSS, Java Script, Telegram Bot, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)n\n"
    msg += "<b>Tillar: </b>\nO'zbek tili (Ona tili);\nIngliz tili (B2);\nArab tili (O'qiy olish);\nYapon tili (N3).\n\n"
    await call.message.answer(msg, reply_markup=band_qilish_Keyboard)
    await state.update_data({'teacher': teacher})
    await state.update_data({'course': course})
    await call.message.delete()




@dp.callback_query_handler(text="backend")
async def select_day(call: CallbackQuery, state: FSMContext):
    teacher = call.data 
    course = call.data
    await state.update_data({'teacher': teacher})
    await state.update_data({'course': course})  
    await call.message.delete()
    await call.message.answer(f"Qaysi kunga band qilmoqchisiz?", reply_markup=hafta_kunlari_Keyboard)




@dp.callback_query_handler(text="frontend")
async def select_day(call: CallbackQuery, state: FSMContext):
    teacher = call.data
    course = call.data
    await state.update_data({'teacher': teacher})
    await state.update_data({'course': course})  
    await call.message.delete()
    await call.message.answer(f"Qaysi kunga band qilmoqchisiz?", reply_markup=hafta_kunlari_Keyboard)




@dp.callback_query_handler(text="cyber")
async def select_day(call: CallbackQuery, state: FSMContext):
    teacher = call.data 
    course = call.data
    await state.update_data({'teacher': teacher})
    await state.update_data({'course': course})  
    await call.message.delete()
    await call.message.answer(f"Qaysi kunga band qilmoqchisiz?", reply_markup=hafta_kunlari_Keyboard)




@dp.callback_query_handler(text=['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba'])
async def select_day(call: CallbackQuery, state: FSMContext):
    day = call.data  
    await state.update_data({'day': day})  
    await call.message.delete()
    await call.message.answer(f"Tanlagan kuningiz: {day}\nQaysi soatga band qilmoqchisiz?", reply_markup=soat_keyboard)




@dp.callback_query_handler(lambda call: call.data in ['10:00 - 11:00', '11:00 - 12:00', '12:00 - 13:00', '14:00 - 15:00', '15:00 - 16:00', '16:00 - 17:00', '17:00 - 18:00', '18:00 - 19:00', '19:00 - 20:00'])
async def choose_time(call: CallbackQuery, state: FSMContext):
    selected_time = call.data  
    await state.update_data({"selected_time": selected_time})  
    await call.message.delete()
    await call.message.answer("Iltimos, familiya, ism va sharifingizni to'liq kiriting:")
    await PersonalData.fullname.set()




@dp.message_handler(state=PersonalData.fullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data({'fullname': fullname})
    username = f"@{message.from_user.username}" if message.from_user.username else "username mavjud emas"
    await message.answer(
        f"Sizning username'ingiz: {username}\n"
        "Tasdiqlaysizmi yoki o'zingiz kiritmoqchimisiz?",
        reply_markup=username_Keyboard  
    )
    await PersonalData.username.set()  




@dp.callback_query_handler(lambda call: call.data in ["confirm_username", "edit_username"], state=PersonalData.username)
async def handle_username_action(call: types.CallbackQuery, state: FSMContext):
    if call.data == "confirm_username":
        username = f"@{call.from_user.username}" if call.from_user.username else "username mavjud emas"
        await state.update_data({'username': username})
        contact_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        contact_keyboard.add(KeyboardButton("📱 Telefon raqamni ulashish", request_contact=True))
        await call.message.answer("Telefon raqamingizni ulashing yoki qo'lda kiriting:", reply_markup=contact_keyboard)
        await PersonalData.phoneNumber.set()
    elif call.data == "edit_username":
        await call.message.answer("Iltimos, username'ingizni kiriting:")
        await PersonalData.username.set()




@dp.message_handler(state=PersonalData.username)
async def answer_username(message: types.Message, state: FSMContext):
    username = message.text
    await state.update_data({'username': username})
    contact_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    contact_keyboard.add(KeyboardButton("📱 Telefon raqamni ulashish", request_contact=True))
    await message.answer("Telefon raqamingizni ulashing yoki qo'lda kiriting:", reply_markup=contact_keyboard)
    await PersonalData.phoneNumber.set()





@dp.message_handler(state=PersonalData.phoneNumber, content_types=[types.ContentType.CONTACT, types.ContentType.TEXT])
async def answer_phone(message: types.Message, state: FSMContext):
    if message.contact:  
        phone = message.contact.phone_number
    elif message.text and message.text.isdigit():  
        phone = message.text
        if len(phone) > 13:
            await message.answer("Telefon raqami 13 xonadan oshmasligi kerak. Iltimos, qaytadan kiriting:")
            return
    else:  
        await message.answer("Telefon raqami faqat sonlardan iborat bo'lishi kerak. Iltimos, qaytadan kiriting:")
        return

    if not phone.startswith('+'):
        phone = f"+{phone}"

    if not phone[1:].isdigit():
        await message.answer("Telefon raqami noto'g'ri formatda. Iltimos, qaytadan kiriting:")
        return

    await state.update_data({'phone': phone})
    await message.answer("Telefon raqam saqlandi. Rahmat!", reply_markup=ReplyKeyboardRemove())


    contact_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    contact_keyboard.add(InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="check"))
    contact_keyboard.add(InlineKeyboardButton(text="❌ Bekor qilish", callback_data="bekor_qilish"))

    data = await state.get_data()
    course = data.get("course")
    teacher = data.get("teacher")
    day = data.get('day')
    selected_time = data.get('selected_time')
    fullname = data.get('fullname')
    username = data.get('username')
    phone = data.get('phone')

    msg = "<b>Quyidagi ma'lumotlar tasdiqlash uchun:</b>\n\n"
    msg += f"<b>Kurs:</b> {course}\n"
    msg += f"<b>Support:</b> {teacher}\n"
    msg += f"<b>Hafta kuni:</b> {day}\n"
    msg += f"<b>Vaqt:</b> {selected_time}\n"
    msg += f"<b>Ismingiz:</b> {fullname}\n"
    msg += f"<b>Username:</b> {username}\n"
    msg += f"<b>Telefon:</b> {phone}"

    await message.answer(msg, reply_markup=contact_keyboard)
    await PersonalData.confirm.set()




@dp.callback_query_handler(text='check', state=PersonalData.confirm)
async def select_category(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    course = data.get("course")
    teacher = data.get("teacher")
    day = data.get('day')
    selected_time = data.get('selected_time')
    fullname = data.get('fullname')
    username = data.get('username')
    phone = data.get('phone')

    msg = "<b>Quyidagi ma'lumotlar qabul qilindi:</b>\n\n"
    msg += f"<b>Kurs:</b> {course}\n"
    msg += f"<b>Support:</b> {teacher}\n"
    msg += f"<b>Hafta kuni:</b> {day}\n"
    msg += f"<b>Vaqt:</b> {selected_time}\n"
    msg += f"<b>Ismingiz:</b> {fullname}\n"
    msg += f"<b>Username:</b> {username}\n"
    msg += f"<b>Telefon:</b> {phone}"
    await send_to_group(GROUP_ID, msg)
    await state.finish()
    




@dp.callback_query_handler(text='bekor_qilish')
async def select_category(call: CallbackQuery):
    await call.message.answer("Bekor qilindi. Boshqa kursni tanlab davom etishingiz mumkin.", reply_markup=kurslar_Keyboard)

    
