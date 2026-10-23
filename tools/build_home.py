"""Builds the home pages of pagelex.app from one template.

Run from the repository root: python3 tools/build_home.py .

Builds every language in T: en, uk, es, de. Spanish and German texts are AI-translated from English.

Demo: each language has its own book page and English word (page, word, pos, gloss, tr, caption).
Pick a word whose everyday meaning readers of that language know, used in another meaning in a
public-domain book; it doesn't have to be the same word for every language.

Copy rule: describe what the reader feels and gets, not how the app works. Don't name
algorithms, review modes, thresholds, word lists or AI models.
"""
import sys
from pathlib import Path

ROOT = Path(sys.argv[1])
SITE = "https://pagelex.app"

# Public domain: Lewis Carroll, "Alice's Adventures in Wonderland" (1865), chapter 1.
ALICE_PAGE = (
    '<p>Alice was <span class="w mastered">beginning</span> to get very tired of sitting by her sister on the '
    '<span class="w new tapped">bank</span>, and of having nothing to do: once or twice she had '
    '<span class="w new">peeped</span> into the book her sister was reading, but it had no pictures or '
    '<span class="w learning">conversations</span> in it, “and what is the use of a book,” thought Alice '
    '“without pictures or conversations?”</p>'
    '<p>So she was <span class="w learning">considering</span> in her own mind (as well as she could, for the hot '
    'day made her feel very sleepy and stupid), whether the pleasure of making a '
    '<span class="w new">daisy</span>-chain would be <span class="w mastered">worth</span> the trouble of getting up '
    'and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.</p>'
)

