import pytest
import logging

logger = logging.getLogger(__name__)


@pytest.fixture(scope='class')
def class_fixture():
    logger.info('class setup')
    yield
    logger.info('class teardown')


@pytest.fixture(scope='function')
def function_fixture():
    logger.info('function setup')
    yield
    logger.info('function teardown')


@pytest.mark.modifyscope(class_fixture='function')
def test_modifyscope(function_fixture, class_fixture):
    logger.info('call')
