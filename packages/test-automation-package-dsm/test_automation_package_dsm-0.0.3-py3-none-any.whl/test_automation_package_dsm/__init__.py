import easygui
from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Test:

  def __init__(self):
    self.vars = {}
    service_object = Service(binary_path)
    self.driver = webdriver.Chrome(service=service_object)
    self.action = ActionChains(self.driver)
    self.driver.maximize_window() 

  def Type(self, selection, input):
    element = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, selection)))
    self.action.move_to_element(element)
    element.click()
    element.send_keys(input)

  def Click(self, selection):
    element = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, selection)))
    self.action.move_to_element(element)
    element.click()


  class Commons:

    def LogInAsGuest(self, baseURL):
      self.vars["UserCredentials"] = easygui.multenterbox('Please fill in your credentials', 'Login', fields=["Username", "Password"])
      self.driver.get(baseURL)
      WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.ID, "usernameInput")))
      self.driver.find_element(By.ID, "usernameInput").send_keys(self.vars["UserCredentials"][0])
      self.driver.find_element(By.ID, "passwordInput").send_keys(self.vars["UserCredentials"][1])
      self.driver.find_element(By.ID, "loginButton").click()
  
    def LogInAsSelf(self, baseURL, username, password):
      self.driver.get(baseURL)
      WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.ID, "usernameInput")))
      self.driver.find_element(By.ID, "usernameInput").send_keys(username)
      self.driver.find_element(By.ID, "passwordInput").send_keys(password)
      self.driver.find_element(By.ID, "loginButton").click()


  class DelvoAnalytics:

    def CreateNewRequest(self):
      self.vars["RandomVialBarcode"] = self.driver.execute_script("return Math.floor(Math.random() * 10000000000);")
      self.vars["RandomSampleID"] = self.driver.execute_script("return Math.floor(Math.random() * 10000000000);")
      self.vars["RandomDay"] = self.driver.execute_script("return Math.floor(Math.random()*(26-15+1)+15)")

      self.Click("//a[contains(@data-item-id, \"159b6aef-dbc3-5b23-a735-cf99f8341771-1\")]")
      self.Click("//button[contains(@data-button-id, \"DSM.RequestForm.actionButton5\")]")
      self.Click("//button[contains(@data-button-id, \"DSM.Sample_NewEdit.actionButton24\")]")
      self.Type("//input[contains(@id, \"DSM.Sample_Barcode_Edit.textBox2\")]", self.vars["RandomVialBarcode"])
      self.Click("//button[contains(@data-button-id, \"DSM.Sample_Barcode_Edit.actionButton2\")]")
      self.Type("//input[contains(@id, \"DSM.Sample_NewEdit.textBox3.54\")]", self.vars["RandomSampleID"])
      self.Type("//input[contains(@id, \"DSM.Sample_NewEdit.datePicker1\")]", str(self.vars["RandomDay"]) + "/Aug/2022")
      self.Click("//div[contains(@data-mendix-id, \"DSM.Sample_NewEdit.referenceSelector1\")]")
      self.Click("//option[. = 'Water']")
      self.Click("//button[contains(@data-mendix-id, \"DSM.Sample_NewEdit.actionButton4\")]")
      self.Click("//tr[contains(@class, \"mx-name-index-0\")]")
      self.Click("//button[contains(@data-mendix-id, \"MasterData.Product_Select_Customer_New.actionButton3\")]")
      self.Click("//input[@type='radio'][@value='No']")
      self.Click("//button[contains(@data-button-id, \"DSM.Sample_NewEdit.actionButton1\")]")
      self.Click("//input[@type='radio'][@value='true']")
      self.Click("//button[contains(@data-button-id, \"DSM.Request_NewEdit.actionButton4\")]")
      self.Click("//button[contains(.,\'OK\')]")