T = {
    "en": dict(
        path="/", name="English", short="EN",
        title="PageLex: read paper books in English and watch the words light up",
        desc="Snap a page of a paper book in English and watch the words light up: the ones you know, the ones you're learning and the new ones. Tap for the meaning the author meant. iPhone app, coming 2027.",
        eyebrow="For readers learning English",
        h1="Read paper books in English. Watch the words light up.",
        lead="Snap a page, and PageLex shows what you know, what you're learning and what's new, right on the page. One tap gives you the meaning the author meant, in your language.",
        badge_small="Coming to the", badge="App Store · 2027", note="iPhone · iOS 27",
        demo_label="Example: a book page with colored words and the card for the tapped word",
        page=ALICE_PAGE, word="bank", pos="noun", gloss="Here: the side of a river, not a place for money.",
        tr="orilla", tr_lang="Spanish",
        caption="Everyone knows “bank” as a place for money. Here Alice sits on the bank of a river, and PageLex knows the difference.",
        magic_h="Reading, with a little magic",
        magic=[
            ("Your page lights up", "Snap a page and watch it change: new words, words you're learning, words you've mastered. Everything else is already yours."),
            ("The meaning the author meant", "Tap a word and get the translation that fits this very sentence, not a long dictionary list."),
            ("Words that stay with you", "Every word you tap comes back at just the right moment, with the sentence from your book, until it's truly yours."),
        ],
        legend=[("new", "New"), ("learning", "Learning"), ("mastered", "Mastered"), ("", "Known: no color")],
        daily_h="A few minutes a day",
        daily_lead="PageLex reminds you when it's time, so new words don't slip away. Short reviews, always with the sentence where you met the word.",
        progress_h="Watch your progress, on paper",
        progress_lead="Every page tells you how much of it you understood. Page by page, fewer words light up, because now you know them.",
        priv_h="Everything stays on your iPhone",
        priv_lead="Many apps send your photos to the cloud. PageLex doesn't.",
        priv=[
            ("No account", "No sign-up and no sign-in. Open the app and scan."),
            ("No analytics", "Not in the app, not on this website, and no cookies."),
            ("Works offline", "Read and review anywhere, even on a plane, once your language is downloaded."),
            ("Photos stay with you", "Page photos never leave your iPhone and are deleted after each scan."),
        ],
        faq_h="Questions",
        faq=[
            ("Which iPhones?", "Any iPhone with iOS 27."),
            ("Which languages?", "You read in English. Translations come in about 20 languages, including Ukrainian, Spanish and German. The app itself is in English."),
            ("Ebooks too?", "PageLex is made for paper books, but a screenshot of an ebook page works too."),
            ("How much does it cost?", "PageLex is a subscription with a free trial. Prices will be in the App Store at launch."),
            ("When can I try it?", "PageLex comes to the App Store in 2027. Follow us on Instagram or YouTube to hear first."),
        ],
        support="Support", follow="Follow",
    ),
    "uk": dict(
        path="/uk/", name="Українська", short="UA",
        title="PageLex: читайте паперові книжки англійською, і слова засвітяться",
        desc="Сфотографуйте сторінку паперової книжки англійською, і слова засвітяться: ті, що ви знаєте, ті, що вчите, і нові. Торкніться слова, щоб отримати значення, яке мав на увазі автор. Застосунок для iPhone, з'явиться у 2027 році.",
        eyebrow="Для тих, хто читає англійською й вивчає мову",
        h1="Читайте паперові книжки англійською. Слова засвітяться самі.",
        lead="Сфотографуйте сторінку, і PageLex покаже прямо на ній, що ви вже знаєте, що вчите і що бачите вперше. Один дотик дає значення, яке мав на увазі автор, вашою мовою.",
        badge_small="Незабаром в", badge="App Store · 2027", note="iPhone · iOS 27",
        demo_label="Приклад: сторінка книжки з кольоровими словами і картка слова, якого торкнулися",
        page=ALICE_PAGE, word="bank", pos="noun", gloss="Here: the side of a river, not a place for money.",
        tr="берег", tr_lang="українська",
        caption="Усі знають «bank» як банк. Але тут Аліса сидить на березі річки, і PageLex це розуміє.",
        magic_h="Читання з дрібкою магії",
        magic=[
            ("Сторінка оживає", "Сфотографуйте сторінку й подивіться, як вона змінюється: нові слова, слова, які ви вчите, і вже засвоєні. Усе інше ви вже знаєте."),
            ("Значення, яке мав на увазі автор", "Торкніться слова й отримайте переклад саме для цього речення, а не довгий список зі словника."),
            ("Слова, що залишаються з вами", "Кожне слово, якого ви торкнулися, повертається саме тоді, коли треба, разом із реченням з вашої книжки, доки не стане вашим."),
        ],
        legend=[("new", "Нове"), ("learning", "Вчу"), ("mastered", "Засвоєне"), ("", "Відоме: без кольору")],
        daily_h="Кілька хвилин на день",
        daily_lead="PageLex нагадає, коли час повторити, щоб нові слова не вислизали. Короткі повторення, завжди з реченням, де ви зустріли слово.",
        progress_h="Прогрес видно на папері",
        progress_lead="Кожна сторінка покаже, скільки ви з неї зрозуміли. Сторінка за сторінкою кольорових слів меншає, бо тепер ви їх знаєте.",
        priv_h="Усе залишається на вашому iPhone",
        priv_lead="Багато застосунків відправляють ваші фото в хмару. PageLex — ні.",
        priv=[
            ("Без акаунта", "Без реєстрації та входу. Відкрийте застосунок і скануйте."),
            ("Без аналітики", "Ні в застосунку, ні на цьому сайті, і жодних cookies."),
            ("Працює офлайн", "Читайте й повторюйте будь-де, навіть у літаку, коли мову завантажено."),
            ("Фото залишаються з вами", "Фото сторінок ніколи не залишають ваш iPhone і видаляються після кожного сканування."),
        ],
        faq_h="Питання",
        faq=[
            ("На яких iPhone працює?", "На будь-якому iPhone з iOS 27."),
            ("Які мови?", "Ви читаєте англійською. Переклад є приблизно 20 мовами, серед них українська, іспанська й німецька. Сам застосунок англійською."),
            ("А електронні книжки?", "PageLex створений для паперових книжок, але скриншот сторінки електронної книжки теж підійде."),
            ("Скільки коштує?", "PageLex працює за підпискою з безкоштовним пробним періодом. Ціни будуть в App Store на старті."),
            ("Коли можна спробувати?", "PageLex з'явиться в App Store у 2027 році. Стежте за нами в Instagram або YouTube, щоб дізнатися першими."),
        ],
        support="Підтримка", follow="Ми в мережі",
    ),
}

PP_WORDS = {
    "universally": "learning", "acknowledged": "mastered", "single": "new", "possession": "learning",
    "fortune": "new", "want": "learning", "neighbourhood": "mastered", "rightful": "new", "property": "mastered",
}


def pp_page(tapped):
    """Public domain: Jane Austen, "Pride and Prejudice" (1813), chapter 1. `tapped` gets the tap outline."""
    def w(word):
        cls = PP_WORDS[word] + (" tapped" if word == tapped else "")
        return f'<span class="w {cls}">{word}</span>'
    return (
        f'<p>It is a truth {w("universally")} {w("acknowledged")}, that a {w("single")} man in '
        f'{w("possession")} of a good {w("fortune")}, must be in {w("want")} of a wife.</p>'
        f'<p>However little known the feelings or views of such a man may be on his first entering a '
        f'{w("neighbourhood")}, this truth is so well fixed in the minds of the surrounding families, that he '
        f'is considered the {w("rightful")} {w("property")} of some one or other of their daughters.</p>'
    )


