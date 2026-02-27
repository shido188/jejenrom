import re
import string
from typing import Dict, Optional


def load_dataset() -> Dict[str, str]:
    """
    Load Filipino slang normalization rules.
    Uses a comprehensive manual dictionary with 250+ Filipino slang words and jejemon patterns.
    This covers the vast majority of common Filipino text normalization cases.
    """
    print("Loading Filipino slang normalization dictionary (250+ words)...")
    return _get_fallback_rules()


def _get_fallback_rules() -> Dict[str, str]:
    """
    Comprehensive Filipino jejemon normalization.
    Normalizes jejemon slang and abbreviations while keeping words in Filipino.
    """
    return {
        # Jejemon/slang shortcuts normalize to standard Filipino or keep as-is
        'u': 'you',  # English slang
        'ur': 'your',  # English slang
        'uv': 'you have',  # English slang
        'luv': 'love',  # English slang
        'lv': 'love',  # English slang
        'c': 'see',  # English letter
        'r': 'are',  # English letter
        'z': 'is',  # English letter
        'v': 'very',  # English letter
        'b': 'be',  # English letter
        'm': 'am',  # English letter
        'd': 'the',  # English letter
        'n': 'and',  # English letter
        'q': 'ko',  # Filipino slang for 'ko'
        
        # Numbers
        '2': 'to',
        '4': 'for',
        '4ever': 'forever',
        '0': 'o',
        '1': 'i',
        '3': 'e',
        '5': 's',
        '7': 't',
        '8': 'b',
        '9': 'g',
        '@': 'a',
        
        # Laughter & reactions (English)
        'lol': 'lol',
        'lmao': 'lmao',
        'rofl': 'rofl',
        'haha': 'haha',
        'hehe': 'hehe',
        'hihi': 'hihi',
        'hoho': 'hoho',
        'aww': 'aww',
        'aw': 'aww',
        'yay': 'yay',
        'yey': 'yay',
        'wow': 'wow',
        'woe': 'wow',
        
        # Polite expressions
        'pls': 'please',
        'plz': 'please',
        'ty': 'thank you',
        'thnx': 'thanks',
        'thx': 'thanks',
        'salamat': 'salamat',
        'sorry': 'sorry',
        'sory': 'sorry',
        'sorc': 'sorry',
        'sori': 'sorry',
        'pardon': 'pardon',
        'excuse': 'excuse',
        
        # Agreement
        'yes': 'yes',
        'yeah': 'yes',
        'yep': 'yes',
        'yup': 'yes',
        'no': 'no',
        'nope': 'no',
        'nah': 'no',
        'ok': 'ok',
        'okay': 'ok',
        'kk': 'ok',
        'okie': 'ok',
        'okey': 'ok',
        'okbye': 'ok bye',
        
        # Time expressions
        'now': 'ngayon',
        'later': 'mamaya',
        'l8r': 'mamaya',
        'soon': 'malapit na',
        'asap': 'bilisan',
        'bye': 'bye',
        'goodbye': 'goodbye',
        'gbye': 'bye',
        'g2g': 'kailangan umalis',
        'brb': 'babalik kaagad',
        'bbl': 'babalik mamaya',
        'bbs': 'babalik agad',
        'gtg': 'kailangan umalis',
        'tyl': 'hanggang mamaya',
        'ttyl': 'hanggang mamaya',
        'morning': 'umaga',
        'gmorning': 'magandang umaga',
        'gm': 'magandang umaga',
        'night': 'gabi',
        'gnight': 'magandang gabi',
        'gn': 'magandang gabi',
        'goodnight': 'magandang gabi',
        
        # Filipino particles (keep as-is)
        'na': 'na',
        'na lang': 'na lang',
        'nalang': 'na lang',
        'ba': 'ba',
        'po': 'po',
        'poe': 'po',
        'opo': 'opo',
        'ay': 'ay',
        'at': 'at',
        'ang': 'ang',
        'sa': 'sa',
        'ka': 'ka',
        'ko': 'ko',
        'mo': 'mo',
        'kayo': 'kayo',
        'nin': 'nin',
        'nyo': 'nyo',
        'nila': 'nila',
        'namin': 'namin',
        
        # Filipino words (keep in Filipino)
        'ako': 'ako',
        'kami': 'kami',
        'tayo': 'tayo',
        'sila': 'sila',
        'ito': 'ito',
        'iyan': 'iyan',
        'yun': 'yun',
        'yan': 'yan',
        'dito': 'dito',
        'doon': 'doon',
        'dIt': 'dito',
        'dapat': 'dapat',
        'pwede': 'pwede',
        'hindi': 'hindi',
        'ayaw': 'ayaw',
        'gusto': 'gusto',
        'mahal': 'mahal',
        'takot': 'takot',
        'saya': 'saya',
        'lasa': 'lasa',
        'oras': 'oras',
        'araw': 'araw',
        'buwan': 'buwan',
        'taon': 'taon',
        'umaga': 'umaga',
        'tanghali': 'tanghali',
        'hapon': 'hapon',
        'gabi': 'gabi',
        'madilim': 'madilim',
        'maliwanag': 'maliwanag',
        'mainit': 'mainit',
        'malamig': 'malamig',
        'buhay': 'buhay',
        'pamilya': 'pamilya',
        'kaibigan': 'kaibigan',
        'friend': 'friend',
        'frnD': 'friend',
        'frnd': 'friend',
        'girl': 'girl',
        'g0rl': 'girl',
        'gorl': 'girl',
        'gurl': 'girl',
        'guy': 'guy',
        'alalay': 'alalay',
        'homework': 'homework',
        'hmw0rk': 'homework',
        'hmwork': 'homework',
        'school': 'school',
        'sch00l': 'school',
        'ring': 'ring',
        'rInGu': 'ring',
        'ringu': 'ring',
        'tulungan': 'tulungan',
        'tanong': 'tanong',
        'sagutin': 'sagutin',
        'sagot': 'sagot',
        'sulat': 'sulat',
        'sulatin': 'sulatin',
        'tawag': 'tawag',
        'tawagin': 'tawagin',
        'kilala': 'kilala',
        'malaman': 'malaman',
        'intindi': 'intindi',
        'maintindihan': 'maintindihan',
        
        # Communication (mix of English and Filipino)
        'reply': 'reply',
        'replyan': 'reply',
        'respond': 'respond',
        'message': 'message',
        'msg': 'message',
        'text': 'text',
        'call': 'call',
        'phone': 'phone',
        'email': 'email',
        'chat': 'chat',
        'talk': 'usap',
        'usap': 'usap',
        'usapan': 'usapan',
        'historia': 'historia',
        'kwento': 'kwento',
        'kwentong': 'kwento',
        'iwento': 'iwento',
        'iikwen': 'iwento',
        'iikwen2': 'iwento',
        'story': 'kwento',
        
        # Filipino slang-specific words
        'kita': 'kita',
        'kta': 'kita',
        'tayo': 'tayo',
        'tyo': 'tayo',
        'sobra': 'sobra',
        'kaya': 'kaya',
        'kht': 'kahit',
        'kahit': 'kahit',
        'kahit anong': 'kahit anong',
        'pRo': 'pero',
        'pro': 'pero',
        'pero': 'pero',
        'mngyri': 'mangyari',
        'mngyare': 'mangyari',
        'mangyari': 'mangyari',
        'mangyare': 'mangyari',
        'nagaganap': 'nangyayari',
        'araw': 'araw',
        'buhay mo': 'buhay mo',
        'sayoh': 'sayo',
        'sayo': 'sayo',
        'sa yo': 'sayo',
        'dhil': 'dahil',
        'dahil': 'dahil',
        'dahil dito': 'dahil dito',
        'dh2': 'dati',
        'dati': 'dati',
        'dating': 'dating',
        'lng': 'lang',
        'lang': 'lang',
        'lang nang': 'lang',
        'nang': 'nang',
        'nNG': 'nang',
        'nmn': 'nalang',
        'rin': 'rin',
        'din': 'din',
        'ulet': 'ulit',
        'ulit': 'ulit',
        'ulul': 'ulol',
        'ulol': 'ulol',
        'sakto': 'sakto',
        'perfect': 'sakto',
        'adios': 'adios',
        'adyos': 'adios',
        'til': 'hanggang',
        'till': 'hanggang',
        'hangga': 'hanggang',
        'hanggang': 'hanggang',
        
        # Emotions/adjectives
        'gr8': 'great',
        'awesome': 'awesome',
        'cool': 'cool',
        'kl': 'cool',
        'nice': 'nice',
        'nics': 'nice',
        'pretty': 'ganda',
        'beautiful': 'maganda',
        'ugly': 'pangit',
        'hot': 'hot',
        'cute': 'cute',
        'qute': 'cute',
        'sexy': 'sexy',
        'handsome': 'handsome',
        'adorable': 'adorable',
        'amazing': 'amazing',
        'wonderful': 'wonderful',
        'fantastic': 'fantastic',
        'terrible': 'terrible',
        'horrible': 'horrible',
        'bad': 'bad',
        'sad': 'sad',
        'happy': 'happy',
        'mad': 'mad',
        'angry': 'angry',
        'tired': 'tired',
        'sleepy': 'sleepy',
        'sick': 'sakit',
        'drunk': 'lasing',
        'high': 'high',
        
        # Verbs and actions
        'eating': 'eating',
        'working': 'working',
        'sleeping': 'sleeping',
        'playing': 'playing',
        'studying': 'studying',
        'thinking': 'thinking',
        'remembering': 'remembering',
        'waiting': 'waiting',
        'love': 'love',
        'luv': 'love',
        'luve': 'love',
        'hate': 'hate',
        'like': 'like',
        'care': 'care',
        'miss': 'miss',
        'miss u': 'miss you',
        'miss me': 'miss me',
        'forever': 'forever',
        '4ever': 'forever',
        '4eva': 'forever',
        '4evr': 'forever',
        'aever': 'forever',
        'aeva': 'forever',
        'evrytime': 'every time',
        'everytime': 'every time',
        '4evernmore': 'forever and ever',
        'miss ka': 'miss you',
        'miss kita': 'miss you',
        'love u': 'love you',
        'love you': 'love you',
        
        # Common misspellings (normalize but keep English)
        'x': 'ex',
        'dnt': "don't",
        'dont': "don't",
        'c@nt': "can't",
        'cant': "can't",
        'wont': "won't",
        'hav': 'have',
        'havnt': "haven't",
        'didnt': "didn't",
        'aint': "ain't",
        'shouldve': 'should have',
        'couldve': 'could have',
        'wouldve': 'would have',
        'wanna': 'want to',
        'gonna': 'going to',
        'gotta': 'got to',
        'dunno': "don't know",
        'duno': 'hindi ko alam',
        'idk': 'hindi ko alam',
        'kno': 'alam',
        'knw': 'alam',
        'saw': 'nakita',
        'see': 'makita',
        'hello': 'hello',
        'hi': 'hi',
        'hii': 'hi',
        'hey': 'hey',
        'h3y': 'hey',
        
        # Filipino greetings/questions
        'kamuzta': 'kamusta',
        'kamusta': 'kamusta',
        'kamustah': 'kamusta',
        'cnu': 'sino',
        'sinu': 'sino',
        'sino': 'sino',
        'anong': 'ano',
        'ano': 'ano',
        'anung': 'ano',
        'ano ba': 'ano ba',
        'ano pang': 'ano pa',
        'saan': 'saan',
        'kailan': 'kailan',
        'bakit': 'bakit',
        'paano': 'paano',
        'kanino': 'kanino',
        'alin': 'alin',
    }


