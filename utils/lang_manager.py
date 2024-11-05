"""
La licence MIT (MIT)

Copyright (c) 2024-présent Lenochxd

La permission est par la présente accordée, sans frais, à toute personne obtenant une
copie de ce logiciel et des fichiers de documentation associés (le "Logiciel"),
de traiter le Logiciel sans restriction, y compris sans limitation
les droits d'utiliser, copier, modifier, fusionner, publier, distribuer, sous-licencier,
et/ou vendre des copies du Logiciel, et de permettre aux personnes à qui le
Logiciel est fourni de le faire, sous réserve des conditions suivantes :

Le présent avis de copyright et cet avis de permission doivent être inclus dans
toutes les copies ou portions substantielles du Logiciel.

LE LOGICIEL EST FOURNI "EN L'ÉTAT", SANS GARANTIE D'AUCUNE SORTE, EXPRESSE
OU IMPLICITE, Y COMPRIS MAIS SANS LIMITATION LES GARANTIES DE COMMERCIALISATION,
D'ADÉQUATION À UN OBJECTIF PARTICULIER ET DE NON-VIOLATION. EN AUCUN CAS, LES
AUTEURS OU DÉTENTEURS DE DROITS D'AUTEUR NE POURRONT ÊTRE TENUS RESPONSABLES DE TOUTE RÉCLAMATION, DOMMAGE OU AUTRE
RESPONSABILITÉ, QUE CE SOIT DANS LE CADRE D'UN CONTRAT, DÉLIT OU AUTRE, DÉCOULANT
DE OU EN LIAISON AVEC LE LOGICIEL OU L'UTILISATION OU AUTRES
TRAITEMENTS DANS LE LOGICIEL.
"""

# REMARQUE : Système de langue créé par Lenochxd, consultez son GitHub (https://github.com/Lenochxd) !

import os

import config_selfbot

