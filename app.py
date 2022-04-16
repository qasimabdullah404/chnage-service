from flask import Flask, jsonify

app = Flask(__name__)

def change(amount):
  # calculate the change and store in res[]
  res = []
  coins = [1,5,10,25] # penny, nickel, dime, quarter
  coin_lookup = {25:"quarters", 10:"dimes", 5:"nickels", 1:"pennies"}
  
  # divide amount*100 -> amount in cents - by coin value
  # record number of coins evenly divided and the remainder
  
  coin = coins.pop()
  num, rem = divmod(int(amount*100), coin)
  
  # append the coin type and no of coins without remainder
  res.append({num:coin_lookup[coin]})
  
  while rem > 0:
    coin = coins.pop()
    num, rem = divmod(rem, coin)
    if num:
      if coin in coin_lookup:
        res.append({num:coin_lookup[coin]})
  
  return res

@app.route('/')
def hello():
  print("Inside hello method - the root route!")
  return jsonify({"Hello":"I can return chnage at /chnage"})

@app.route('/change/<dollars>/<cents>')
def changeRoute(dollars, cents):
  print(f"Make chnage for {dollars}.{cents}")
  amount = f"{dollars}.{cents}"
  result = change(float(amount))
  return jsonify(result)