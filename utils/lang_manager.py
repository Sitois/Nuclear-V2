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
    """Constructor.

    Parameters
    ----------
    path: :class:`str`
        The path of the folder containing .lang translations.
        'r string' are recommended (i.g.: r'./langs').

        Default to ./translations.

    default_language: :class:`str`
        The default language to use (if the text wasn't found on the specified language).

        Default to "en_US".

    Raises
    ------
    KeyError
        No path were given or given path doesn't exists.
    """
    def __init__(self,
                 path: str = os.path.join(".", "translations"),
                 default_language: str = "en_US"):
        self.path: str = path
        if not os.path.exists(self.path):
            raise KeyError("No path were given or given path doesn't exists.")
        self.lang_files: dict = {}
        self.default_language: str = default_language
        # Load all lang files at class init.
        self.load_all_lang_files()

    def load_lang_file(self, lang: str) -> dict:
        """Loads .lang file.

        Parameters
        ----------
        lang: :class:`str`
            The lang name (i.g.: en_US, fr_FR...).

        Raises
        ------
        TypeError
            Lang file error.

        Returns
        -------
        lang_dictionary: :class:`dict`
            A dict version of the the loaded .lang file.
        """

        lang_dictionary = {}
        lang_path = os.path.join(self.path, f"{lang}.lang")
        if not os.path.isfile(lang_path):
            for root, dirs, files in os.walk(self.path):
                for file in files:
                    if file.endswith(".lang") and file.startswith(lang):
                        lang_path = os.path.join(".", self.path, file)

        with open(lang_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if (line.replace(" ", "").replace("\n", "") != ""
                    and not line.startswith("//")
                    and not line.startswith("#")):
                    try:
                        key, value = line.strip().replace("\n", "").split("=", 1)
                        lang_dictionary[key] = value.strip()
                    except Exception as e:
                        line = line.replace("\n", "")
                        raise TypeError(f'\nLANG FILE ERROR:\nLine: {line}\nError: {e}\n')
        return lang_dictionary

    def load_all_lang_files(self, path: str = None) -> dict:
        """Loads all .lang files.

        Parameters
        ----------
        path: :class:`str`
            The path of the folder containing .lang translations.

            Default to the contructor path.

        Returns
        -------
        lang_files: :class:`dict`
            A dict version of the the loaded .lang files.
        """

        if path is None:
            path = self.path

        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(".lang"):
                    lang = file.split(".")[0]
                    self.lang_files[lang] = self.load_lang_file(lang)
        return self.lang_files

    def reload_all_lang_files(self) -> None:
        """Reloads all .lang files."""
        self.lang_files = self.load_all_lang_files(self.path)

    def language_exists(self, lang: str = None) -> bool:
        """Check whatever a language exists in the translations folder.

        Parameters
        ----------
        lang: :class:`str`
            The language to check.

        Returns
        --------
        :class:`bool`
            Whatever if the given language exists.
        """

        lang = next((l for l in self.lang_files if l.lower().startswith(lang.lower())), '')
        return lang in self.lang_files

    def languages(self) -> list[dict]:
        """Retrieve available languages.

        Returns
        -------
        languages: :class:`list[dict]`
            A :class:`list` containing :class:`dict` with lang informations.
        """

        languages_info = []
        for lang in self.lang_files:
            languages_info.append({
                'name': lang,
                'code': self.lang_files[lang]['lang_code'],
                'native_name': self.lang_files[lang]['lang_name'],
                'credits': self.lang_files[lang]['credits'],
            })

        return languages_info

    def text(self,
             text: str = None,
             lang: str = None) -> str:
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

        if text is None:
            return ""

        if lang is None:
            lang = self.default_language

        lang = next((l for l in self.lang_files if l.lower().startswith(lang.lower())), self.default_language)

        if not lang in self.lang_files:
            lang = self.default_language

        # TODO: Should improve here.
        if not text in self.lang_files[lang]:
            try:
                return self.lang_files[lang][text].replace(
            '\\n', '\n').replace(
            '\\r', '\r')
            except KeyError:
                raise KeyError("Given text wasn't found on both default language and given language.")

        return self.lang_files[lang][text].replace(
            '\\n', '\n').replace(
            '\\r', '\r').replace(
            '%prefix%', config_selfbot.prefix)

    def t(self,
          text: str = None,
          lang: str = None) -> str:
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
           path=os.path.join(".", "translations"))
except Exception:
    lang = Lang(default_language="en_US",
           path=os.path.join("..", "translations"))