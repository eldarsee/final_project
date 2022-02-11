from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#id_login-username")
    REGISTER_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PSWD1_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    PSWD2_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.NAME, "registration_submit")


class ProductPageLocators:
    CART = (By.CLASS_NAME, "btn-add-to-basket")
    PRICE_FIELD = (By.CSS_SELECTOR, ".alert .alertinner p:first-child")
    PRICE_FIELD_START = (By.CLASS_NAME, "col-sm-6.product_main > p")
    PRODUCT_FIELD = (By.CLASS_NAME, "alertinner > strong")
    PRODUCT_FIELD_START = (By.CLASS_NAME, "col-sm-6.product_main > h1")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, '.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle)')
    BASKET_ITEM = (By.CLASS_NAME, "basket-items")
    BASKET_TEXT = (By.TAG_NAME, "p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
