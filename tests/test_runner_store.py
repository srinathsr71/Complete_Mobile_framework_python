# from pytest_bdd import scenario, scenarios

#
# scenarios("../features/general_store.feature")

import pytest
# from pytest_bdd import scenarios
# from tests.steps.test_general_storestep import *
# from tests.steps.test_apidemos_step import *
# @pytest.mark.store
# @pytest.mark.tc01case
# @scenario("../features/general_store.feature",
#           "Successful shopping general store")
# def test_tc01():
#     pass
#
#
# @pytest.mark.store
# @pytest.mark.tc02case
# @scenario("../features/general_store.feature",
#           "Successful shopping general store adding products")
# def test_tc02():
#     pass
#
# @pytest.mark.tc01APIDemos
# @scenario("../features/APIdemo.feature",
#           "Navigate to App Activity Custom Title")
# def test_APIDemos():
#     pass
from pytest_bdd import scenarios
from tests.steps.test_general_storestep import *
from tests.steps.test_apidemos_step import *


# auto load all scenarios
scenarios("../features")