class Lang():
    """Constructeur.

    Paramètres
    ----------
    path: :class:`str`
        Le chemin du dossier contenant les traductions .lang.
        Les chaînes 'r string' sont recommandées (ex.: r'.\langs').

        Défaut à r"./translations".

    default_language: :class:`str`
        La langue par défaut à utiliser (si le texte n'a pas été trouvé dans la langue spécifiée).

        Défaut à "en_US".

    Lève
    ------
    KeyError
        Aucun chemin n'a été donné ou le chemin donné n'existe pas.
    """
    def __init__(self,
                 path: str = r".\translations",
                 default_language: str = "en_US"):
        self.path: str = path  # Chemin du dossier de traductions
        if not os.path.exists(self.path):
            raise KeyError("Aucun chemin n'a été donné ou le chemin donné n'existe pas.")
        self.lang_files: dict = {}  # Dictionnaire pour stocker les fichiers de langue
        self.default_language: str = default_language  # Langue par défaut
        # Charger tous les fichiers de langue à l'initialisation de la classe.
        self.load_all_lang_files()

    def load_lang_file(self, lang: str) -> dict:
        """Charge le fichier .lang.

        Paramètres
        ----------
        lang: :class:`str`
            Le nom de la langue (ex.: en_US, fr_FR...).

        Lève
        ------
        TypeError
            Erreur de fichier de langue.

        Retourne
        -------
        lang_dictionary: :class:`dict`
            Une version dict du fichier .lang chargé.
        """

        lang_dictionary = {}
        lang_path = f"{self.path}/{lang}.lang"  # Chemin du fichier de langue
        if not os.path.isfile(f"{self.path}/{lang}.lang"):  # Vérifie si le fichier existe
            for root, dirs, files in os.walk(self.path):
                for file in files:
                    if file.endswith(".lang") and file.startswith(lang):  # Recherche le fichier de langue
                        lang_path = f"./{self.path}/{file}"

        with open(lang_path, "r", encoding="utf-8") as f:  # Ouvre le fichier de langue
            lines = f.readlines()
            for line in lines:
                if (line.replace(" ", "").replace("\n", "") != ""  # Ignore les lignes vides
                    and not line.startswith("//")  # Ignore les commentaires
                    and not line.startswith("#")):
                    try:
                        key, value = line.strip().replace("\n", "").split("=", 1)  # Sépare la clé et la valeur
                        lang_dictionary[key] = value.strip()  # Ajoute au dictionnaire
                    except Exception as e:
                        line = line.replace("\n", "")
                        raise TypeError(f'\nERREUR DE FICHIER LANG:\nLigne: {line}\nErreur: {e}\n')
        return lang_dictionary

    def load_all_lang_files(self, path: str = None) -> dict:
        """Charge tous les fichiers .lang.

        Paramètres
        ----------
        path: :class:`str`
            Le chemin du dossier contenant les traductions .lang.

            Défaut au chemin du constructeur.

        Retourne
        -------
        lang_files: :class:`dict`
            Une version dict des fichiers .lang chargés.
        """

        if path is None:
            path = self.path

        for root, dirs, files in os.walk(self.path):  # Parcourt tous les fichiers dans le dossier
            for file in files:
                if file.endswith(".lang"):  # Vérifie si c'est un fichier de langue
                    lang = file.split(".")[0]  # Extrait le nom de la langue
                    self.lang_files[lang] = self.load_lang_file(lang)  # Charge le fichier de langue
        return self.lang_files

    def reload_all_lang_files(self) -> None:
        """Recharge tous les fichiers .lang."""
        self.lang_files = self.load_all_lang_files(self.path)

    def language_exists(self, lang: str = None) -> bool:
        """Vérifie si une langue existe dans le dossier de traductions.

        Paramètres
        ----------
        lang: :class:`str`
            La langue à vérifier.

        Retourne
        --------
        :class:`bool`
            Vérifie si la langue donnée existe.
        """

        lang = next((l for l in self.lang_files if l.lower().startswith(lang.lower())), '')
        return lang in self.lang_files

    def languages(self) -> list[dict]:
        """Récupère les langues disponibles.

        Retourne
        -------
        languages: :class:`list[dict]`
            Une :class:`list` contenant :class:`dict` avec les informations sur les langues.
        """

        languages_info = []
        for lang in self.lang_files:  # Parcourt les fichiers de langue chargés
            languages_info.append({
                'name': lang,  # Nom de la langue
                'code': self.lang_files[lang]['lang_code'],  # Code de la langue
                'native_name': self.lang_files[lang]['lang_name'],  # Nom natif de la langue
                'credits': self.lang_files[lang]['credits'],  # Crédits pour la langue
            })

        return languages_info

    def text(self,
             text: str = None,
             lang: str = None) -> str:
        """Retourne le texte donné dans la langue spécifiée.

        Paramètres
        ----------
        text: :class:`str`
            Le texte à obtenir dans la langue donnée.
        lang: :class:`str`
            La langue dans laquelle obtenir le texte.

            Défaut à la langue par défaut.

        Lève
        ------
        KeyError
            Le texte donné n'a pas été trouvé dans la langue par défaut et dans la langue donnée.

        Retourne
        -------
        :class:`str`
            Le texte traduit.
        """

        if text is None:
            return ""

        if lang is None:
            lang = config_selfbot.lang  # Récupère la langue par défaut de la config

        lang = next((l for l in self.lang_files if l.lower().startswith(lang.lower())), self.default_language)

        if not lang in self.lang_files:
            lang = self.default_language  # Utilise la langue par défaut si la langue spécifiée n'est pas trouvée

        # TODO : Améliorer ici.
        if not text in self.lang_files[lang]:  # Vérifie si le texte existe dans le fichier de langue
            try:
                return self.lang_files[lang][text].replace(  # Remplace les séquences d'échappement
            '\\n', '\n').replace(
            '\\r', '\r').replace(
                '%prefix%', config_selfbot.prefix)  # Remplace le préfixe par celui de la config
            except KeyError:
                raise KeyError("Le texte donné n'a pas été trouvé ni dans la langue par défaut ni dans la langue donnée.")

        return self.lang_files[lang][text].replace(
            '\\n', '\n').replace(
            '\\r', '\r').replace(
                '%prefix%', config_selfbot.prefix)

    def t(self,
          text: str = None,
          lang: str = None) -> str:
        """Retourne le texte donné dans la langue spécifiée.

        Raccourci pour Lang().text()

        Paramètres
        ----------
        text: :class:`str`
            Le texte à obtenir dans la langue donnée.
        lang: :class:`str`
            La langue dans laquelle obtenir le texte.

            Défaut à la langue par défaut.

