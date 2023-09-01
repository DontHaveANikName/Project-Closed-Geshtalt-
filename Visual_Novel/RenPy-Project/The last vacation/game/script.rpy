﻿define olek = Character("Олексій", color="#FFFFFF")
define mil = Character("Міла", color="#FFFFFF", image="mila")
define rom = Character("Роман", color="#FFFFFF")
#Другорядні
define vla = Character("Владімєр", color="#FFFFFF")
define kok = Character("Григорій", color="#FFFFFF")
# Епізодичні
define vas = Character("Васильович", color="#FFFFFF", image="vasyliovych")
define chel = Character("Чоловік на статуї", color="#FFFFFF")
define noname = Character("???", color="#FFFFFF")
define guch = Character("Гучномовець", color="#FFFFFF")
define gumanoid = Character("Гуманоїд", color="#009900")
define maks = Character("Максим", color="#FFFFFF", image="maks")
define diary = Character(None, kind=nvl, what_text_align=0, what_xalign=0.5)

default persistent.end = False

label start:
    stop music fadeout 3
    window hide
    scene day_1 with fade
    pause(1.5)
    scene dream_1 with fade
    window show
    "Сьогодні я знову йду на роботу ввечері"
    "В принципі, як і завжди, але зараз вилиці абсолютно пусті"
    "Не сказати, що це якось дуже дивно, але в цей час на вулицях знаходяться як мінімум алкоголіки, чи вічно гучні підлітки"
    "Чесне слово, я відчуваю себе якимось не таким, коли бачу їх, бо я ніколи не був гучним підлітком, і сподіваюсь ніколи не стану алкоголіком"
    "Втім зараз все пливе як в тумані, ніби я таки випив чимало"
    "..."
    "Крізь уже звичну тишу почав пробиватись якийсь голос"
    noname "Олексію..."
    "Поступово голос почав наближатись і ставати гучніше"
    noname "Олексію... {w} Олексію.."
    "Тепер голос звучав так широко і в той же час близько, що мені здалось, що він у моїй голові"
    "Це був жіночий, ніжний, як море у штиль, голос"
    scene dream_2 with fade
    olek "Хто ви, пані? Що вам треба?"
    noname "Скажи, Олексію, ти готовий?"
    olek "Так, пані, я абсолютно готовий"
    noname "Ось і чудово.."
    noname "Тоді, прокинся.."
    scene awakening_1
    ""
    scene awakening_2
    "..."
    scene awakening_3
    "Це знову був той сон.."
    scene awakening_4
    "Давно ж він мені не снився.."
    scene military_room
    "Напевно останній раз був рік тому"
    "В день коли на місто впав метеорит і змінив усе"
    "Спогади почали спливати у моїй голові, а шкірою пробіг нестерпний холодок"
    "Ніби, для закріплення ефекту мені в очі впав подряпаний щоденник" 
    "Щоенник, який лежав на поличці ніби чекаючи щоб я його взяв повернувшись до минулого, яке я би волів забути"
    "Я робив записи у нього у ті дні, коли все це починалось, коли ще було відчуття, що все це може швидко скінчитись та повернутись до звичайного життя"
    "Дивлячись на цей подряпаний щоденник, я відчував, як він тягне мене до себе"
    "Спогади у моїй голові, ще не збілки, тому я не хотів собі нагадувати те що тоді відбувалось, але рука мимоволі сама тяглася до маленького блокнотика відкриваючи перші сторінки"
    scene military_diary
    "На форзаці було написано: \"Від люблячих батьків, для найкращого сина\""
    "Це був останній подарунок на день сина, який я отримав від них. Тепер я навіть не знаю, чи живі вони, чи щось сталося. Жодної вісточки..."
    "Я почав читати"
    nvl clear
    diary """
    
    ~ День 1 ~ 20.11 ~

    Сьогодні на місто впав метеорит, який приніс з собою, якийсь зелений газ з космосу

    Якщо я правильно зрозумів, то він, газ, може перетворювати людей на якихось гуманоїдів

    Отже йти до людей не дуже хороша ідея, особливо, якщо люди озброєні, оскільки вони також можуть мутувати

    Також з моїх спостережень: цей газ підкосив чимало людей, а інших вже викосили гуманоїди...

    __________________________________________________________________________________

    Основне, що я зміг зрозуміти за перший день:

    1) Гуманоїди набагато сильніші за людей, їх кістки проросли у зворотньому напрямку, а їх мотиви взагалі не зрозумілі

    2) Правління вже відрядило величезний гвинтокрил, який називають \"Рятувалиний ковчег\" він має бути ністільки великим, що зможе евакуювати цілу область (проте я на нього все одно не піду з вище вказаних причин)

    3) Газ блокує будь який зв'язок, а апаратура в яку потрапляє газ перестає працювати

    Виходячи з вище сказаного мені просто потрбно протриматись у місті кілька днів, поки влада не пришле військових на зачистку території (а це має статись напевно після відльоту ковчега), доти ж мені просто треба триматись

    """
    nvl hide
    
    "На всю наступну сторінку було написано"
    
    nvl clear
    diary """
    
    Борись.
    
    Борись.. 
    
    Борись..!
    
    """
    nvl hide

    "Записи продовжились вже з сьомого дня"

    nvl clear
    diary """
    
    ~ День 7 ~ 27.11 ~

    Останні дні були просто скажені, хоча після падіння метеориту вони всі такі..

    Газ з того метеорита перетворив Київ на зону жаху і безпека стала моїм головним пріоритетом
    
    Перші дні я у постійному пошуку провізії, а ще здибав собі пістолет, весь інший тиждень я постійно пересувався з одного місця на інше, шукаючи безпечних укриттів у занедбаних будівлях. Але здається, що ніде не було повністю безпечно

    Найскладніше було залишити свою квартиру, де я проживав. Там я відчувався як відсторонений, але зомбі атакували майже постійно, і я був змушений шукати нового притулку

    В решті решт  мені вдалося знайти цілий будинок на околиці міста, який виглядає мало пошкодженим 
    
    Здається, що його власники вже покинули його до падіння метеориту, але я весь час відчував себе якимось винним, що задерся у чужий дім, в той же час я розумію, що у цій ситуації немає місця на сумніви
    
    Я став дуже пильним, я би навіть сказав, що ця пильність знаходиться на межі параної 
    
    Я смикаюсь через будь який найменший звук думаючи, що гуманоїди пробрались у моє укриття, але в основному це виявляється щось не значне, типу вітерець подув і хвіртка скрипнула, а я вже цілюсь вишукуючи гуманоїда на порозі

    Втім на моє здивування сьогодні все було досить тихо

    За цілий день я не побачив жодного гуманоїда, проте сьогодні я бачив, як над містом летить таки той гвинтокрил, який ще ковчегом назвали

    Він дійсно величений, це видно навіть незважаючи на його віддаленість від землі

    Якщо я побачив його над містом, отже за розрахунками військові мають вже скоро прийти на зачистку міста

    """
    nvl hide

    "Наступна нотатка датувалась двадцять восьмим листопада"

    nvl clear
    diary """
    
    ~ День 8 ~ 28.11 ~

    Цей день став найжахливішим досвідом за все моє виживання з моменту падіння метеорита 
    
    Військові почали бомбити місто, і я опинився у полоні вогню і руйнувань

    Вранці я почув гучний , а згодом і вибухи 
    
    Я піднявшись на дах будинку, я був шокований картиною, що розгортається переді мною 
    
    Військові літаки бомбили місто, спустошуючи будівлі і вулиці 
    
    Здавалося, що ніщо не залишиться стояти

    Моя перша реакція була сховатися, тож я занурився в підвал будинку, сподіваючись, що стіни зможуть захистити мене від смертоносних фрагментів та уламків 
    
    Вибухи трясли землю, але я мусив утримувати свою паніку під контролем, але у мене не вдавалось це робити доки голову сверлило єдине запитання: \"Нащо?\"

    За весь час поки я був під обстрілами я все перебирав варіанти і єдиним хоч якось логічним поясненням стало те що верхівка влади вирішила, що в місті нікого не мало би лишитись, всі мали би евокуюватись на ковчезі

    Але це все одно не могло виправдати їх..

    Після декількох годин бомбардування вибухи затихли

    """
    nvl hide

    "Наступна сторінка була майже не заповнена, буквально кілька речень"

    nvl clear
    diary """
    
    ~ День 12 ~ 04.12 ~

    Увесь цей час, усі ці чотири дні бомбардування повторювались, як мінімум раз на день, але я все ж намагався приводити собі якісь аргументи за те щоб залишитись у місті, але сьогодні, коли бомбардування затихли на декілька годин я виходив на розвідку

    Побачвши все залишки міста я зрозумів, що настав час зізнатися собі, що моє місто тепер знаходиться у руїнах, а отже залишатись у ньому просто немає сенсу

    Завтра я виїзжаю з міста до найближчого поселення, яке буде достатньо маленьким аби постійно не зустрічатись із гуманоїдами

    """
    nvl hide

    "Наступна нотатка виявилась останньою"

    nvl clear
    diary """
    
    ~ День 13 ~ 05.12 ~

    Сьогодні був один з найскладніших днів в моєму житті після цієї апокаліптичної катастрофи. Я вирішив перетнути річку і знайти нове притулок, але те, що я побачив, залишило мене безмовним.

    Наближаючись до найближчого мосту через річку, я відразу помітив, що міст був повністю зруйнований. Лише розірвані шматки сталі залишилися, свідчачи про те, що тут колись було переправою. Річка здавалася непрохідною перепоною, але я не міг сидіти на місці.

    Знімаючи лишню одежу, щоб не стати важким тягарем, вирішив перепливати річку. Вода була холодною і потужною, але я протистояв їй з усією силою, якою мав.

    Потрапивши на протилежний берег, я майже втратив надію. Тут відкривався міжнародний барикадний пост, або, скоріше, те, що від нього залишилося. Люди обкрадали та вбивали одне одного просто небацьким чином. Беззаперечно, люди стали небезпечнішими за гуманоїдів.

    Тривало мить, щоб зрозуміти, що маю справу зі збрехливими, безжалісними супротивниками. Я не можу довіряти навіть тим, що здаються найбільшими союзниками. Вони стали живими пастками, а потенційна загроза зіткнення з ними лише збільшується.

    Мій внутрішній голос каже мені, що найкраще, що я можу зробити - уникати будь-яких контактів з людьми. Залишаючись на своєму шляху, я віддаю перевагу самотності. Можливо, з таким підходом я збережу своє життя.

    """
    nvl hide
    scene military_room
    show maks_normal
    "Моє читання перервав побратим Максим, який зайшов до казарми"
    maks "Шо ти, Олекса, готовий відправитись на відвойовування Києва?"
    olek "Ти навіть не уявляєш на скільки"
    maks "І що тобі взагалі не лячно повертатись у зруйноване місто?"
    olek "Звісно страшно, я ж в ньому виріс, і не хочеться дивитись на всі ці зруйновані будинки та згадувати, як ти гасав цими вуличками з друзями, але чимало людей поклали своє життя, щоб ми змогли повернути, хоча б цю північ країни"
    maks "Твоя правда"
    maks "Ну, добре, збирайся. Збір через десять хвилин, перевір чи все ти з собою взяв і виходь до злітної смуги, я буду чекати тебе там"
    olek "Добре, Максе, побачимось за десять хвилин"
    "Він вийшов з казарми та попрямував злітної смоги"
    "Я також довго не чекав"
    "Швидко зібрав усі речі та попрямував до злітної смуги"
    "Маким, як і казав уже чекав мене там"
    maks "О ти вже тут? І десяти хвилин не пройшло"
    olek "Ну так старався..!"
    "З посмішкою сказав я"
    maks "Слухай, я хотів тобі сказати якщо у мене не буде потім можливості.."
    olek "Давай без всяких пересмертних промов, добре?"
    maks "Та я не.."
    maks "..."
    maks "І все ж я хочу тобі сказати, що я ради, що ти приєднався до війська рік тому.."
    olek "Я також радий, що приєданвся, Максиме"
    scene end30
    pause
    if persistent.end == False:
        $ renpy.notify("Кінцівку здобуто")
        $ persistent.end30 = True
    return