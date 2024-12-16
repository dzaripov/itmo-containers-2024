# Отчет по проделанной лабораторной работе №3
1. Установили и запустили minikube
   ![image](https://github.com/user-attachments/assets/60deaefb-a0ac-4de9-a6a4-98f08430e282)
2. Собираем по манифестам Deployment, Service и ConfigMap объекты через CLI
![image](https://github.com/user-attachments/assets/bb6d9fbb-5eb4-47b8-8313-6ddabb476f21)
3. Проверяем, что они все объекты создались, с помощью команды kubectl get
![image](https://github.com/user-attachments/assets/b85bbcb4-433d-4a74-8d9e-e0b664cdc8d1)
4. Обращаемся к созданному Deployment через kubectl describe
 ![image](https://github.com/user-attachments/assets/4f834a12-f17a-48fa-b681-a828384bf46c)
5. После создания из манифеста некстклауда сущностей Secret и Deployment, смотрим, что содержимое секретов реально не показывается.
 ![image](https://github.com/user-attachments/assets/e7ba0009-482c-43fc-b3f1-aba6bd342b34)
6. Обратились к Deployment некстклауда.
![image](https://github.com/user-attachments/assets/890bfb4e-6447-4bc2-a327-dd5b86ad63a9)
7. Смотрим в логи пода некстклауда, убедились, что она создалась.
![image](https://github.com/user-attachments/assets/92e1039d-90d0-4a1b-a30e-aa9ab4938374)
8. Создаём для некстклауда Service уже через команду, а не манифест.
 ![image](https://github.com/user-attachments/assets/9ebdee04-658f-4f9d-b41f-c1daa8a6b371)
9. Успешно попадаем в некстклауд после выполнения команды minikube describe nextcloud.
![image](https://github.com/user-attachments/assets/63ce56f8-1d52-49e5-801d-fa53abe51a87)
10. Попали в дэшборд, соответствующий нашему minikube, после команды minikube dashboard --url
![image](https://github.com/user-attachments/assets/60cf4541-67d5-400f-95cc-24a790c260d3)

## Ответы на вопросы
### Важен ли порядок выполнения этих манифестов? Почему?
Да. ConfigMap содержит в себе настройки среды (POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD), которые используются в поде, описанном в Deployment. В Deployment эта информация передаётся через envFrom, которая ссылается на ConfigMap. Если ConfigMap не будет создан заранее, Deployment не сможет найти нужные настройки, и контейнеры не запустятся. На скринах ниже видно состояние пода, который был создан из Deployment'а, созданного раньше, чем ConfigMap(статус Pending) и когда Deployment был создан после ConfigMap (статус Running). 
#### Cтатус: Pending
![image](https://github.com/user-attachments/assets/fe25c1f6-dfe9-4a94-904d-da601d580838)
#### Cтатус: Running
![image](https://github.com/user-attachments/assets/833c8fcc-7e7b-4915-bc91-e1b12cc3345f)

Service обычно создаётся после ConfigMap, но до Deployment. Service создаёт сеть внутри кластера, через которую можно обращаться к подам и устраивать их взаимодействие. 

Good practice - создавать Service до создания Deployment, чтобы обеспечить доступность сети сразу после развертывания подов.

Deployment создаётся последним, так как он ссылается на ConfigMap для настройки среды и предполагает, что, если ему требуется доступ извне, сеть уже настроена через Service.
#### Итого, корректный порядок выполнения манифестов:
1. ConfigMap
2. Service
3. Deployment

### Что (и почему) произойдет, если отскейлить количество реплик postgres-deployment в 0, затем обратно в 1, после чего попробовать снова зайти на Nextcloud?

Когда уменьшается количество реплик Postgres до 0, это фактически останавливает все экземпляры БД в кластере. В этот момент Nextсloud теряет соединение с БД, поскольку она больше не доступна.
Когда количество реплик Postgres возвращается обратно к 1, БД снова запускается, но NextCloud все равно не может подключиться к ней. 
Это происходит из-за того, что NextCloud не смог установить соединение с БД (так как под был отключен) и больше не пытался подключиться автоматически.

![image](https://github.com/user-attachments/assets/ddb3fc0c-936f-48dc-9c08-442690872f33)

В гите две папки: 
  * old_manifests - манифесты, которые создавались, когда мы следовали описанной в лабораторной работе последовательности дейтсвий. 
  * new_manifests - новые манифесты, которые мы создали, в процессе решения технических заданий.

