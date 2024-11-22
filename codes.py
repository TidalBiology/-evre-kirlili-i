import discord
from discord.ext import commands
# İntentleri ayarla
intents = discord.Intents.default()
intents.message_content = True
# Botu oluştur
bot = commands.Bot(command_prefix='/', intents=intents)
@bot.event
async def on_ready():
    print(f'Bot giriş yaptı: {bot.user}')
# **BURAYA KOMUTLAR EKLENECEK**
@bot.command()
async def elektrikli(ctx):
    await ctx.send("Elektrikli araçlar, enerji kaynağı olarak tamamen elektrik kullanan ve fosil yakıt tüketmeyen çevre dostu "
                "taşıtlardır. Bu araçlar, elektrik motorları sayesinde sessiz bir sürüş deneyimi sunar ve karbon emisyonlarını "
                "önemli ölçüde azaltır. Elektrikli araçlar, bataryalarını şarj istasyonlarında veya ev tipi şarj cihazlarında "
                "doldurur ve yüksek enerji verimliliği ile dikkat çeker. Ayrıca, daha az hareketli parça içerdiğinden bakım "
                "maliyetleri düşüktür. Yenilenebilir enerji kaynaklarıyla birleştirildiğinde, elektrikli araçlar daha sürdürülebilir "
                "bir ulaşım çözümü sunarak, fosil yakıtlı araçlara karşı güçlü bir alternatif haline gelmiştir.")
@bot.command()
async def gas_cars(ctx):
    await ctx.send("Benzinli araçlar, içten yanmalı motorlarla çalışan ve yakıt olarak benzin kullanan araçlardır. "
                "Bu motorlar, benzinin yanmasıyla oluşan kimyasal enerjiyi mekanik enerjiye dönüştürerek tekerleklere "
                "hareket sağlar. Benzinli araçlar, hızlı hızlanma ve yüksek performans sunmaları nedeniyle uzun yıllar boyunca "
                "popüler olmuştur. Ancak, fosil yakıtların kullanımı nedeniyle karbondioksit gibi zararlı gazların atmosfere "
                "salınmasına yol açar, bu da çevresel sorunlara ve küresel ısınmaya katkıda bulunur. Günümüzde, benzinli araçlar "
                "geleneksel bir seçenek olmaya devam ederken, elektrikli ve hibrit araçlara olan ilgi artmaktadır.")
@bot.command()
async def fuelcell(ctx):
    await ctx.send("Fuel cell (yakıt hücresi) teknolojisi, kimyasal enerjiyi doğrudan elektrik enerjisine dönüştüren "
                 "temiz ve verimli bir enerji üretim yöntemidir. Bu teknoloji, özellikle hidrojenin yakıt olarak "
                 "kullanılması durumunda çevre dostu bir seçenek sunar. Yakıt hücreleri, hidrojen gibi bir yakıt ile "
                 "oksijen arasındaki elektrokimyasal reaksiyonu kullanarak elektrik, su ve ısı üretir. Yanma süreci "
                 "olmadığı için karbon emisyonları yoktur ve yalnızca su buharı açığa çıkar. Çeşitli boyutlarda ve "
                 "kapasitelerde tasarlanabilen yakıt hücreleri, taşınabilir cihazlardan elektrikli araçlara ve enerji "
                 "santrallerine kadar farklı uygulamalarda kullanılabilir.")
@bot.command()
async def kiyasla(ctx):
    await ctx.send("Benzinli, elektrikli ve yakıt hücreli araçlar farklı enerji kaynaklarıyla çalışarak kendilerine özgü avantajlar "
        "ve dezavantajlar sunar. Benzinli araçlar, yaygın altyapıları ve yüksek performanslarıyla uzun yıllardır tercih "
        "edilmektedir, ancak fosil yakıt kullanımı nedeniyle çevreye zarar verir ve karbon emisyonlarına yol açar. "
        "Elektrikli araçlar, sıfır emisyonlu ve sessiz olmalarıyla dikkat çeker, ancak batarya üretimi ve şarj süreleri "
        "halen geliştirilmesi gereken alanlardır. Yakıt hücreli araçlar ise hidrojen gibi temiz enerji kaynaklarıyla çalışır "
        "ve yalnızca su buharı açığa çıkarır. Bununla birlikte, hidrojen altyapısının sınırlı olması ve yüksek maliyetleri, "
        "yaygınlaşmalarını engelleyen başlıca faktörlerdir. Sonuç olarak, elektrikli araçlar şehir içi kullanımda öne çıkarken, "
        "yakıt hücreli araçlar uzun mesafelerde çevre dostu bir alternatif sunar. Benzinli araçlar ise halen geniş bir kullanıcı "
        "kitlesine hitap eden geleneksel bir seçenek olarak varlığını sürdürmektedir.")                 
# Botu çalıştır

bot.run("")
