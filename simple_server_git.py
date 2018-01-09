# TD3/simple_server.py
#
# Exemple de serveur de raytracing

import http.server
import socketserver
from urllib.parse import urlparse, parse_qs, unquote_plus
import sqlite3
import json

# Définition du handler
class RequestHandler(http.server.SimpleHTTPRequestHandler):

  # sous-répertoire racine des documents statiques
  static_dir = '/client'

  # version du serveur
  server_version = 'TD3/simple_server.py/0.1'

  # méthode pour traiter les requêtes GET
  def do_GET(self):

    # GET * - requête soumise au serveur de documents statiques
    self.send_static()


  # méthode pour traiter les requêtes HEAD
  def do_HEAD(self):

    # réservée aux documents statiques
    self.send_static()


  # méthode pour traiter les requêtes POST
  def do_POST(self):

    # méthode non autorisée (pour l'instant)
    self.send_error(405)


  # on envoie le document statique demandé
  def send_static(self):

    # on modifie le chemin d'accès en insérant le répertoire préfixe
    self.path = self.static_dir + self.path

    # on calcule le nom de la méthode (do_GET ou do_HEAD) à appeler
    # via la classe mère, à partir du verbe HTTP (GET ou HEAD)
    method = 'do_{}'.format(self.command)

    # on traite la requête via la classe mère
    getattr(http.server.SimpleHTTPRequestHandler,method)(self)


# port utilisé par le serveur
PORT = 8080
print('Running on port {}'.format(PORT))

# instanciation et lancement du serveur
httpd = socketserver.TCPServer(("", PORT), RequestHandler)
httpd.serve_forever()

