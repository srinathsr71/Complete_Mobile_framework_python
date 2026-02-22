# 🚀 Unified Mobile Automation Framework (Python + Appium + Pytest-BDD)

**Designed with Clean Architecture | Platform Abstraction | BDD | Local + Remote Execution**

---

## 📌 Overview

This framework is a **professional, scalable mobile automation solution** built using:

* **Python 3**
* **Appium** (Android & iOS)
* **Pytest-BDD** (Behavior Driven Development)
* **Allure Reporting**
* **Clean Architecture & SOLID principles**

It is designed to be:

* ✅ Easy to understand
* ✅ Easy to extend
* ✅ Platform-agnostic (Android / iOS)
* ✅ CI/CD ready
* ✅ Stable for real devices & emulators

---

## 🎯 Key Capabilities

* Android & iOS support in a **single codebase**
* BDD using Gherkin (`.feature` files)
* Platform abstraction for locators
* Robust driver lifecycle management
* Explicit waits (no `sleep()`)
* Screenshot capture on failure
* Retry mechanism for flaky tests
* Environment-based configuration
* Clean test isolation

---

## 🧠 Architecture Summary

### 🔹 Driver Management

* **DriverFactory**

  * Creates Android / iOS drivers
  * Supports local & remote execution
* **AppiumService**

  * Starts and stops Appium automatically (local runs)

---

### 🔹 Runtime Configuration

* **runtime_config.py**

  * Reads execution context from environment variables
  * Platform, device type, environment, execution mode

---

### 🔹 Configuration Management

* Environment-based config loading

```
config/
 ├── dev/
 │    ├── config.yml
 │    ├── android_caps.json
 │    └── ios_caps.json
 └── test/
```

Priority order:

1. Environment variables
2. Environment-specific config files

---

### 🔹 BDD Layer (Pytest-BDD)

* Feature files written in **Gherkin**
* Step definitions mapped using decorators
* Clean separation between **WHAT** and **HOW**

---

### 🔹 Page Object Model (POM)

* **BasePage**

  * Common actions (click, type)
  * Centralized waits
* Page classes represent **screens**, not tests

---

### 🔹 Platform Abstraction (Critical Design)

```python
get_locator(android_locator, ios_locator)
```

* Single locator variable
* Automatically resolves based on platform
* No duplicate page classes

---

### 🔹 Assertions Layer

* Centralized in `utils/assertions.py`
* All assertions:

  * Log failures
  * Attach info to Allure

---

### 🔹 Test Isolation & Stability

* App reset after each test
* Screenshot on failure
* Retry failed tests automatically

---

## 📂 Folder Structure

```
MobileAutomationFramework/
│
├── core/
│   ├── driver_factory.py
│   ├── appium_service.py
│
├── pages/
│   ├── base_page.py
│   └── storepage/
│       └── e2eplaceorderpage.py
│
├── steps/
│   └── test_general_storestep.py
│
├── tests/
│   └── test_runner_store.py
│
├── features/
│   └── general_store.feature
│
├── utils/
│   ├── assertions.py
│   ├── wait_utils.py
│   ├── config_reader.py
│   ├── runtime_config.py
│   └── platform_utils.py
│
├── config/
│   └── dev/
│       ├── config.yml
│       ├── android_caps.json
│       └── ios_caps.json
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── runtests.bat
└── README.md
```

---

## ▶ How to Execute Tests

### Step 1: Run Batch File

```bash
runtests.bat
```

---

### Step 2: Select Options

Interactive menu allows you to choose:

* Web or Mobile
* Android or iOS
* Real device / Emulator / Simulator
* Local Appium or Remote Grid
* Pytest markers (smoke / regression)

---

## ▶ Example: Local Android Execution

```
2  → Mobile
1  → Android
1  → Real Device
1  → Local Appium
smoke
```

Executes:

```bash
pytest -v -m smoke --alluredir=allure-results
```

---

## 📊 Reporting

* Allure results generated per execution
* Screenshots automatically attached on failure

Generate report:

```bash
allure generate allure-results -o allure-report
```

---

## 🧪 Example Feature File

```gherkin
Feature: Verify General Store Shopping

Scenario: Successful shopping general store
  Given user is on General Store home
  When user selects country "India"
  And user enters name "Ankit"
  And user selects gender "male"
  Then user proceeds to shop
```

---

## 🧠 Example Step Definition

```python
@given("user is on General Store home", target_fixture="home")
def user_is_on_home(driver, wait_utils):
    home = PlaceOrderPage(driver, wait_utils)
    assert_true(home.is_loaded(), "Home screen not loaded")
    return home
```

---

## 🧠 Why This Framework Is Strong

* Single framework for Android & iOS
* Clean separation of concerns
* Platform-independent locators
* Stable execution (explicit waits + retries)
* Easy onboarding for new team members
* Professional enterprise-ready design

---

## 📦 Adding New Tests

1. Add a new `.feature` file
2. Create matching step definitions
3. Add a new Page Object
4. Reuse BasePage methods

No framework changes required.

---

## 🏁 Final Note

This framework is designed not just to **run tests**, but to:

* Teach good automation practices
* Scale with team growth
* Survive real-world CI/CD pipelines

If you understand this framework, you understand **real automation engineering**.

---

✅ **Happy Testing!**
