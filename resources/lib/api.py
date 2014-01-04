# coding=utf-8
"""

Created on 1/3/14

@author: monizh
  
"""
import json
import urllib
import gzip

from StringIO import StringIO

class EyeTV(object):
    def __init__(self, server='10.0.1.37', port=2170):
        self.base_url = 'http://%s:%s' % (server, port)

    def _get_json_data(self, url):
        print "Get: %s" % self.base_url + url
        response = urllib.urlopen(self.base_url + url)
        buf = StringIO(response.read())
        if response.headers.get('Content-Encoding') == 'gzip':
            data = gzip.GzipFile(fileobj=buf)
        else:
            data = buf
        return json.load(data)

    def get_playlists(self):
        """
        http://10.0.1.37:2170/live/playlists/0/0/-1/
        """
        data = self._get_json_data('/live/playlists/0/0/-1/')
        return data['playlists']

    def get_thumbnail(self, ref_id):
        """
        http://10.0.1.37:2170/live/thumbnail/0/410309940
        """
        return self.base_url + '/live/thumbnail/0/%s' % ref_id

    def get_ref_movie(self, ref_id):
        """
        http://10.0.1.37:2170/live/recordingFile/410482741/refmovie.mov
        """
        return self.base_url + '/live/recordingFile/%s/refmovie.mov' % ref_id

    def get_recordings(self, playlist_id):
        """
        http://10.0.1.37:2170/live/recordings/0/69128906691/-1/-1/-date/_REC_WIFIACCESS
        """
        data = self._get_json_data('/live/recordings/0/%s/-1/-1/-date/_REC_WIFIACCESS' % playlist_id)
        return data['recordings']

