class Xpath(object):
    # javascript specific
    javaScript = "document.getElementsByClassName('replaceclass')[index].value = 'replacevalue' "

    # application specific
    input_operator = '//input[@type = "text" and @data-qa="celular-operator"]'
    input_number = '//input[@type="text" and @data-qa="celular-mobile"]'
    input_amount = '//input[@type="text" and @data-qa="celular-amount"]'
    sign_button = '(//div//button[@perform="payment" and text()="Siguiente"])[1]'
    payment_screen = '//div[text()="Resumen de la compra"]'
    Payment_tarjeta = '//div//p[text()="Tarjeta"]'
    user_nueva = '//span[text()="Usar nueva tarjeta"]'
    Payment_button = '(//button//span[text()="Pagar con Tarjeta"])[2]'
    input_email = '(//input[@name="txtEmail"])[1]'
    email_field = '//input[@type="text" and @id="usrname"]'
    password_field = '//input[@type="password" and @id="psw"]'
    captcha = '(//div[@class="recaptcha-checkbox-border"])[1]'
    acceso = '//button[text()="Acceso"]'
    success_message = '//div[text()="¡Recarga Exitosa!"]'

    # frames
    captchaframe = '//iframe[@title="reCAPTCHA"]'

    # generic xpath
    choose_Operador = '//li//div//b[text()="replace"]'
    choose_amount = '(//div[text()="replace"])[1]'
    input_name = '(//input[@name="replace"])[2]'
