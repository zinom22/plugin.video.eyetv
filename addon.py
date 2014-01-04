# coding=utf-8
"""

Created on 1/3/14

@author: monizh

"""
from xbmcswift2 import Plugin
from resources.lib.api import EyeTV

plugin = Plugin()
api = EyeTV(server=plugin.get_setting('server'), port=plugin.get_setting('port'))


@plugin.route('/')
def index():
    items = [{
        'label': p['title'],
        'path': plugin.url_for('playlist', playlist_id=p['Playlist ID']),
    } for p in api.get_playlists()]
    return items

@plugin.route('/playlist/<playlist_id>/')
def playlist(playlist_id):
    items = [{
        'label': r['display title'],
        'thumbnail': api.get_thumbnail(r['id']),
        'path': plugin.url_for('play_episode', ref_id=r['id']),
        'is_playable': True
    } for r in api.get_recordings(playlist_id)]
    return items

@plugin.route('/play/<ref_id>/')
def play_episode(ref_id):
    url = api.get_ref_movie(ref_id)
    plugin.log.info('Playing url: %s' % url)
    plugin.set_resolved_url(url)


if __name__ == '__main__':
    plugin.run()
