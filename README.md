# Kafka-with-REST


## Gereksinimler

Projeyi çalıştırmak için bağımlılıklar;

* Docker
* docker-compose


## Nasıl Çalıştırabilirim

1. Projeyi kendi bilgisayarınıza klonlayın veya indirin.
2. Terminal ile projeyi klonladığınız dizine gelin. Ardından;
    ```bash
        cd Kafka-with-REST
    ```
    komutu yardımıyla projenin ana dizinine eriştikten sonra:
3. Terminal ile aşağıdaki komutu yazıp konteynerlerin gerek duyduğu yazılımları yüklemesini bekleyin.
    ```bash
        docker-compose up --build
    ```
4. Tebrikler projeyi ayağa kaldırmış oldunuz. Nasıl test edebileceğiniz aşağıda yazmaktadır.


## Nasıl Test Edebilirim

1. İlk olarak bir tarayıcı sekmesinde http://127.0.0.1:8000/ adresini açın.
2. Daha sonra **_Projenin Endpoint Adresleri_** başlığında belirtilen http://127.0.0.1:8000/api/ ve http://127.0.0.1:8000/api/detail/ adreslerine ister tarayıcı ile ister curl isterseniz de istediğiniz bir REST test yazılımı ile istek atın. Örnek curl isteği: 
```bash
    curl -v http://127.0.0.1:8000/api/
```
3. API isteklerini gönderdikten sonra ana ekrandan grafiğin canlı olarak güncellenmesini görebilirsiniz.

##### Projenin Endpoint Adresleri

* http://127.0.0.1:8000/
    - Projedeki request istatistiklerinin görselleştirilmiş halde sunulduğu alan. İstatistikler canlı olarak güncellenmektedir.
* http://127.0.0.1:8000/api/
    - GET isteği atabileceğiniz API endpointi. Aynı zamanda veritabanındaki log verileri burda da listelenir.
* http://127.0.0.1:8000/api/detail/
    - POST, PUT ve DELETE istekleri bu API adresinden yapılmaktadır.
* http://127.0.0.1:8000/api/stats/
    - Bu endpoint istatistiklerin canlı olarak güncellenmesi için oluşturulmuştur. Tüm istek tiplerinin son 1 saat içerisinde ne kadar sürede tamamlandıkları bilgisi burdan çekiliyor.



