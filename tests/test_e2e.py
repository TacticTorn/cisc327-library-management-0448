from playwright.sync_api import sync_playwright
import pytest
import subprocess
import time
import os
import signal

@pytest.fixture(scope="session", autouse=True)
def start_flask():
    #start
    proc = subprocess.Popen(["python", "app.py"])
    time.sleep(3)  #wait
    yield
    #stop
    os.kill(proc.pid, signal.SIGTERM)
'''
def test_add_and_borrow_book():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:5000")

        #add a new book
        page.click("text=Add Book")
        page.fill('input[name="title"]', "The Pragmatic Programmer")
        page.fill('input[name="author"]', "Andrew Hunt")
        page.fill('input[name="isbn"]', "978-0201616224")
        page.fill('input[name="copies"]', "3")
        page.click("text=Add Book")

        #verify success message
        assert page.locator("text=Book added successfully!").is_visible()

        #verify book appears in catalog
        page.wait_for_selector("text=The Pragmatic Programmer")

        #borrow book
        page.click("text=Borrow")
        page.fill('input[name="patron_id"]', "12345")
        page.select_option("select[name='book_id']", label="The Pragmatic Programmer")
        page.click("text=Borrow")

        #confirm success
        assert page.locator("text=Book borrowed successfully!").is_visible()

        browser.close()
'''