T["es"] = dict(
    path="/es/", name="Español", short="ES",
    title="PageLex: lee libros en papel en inglés y mira cómo se iluminan las palabras",
    desc="Haz una foto de una página de un libro en inglés y mira cómo se iluminan las palabras: las que conoces, las que estás aprendiendo y las nuevas. Toca una para ver el significado que quiso el autor. App para iPhone, llega en 2027.",
    eyebrow="Para quien lee en inglés y aprende el idioma",
    h1="Lee libros en papel en inglés. Mira cómo se iluminan las palabras.",
    lead="Haz una foto de la página y PageLex te muestra, sobre la misma página, lo que ya sabes, lo que estás aprendiendo y lo nuevo. Un toque te da el significado que quiso el autor, en tu idioma.",
    badge_small="Llega al", badge="App Store · 2027", note="iPhone · iOS 27",
    demo_label="Ejemplo: una página de libro con palabras de colores y la ficha de la palabra tocada",
    page=pp_page("single"), word="single", pos="adjective", gloss="Here: not married, not “only one”.",
    tr="soltero", tr_lang="español",
    caption="Todos conocen «single» como «único». Aquí significa «soltero», y PageLex lo entiende.",
    magic_h="Leer, con un poco de magia",
    magic=[
        ("La página se ilumina", "Haz una foto y mira cómo cambia: palabras nuevas, palabras que estás aprendiendo y palabras que ya dominas. Todo lo demás ya es tuyo."),
        ("El significado que quiso el autor", "Toca una palabra y obtén la traducción que encaja en esta misma frase, no una larga lista de diccionario."),
        ("Palabras que se quedan contigo", "Cada palabra que tocas vuelve justo en el momento adecuado, con la frase de tu libro, hasta que es tuya de verdad."),
    ],
    legend=[("new", "Nueva"), ("learning", "Aprendiendo"), ("mastered", "Dominada"), ("", "Conocida: sin color")],
    daily_h="Unos minutos al día",
    daily_lead="PageLex te avisa cuando toca repasar, para que las palabras nuevas no se escapen. Repasos cortos, siempre con la frase donde encontraste la palabra.",
    progress_h="Tu progreso, sobre el papel",
    progress_lead="Cada página te dice cuánto entendiste. Página a página se iluminan menos palabras, porque ahora ya las conoces.",
    priv_h="Todo se queda en tu iPhone",
    priv_lead="Muchas apps envían tus fotos a la nube. PageLex no.",
    priv=[
        ("Sin cuenta", "Sin registro ni inicio de sesión. Abre la app y escanea."),
        ("Sin analítica", "Ni en la app ni en esta web, y sin cookies."),
        ("Funciona sin conexión", "Lee y repasa donde quieras, incluso en un avión, una vez descargado tu idioma."),
        ("Las fotos se quedan contigo", "Las fotos de las páginas nunca salen de tu iPhone y se borran tras cada escaneo."),
    ],
    faq_h="Preguntas",
    faq=[
        ("¿En qué iPhone funciona?", "En cualquier iPhone con iOS 27."),
        ("¿Qué idiomas?", "Lees en inglés. Las traducciones llegan en unos 20 idiomas, entre ellos español, alemán y ucraniano. La app está en inglés."),
        ("¿También ebooks?", "PageLex está pensada para libros en papel, pero una captura de pantalla de un ebook también funciona."),
        ("¿Cuánto cuesta?", "PageLex es una suscripción con prueba gratuita. Los precios estarán en el App Store en el lanzamiento."),
        ("¿Cuándo puedo probarla?", "PageLex llega al App Store en 2027. Síguenos en Instagram o YouTube para enterarte primero."),
    ],
    support="Soporte", follow="Síguenos",
)

