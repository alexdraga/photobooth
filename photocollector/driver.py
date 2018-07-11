# -*- coding: utf-8 -*-
import mimetools
import mimetypes
import urllib
import urllib2
from io import BytesIO
import oauth2
from urlparse import parse_qsl

from urllib3.filepost import iter_fields, writer

from config import flickr_settings


class PhotoCollectorDriver(object):
    key = None
    secret = None
    consumer = None
    client = None
    client2 = None
    token = None
    token2 = None
    requested_tokens = None
    oauth_token = flickr_settings.oauth_token
    oauth_token_secret = flickr_settings.oauth_token_secret
    headers = {'User-agent': 'Python-Flickr 00'}

    def __init__(self):
        self.key = flickr_settings.key
        self.secret = flickr_settings.secret
        self.consumer = oauth2.Consumer(self.key, self.secret)
        self.client = oauth2.Client(self.consumer)
        if self.oauth_token is not None and self.oauth_token_secret is not None:
            self.token2 = oauth2.Token(self.oauth_token, self.oauth_token_secret)

    def request_tokens(self):
        resp, content = self.client.request(
            '%s?oauth_callback=%s' % (flickr_settings.request_token_url,
                                      "https://www.flickr.com/"), 'GET', **{})
        self.requested_tokens = dict(parse_qsl(content))
        auth_url_params = {'oauth_token': self.requested_tokens['oauth_token'], "perms": "write"}
        self.requested_tokens['auth_url'] = '%s?%s' % (flickr_settings.authorize_url, urllib.urlencode(auth_url_params))
        return self.requested_tokens

    def request_auth(self, oauth_verifier):
        params = {"oauth_verifier": oauth_verifier}
        self.token = oauth2.Token(self.requested_tokens["oauth_token"],
                                  self.requested_tokens["oauth_token_secret"])
        self.client2 = oauth2.Client(self.consumer, self.token)
        resp, content = self.client2.request(
            '%s?%s' % (flickr_settings.access_token_url, urllib.urlencode(params)), 'GET')
        oauth_tokens = dict(parse_qsl(content))
        self.oauth_token = oauth_tokens["oauth_token"]
        self.oauth_token_secret = oauth_tokens["oauth_token_secret"]
        self.token2 = oauth2.Token(self.oauth_token, self.oauth_token_secret)
        flickr_settings.oauth_token = self.oauth_token
        flickr_settings.oauth_token_secret = self.oauth_token_secret
        return self.token2

    def upload_file(self, name, image):

        faux_req = oauth2.Request.from_consumer_and_token(self.consumer,
                                                          token=self.token2,
                                                          http_method="POST",
                                                          http_url=flickr_settings.upload_api_url,
                                                          parameters={})
        faux_req.sign_request(oauth2.SignatureMethod_HMAC_SHA1(),
                              self.consumer,
                              self.token2)
        all_upload_params = dict(parse_qsl(faux_req.to_postdata()))
        all_upload_params['photo'] = (name, image)
        body, content_type = self.encode_multipart_formdata(all_upload_params)
        self.headers.update({
            'Content-Type': content_type,
            'Content-Length': str(len(body))
        })
        req = urllib2.Request(flickr_settings.upload_api_url, body, self.headers)
        req = urllib2.urlopen(req)
        assert req.code == 200, "Error received during image upload"

    def get_content_type(self, filename):
        return mimetypes.guess_type(filename)[0] or 'application/octet-stream'

    def encode_multipart_formdata(self, fields, boundary=None):
        """
        Encode a dictionary of ``fields`` using the multipart/form-data mime format.
        :param fields:
            Dictionary of fields or list of (key, value) field tuples.  The key is
            treated as the field name, and the value as the body of the form-data
            bytes. If the value is a tuple of two elements, then the first element
            is treated as the filename of the form-data section.
            Field names and filenames must be unicode.
        :param boundary:
            If not specified, then a random boundary will be generated using
            :func:`mimetools.choose_boundary`.
        """
        body = BytesIO()
        if boundary is None:
            boundary = mimetools.choose_boundary()

        for fieldname, value in iter_fields(fields):
            body.write('--%s\r\n' % (boundary))

            if isinstance(value, tuple):
                filename, data = value
                writer(body).write('Content-Disposition: form-data; name="%s"; '
                                   'filename="%s"\r\n' % (fieldname, filename))
                body.write('Content-Type: %s\r\n\r\n' %
                           (self.get_content_type(filename)))
            else:
                data = value
                writer(body).write('Content-Disposition: form-data; name="%s"\r\n'
                                   % (fieldname))
                body.write(b'Content-Type: text/plain\r\n\r\n')

            if isinstance(data, int):
                data = str(data)  # Backwards compatibility

            if isinstance(data, unicode):
                writer(body).write(data)
            else:
                body.write(data)

            body.write(b'\r\n')

        body.write('--%s--\r\n' % (boundary))

        content_type = 'multipart/form-data; boundary=%s' % boundary

        return body.getvalue(), content_type
