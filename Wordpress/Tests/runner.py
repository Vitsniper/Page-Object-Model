import unittest
import HtmlTestRunner

# import test modules
from PageObjectModel.Wordpress.Tests import login_test
from PageObjectModel.Wordpress.Tests import basic_post_test
from PageObjectModel.Wordpress.Tests import page_test
from PageObjectModel.Wordpress.Tests import added_post_show_up_test
from PageObjectModel.Wordpress.Tests import search_post_test

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# adding tests to the suite
# suite.addTests(loader.loadTestsFromModule(login_test))
# suite.addTests(loader.loadTestsFromModule(basic_post_test))
# suite.addTests(loader.loadTestsFromModule(page_test))
# suite.addTests(loader.loadTestsFromModule(added_post_show_up_test))
suite.addTests(loader.loadTestsFromModule(search_post_test))

# initialize a runner
runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="Wordpress_test_results", verbosity=3, output="C:/Users/Vitalik/"
                         "PycharmProjects/Selenium/venv/PageObjectModel/Wordpress/Reports")
# runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)