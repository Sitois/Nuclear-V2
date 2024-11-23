"""
The MIT License (MIT)

Copyright (c) 2024-present Lenochxd

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

# NOTE: Language system made by Lenochxd, check her github(https://github.com/Lenochxd) !

import config_selfbot

import os

class Lang():
    def __init__(self,
                 path: str = r"./translations",
                 misc_lang_files_dir: str = r"./translations/misc",
                 default_language: str = "en_US"):
        self.path: str = path
        self.misc_lang_files_dir: str = misc_lang_files_dir
        if not os.path.exists(self.path):
            raise KeyError("No LANG path were given or given path doesn't exists.")
        self.misc_lang_files_dir: str = misc_lang_files_dir
        if not os.path.exists(self.misc_lang_files_dir):
            print("WARNING: No MISC path were given or given path doesn't exists.")
        self.default_language: str = default_language
        self.load_all_lang_files()
        self.lang_files: dict = {}
        self.languages_info: list = self.get_languages_info(self.lang_files)
        self.set_default_language(self.default_language)
        self.reload_all_lang_files()

    def load_lang_file(self, lang) -> dict:
        lang_dictionary = {}
        lang_path = f"{self.path}/{lang}.lang"

        if not os.path.isfile(lang_path):
            lang_path = f"{self.misc_lang_files_dir}/{lang}.lang"

        if not os.path.isfile(lang_path):
            for root, dirs, files in os.walk(self.path):
                for file in files:
                    if file.endswith(".lang") and file.startswith(lang):
                        lang_path = os.path.join(self.path, file)
                        break
                if lang_path != os.path.join(self.path, f"{lang}.lang"):
                    break

        with open(lang_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith(("//", "#")):
                    try:
                        key, value = line.split("=", 1)
                        lang_dictionary[key.strip()] = value.strip()
                    except ValueError as e:
                        raise ValueError(f'Invalid line format: {line}') from e

        return lang_dictionary


    def get_language(self, lang=None) -> str:
        if lang is None:
            lang = self.default_language

        for available_lang in self.lang_files:
            if available_lang.lower().startswith(lang.lower()):
                return available_lang
        
        return self.default_language

    def language_exists(self, lang=None) -> bool:
        return self.get_language(lang) in self.lang_files

    def set_default_language(self, lang: str) -> None:
        if self.language_exists(lang):
            self.default_language = lang
        else:
            raise ValueError(f"Language '{lang}' does not exist. Default language remains '{self.default_language}'.")

    def load_all_lang_files(self) -> dict:
        self.lang_files = {}
        for file in os.listdir(self.path):
            if file.endswith(".lang"):
                lang = file.split(".")[0]
                self.lang_files[lang] = self.load_lang_file(lang)
                self.lang_files[lang]['misc'] = False

        if self.misc_lang_files_dir and os.path.isdir(self.misc_lang_files_dir):
            for file in os.listdir(self.misc_lang_files_dir):
                if file.endswith(".lang"):
                    lang = file.split(".")[0]
                    if lang not in self.lang_files:
                        self.lang_files[lang] = self.load_lang_file(lang)
                    self.lang_files[lang]['misc'] = True
        return self.lang_files

    def reload_all_lang_files(self) -> None:
        self.lang_files = self.load_all_lang_files()
        
    def get_languages_info(self, lang_files) -> list:
        if not self.lang_files:
            self.lang_files = self.load_all_lang_files()
        
        languages_info = []
        for lang, lang_data in self.lang_files.items():
            languages_info.append({
                'code': lang,
                'code_short': lang_data['lang_code'],
                'native_name': lang_data['native_name'],
                'english_name': lang_data['english_name'],
                'author_name': lang_data['author_name'],
                'author_github_username': lang_data['author_github_username'],
                'misc': lang_data.get('misc', False),
            })
        
        return languages_info

    def text(self, text: str = None, lang: str = None) -> str:
        """Returns the given text in the given language.

        Parameters
        ----------
        text: :class:`str`
            The text to get in the given language.
        lang: :class:`str`
            The language to get the text into.

            Default to the default language.

        Raises
        ------
        KeyError
            Given text wasn't found on both default language and given language.

        Returns
        -------
        :class:`str`
            The translated text.
        """
        lang = self.get_language(lang or self.default_language)

        if text is None:
            return ""

        if lang not in self.lang_files:
            raise KeyError("Given text wasn't found on both default language and given language.")

        return self.lang_files[lang].get(text, text).replace(
            '\\n', '\n').replace(
            '\\r', '\r').replace(
                '%prefix%', config_selfbot.prefix)

    def t(self, text: str = None, lang: str = None) -> str:
        """Returns the given text in the given language.

        Shortcut for Lang().text()

        Parameters
        ----------
        text: :class:`str`
            The text to get in the given language.
        lang: :class:`str`
            The language to get the text into.

            Default to the default language.

        Raises
        ------
        KeyError
            Given text wasn't found on both default language and given language.

        Returns
        -------
        :class:`str`
            The translated text.
        """

        return self.text(text, lang)

try:
    lang = Lang(default_language="en_US",
           path=r".\translations")
except Exception:
    lang = Lang(default_language="en_US",
           path=r"..\translations")