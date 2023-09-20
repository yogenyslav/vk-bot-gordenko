from typing import Optional, Any
from enum import Enum
from vk_api import VkApi
from vk_api.longpoll import VkEventType, VkLongPoll
from pydantic import BaseModel, Field


class UserDeactivated(str, Enum):
    deleted = "deleted"
    banned = "banned"


class FirstNameCase(str, Enum):
    nom = "nom"
    gen = "gen"
    dat = "dat"
    acc = "acc"
    ins = "ins"
    abl = "abl"


class FriendStatus(int, Enum):
    not_friend = 0
    sent_request = 1
    received_request = 2
    friend = 3


class LastSeenPlatform(int, Enum):
    mobile = 1
    iphone = 2
    ipad = 3
    android = 4
    windows_phone = 5
    windows_10 = 6
    web = 7


class OccupationType(str, Enum):
    work = "work"
    school = "school"
    university = "university"


class Political(int, Enum):
    communist = 1
    socialist = 2
    moderate = 3
    liberal = 4
    conservative = 5
    monarchist = 6
    ultraconservative = 7
    indifferent = 8
    libertarian = 9


class PeopleMain(int, Enum):
    mind_and_creativity = 1
    kindness_and_honesty = 2
    beauty_and_health = 3
    wealth_and_power = 4
    courage_and_persistence = 5
    humor_and_love_of_life = 6


class LifeMain(int, Enum):
    family_and_children = 1
    career_and_money = 2
    entertainment_and_leisure = 3
    science_and_research = 4
    improving_the_world = 5
    personal_development = 6
    beauty_and_art = 7
    fame_and_influence = 8


class Smoking(int, Enum):
    sharply_negative = 1
    negative = 2
    compromisable = 3
    neutral = 4
    positive = 5


class Alcohol(int, Enum):
    sharply_negative = 1
    negative = 2
    compromisable = 3
    neutral = 4
    positive = 5


class RelativeType(str, Enum):
    child = "child"
    sibling = "sibling"
    parent = "parent"
    grandparent = "grandparent"
    grandchild = "grandchild"


class Relation(int, Enum):
    not_specified = 0
    not_married = 1
    has_friend = 2
    engaged = 3
    married = 4
    complicated = 5
    actively_searching = 6
    in_love = 7
    in_civil_union = 8


class WallDefault(str, Enum):
    owner = "owner"
    all = "all"


class Career(BaseModel):
    group_id: Optional[int] = Field(
        None, description="идентификатор сообщества (если доступно, иначе company)"
    )
    company: Optional[str] = Field(
        None, description="название компании (если доступно, иначе group_id)"
    )
    country_id: Optional[int] = Field(None, description="идентификатор страны")
    city_id: Optional[int] = Field(
        None, description="идентификатор города (если доступно, иначе city_name)"
    )
    city_name: Optional[str] = Field(
        None, description="название города (если доступно, иначе city_id)"
    )
    from_: Optional[int] = Field(None, description="год начала работы", alias="from")
    until: Optional[int] = Field(None, description="год окончания работы")
    position: Optional[str] = Field(None, description="должность")


class City(BaseModel):
    id: int = Field(..., description="идентификатор города")
    title: str = Field(..., description="название города")


class Contacts(BaseModel):
    mobile_phone: Optional[str] = Field(
        None,
        description="номер мобильного телефона (только для Standalone-приложений).",
    )
    home_phone: Optional[str] = Field(
        None, description="дополнительный номер телефона."
    )


class Counters(BaseModel):
    albums: Optional[int] = Field(None, description="количество фотоальбомов")
    videos: Optional[int] = Field(None, description="количество видеозаписей")
    audios: Optional[int] = Field(None, description="количество аудиозаписей")
    photos: Optional[int] = Field(None, description="количество фотографий")
    notes: Optional[int] = Field(None, description="количество заметок")
    friends: Optional[int] = Field(None, description="количество друзей")
    gifts: Optional[int] = Field(None, description="количество подарков")
    groups: Optional[int] = Field(None, description="количество сообществ")
    online_friends: Optional[int] = Field(None, description="количество друзей онлайн")
    mutual_friends: Optional[int] = Field(None, description="количество общих друзей")
    user_videos: Optional[int] = Field(
        None, description="количество видеозаписей с пользователем"
    )
    user_photos: Optional[int] = Field(
        None, description="количество фотографий с пользователем"
    )
    followers: Optional[int] = Field(None, description="количество подписчиков")
    pages: Optional[int] = Field(
        None, description="количество объектов в блоке «Интересные страницы»"
    )
    subscriptions: Optional[int] = Field(
        None,
        description="количество подписок пользователя (на кого пользователь подписан)",
    )


