import time
import inspect


def advertisements(store):
    store[inspect.stack()[0][3]] = int(round(time.time() * 1000))


def broken_links(store):
    time.sleep(1)
    store[inspect.stack()[0][3]] = int(round(time.time() * 1000))


def internationalization(store):
    time.sleep(1)
    store[inspect.stack()[0][3]] = int(round(time.time() * 1000))


def internet_domain(store):
    store[inspect.stack()[0][3]] = int(round(time.time() * 1000))


def inlinks(store):
    store[inspect.stack()[0][3]] = int(round(time.time() * 1000))


def modified_date_time(store):
    store[inspect.stack()[0][3]] = int(round(time.time() * 1000))


def real_world_presence(store):
    store[inspect.stack()[0][3]] = int(round(time.time() * 1000))


def outlinks(store):
    store[inspect.stack()[0][3]] = int(round(time.time() * 1000))


def misspell(store):
    store[inspect.stack()[0][3]] = int(round(time.time() * 1000))


def text_to_image_ratio(store):
    store[inspect.stack()[0][3]] = int(round(time.time() * 1000))


def responsive_design(store):
    store[inspect.stack()[0][3]] = int(round(time.time() * 1000))


def page_load_time(store):
    store[inspect.stack()[0][3]] = int(round(time.time() * 1000))
