from loader import bot, db


import handlers

# db.create_users()
# db.create_categories()
# db.create_products()
# category = ["🌯Lavashlar","🍹Ichimliklar", "🥪Klab Sendvich", "🌭Hotdoglar","🍔Burgerlar", "🍕Pitsalar", "🍅Souslar","🥗Saladlar"]
# for i in category:
#     db.insert_categories(i)
#
#
# db.insert_product("Oddiy Lavash",25000, 'https://pasta.uz/upload/products/OL%20x%20Pasta%20Original%20lavash.jpg', 1)
# db.insert_product("Sirli Lavash", 27000, 'https://pasta.uz/upload/products/OL%20x%20Pasta%20Pishloqli%20lavash.jpg', 1)
# db.insert_product("Mini Lavash", 23000, 'https://pasta.uz/upload/products/OL%20x%20Pasta%20Pishloqli%20tandir%20lavash.jpg', 1)
# db.insert_product("Tandir Lavash", 28000, 'https://pasta.uz/upload/products/OL%20x%20Pasta%20Original%20lavash.jpg', 1)
# db.insert_product("Pepsi 1l", 9000, 'https://pasta.uz/upload/products/OL%20x%20Pasta%20Pepsi%201.5L.jpg', 2)
# db.insert_product("Coca Cola 1l", 9000,'https://images.uzum.uz/cf7p3f2vtie1lhbhc7ig/original.jpg', 2)
# db.insert_product('Fanta 1l', 10000,'https://images.uzum.uz/cegs9r8v1htd23ajb19g/original.jpg', 2)
# db.insert_product('Oddiy suv 0.5l', 5000,'https://cdn.yaponamama.uz/products/thumbs/102_1677634652.jpg', 2)
# db.insert_product('Klub sendvich', 28000,'https://maxway.uz/_next/image?url=https%3A%2F%2Fcdn.delever.uz%2Fdelever%2Fd5306c3e-c2d9-4a51-980d-94b5dd0736cd&w=1920&q=75', 3)
# db.insert_product('Hot Dog', 28000,'https://cdn.express24.uz/i/732/1500/upload/iblock/12e/12ec91374046e112e5a653ced306f7eb.JPG', 4)
# db.insert_product('New York Hot Dog', 28000,'https://cdn.express24.uz/i/732/1500/upload/iblock/082/082a61de9a9ec43fa374d3022d38d088.JPG', 4)
# db.insert_product("Chiz dog", 25000,'https://cdn.express24.uz/i/732/1500/upload/iblock/823/823ad83a9e315f74cebc3c95fbfca2ea.JPG' ,4)
# db.insert_product("Gamburger", 22000, 'https://s7d1.scene7.com/is/image/mcdonalds/mcdonalds-hamburger:1-3-product-tile-desktop?wid=829&hei=513&dpr=off', 5)
# db.insert_product("Chizburger", 24000, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTyLnu_KYBtEwMtlztR8NIbNHq68cz8V5O7TQ&usqp=CAU', 5)
# db.insert_product("BigBurger", 33000, 'https://images.unsplash.com/photo-1553979459-d2229ba7433b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8YmlnJTIwYnVyZ2VyfGVufDB8fDB8fHww&w=1000&q=80', 5)
# db.insert_product("BigChiz", 37000, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTo5BhNmUxdMY27OtR39QM0B5-8aPQGq5JwWV6lPh8VIin-aXW7w2_gIXwluenQ9bzA0JA&usqp=CAU', 5)
# db.insert_product("Kombo Pitsa", 89000,'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWOM9NerDAyhgfWfmniF7zu7bOxb6bP5KawQ&usqp=CAU',6)
# db.insert_product("Go'shtli Pitsa", 97000,'https://cdn.cakelab.uz/products/thumbs/1_1643829509.jpeg',6)
# db.insert_product("Qazli Pitsa",90000,'https://images.bolt.eu/store/2022/2022-03-16/eca0db68-e130-455f-90e4-af7a83f6d59a.jpeg',6)
# db.insert_product("Pepperoni Pitsa", 75000, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQTty4cXhefOG34z2M5sTer8aCsUASGrNHVA&usqp=CAU', 6)
# db.insert_product("Ketchup", 2000, 'https://buy.am/media/image/70/d4/66/Ketchup_kfc.jpg', 7)
# db.insert_product("Mayonez", 3000, 'https://buy.am/media/image/0f/da/9f/Garlic____sauce____KFC.jpg', 7)
# db.insert_product("Pishloqli", 2000, 'https://buy.am/media/image/42/96/8b/Cheese____sauce____KFC_200x200.jpg1', 7)
# db.insert_product("Achchiq Sous", 4000, 'https://buy.am/media/image/84/8e/df/Teriyaki____Sauce____KFC_200x200.jpg', 7)
# db.insert_product("Murskoy Kapriz Salati", 23000, 'https://lagmonjon.uz/wp-content/uploads/2023/01/salat-muzhskoj-kapriz-500x500.png', 11)
# db.insert_product("Sezar Kapriz", 23000, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6FvNpBC5YmQjT4NDutTJQbev2TndpeL4Yzz1FMEb6lDdMaVBL1yQAnNLkqJWfn6KN6Co&usqp=CAU', 11)



if __name__ == '__main__':
    print("Bot ishladi")
    bot.infinity_polling()