class Country(BaseModel):
    id: int = Field(..., description="идентификатор страны.")
    title: str = Field(..., description="название страны.")


class PhotoSize(BaseModel):
    type: str = Field(..., description="тип фотографии.")
    url: str = Field(..., description="url копии фотографии.")
    width: int = Field(..., description="ширина копии в px.")
    height: int = Field(..., description="высота копии в px.")


class Photo(BaseModel):
    id: int = Field(..., description="идентификатор фотографии.")
    album_id: int = Field(
        ..., description="идентификатор альбома, в котором находится фотография."
    )
    owner_id: int = Field(..., description="идентификатор владельца фотографии.")
    user_id: int = Field(
        ...,
        description="идентификатор пользователя, загрузившего фото (если фотография размещена в сообществе). Для фотографий, размещенных от имени сообщества, user_id = 100.",
    )
    text: str = Field(..., description="текст описания фотографии.")
    date: int = Field(..., description="дата добавления в формате Unixtime.")
    sizes: list[PhotoSize] = Field(
        ..., description="массив с копиями изображения в разных размерах."
    )
    width: Optional[int] = Field(
        None, description="ширина оригинала фотографии в пикселах."
    )
    height: Optional[int] = Field(
        None, description="высота оригинала фотографии в пикселах."
    )


class Crop(BaseModel):
    x: int = Field(..., description="координата X левого верхнего угла в процентах.")
    y: int = Field(..., description="координата Y левого верхнего угла в процентах.")
    x2: int = Field(..., description="координата X правого нижнего угла в процентах.")
    y2: int = Field(..., description="координата Y правого нижнего угла в процентах.")


class Rect(Crop):
    ...


class CropPhoto(BaseModel):
    photo: Photo = Field(
        ...,
        description="объект photo фотографии пользователя, из которой вырезается главное фото профиля.",
    )
    crop: Crop = Field(..., description="вырезанная фотография пользователя.")
    rect: Rect = Field(
        ...,
        description="миниатюрная квадратная фотография, вырезанная из фотографии crop.",
    )


class Education(BaseModel):
    university: Optional[int] = Field(None, description="идентификатор университета.")
    university_name: Optional[str] = Field(None, description="название университета.")
    faculty: Optional[int] = Field(None, description="идентификатор факультета.")
    faculty_name: Optional[str] = Field(None, description="название факультета.")
    graduation: Optional[int] = Field(None, description="год окончания.")


class LastSeen(BaseModel):
    time: int = Field(..., description="время последнего посещения в формате Unixtime.")
    platform: LastSeenPlatform = Field(..., description="тип платформы.")


class Military(BaseModel):
    unit: Optional[str] = Field(None, description="номер части.")
    unit_id: Optional[int] = Field(
        None, description="идентификатор части в базе данных."
    )
    country_id: Optional[int] = Field(
        None, description="идентификатор страны, в которой находится часть."
    )
    from_: Optional[int] = Field(None, description="год начала службы", alias="from")
    until: Optional[int] = Field(None, description="год окончания службы")


class Occupation(BaseModel):
    type: Optional[OccupationType] = Field(None, description="тип.")
    id: Optional[int] = Field(
        None, description="идентификатор школы, вуза, сообщества."
    )
    name: Optional[str] = Field(
        None, description="название школы, вуза или места работы."
    )


class Personal(BaseModel):
    political: Optional[Political] = Field(
        None, description="политические предпочтения."
    )
    langs: Optional[list[str]] = Field(None, description="языки.")
    religion: Optional[str] = Field(None, description="мировоззрение.")
    inspired_by: Optional[str] = Field(None, description="источники вдохновения.")
    people_main: Optional[PeopleMain] = Field(None, description="главное в людях.")
    life_main: Optional[LifeMain] = Field(None, description="главное в жизни.")
    smoking: Optional[Smoking] = Field(None, description="отношение к курению.")
    alcohol: Optional[Alcohol] = Field(None, description="отношение к алкоголю.")


class Relative(BaseModel):
    id: int = Field(..., description="идентификатор пользователя.")
    name: str = Field(
        ...,
        description="имя родственника (если родственник не является пользователем ВКонтакте, то предыдущее значение id возвращено не будет).",
    )
    type: str = Field(..., description="родственная связь.")


class RelationPartner(BaseModel):
    id: int = Field(..., description="идентификатор пользователя.")
    name: str = Field(..., description="имя пользователя.")