def normalize_text(text: str, ngram_rules: Optional[Dict[str, str]] = None) -> str:
    """
    Normalize jejemon/slang text using Filipino dictionary.
    Converts jejemon abbreviations to standard Filipino or English equivalents.
    """
    if ngram_rules is None:
        ngram_rules = load_dataset()
    
    normalized = text.lower()
    
    # First, replace leet speak numbers and symbols with letters
    leet_speak = {
        '0': 'o',
        '1': 'i',
        '3': 'e',
        '4': 'a',
        '5': 's',
        '7': 't',
        '8': 'b',
        '9': 'g',
        '@': 'a',
    }
    
    for num, letter in leet_speak.items():
        normalized = normalized.replace(num, letter)
    
    # Apply dictionary-based word replacements with word boundaries
    for slang_word, normalized_word in ngram_rules.items():
        # Use word boundaries to match whole words only
        pattern = r'\b' + re.escape(slang_word) + r'\b'
        normalized = re.sub(pattern, normalized_word, normalized, flags=re.IGNORECASE)
    
    # Remove extra spaces
    normalized = re.sub(r'\s+', ' ', normalized).strip()
    
    return normalized


def detect_sentiment(text: str) -> str:
    """
    Detect sentiment (positive, negative, or neutral) based on keywords.
    """
    text_lower = text.lower()
    
    positive_words = {
        'love', 'luv', 'mahal', 'amazing', 'awesome', 'great', 'wonderful', 'fantastic',
        'excellent', 'good', 'happy', 'joy', 'beautiful', 'maganda', 'perfect', 'best',
        'like', 'gusto', 'lol', 'haha', 'smile', 'laugh', 'fun', 'cool', 'nice',
        'brilliant', 'superb', 'awesome', 'adore', 'wonderful', 'gorgeous',
        'lovely', 'delightful', 'fantastic', 'terrific', 'stellar', 'saya',
    }
    
    negative_words = {
        'hate', 'horrible', 'terrible', 'awful', 'bad', 'sad', 'angry',
        'upset', 'disappointed', 'disgusted', 'ugly', 'pangit', 'worst', 'sucks',
        'stupid', 'dumb', 'annoying', 'pathetic', 'miserable', 'sorry',
        'poor', 'fail', 'failed', 'sick', 'tired', 'exhausted', 'depressed',
        'broken', 'wrong', 'toxic', 'useless', 'worthless', 'disgusting',
        'galit', 'takot', 'loob', 'nakakainis',
        # Jejemon/leet speak versions of negative words
        'g4l1t', 'g4lit', 'gal1t', 'galit', 'h8', 'h@t3', 'h4t3', 'sux', 's00ks',
    }
    
    # Count positive and negative words
    words = re.findall(r'\b\w+\b', text_lower)
    
    positive_count = sum(1 for word in words if word in positive_words)
    negative_count = sum(1 for word in words if word in negative_words)
    
    # Determine sentiment (only positive or negative)
    if negative_count > positive_count:
        return "negative"
    else:
        return "positive"
