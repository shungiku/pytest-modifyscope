import pytest
import logging

logger = logging.getLogger(__name__)


@pytest.fixture(scope='class', autouse=True)
def ca1(s1):
    logger.info('class setup auto')
    yield
    logger.info('class teardown auto')


@pytest.fixture(scope='session')
def s1():
    logger.info('session setup')
    yield
    logger.info('session teardown')


@pytest.fixture(scope='class')
def c1():
    logger.info('class setup')
    yield
    logger.info('class teardown')


@pytest.fixture(scope='class', autouse=True)
def c2():
    logger.info('class setup 2')
    yield
    logger.info('class teardown 2')


@pytest.fixture(scope='function')
def f1(c1):
    logger.info('function setup')
    yield
    logger.info('function teardown')


@pytest.mark.modifyscope(c1='function', c2='function')
def test_modifyscope(f1, c2):
    logger.info('call')
