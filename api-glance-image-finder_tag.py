from keystoneauth1 import loading
from keystoneauth1 import session
#from glanceclient import Client as glanceclient
import glanceclient
from glanceclient.common import exceptions as glance_exceptions

from oslo_utils import uuidutils


from oslo_utils import encodeutils

args = {
        'endpoint': "http://172.16.69.115/image",
        'auth_url': "http://172.16.69.115:5000/v3",
        'token': "gAAAAABZoAXKWLfhJs74ggla1vBt301YD60WArfi3njQKzK_lEyNsphvOp1yYsuBeAqczwPADeryZxkzHrKvS50-jnl_OAmkFMJsowGiU7ydxK0QhzUbk3Hkg3azXA1qA2VLohs5Dg5Lt-g4QymR_vbi9xX9FbzMhC0tcBVFxtrjy9dAIIa8tos",
        'username': "demo",
        'password': "password"
#        'cacert': self._get_client_option('glance', 'ca_file'),
#        'cert': self._get_client_option('glance', 'cert_file'),
#       'key': self._get_client_option('glance', 'key_file'),
#       'insecure': self._get_client_option('glance', 'insecure')
         }

glanceclient_version = 2

glance = glanceclient.Client(glanceclient_version, **args)

#for i in cli.images.list():
#    print i

#d = cli.images.get('cir:xyz')


def find_image(image_ident, image_tag):
    matches = find_images(image_ident, exact_match=True)
#    print('Found matches %s ', len(matches))
    match = []
    for i in range(len(matches)):
#    for i in matches:
       print(i)
       print('%s......%s.., .%s...%d..'%(image_tag, matches[i]['tags'],type(matches[i]['tags']),i))


       if matches[i]['tags']:
           if len(image_tag) < len(matches[i]['tags']):
               data1, data2 = image_tag, matches[i]['tags']
           else:
               data1, data2 = matches[i]['tags'], image_tag
           if all(map(lambda x: x in data1, data2)):
         # if image_tag == encodeutils.safe_decode(matches[i]['tags'][0]):
               match.append(matches[i])
       else:
           match.append(matches[i])
    if len(match) == 1:
       print(match)
    if len(match) == 0:
        print("ImageNotFound")
    if len(match) > 1:
        msg = ("Multiple images exist with same name "
               "%(image_ident)s. Please use the image id "
               "instead.") % {'image_ident': image_ident}
        print(msg)
        #raise exception.Conflict(msg)

def find_images(image_ident, exact_match):
#    glance = create_glanceclient(context)
    if uuidutils.is_uuid_like(image_ident):
        images = []
        try:
            image = glance.images.get(image_ident)
            if image.container_format == 'docker':
                images.append(image)
        except glance_exceptions.NotFound:
            # ignore exception
            pass
    else:
        filters = {'container_format': 'docker'}
        images = list(glance.images.list(filters=filters))
        if exact_match:
            images = [i for i in images if i.name == image_ident ]
        else:
            images = [i for i in images if image_ident in i.name ]

    return images



data = [('cir:123','v12'),('cir:123', 'v123'),('cir:xyz', 'v123'),('cir:123', 'v12,cirros'),('cir:123',None),('cir_test','')]

for i in range(len(data)):
    print("*************************************")
    print(data[i][0],data[i][1])
    find_image(data[i][0],data[i][1])
# find_image('cir:123', 'v12')
#find_image('cir:123', 'v123')
#find_image('cir:xyz', 'v123')
#find_image('cir:123', 'v12,cirros')
#find_image('cir:123',None)
#ind_image('cir_test','')
