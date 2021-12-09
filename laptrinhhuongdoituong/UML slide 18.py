class Item:
  shippingWeight:str
  description:str
  def __init__(self,shippingWeight,description):
    self.shippingWeight=shippingWeight
    self.description=description
  def  getPriceForQuantity(self):
    pass
  def getTax(self):
    pass
  def inStock(self):
    pass

class OrderDetail:
  item:Item
  quantity: str
  taxStatus:str
  def __init__(self,quantity,taxStatus):
    self.quantity=quantity
    self.taxStatus=taxStatus
  def calcSubTotal(self):
    pass
  def calcWeight(self):
    pass
  def calcTax(self):
    pass

class Payment:
  amount:float
  def __init__(self,amount):
    self.amount=amount

class Cash(Payment):
  cashTendered: float
  def __init__(self,amount,cashTendered):
    Payment.__init__(self,amount)
    self.cashTendered=cashTendered

class Check(Payment):
  name: str
  bankID: str
  def __init__(self,amount,name,bankID):
    Payment.__init__(self,amount)
    self.name=name
    self.bankID=bankID
  def authorized(self):
    pass

class Credit(Payment):
  number: str
  type: str
  expDate: str
  def __init__(self,amount,number,type,expDate):
    Payment.__init__(self,amount)
    self.number=number
    self.type=type
    self.expDate=expDate
  def authorized(self):
    pass

class Order:
  orderdetail:list[OrderDetail]
  payment:list[Cash,Check,Credit]
  date:str
  status:str
  def __init__(self,date,status):
    self.orderdetail=[]
    self.payment=[]
    self.date=date
    self.status=status
  def calcSubTotal(self):
    pass
  def calcTax(self):
    pass
  def calcTotal(self):
    pass
  def calcTotalWeight(self):
    pass

class Customer:
  order:list[Order]
  name:str
  address:str
  def __init__(self,name,address):
    self.order=[]
    self.name=name
    self.address=address