class School(BaseModel):
    id: Optional[str] = Field(None, description="идентификатор школы.")
    country: Optional[int] = Field(
        None, description="идентификатор страны, в которой расположена школа."
    )
    city: Optional[int] = Field(
        None, description="идентификатор города, в котором расположена школа."
    )
    name: Optional[str] = Field(None, description="название школы")
    year_from: Optional[int] = Field(None, description="год начала обучения")
    year_to: Optional[int] = Field(None, description="год окончания обучения")
    year_graduated: Optional[int] = Field(None, description="год выпуска")
    class_: Optional[str] = Field(None, description="буква класса", alias="class")
    speciality: Optional[str] = Field(None, description="специализация")
    type: Optional[int] = Field(None, description="идентификатор типа")
    type_str: Optional[Any] = Field(None)


class Sex(int, Enum):
    female = 1
    male = 2
    not_specified = 0


class University(BaseModel):
    id: Optional[int] = Field(None, description="идентификатор университета.")
    country: Optional[int] = Field(
        None, description="идентификатор страны, в которой расположен университет."
    )
    city: Optional[int] = Field(
        None, description="идентификатор города, в котором расположен университет."
    )
    name: Optional[str] = Field(None, description="название университета.")
    faculty: Optional[int] = Field(None, description="идентификатор факультета.")
    faculty_name: Optional[str] = Field(None, description="название факультета.")
    chair: Optional[int] = Field(None, description="идентификатор кафедры.")
    chair_name: Optional[str] = Field(None, description="название кафедры.")
    graduation: Optional[int] = Field(None, description="год окончания обучения.")
    education_form: Optional[str] = Field(None, description="форма обучения.")
    education_status: Optional[str] = Field(
        None, description="статус (например, «Выпускник (специалист)»)."
    )


