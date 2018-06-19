import os
import time
import arrow
import requests
import cssselect
import tldextract
import subprocess
from urllib.parse import urljoin
from django.conf import settings
from multiprocessing import Process, Manager
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from webcred.utilities.decorators import feature


@feature
def advertisements(data, store):

    with open('webcred/data/easylist.txt') as f:
        # elemhide rules are prefixed by ## in the filter syntax
        css_rules = [line[2:] for line in f if line[:2] == "##"]

    # convert css rules from filter list to xpath rules
    xpath_rules = []
    translator = cssselect.HTMLTranslator()
    for rule in css_rules:
        try:
            xpath_rules.append(translator.css_to_xpath(rule))
        except cssselect.SelectorError:
            # skip bad selectors
            pass

    # create one large query by joining the rules using the xpath OR operator
    xpath_query = '|'.join(xpath_rules)

    ad_count = len(data['doc'].xpath(xpath_query))

    store['advertisements'] = ad_count


@feature
def broken_links(data, store):

    def get_status_code(url, store):
        store.append(requests.get(url).status_code)

    validate = URLValidator()

    # capture all links in href and src attributes
    xpath_rules = [
        '//*/@href',
        '//*/@src',
    ]

    # create one large query by joining the rules using the xpath OR operator
    xpath_query = '|'.join(xpath_rules)
    mixed_links = data['doc'].xpath(xpath_query)

    # convert all links to absolute URLs
    links = []
    for link in mixed_links:
        try:
            validate(link)
        except ValidationError:
            link = urljoin(data['url'], link)
        finally:
            links.append(link)

    manager = Manager()
    status_codes = manager.list()
    processes = [
        Process(target=get_status_code, args=(link, status_codes))
        for link in links
    ]

    for proc in processes:
        proc.start()

    for proc in processes:
        proc.join()

    # 4xx, 5xx status codes indicate errors
    broken_count = 0
    for result in status_codes:
        if int(str(result)[:1]) in [4, 5]:
            broken_count += 1

    store['broken_links'] = broken_count


@feature
def internationalization(data, store):

    xpath_rules = [
        '//*/@lang',
        '//*/@hreflang'
    ]

    xpath_query = '|'.join(xpath_rules)
    languages = data['doc'].xpath(xpath_query)

    store['internationalization'] = len(set([l.lower() for l in languages]))


def internet_domain(data, store):

    # tldextract looks up TLDs in the Public Suffix List,
    # maintained by Mozilla volunteers
    store['internet_domain'] = tldextract.extract(data['url']).suffix


# TODO: Add inlinks
@feature
def inlinks(data, store):

    store['inlinks'] = int(round(time.time() * 1000))


@feature
def modified_date_time(data, store):

    res = requests.get('http://archive.org/wayback/available',
                       params={
                           'url': data['url']
                       }).json()
    mod_time = arrow.get(res['archived_snapshots']['closest']['timestamp'],
                         'YYYYMMDDHHmmss').timestamp

    store['modified_date_time'] = mod_time


# TODO: Add real_world_presence
@feature
def real_world_presence(data, store):

    store['real_world_presence'] = int(round(time.time() * 1000))


def outlinks(data, store):

    domain = tldextract.extract(data['url']).domain
    validate = URLValidator()

    # capture all links in href and src attributes
    xpath_rules = [
        '//*/@href',
        '//*/@src',
    ]

    # create one large query by joining the rules using the xpath OR operator
    xpath_query = '|'.join(xpath_rules)
    mixed_links = data['doc'].xpath(xpath_query)

    # convert all links to absolute URLs
    external_links = []
    for link in mixed_links:
        try:
            validate(link)
        except ValidationError:
            link = urljoin(data['url'], link)
        finally:
            if tldextract.extract(link).domain != domain:
                external_links.append(link)

    store['outlinks'] = len(external_links)


# TODO: Add misspell
@feature
def misspell(data, store):
    pass


# TODO: Add text_to_image_ratio
@feature
def text_to_image_ratio(data, store):
    pass


@feature
def responsive_design(data, store):

    api_url = 'https://searchconsole.googleapis.com/v1/urlTestingTools/' \
              'mobileFriendlyTest:run'

    response = requests.post(api_url, json={
        'url': data['url']
    }, params={
        'fields': 'mobileFriendliness',
        'key': os.environ.get('GOOGLE_API_KEY')
    }).json()

    try:
        state = response['mobileFriendliness']
    except KeyError:
        state = response['error']['message']

    store['responsive_design'] = state


@feature
def page_load_time(data, store):

    state = subprocess.check_output(
        './phantomjs loadspeed.js {}'.format(data['url']).split(),
        cwd=os.path.join(settings.BASE_DIR, 'webcred', 'utilities')
    ).decode().strip()

    if state.isdigit():
        state = int(state)

    store['page_load_time'] = state


# TODO: Find some use for pagespeed
@feature
def pagespeed_score(data, store):

    api_url = 'https://www.googleapis.com/pagespeedonline/v4/runPagespeed'

    response = requests.get(api_url, params={
        'url': data['url'],
        'key': os.environ.get('GOOGLE_API_KEY')
    }).json()

    try:
        state = response['ruleGroups']['SPEED']['score']
    except KeyError:
        state = response['error']['message']

    store['pagespeed_score'] = state