T["de"] = dict(
    path="/de/", name="Deutsch", short="DE",
    title="PageLex: lies gedruckte Bücher auf Englisch und sieh die Wörter aufleuchten",
    desc="Fotografiere eine Seite eines englischen Buchs und sieh zu, wie die Wörter aufleuchten: die bekannten, die, die du gerade lernst, und die neuen. Tippe ein Wort an für die Bedeutung, die der Autor meinte. iPhone-App, kommt 2027.",
    eyebrow="Für alle, die auf Englisch lesen und die Sprache lernen",
    h1="Lies gedruckte Bücher auf Englisch. Sieh die Wörter aufleuchten.",
    lead="Fotografiere eine Seite, und PageLex zeigt dir direkt darauf, was du schon kennst, was du gerade lernst und was neu ist. Ein Tippen gibt dir die Bedeutung, die der Autor meinte, in deiner Sprache.",
    badge_small="Bald im", badge="App Store · 2027", note="iPhone · iOS 27",
    demo_label="Beispiel: eine Buchseite mit farbigen Wörtern und der Karte zum angetippten Wort",
    page=pp_page("fortune"), word="fortune", pos="noun", gloss="Here: a lot of money, not luck.",
    tr="Vermögen", tr_lang="Deutsch",
    caption="„Fortune“ klingt nach Glück. Hier ist es ein großes Vermögen, und PageLex versteht das.",
    magic_h="Lesen, mit ein bisschen Magie",
    magic=[
        ("Deine Seite leuchtet auf", "Fotografiere eine Seite und sieh zu, wie sie sich verändert: neue Wörter, Wörter, die du lernst, und Wörter, die du sicher kannst. Alles andere kennst du schon."),
        ("Die Bedeutung, die der Autor meinte", "Tippe ein Wort an und erhalte die Übersetzung, die genau zu diesem Satz passt, keine lange Wörterbuchliste."),
        ("Wörter, die bleiben", "Jedes angetippte Wort kommt genau im richtigen Moment zurück, mit dem Satz aus deinem Buch, bis es wirklich dir gehört."),
    ],
    legend=[("new", "Neu"), ("learning", "Lernen"), ("mastered", "Sicher"), ("", "Bekannt: ohne Farbe")],
    daily_h="Ein paar Minuten am Tag",
    daily_lead="PageLex erinnert dich, wenn es Zeit ist, damit dir neue Wörter nicht entwischen. Kurze Wiederholungen, immer mit dem Satz, in dem du das Wort getroffen hast.",
    progress_h="Dein Fortschritt, auf Papier",
    progress_lead="Jede Seite zeigt dir, wie viel du verstanden hast. Seite für Seite leuchten weniger Wörter auf, weil du sie jetzt kennst.",
    priv_h="Alles bleibt auf deinem iPhone",
    priv_lead="Viele Apps schicken deine Fotos in die Cloud. PageLex nicht.",
    priv=[
        ("Kein Konto", "Keine Registrierung, keine Anmeldung. App öffnen und scannen."),
        ("Keine Analyse", "Weder in der App noch auf dieser Website, und keine Cookies."),
        ("Funktioniert offline", "Lies und wiederhole überall, sogar im Flugzeug, sobald deine Sprache geladen ist."),
        ("Fotos bleiben bei dir", "Seitenfotos verlassen nie dein iPhone und werden nach jedem Scan gelöscht."),
    ],
    faq_h="Fragen",
    faq=[
        ("Auf welchen iPhones?", "Auf jedem iPhone mit iOS 27."),
        ("Welche Sprachen?", "Du liest auf Englisch. Übersetzungen gibt es in etwa 20 Sprachen, darunter Deutsch, Spanisch und Ukrainisch. Die App selbst ist auf Englisch."),
        ("Auch E-Books?", "PageLex ist für gedruckte Bücher gemacht, aber ein Screenshot einer E-Book-Seite funktioniert auch."),
        ("Was kostet es?", "PageLex ist ein Abo mit kostenlosem Testzeitraum. Die Preise stehen zum Start im App Store."),
        ("Wann kann ich es ausprobieren?", "PageLex kommt 2027 in den App Store. Folge uns auf Instagram oder YouTube, um es als Erste zu erfahren."),
    ],
    support="Support", follow="Folgen",
)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def page(code):
    t = T[code]
    path = t["path"]
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{c}" href="{SITE}{v["path"]}">' for c, v in T.items()
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{SITE}/">'
    langs = "\n".join(
        f'      <li><a href="{v["path"]}" lang="{c}" hreflang="{c}" title="{v["name"]}"'
        + (' aria-current="page"' if c == code else "")
        + f'>{v["short"]}</a></li>'
        for c, v in T.items()
    )
    magic = "\n".join(
        f'      <li class="tile"><h3>{esc(h)}</h3><p>{esc(p)}</p></li>' for h, p in t["magic"]
    )
    legend = "\n".join(
        (f'      <li><span class="w {cls}">{esc(lbl)}</span></li>' if cls else f"      <li>{esc(lbl)}</li>")
        for cls, lbl in t["legend"]
    )
    priv = "\n".join(f'      <li class="tile"><h3>{esc(h)}</h3><p>{esc(p)}</p></li>' for h, p in t["priv"])
    faq = "\n".join(f"      <details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in t["faq"])
    return f"""<!doctype html>
<html lang="{code}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t["title"])}</title>
<meta name="description" content="{esc(t["desc"])}">
<link rel="canonical" href="{SITE}{path}">
{alternates}
<meta property="og:type" content="website">
<meta property="og:site_name" content="PageLex">
<meta property="og:title" content="{esc(t["title"])}">
<meta property="og:description" content="{esc(t["desc"])}">
<meta property="og:url" content="{SITE}{path}">
<meta name="theme-color" content="#fbfaf7" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#111214" media="(prefers-color-scheme: dark)">
<link rel="icon" href="/assets/icon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{path}"><img src="/assets/icon.svg" alt="" width="32" height="32">PageLex</a>
    <ul class="lang" aria-label="Language">
{langs}
    </ul>
  </div>
</header>

<main>
<div class="hero">
  <div class="wrap">
    <div>
      <p class="eyebrow">{esc(t["eyebrow"])}</p>
      <h1>{esc(t["h1"])}</h1>
      <p class="lead">{esc(t["lead"])}</p>
      <div class="cta">
        <span class="store-badge" role="note"><small>{esc(t["badge_small"])}</small><strong>{esc(t["badge"])}</strong></span>
        <span class="note">{esc(t["note"])}</span>
      </div>
    </div>
    <figure class="demo" aria-label="{esc(t["demo_label"])}">
      <div class="paper" lang="en">
        {t["page"]}
      </div>
      <div class="card" aria-hidden="true">
        <div class="head"><span class="word" lang="en">{esc(t["word"])}</span><span class="pos" lang="en">{esc(t["pos"])}</span></div>
        <p class="tr">{esc(t["tr"])}<span>{esc(t["tr_lang"])}</span></p>
        <p class="why" lang="en">{esc(t["gloss"])}</p>
      </div>
      <figcaption>{esc(t["caption"])}</figcaption>
    </figure>
  </div>
</div>

<section id="magic">
  <div class="wrap">
    <h2>{esc(t["magic_h"])}</h2>
    <ul class="grid three">
{magic}
    </ul>
    <ul class="legend">
{legend}
    </ul>
  </div>
</section>

<section id="daily">
  <div class="wrap feature">
    <div>
      <h2>{esc(t["daily_h"])}</h2>
      <p class="section-lead">{esc(t["daily_lead"])}</p>
    </div>
    <div aria-hidden="true" lang="en">
      <div class="notif"><img src="/assets/icon.svg" alt=""><div><div class="top"><strong>PageLex</strong><span>now</span></div><p>12 words waiting, 4 from Alice in Wonderland</p></div></div>
      <div class="notif"><img src="/assets/icon.svg" alt=""><div><div class="top"><strong>PageLex</strong><span>yesterday</span></div><p>8 words waiting, 3 from Sherlock Holmes</p></div></div>
    </div>
  </div>
</section>

<section id="progress">
  <div class="wrap feature flip">
    <div>
      <h2>{esc(t["progress_h"])}</h2>
      <p class="section-lead">{esc(t["progress_lead"])}</p>
    </div>
    <div class="mock score" aria-hidden="true" lang="en">
      <p class="label">Page score</p>
      <p class="big">96%</p>
      <p class="sub">You knew 96% of this page</p>
      <div class="bar"><span></span><span></span><span></span></div>
    </div>
  </div>
</section>

<section id="privacy">
  <div class="wrap">
    <h2>{esc(t["priv_h"])}</h2>
    <p class="section-lead">{esc(t["priv_lead"])}</p>
    <ul class="grid four">
{priv}
    </ul>
  </div>
</section>

<section id="faq">
  <div class="wrap faq">
    <h2>{esc(t["faq_h"])}</h2>
{faq}
  </div>
</section>
</main>

<footer class="site-footer">
  <div class="wrap">
    <ul>
      <li><a href="/support/">{esc(t["support"])}</a></li>
      <li><a href="mailto:support@pagelex.app">support@pagelex.app</a></li>
    </ul>
    <ul aria-label="{esc(t["follow"])}">
      <li><a href="https://www.instagram.com/pagelex.app/" rel="me">Instagram</a></li>
      <li><a href="https://www.youtube.com/@pagelex" rel="me">YouTube</a></li>
      <li>© 2026 PageLex</li>
    </ul>
  </div>
</footer>
</body>
</html>
"""


for code, v in T.items():
    out = ROOT / "index.html" if v["path"] == "/" else ROOT / v["path"].strip("/") / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(code), encoding="utf-8")
    print("wrote", out)
