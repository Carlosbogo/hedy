import hedy
from test_level_01 import HedyTester
import hedy_translation


def check_local_lang_bool(func):
    def inner(self):
        if not hedy.local_keywords_enabled:
            return

        return func(self)

    return inner


    # tests should be ordered as follows:
    # * Translation from English to Dutch
    # * Translation from Dutch to English
    # * Translation to several languages
    # * Error handling


class TestsTranslationLevel6(HedyTester):
    level = 6
    keywords_from = hedy_translation.keywords_to_dict('en')
    keywords_to = hedy_translation.keywords_to_dict('nl')

    @check_local_lang_bool
    def test_repeat_english_dutch(self):
        code = "repeat 3 times print 'Hedy is fun!'"

        result = hedy_translation.translate_keywords(code, from_lang="en", to_lang="nl", level=self.level)
        expected = "herhaal 3 keer print 'Hedy is fun!'"

        self.assertEqual(result, expected)


    @check_local_lang_bool
    def test_repeat_dutch_english(self):
        code = "herhaal 3 keer print 'Hedy is fun!'"

        result = hedy_translation.translate_keywords(code, from_lang="nl", to_lang="en", level=self.level)
        expected = "repeat 3 times print 'Hedy is fun!'"

        self.assertEqual(result, expected)


    @check_local_lang_bool
    def test_translate_back(self):
        code ="print 'Hallo welkom bij Hedy' 5 + 7"

        result = hedy_translation.translate_keywords(code, from_lang="en", to_lang="nl", level=self.level)
        result = hedy_translation.translate_keywords(result, from_lang="nl", to_lang="en", level=self.level)

        self.assertEqual(code, result)


    @check_local_lang_bool
    def test_invalid(self):
        code = "hallo"

        result = hedy_translation.translate_keywords(code, from_lang="en", to_lang="nl", level=self.level)
        expected = "hallo"

        self.assertEqual(result, expected)

    @check_local_lang_bool
    def no_argument_ask(self):
        code = "ask"

        result = hedy_translation.translate_keywords(code, from_lang="en", to_lang="nl", level=self.level)
        expected = "ask"

        self.assertEqual(result, expected)