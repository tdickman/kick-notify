from pushbullet import Pushbullet
import requests
from BeautifulSoup import BeautifulSoup
from firebase import firebase
import os


class Kick(object):
    def __init__(self, firebase_subdomain, pushbullet_key, pushbullet_chan):
        self.fb = firebase.FirebaseApplication('https://{}.firebaseio.com'.format(firebase_subdomain), None)
        pb = Pushbullet(pushbullet_key)
        self.pb_chan = filter(lambda x: x.channel_tag == pushbullet_chan, pb.channels)[0]

    def get_new_offers(self):
        '''Find new offers, and compare'''
        r = requests.get('http://kickfurther.com/offers')
        soup = BeautifulSoup(r.text)
        found = []
        for offer in soup.findAll('div', {'class': 'offer'}):
            link = offer.find('a', href=True)['href']
            if not self.fb.get(link, None):
                found.append(link)
        return found

    def send_notification(self, link):
        '''Sends a notification for the given item, and then marks it as sent in firebase'''
        self.fb.post(link, True)
        self.pb_chan.push_link('New Kickfurther Offer', 'http://kickfurther.com{}'.format(link))
        print 'Sent notification for {}'.format(link)


env = os.environ
kick = Kick(env['FB_SUB'], env['PB_KEY'], env['PB_CHAN'])
new_offers = kick.get_new_offers()
for link in new_offers:
    kick.send_notification(link)
