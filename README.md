# boto3-flask-api
AWS EC2 Instance Listeleme/Başlatma/Durdurma
## Listeleme

Endpoint-1: http://<api_host>:<api_port>/ec2/list

AWS Access Key Id, AWS Secret Access Key ve Region Name parametreleri ile Endpoint1'e GET methodu ile istek yolladığımızda, ilgili Region'daki Instanceleri listeler.

## Başlatma

Endpoint-2: http://<api_host>:<api_port>/ec2/start

AWS Access Key Id, AWS Secret Access Key, Region Name ve Instance Id parametreleri ile Endpoint'2 GET methodu ile istek yolladığımızda, ilgili Region'daki ilgili Instance başlatır.

## Durdurma

Endpoint-3: http://<api_host>:<api_port>/ec2/stop

AWS Access Key Id, AWS Secret Access Key, Region Name ve Instance Id parametreleri ile Endpoint'3 GET methodu ile istek yolladığımızda, ilgili Region'daki ilgili Instance durdurur.

## Log Bilgisi

Uygulama çalıştırıldığında aynı dizinde app.log isimli bir dosya oluşturulur ve tutulan log bilgileri bu dosyaya kaydedilir.

## Requirement.txt 

Uygulamanın çalışması için gerekli gereksinimler requirements.txt dosyasında belirtilmiştir.
