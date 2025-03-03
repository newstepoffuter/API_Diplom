# Проект по автоматизации тестирования Gismeteo Api Petstore
<a target="_blank" href="https://petstore.swagger.io/">Сайт проекта</a>

## 📄 Содержание
- [Технологии и инструменты](#tech_and_ins-технологии-и-инструменты)
- [Примеры API тестов](#scroll-Примеры-API-тестов)
- [Сборка в Jenkins](#-Сборка-в-Jenkins)
- [Allure отчет](#-Allure-отчет)
- [Отчет в Telegram с помощью бота](#-Отчет-в-Telegram-с-помощью-бота)

## :wrench: Технологии и инструменты
<p>
<a href="https://www.python.org/"><img src="resources/python.svg" width="50" height="50"  alt="Python" title="Python"/></a>
<a href="https://requests.readthedocs.io/en/latest/"><img src="resources/requests-sidebar.webp" width="50" height="50"  alt="requests" title="requests"/></a>
<a href="https://www.jetbrains.com/pycharm/"><img src="resources/PyCharm_Icon.svg" width="50" height="50"  alt="Pycharm" title="IntelliJ IDEA"/></a>
<a href="https://github.com/"><img src="resources/Github.svg" width="50" height="50"  alt="Github" title="GitHub"/></a>
<a href="https://www.jenkins.io/"><img src="resources/Jenkins.svg" width="50" height="50"  alt="Jenkins" title="Jenkins"/></a>
<a href="https://github.com/allure-framework/allure2"><img src="resources/Allure_Report.svg" width="50" height="50"  
alt="Allure" title="Allure"/></a>
<a href="https://telegram.org/"><img src="resources/Telegram.svg" width="50" height="50"  alt="Telegram" title="Telegram"/></a>
<a href="https://qameta.io/"><img src="resources/Allure_Testops.svg" width="120" height="50"  alt="Allure_Test_Ops" title="Allure_Test_Ops"/></a>



В данном проекте автотесты написаны на <code>Python</code> с использованием <code>Pytest</code> для UI-тестов и библиотекой <code>Requests</code>

> <code>Allure Report</code> формирует отчет о запуске тестов.
>
> <code>Jenkins</code> выполняет запуск тестов.
> После завершения прогона отправляются уведомления с помощью бота в <code>Telegram</code>.


## :pager: Примеры API тестов

- Валидирование ответов
- Проверка статус кода
- Проверка данных ответа

Данные примеры применимы к метода Post, Get, а также Delete


## <img src="resources/Jenkins.svg" width="25" height="25"  alt="Jenkins" title="Jenkins"/></a> Сборка в Jenkins

> Запуск джоба происходит по нажатию кнопки <code>Build now</code>
<p align="center">
<img title="Сборка в Jenkins" src="resources/Jenkins_parametrs.png">
</p>

## <img src="resources/Allure_Report.svg" width="25" height="25"  alt="Allure_Report" title="Allure_Report" title="Allure_Report"/></a> Allure отчет
>
> Allure формирует подробный отчет о прогоне тестов. Кастомные фильтры и листенеры делают отчет максимально понятным.
> Отчёт также сопровождается данными ответа и логами
<p align="center">
<img title="Allure отчет" src="resources/Allure_Overview.png">
</p>
<p align="center">
<img title="Allure отчет" src="resources/Allure_suites.png">
</p>
<p align="center">
<img title="Allure отчет" src="resources/Allure_graphs.png">
</p>

## <img width="4%" title="Telegram" src="resources/Telegram.svg"> Отчет в Telegram с помощью бота
>
> После прогона всех тестов в <code>Telegram</code> чат автоматически приходит сообщение с полной информацией о прогоне и ссылкой на <code>Allure</code>
>
<p>
<img title="Отчет в Telegram с помощью бота" src="resources/Telegram_results.png">
</p>
