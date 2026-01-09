import random

MOVIES = [
    {
        "title": "Интерстеллар",
        "description": "Научная фантастика о путешествии сквозь пространство и время ради спасения человечества.",
        "image": "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
        "links": {
            "Netflix": "https://www.netflix.com",
            "Kinopoisk": "https://www.kinopoisk.ru"
        }
    },
    {
        "title": "Бойцовский клуб",
        "description": "Культовый фильм о внутреннем бунте, обществе потребления и поиске себя.",
        "image": "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
        "links": {
            "Amazon": "https://www.amazon.com",
            "Kinopoisk": "https://www.kinopoisk.ru"
        }
    },
    {
        "title": "Зелёная миля",
        "description": "Трогательная история о человечности, чуде и сострадании.",
        "image": "https://upload.wikimedia.org/wikipedia/en/e/e2/The_Green_Mile_%28movie_poster%29.jpg",
        "links": {
            "Apple TV": "https://tv.apple.com",
            "Kinopoisk": "https://www.kinopoisk.ru"
        }
    },
    {
        "title": "Начало",
        "description": "Фильм о снах внутри снов и манипуляциях сознанием.",
        "image": "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
        "links": {
            "Netflix": "https://www.netflix.com",
            "Kinopoisk": "https://www.kinopoisk.ru"
        }
    },
    {
        "title": "Матрица",
        "description": "Классическая научная фантастика о виртуальной реальности и борьбе за свободу.",
        "image": "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
        "links": {
            "Netflix": "https://www.netflix.com",
            "Kinopoisk": "https://www.kinopoisk.ru"
        }
    },
    {
        "title": "Форрест Гамп",
        "description": "Трогательная история о простом человеке, который меняет жизни окружающих.",
        "image": "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
        "links": {
            "Amazon": "https://www.amazon.com",
            "Kinopoisk": "https://www.kinopoisk.ru"
        }
    },
    {
        "title": "Темный рыцарь",
        "description": "Супергеройский фильм о Бэтмене и борьбе с хаосом в Готэм-сити.",
        "image": "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
        "links": {
            "Netflix": "https://www.netflix.com",
            "Kinopoisk": "https://www.kinopoisk.ru"
        }
    },
    {
        "title": "Дюна",
        "description": "Эпическая сага о борьбе за власть и выживание на пустынной планете Арракис.",
        "image": "https://upload.wikimedia.org/wikipedia/en/4/44/Dune_%282021_film%29.jpg",
        "links": {
            "Apple TV": "https://tv.apple.com",
            "Kinopoisk": "https://www.kinopoisk.ru"
        }
    },
    {
        "title": "Гладиатор",
        "description": "Эпический фильм о мести, чести и борьбе за свободу в Древнем Риме.",
        "image": "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
        "links": {
            "Amazon": "https://www.amazon.com",
            "Kinopoisk": "https://www.kinopoisk.ru"
        }
    },
    {
        "title": "Начало",
        "description": "Фильм о внедрении идей в чужие сны и психологических манипуляциях.",
        "image": "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
        "links": {
            "Netflix": "https://www.netflix.com",
            "Kinopoisk": "https://www.kinopoisk.ru"
        }
    },
    {
        "title": "Отступники",
        "description": "Драматический триллер о двойных агентах и борьбе с преступностью.",
        "image": "https://upload.wikimedia.org/wikipedia/en/5/50/Departed234.jpg",
        "links": {
            "Netflix": "https://www.netflix.com",
            "Kinopoisk": "https://www.kinopoisk.ru"
        }
    },
    {
        "title": "Остров проклятых",
        "description": "Детективный триллер о расследовании исчезновения на отдаленном острове.",
        "image": "https://upload.wikimedia.org/wikipedia/en/7/77/Shutter_Island_film_poster.jpg",
        "links": {
            "Amazon": "https://www.amazon.com",
            "Kinopoisk": "https://www.kinopoisk.ru"
        }
    },
    {
        "title": "Титаник",
        "description": "Эпическая романтическая драма о любви и трагедии на Титанике.",
        "image": "https://upload.wikimedia.org/wikipedia/en/2/2e/Titanic_poster.jpg",
        "links": {
            "Netflix": "https://www.netflix.com",
            "Kinopoisk": "https://www.kinopoisk.ru"
        }
    },
    {
        "title": "Властелин колец: Братство кольца",
        "description": "Фэнтезийная сага о борьбе добра и зла за могущественное кольцо.",
        "image": "https://upload.wikimedia.org/wikipedia/en/8/87/Ringstrilogyposter.jpg",
        "links": {
            "Amazon": "https://www.amazon.com",
            "Kinopoisk": "https://www.kinopoisk.ru"
        }
    },
    {
        "title": "Гарри Поттер и философский камень",
        "description": "Начало волшебного приключения Гарри Поттера в школе Хогвартс.",
        "image": "https://upload.wikimedia.org/wikipedia/en/6/6b/HP1_poster.jpg",
        "links": {
            "Netflix": "https://www.netflix.com",
            "Kinopoisk": "https://www.kinopoisk.ru"
        }
    }
]

def get_random_movie():
    return random.choice(MOVIES)
