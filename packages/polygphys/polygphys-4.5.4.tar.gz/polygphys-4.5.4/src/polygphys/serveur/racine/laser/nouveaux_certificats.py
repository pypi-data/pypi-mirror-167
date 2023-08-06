# -*- coding: utf-8 -*-
"""Créé le Wed Aug 17 14:15:04 2022 par emilejetzer."""

import subprocess

from pathlib import Path
from datetime import datetime

import schedule

from polygphys.serveur.racine.canari import créer_journal, noter_exceptions
from polygphys.sst.certificats_laser.nouveau_certificats import SSTLaserCertificatsConfig, SSTLaserCertificatsForm
from polygphys.outils.reseau import OneDrive


# Script (modèle)

journal = créer_journal(__name__, __file__)
horaire = schedule.every(10).minutes


@noter_exceptions(journal)
def main():
    chemin_config = Path('~').expanduser() / 'certificats_laser.cfg'
    config = SSTLaserCertificatsConfig(chemin_config)
    dossier = OneDrive('',
                       config.get('onedrive', 'organisation'),
                       config.get('onedrive', 'sous-dossier'),
                       partagé=True)
    fichier = dossier / config.get('formulaire', 'nom')
    config.set('formulaire', 'chemin', str(fichier))
    formulaire = SSTLaserCertificatsForm(config)

    try:
        exporteur = subprocess.Popen(['unoconv', '--listener'])
        formulaire.mise_à_jour()
    finally:
        exporteur.terminate()


def html(chemin: Path):
    with chemin.open('w') as fichier:
        print('<html>',
              '    <head>',
              f'        <title>{__name__} à {__file__}</title>',
              '    </head>',
              '    <body>',
              f'        <h1>{__name__} à {__file__}</h1>',
              f'        <p>Fonctionnel à {datetime.isoformat(datetime.now())}.</p>',
              '        <hr/>',
              f'        <h1>{chemin.with_suffix(".log")}</h1>',
              f'        <pre>{chemin.with_suffix(".log").open("r").read()}</pre>',
              '    </body>',
              '</html>',
              sep='\n',
              file=fichier)


if __name__ == '__main__':
    main()