class User(BaseModel):
    id: int = Field(..., description="id пользователя.")
    first_name: str = Field(..., description="имя пользователя.")
    last_name: str = Field(..., description="фамилия пользователя.")
    is_closed: bool = Field(
        ..., description="скрыт ли профиль пользователя настройками приватности."
    )
    can_access_closed: bool = Field(
        ...,
        description="может ли текущий пользователь видеть профиль при is_closed=1 (например, он есть в друзьях).",
    )

    deactivated: Optional[UserDeactivated] = Field(
        None,
        description="поле возвращается, если страница пользователя удалена или заблокирована, содержит значение deleted или banned. В этом случае опциональные поля не возвращаются.",
    )

    about: Optional[str] = Field(
        None, description="содержимое поля «О себе» из профиля."
    )
    activities: Optional[str] = Field(
        None, description="содержимое поля «Деятельность» из профиля."
    )
    bdate: Optional[str] = Field(
        None,
        description="дата рождения. Возвращается в формате D.M.YYYY или D.M (если год рождения скрыт). Если дата рождения скрыта целиком, поле отсутствует в ответе.",
    )
    blacklisted: Optional[int] = Field(
        None,
        description="информация о том, находится ли текущий пользователь в черном списке. Возможные значения: 1 — находится; 0 — не находится.",
    )
    blacklisted_by_me: Optional[int] = Field(
        None,
        description="информация о том, находится ли пользователь в черном списке у текущего пользователя. Возможные значения: 1 — находится; 0 — не находится.",
    )
    books: Optional[str] = Field(
        None, description="содержимое поля «Любимые книги» из профиля пользователя."
    )
    can_post: Optional[int] = Field(
        None,
        description="информация о том, может ли текущий пользователь оставлять записи на стене. Возможные значения: 1 — может; 0 — не может.",
    )
    can_see_all_posts: Optional[int] = Field(
        None,
        description="информация о том, может ли текущий пользователь видеть чужие записи на стене. Возможные значения: 1 — может; 0 — не может.",
    )
    can_see_audio: Optional[int] = Field(
        None,
        description="информация о том, может ли текущий пользователь видеть аудиозаписи. Возможные значения: 1 — может; 0 — не может.",
    )
    can_send_friend_request: Optional[int] = Field(
        None,
        description="информация о том, будет ли отправлено уведомление пользователю о заявке в друзья от текущего пользователя. Возможные значения: 1 — уведомление будет отправлено; 0 — уведомление не будет отправлено.",
    )
    can_write_private_message: Optional[int] = Field(
        None,
        description="информация о том, может ли текущий пользователь отправить личное сообщение. Возможные значения: 1 — может; 0 — не может.",
    )
    career: Optional[Career] = Field(
        None, description="информация о карьере пользователя."
    )
    city: Optional[City] = Field(
        None,
        description="информация о городе, указанном на странице пользователя в разделе «Контакты».",
    )
    common_count: Optional[int] = Field(
        None, description="количество общих друзей с текущим пользователем."
    )
    connections: Optional[dict] = Field(
        None,
        description='возвращает данные об указанных в профиле сервисах пользователя, таких как: skype, livejournal. Для каждого сервиса возвращается отдельное поле с типом string, содержащее никнейм пользователя. Например, "skype": "username".',
    )
    contacts: Optional[Contacts] = Field(
        None,
        description="информация о телефонных номерах пользователя (если данные указаны и не скрыты настройками приватности).",
    )
    counters: Optional[Counters] = Field(
        None, description="количество различных объектов у пользователя."
    )
    country: Optional[Country] = Field(
        None,
        description="информация о стране, указанной на странице пользователя в разделе «Контакты».",
    )
    crop_photo: Optional[CropPhoto] = Field(
        None,
        description="возвращает данные о точках, по которым вырезаны профильная и миниатюрная фотографии пользователя, при наличии.",
    )
    domain: Optional[str] = Field(
        None,
        description='короткий адрес страницы. Возвращается строка, содержащая короткий адрес страницы (например, andrew). Если он не назначен, возвращается "id"+user_id, например, id35828305.',
    )
    education: Optional[Education] = Field(
        None, description="информация о высшем учебном заведении пользователя."
    )
    exports: Optional[Any] = Field(
        None,
        description="внешние сервисы, в которые настроен экспорт из ВК ( livejournal).",
    )
    first_name_nom: Optional[str] = Field(
        None, description="имя в именительном падеже."
    )
    first_name_gen: Optional[str] = Field(None, description="имя в родительном падеже.")
    first_name_dat: Optional[str] = Field(None, description="имя в дательном падеже.")
    first_name_acc: Optional[str] = Field(None, description="имя в винительном падеже.")
    first_name_ins: Optional[str] = Field(
        None, description="имя в творительном падеже."
    )
    first_name_abl: Optional[str] = Field(None, description="имя в предложном падеже.")
    followers_count: Optional[int] = Field(
        None, description="количество подписчиков пользователя."
    )
    friend_status: Optional[FriendStatus] = Field(
        None, description="статус дружбы с пользователем."
    )
    games: Optional[str] = Field(
        None, description="содержимое поля «Любимые игры» из профиля."
    )
    has_mobile: Optional[int] = Field(
        None,
        description="информация о том, известен ли номер мобильного телефона пользователя. Возвращаемые значения: 1 — известен, 0 — не известен.",
    )
    has_photo: Optional[int] = Field(
        None,
        description="информация о том, установлена ли у пользователя фотография. Возвращаемые значения: 1 — установлена, 0 — не установлена.",
    )
    home_town: Optional[str] = Field(None, description="название родного города.")
    interests: Optional[str] = Field(
        None, description="содержимое поля «Интересы» из профиля."
    )
    is_favorite: Optional[int] = Field(
        None,
        description="информация о том, находится ли пользователь в закладках у текущего пользователя. Возможные значения: 1 — есть; 0 — нет.",
    )
    is_friend: Optional[int] = Field(
        None,
        description="информация о том, является ли пользователь другом текущего пользователя. Возможные значения: 1 — да; 0 — нет.",
    )
    is_hidden_from_feed: Optional[int] = Field(
        None,
        description="информация о том, скрыт ли пользователь из ленты новостей текущего пользователя. Возможные значения: 1 — да; 0 — нет.",
    )
    is_no_index: Optional[int] = Field(
        None,
        description="индексируется ли профиль текущим пользователем. Возможные значения: 1 — профиль скрыт от поисковых сайтов; 0 — профиль доступен поисковым сайтам. (В настройках приватности: https://vk.com/settings?act=privacy, в пункте «Кому в интернете видна моя страница», выбрано значение «Всем»).",
    )
    last_name_nom: Optional[str] = Field(
        None, description="фамилия в именительном падеже."
    )
    last_name_gen: Optional[str] = Field(
        None, description="фамилия в родительном падеже."
    )
    last_name_dat: Optional[str] = Field(
        None, description="фамилия в дательном падеже."
    )
    last_name_acc: Optional[str] = Field(
        None, description="фамилия в винительном падеже."
    )
    last_name_ins: Optional[str] = Field(
        None, description="фамилия в творительном падеже."
    )
    last_name_abl: Optional[str] = Field(
        None, description="фамилия в предложном падеже."
    )
    last_seen: Optional[LastSeen] = Field(
        None, description="данные о последнем посещении пользователя."
    )
    lists: Optional[str] = Field(
        None,
        description="разделенные запятой идентификаторы списков друзей, в которых состоит пользователь.",
    )
    maiden_name: Optional[str] = Field(None, description="девичья фамилия.")
    military: Optional[Military] = Field(
        None, description="информация о военной службе пользователя."
    )
    movies: Optional[str] = Field(
        None, description="содержимое поля «Любимые фильмы» из профиля."
    )
    music: Optional[str] = Field(
        None, description="содержимое поля «Любимая музыка» из профиля."
    )
    nickname: Optional[str] = Field(
        None, description="никнейм (отчество) пользователя."
    )
    occupation: Optional[Occupation] = Field(
        None, description="информация о текущем роде занятия пользователя."
    )
    online: Optional[int] = Field(
        None,
        description="информация о том, находится ли пользователь сейчас на сайте. Если пользователь использует мобильное приложение либо мобильную версию, возвращается дополнительное поле online_mobile, содержащее 1. При этом, если используется именно приложение, дополнительно возвращается поле online_app, содержащее его идентификатор.",
    )
    online_mobile: Optional[int] = Field(None)
    online_app: Optional[int] = Field(None)
    personal: Optional[Personal] = Field(
        None, description='информация о полях из раздела "Жизненная позиция".'
    )
    photo_50: Optional[str] = Field(
        None,
        description="URL квадратной фотографии пользователя, имеющей ширину 50 пикселей. В случае отсутствия у пользователя фотографии возвращается https://vk.com/images/camera_50.png.",
    )
    photo_100: Optional[str] = Field(
        None,
        description="URL квадратной фотографии пользователя, имеющей ширину 100 пикселей. В случае отсутствия у пользователя фотографии возвращается https://vk.com/images/camera_100.png.",
    )
    photo_200_orig: Optional[str] = Field(
        None,
        description="URL фотографии пользователя, имеющей ширину 200 пикселей. В случае отсутствия у пользователя фотографии возвращается https://vk.com/images/camera_200.png.",
    )
    photo_200: Optional[str] = Field(
        None,
        description="URL квадратной фотографии, имеющей ширину 200 пикселей. Если у пользователя отсутствует фотография таких размеров, в ответе вернется https://vk.com/images/camera_200.png",
    )
    photo_400_orig: Optional[str] = Field(
        None,
        description="URL фотографии, имеющей ширину 400 пикселей. Если у пользователя отсутствует фотография такого размера, в ответе вернется https://vk.com/images/camera_400.png.",
    )
    photo_id: Optional[str] = Field(
        None,
        description="Строковый идентификатор главной фотографии профиля пользователя в формате {user_id}_{photo_id}, например, 6492_192164258. Обратите внимание, это поле может отсутствовать в ответе.",
    )
    photo_max: Optional[str] = Field(
        None,
        description="URL квадратной фотографии с максимальной шириной. Может быть возвращена фотография, имеющая ширину как 200, так и 100 пикселей. В случае отсутствия у пользователя фотографии возвращается https://vk.com/images/camera_200.png.",
    )
    photo_max_orig: Optional[str] = Field(
        None,
        description="URL фотографии максимального размера. Может быть возвращена фотография, имеющая ширину как 400, так и 200 пикселей. В случае отсутствия у пользователя фотографии возвращается https://vk.com/images/camera_400.png.",
    )
    quotes: Optional[str] = Field(None, description="любимые цитаты пользователя.")
    relatives: Optional[list[Relative]] = Field(
        None, description="список родственников пользователя."
    )
    relation: Optional[Relation] = Field(
        None, description="семейное положение пользователя."
    )
    relation_partner: Optional[RelationPartner] = Field(None)
    schools: Optional[list[School]] = Field(
        None, description="список школ, в которых учился пользователь."
    )
    screen_name: Optional[str] = Field(None, description="короткое имя страницы.")
    sex: Optional[Sex] = Field(None, description="пол пользователя.")
    site: Optional[str] = Field(None, description="адрес сайта, указанный в профиле.")
    status: Optional[str] = Field(None, description="статус пользователя.")
    status_audio: Optional[Any] = Field(None)
    timezone: Optional[int] = Field(None, description="временная зона пользователя.")
    trending: Optional[int] = Field(None)
    tv: Optional[str] = Field(None, description="любимые телешоу.")
    universities: Optional[list[University]] = Field(
        None, description="список вузов, в которых учился пользователь."
    )
    verified: Optional[int] = Field(None, description="верифицирован ли пользователь.")
    wall_default: Optional[WallDefault] = Field(
        None, description="режим стены по умолчанию."
    )
